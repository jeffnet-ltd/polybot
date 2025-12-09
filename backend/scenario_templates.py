"""
Scenario Templates for Scenario-Based Practice Mode
Defines scenario data structures and Stage Manager Pattern prompts
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ScenarioTemplate:
    """Data structure for a practice scenario"""
    scenario_id: str
    title: str
    description: str
    system_prompt_template: str
    winning_condition: str
    user_goal_description: str  # User-friendly goal instructions for learners
    vocabulary_primer: List[str]
    estimated_duration: str = "5-10 minutes"
    difficulty: str = "Beginner"


# Scenario database
SCENARIOS: Dict[str, ScenarioTemplate] = {
    "coffee_order": ScenarioTemplate(
        scenario_id="coffee_order",
        title="Ordering Coffee at a Café",
        description="Practice ordering coffee and pastries at an Italian café. Learn to ask for items, specify preferences, and complete your order.",
        system_prompt_template="""You are roleplaying as a Barista in a busy Italian café.

IMPORTANT ROLE CLARIFICATION:
- YOU are the Barista (the café employee)
- The USER is the Customer (the person ordering)
- You should NEVER act as the customer or place orders yourself
- You should ONLY respond as the barista taking the customer's order

Current Scene: The user is a customer ordering a cappuccino and a cornetto.

Your Goal: 
1. Take their order (listen to what they want)
2. Ask if they want it 'al banco' (at the bar) or 'al tavolo' (at the table)
3. Calculate the total price
4. STATE THE TOTAL PRICE CLEARLY to the customer (e.g., "Sono 4 euro" or "In totale fa 4,50 euro")
5. Wait for the customer to acknowledge or say goodbye

Constraints: 
- Keep responses short (under 20 words). 
- Speak ONLY in {target_lang}.
- You are the BARISTA, not the customer. Do not place orders or ask for items as if you were the customer.
- If the user changes the topic (e.g., asks about the weather), politely bring them back to the order.
- Use natural, friendly café language.
- Wait for the user to complete their order before asking about seating preference.
- After the customer specifies seating preference, you MUST calculate and state the total price clearly.""",
        winning_condition="The customer has successfully placed their order, specified whether they want to sit at a table or at the bar, the barista has calculated and stated the total price clearly, and the customer has acknowledged or completed the transaction (e.g., by thanking the barista or saying goodbye).",
        user_goal_description="""🎯 Your Mission: Master the Italian café experience!

You're about to step into a bustling Italian café and order like a local! Your goal is to:
✨ Place your order (coffee, pastries, whatever you fancy!)
✨ Choose where you'd like to sit (al banco = at the bar, al tavolo = at a table)
✨ Complete your transaction when the barista tells you the total
✨ End with a friendly goodbye

💡 Pro Tips:
• The barista might ask follow-up questions like "Which coffee would you like?" or "What type of pastry filling do you want?" - use context clues to understand!
• If you're really stuck, you have ONE translation available - use it wisely! 
• Don't worry about being perfect - this is practice! You'll get a report card at the end showing what you did well and where you can improve.

Ready to order? Let's go! 🚀""",
        vocabulary_primer=["cappuccino", "cornetto", "al banco", "al tavolo", "quanto costa", "ecco a lei"],
        estimated_duration="5-10 minutes",
        difficulty="Beginner"
    )
}


def get_scenario_template(scenario_id: str) -> Optional[ScenarioTemplate]:
    """
    Retrieve a scenario template by ID
    
    Args:
        scenario_id: Unique identifier for the scenario
        
    Returns:
        ScenarioTemplate if found, None otherwise
    """
    return SCENARIOS.get(scenario_id)


def get_all_scenarios() -> List[ScenarioTemplate]:
    """
    Get all available scenarios
    
    Returns:
        List of all ScenarioTemplate objects
    """
    return list(SCENARIOS.values())


def build_stage_manager_prompt(scenario: ScenarioTemplate, target_lang: str, native_lang: str) -> str:
    """
    Build a Stage Manager Pattern system prompt from a scenario template
    
    Args:
        scenario: ScenarioTemplate object
        target_lang: Target language code (e.g., "it", "en")
        native_lang: Native language code for explanations
        
    Returns:
        Formatted system prompt string
    """
    # Get full language name for better prompts
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
    
    # Format the prompt template with language placeholders
    prompt = scenario.system_prompt_template.format(
        target_lang=target_lang_name,
        native_lang=native_lang
    )
    
    # Add invisible reminder for drift prevention
    if scenario.scenario_id == "coffee_order":
        prompt += "\n\n[System Note: You are the BARISTA. The user is the CUSTOMER. You take orders, you do not place them. After the customer specifies seating preference, you MUST calculate and state the total price clearly. Focus on the current scene goal; do not discuss unrelated topics.]"
    else:
        prompt += "\n\n[System Note: Focus on the current scene goal; do not discuss unrelated topics.]"
    
    return prompt

