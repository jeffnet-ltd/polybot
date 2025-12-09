"""
Practice Mode Module - Game State Architecture
Handles conversation state, goal checking, and post-game feedback
"""

import json
import re
import asyncio
import logging
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from scenario_templates import ScenarioTemplate

logger = logging.getLogger(__name__)


@dataclass
class GameState:
    """Tracks conversation state for scenario-based practice"""
    scene_status: str = "ACTIVE"  # "ACTIVE" or "COMPLETE"
    conversation_history: List[Dict[str, str]] = field(default_factory=list)
    scenario_id: str = ""
    winning_condition: str = ""
    user_transcripts: List[Dict[str, Any]] = field(default_factory=list)  # Includes Whisper confidence scores
    
    def add_message(self, role: str, content: str):
        """Add a message to conversation history"""
        self.conversation_history.append({"role": role, "content": content})
    
    def add_user_transcript(self, text: str, confidence: float = 0.0, phonetic_score: float = 0.0):
        """Add a user transcription with metadata"""
        self.user_transcripts.append({
            "text": text,
            "confidence": confidence,
            "phonetic_score": phonetic_score
        })
    
    def to_dict(self) -> Dict:
        """Convert GameState to dictionary for serialization"""
        return {
            "scene_status": self.scene_status,
            "conversation_history": self.conversation_history,
            "scenario_id": self.scenario_id,
            "winning_condition": self.winning_condition,
            "user_transcripts": self.user_transcripts
        }


async def check_goal_achievement(
    conversation_history: List[Dict[str, str]],
    winning_condition: str,
    target_lang: str,
    text_generator,
    generate_chat_input_func
) -> Dict[str, str]:
    """
    Goal Check Classifier using "Hidden Thought" Method
    Requests structured JSON output from Llama 3 containing internal state and external speech
    
    Args:
        conversation_history: List of conversation messages
        winning_condition: Description of the goal that ends the interaction
        target_lang: Target language code
        text_generator: Llama 3 text generation function
        generate_chat_input_func: Function to format chat input for Llama 3
        
    Returns:
        Dictionary with "thought", "scene_status" ("ACTIVE" or "COMPLETE"), and "reply"
    """
    # Build the goal check prompt requesting JSON output
    # Use more context (last 12 messages or full conversation if shorter)
    context_messages = conversation_history[-12:] if len(conversation_history) > 12 else conversation_history
    
    goal_check_prompt = f"""You are analyzing a conversation to determine if a learning goal has been achieved.

Winning Condition: {winning_condition}

IMPORTANT: The conversation is COMPLETE if ALL of these conditions are met:
1. The customer has placed their order
2. The customer has specified seating preference (al banco or al tavolo)
3. The barista has calculated and stated the total price clearly
4. The customer has acknowledged or completed the transaction (e.g., by thanking, saying goodbye, or confirming)

If ALL conditions above are met, respond with "scene_status": "COMPLETE".
If ANY condition is missing, respond with "scene_status": "ACTIVE".

Conversation History:
"""
    for msg in context_messages:
        role = msg.get('role', 'user')
        content = msg.get('content', '')
        goal_check_prompt += f"{role.upper()}: {content}\n"
    
    goal_check_prompt += f"""
Your task: Determine if the winning condition has been met. Respond in JSON format with three fields:
1. "thought": Your internal analysis of whether ALL conditions are met (in English)
2. "scene_status": Either "ACTIVE" (goal not met, continue conversation) or "COMPLETE" (goal achieved - ALL conditions met)
3. "reply": If COMPLETE, provide a natural closing line in {target_lang}. If ACTIVE, provide the next character response in {target_lang}.

IMPORTANT: Respond ONLY with valid JSON. No additional text before or after.

Example format (if COMPLETE):
{{
  "thought": "The customer has successfully placed their order, specified seating (al banco), the barista stated the total price (2.50 euro), and the customer thanked and said goodbye. ALL conditions are met.",
  "scene_status": "COMPLETE",
  "reply": "Ecco a lei. Buona giornata!"
}}

Example format (if ACTIVE):
{{
  "thought": "The customer placed an order but the barista has not yet stated the total price. Missing condition 3.",
  "scene_status": "ACTIVE",
  "reply": "Al banco o al tavolo?"
}}

Now analyze the conversation and respond:"""
    
    try:
        # Format for Llama 3
        prompt_input = generate_chat_input_func(goal_check_prompt, [])
        
        # Generate response
        loop = asyncio.get_event_loop()
        output = await loop.run_in_executor(
            None,
            lambda: text_generator(prompt_input, max_new_tokens=150, temperature=0.3, return_full_text=False)
        )
        
        raw_response = output[0]['generated_text'].strip()
        
        # Log raw response for debugging
        logger.info(f"[Goal Check] Raw LLM response: {raw_response[:200]}")
        
        # Improved JSON extraction - try multiple patterns
        json_str = None
        
        # Pattern 1: Look for JSON object with all three required fields (improved regex)
        json_match = re.search(r'\{[^{}]*(?:"thought"[^{}]*"scene_status"[^{}]*"reply"|"scene_status"[^{}]*"thought"[^{}]*"reply"|"reply"[^{}]*"thought"[^{}]*"scene_status")[^{}]*\}', raw_response, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
        else:
            # Pattern 2: Look for any JSON object that might contain our fields
            json_match = re.search(r'\{[^{}]*"scene_status"[^{}]*\}', raw_response, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                # Pattern 3: Try to find JSON object boundaries more flexibly
                json_match = re.search(r'\{.*?"scene_status".*?\}', raw_response, re.DOTALL)
                if json_match:
                    json_str = json_match.group(0)
        
        if json_str:
            try:
                result = json.loads(json_str)
                
                # Validate and normalize
                scene_status = result.get("scene_status", "ACTIVE").upper()
                if scene_status not in ["ACTIVE", "COMPLETE"]:
                    scene_status = "ACTIVE"
                
                thought = result.get("thought", "")
                reply = result.get("reply", "")
                
                logger.info(f"[Goal Check] Parsed result - scene_status: {scene_status}, thought: {thought[:100]}")
                
                return {
                    "thought": thought,
                    "scene_status": scene_status,
                    "reply": reply
                }
            except json.JSONDecodeError as e:
                logger.warning(f"[Goal Check] JSON decode error: {e}, attempting fallback parsing")
        
        # Fallback: try to parse as JSON directly
        try:
            result = json.loads(raw_response)
            scene_status = result.get("scene_status", "ACTIVE").upper()
            if scene_status not in ["ACTIVE", "COMPLETE"]:
                scene_status = "ACTIVE"
            
            logger.info(f"[Goal Check] Direct JSON parse - scene_status: {scene_status}")
            
            return {
                "thought": result.get("thought", ""),
                "scene_status": scene_status,
                "reply": result.get("reply", "")
            }
        except json.JSONDecodeError:
            # Ultimate fallback: analyze text for completion keywords and context
            response_lower = raw_response.lower()
            has_complete_keywords = any(keyword in response_lower for keyword in ["complete", "finished", "done", "achieved", "all conditions"])
            has_active_keywords = any(keyword in response_lower for keyword in ["active", "continue", "not yet", "missing"])
            
            # Check if conversation history suggests completion
            last_messages = " ".join([msg.get('content', '').lower() for msg in conversation_history[-4:]])
            has_goodbye = any(word in last_messages for word in ["grazie", "arrivederci", "ciao", "thank", "goodbye", "bye"])
            has_price = any(word in last_messages for word in ["euro", "costa", "totale", "price", "total"])
            
            if has_complete_keywords or (has_goodbye and has_price and len(conversation_history) >= 6):
                logger.info(f"[Goal Check] Fallback detected COMPLETE - keywords: {has_complete_keywords}, goodbye: {has_goodbye}, price: {has_price}")
                return {
                    "thought": "Goal appears to be achieved based on response analysis and conversation context.",
                    "scene_status": "COMPLETE",
                    "reply": raw_response[:100] if raw_response else "Buona giornata!"
                }
            else:
                logger.info(f"[Goal Check] Fallback detected ACTIVE - no clear completion signals")
                return {
                    "thought": "Could not determine goal status from response.",
                    "scene_status": "ACTIVE",
                    "reply": raw_response[:100] if raw_response else "..."
                }
    
    except Exception as e:
        # Error fallback
        logger.error(f"[Goal Check] Error during goal check: {e}", exc_info=True)
        return {
            "thought": f"Error during goal check: {str(e)}",
            "scene_status": "ACTIVE",
            "reply": "..."
        }


def generate_pronunciation_feedback(user_transcripts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate pronunciation feedback from user transcripts
    
    Args:
        user_transcripts: List of transcriptions with confidence and phonetic scores
        
    Returns:
        Dictionary with pronunciation analysis
    """
    if not user_transcripts:
        return {
            "overall_score": 0.0,
            "feedback": "No pronunciation data available.",
            "issues": [],
            "strengths": []
        }
    
    # Calculate average scores
    confidences = [t.get("confidence", 0.0) for t in user_transcripts]
    phonetic_scores = [t.get("phonetic_score", 0.0) for t in user_transcripts]
    
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
    avg_phonetic = sum(phonetic_scores) / len(phonetic_scores) if phonetic_scores else 0.0
    overall_score = (avg_confidence * 0.4 + avg_phonetic * 0.6)  # Weighted average
    
    # Identify issues
    issues = []
    strengths = []
    
    low_confidence_count = sum(1 for c in confidences if c < 0.5)
    low_phonetic_count = sum(1 for p in phonetic_scores if p < 0.6)
    
    if low_confidence_count > len(user_transcripts) * 0.5:
        issues.append("Some words were unclear. Try to speak more clearly and enunciate each syllable.")
    
    if low_phonetic_count > len(user_transcripts) * 0.5:
        issues.append("Pronunciation accuracy needs improvement. Focus on vowel sounds and word stress.")
    
    if overall_score >= 0.8:
        strengths.append("Excellent pronunciation! Your accent is very clear.")
    elif overall_score >= 0.6:
        strengths.append("Good pronunciation overall. Keep practicing!")
    
    # Find specific low-scoring transcriptions
    problem_transcripts = [
        t for t in user_transcripts 
        if t.get("confidence", 1.0) < 0.5 or t.get("phonetic_score", 1.0) < 0.6
    ]
    
    feedback = f"Your overall pronunciation score: {overall_score:.1%}. "
    if issues:
        feedback += " ".join(issues)
    if strengths:
        feedback += " " + " ".join(strengths)
    
    return {
        "overall_score": round(overall_score, 2),
        "feedback": feedback,
        "issues": issues,
        "strengths": strengths,
        "problem_transcripts": [t.get("text", "") for t in problem_transcripts[:3]],  # Top 3 issues
        "average_confidence": round(avg_confidence, 2),
        "average_phonetic_score": round(avg_phonetic, 2)
    }


async def generate_grammar_vocabulary_review(
    conversation_transcript: str,
    target_lang: str,
    native_lang: str,
    text_generator,
    generate_chat_input_func
) -> Dict[str, Any]:
    """
    Generate grammar and vocabulary review from conversation transcript
    
    Args:
        conversation_transcript: Full conversation text
        target_lang: Target language code
        native_lang: Native language code for explanations
        text_generator: Llama 3 text generation function
        generate_chat_input_func: Function to format chat input for Llama 3
        
    Returns:
        Dictionary with grammar errors, suggestions, and vocabulary recommendations
    """
    lang_names = {
        'en': 'English',
        'fr': 'French', 
        'es': 'Spanish',
        'it': 'Italian',
        'pt': 'Portuguese',
        'tw': 'Twi',
        'de': 'German'
    }
    target_lang_name = lang_names.get(target_lang.lower(), target_lang)
    
    review_prompt = f"""You are an expert language tutor reviewing a student's conversation transcript.

Target Language: {target_lang_name}
Native Language: {native_lang}

Conversation Transcript:
{conversation_transcript}

Your task: Review this transcript and provide feedback in {native_lang}. Find:
1. Up to 3 grammatical errors (if any) with corrections
2. Up to 2 vocabulary suggestions (better word choices for a beginner learner)

Format your response as follows:

GRAMMAR_ERRORS:
1. [Error description] → [Correction]
2. [Error description] → [Correction]
3. [Error description] → [Correction]
(Or "No significant errors found" if the grammar is correct)

VOCABULARY_SUGGESTIONS:
1. [Original word/phrase] → [Better alternative] (Explanation)
2. [Original word/phrase] → [Better alternative] (Explanation)
(Or "Vocabulary was appropriate" if no suggestions)

OVERALL_FEEDBACK:
[2-3 sentences of overall feedback in {native_lang}]

Now review the transcript:"""
    
    try:
        prompt_input = generate_chat_input_func(review_prompt, [])
        loop = asyncio.get_event_loop()
        output = await loop.run_in_executor(
            None,
            lambda: text_generator(prompt_input, max_new_tokens=300, temperature=0.3, return_full_text=False)
        )
        
        raw_response = output[0]['generated_text'].strip()
        
        # Parse the structured response
        grammar_errors = []
        vocabulary_suggestions = []
        overall_feedback = ""
        
        # Extract grammar errors
        if "GRAMMAR_ERRORS:" in raw_response:
            grammar_section = raw_response.split("GRAMMAR_ERRORS:")[1].split("VOCABULARY_SUGGESTIONS:")[0].strip()
            if "No significant errors found" not in grammar_section:
                for line in grammar_section.split("\n"):
                    if "→" in line or "->" in line:
                        grammar_errors.append(line.strip())
        
        # Extract vocabulary suggestions
        if "VOCABULARY_SUGGESTIONS:" in raw_response:
            vocab_section = raw_response.split("VOCABULARY_SUGGESTIONS:")[1].split("OVERALL_FEEDBACK:")[0].strip()
            if "Vocabulary was appropriate" not in vocab_section:
                for line in vocab_section.split("\n"):
                    if "→" in line or "->" in line:
                        vocabulary_suggestions.append(line.strip())
        
        # Extract overall feedback
        if "OVERALL_FEEDBACK:" in raw_response:
            overall_feedback = raw_response.split("OVERALL_FEEDBACK:")[1].strip()
        
        return {
            "grammar_errors": grammar_errors[:3],  # Limit to 3
            "vocabulary_suggestions": vocabulary_suggestions[:2],  # Limit to 2
            "overall_feedback": overall_feedback or "Good effort! Keep practicing.",
            "raw_response": raw_response
        }
    
    except Exception as e:
        return {
            "grammar_errors": [],
            "vocabulary_suggestions": [],
            "overall_feedback": f"Error generating review: {str(e)}",
            "raw_response": ""
        }

