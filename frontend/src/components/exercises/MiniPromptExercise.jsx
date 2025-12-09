/**
 * MiniPromptExercise Component
 *
 * A context-based language exercise where users respond to specific scenarios.
 * Features intelligent validation for formality, greetings, introductions, and more.
 * Includes accented letter support for Italian and other languages.
 */

import React, { useState, useRef } from 'react';
import { Loader2 } from 'lucide-react';
import AccentedLetterChips from '../common/AccentedLetterChips';
import { sendTutorMessage } from '../../services/tutorService';

const MiniPromptExercise = ({ prompt, context, task, targetLang, nativeLang, onAnswer, explanation }) => {
    const [userInput, setUserInput] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);
    const [feedback, setFeedback] = useState(null);
    const [feedbackExplanation, setFeedbackExplanation] = useState(null);
    const [isComplete, setIsComplete] = useState(false);
    const textareaRef = useRef(null);

    const handleSubmit = async () => {
        if (!userInput.trim() || isProcessing || isComplete) return;

        setIsProcessing(true);
        setFeedback(null);

        try {
            // Use /tutor endpoint for AI validation
            const responseData = await sendTutorMessage({
                user_message: userInput.trim(),
                chat_history: [],
                target_language: targetLang,
                native_language: nativeLang,
                level: "Beginner",
                lesson_id: null
            });

            const aiResponse = responseData.text || "";
            const status = responseData.status;

            // Improved validation logic for mini-prompt exercises
            // Check for appropriate responses based on context and task
            const userLower = userInput.toLowerCase().trim();
            let resultStatus = 'incorrect'; // 'correct', 'almost', or 'incorrect'

            // Context-specific validation
            if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                // Informal greeting context - check for informal Italian greetings
                // Accept: Ciao, Come stai, Come va, etc.
                const hasInformalGreeting = userLower.includes("ciao") ||
                    userLower.includes("come stai") ||
                    userLower.includes("come va") ||
                    (userLower.includes("salve") && !userLower.includes("buongiorno") && !userLower.includes("buonasera"));
                // Reject if uses formal greetings
                const usesFormalGreeting = userLower.includes("buongiorno") || userLower.includes("buonasera");

                if (hasInformalGreeting && !usesFormalGreeting) {
                    resultStatus = 'correct';
                } else if (hasInformalGreeting && usesFormalGreeting) {
                    // Partial: Has informal but also formal - this is "almost"
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                // Formal context - check for formal greetings
                const hasFormalGreeting = userLower.includes("buongiorno") ||
                    userLower.includes("buonasera") ||
                    userLower.includes("salve");
                // Reject if uses informal greeting
                const usesInformalGreeting = userLower.includes("ciao") && !userLower.includes("buongiorno") && !userLower.includes("buonasera");

                if (hasFormalGreeting && !usesInformalGreeting) {
                    resultStatus = 'correct';
                } else if (hasFormalGreeting && usesInformalGreeting) {
                    // Partial: Has formal but also informal
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                // "Chi sei?" (Who are you?) context - must respond with "Io sono" + name
                // Check for "Io sono" pattern (with or without "Io")
                const hasIoSono = userLower.includes("io sono") ||
                    (userLower.startsWith("sono ") && userLower.split("sono ")[1]?.trim().length > 0);
                // Also accept "Mi chiamo" as alternative
                const hasMiChiamo = userLower.includes("mi chiamo");

                // For "Io sono" - check if there's text after it (the name)
                let hasName = false;
                if (userLower.includes("io sono")) {
                    const afterIoSono = userLower.split("io sono")[1]?.trim();
                    hasName = afterIoSono && afterIoSono.length > 0 && !afterIoSono.match(/^[.,!?;:]+$/);
                } else if (userLower.startsWith("sono ")) {
                    const afterSono = userLower.split("sono ")[1]?.trim();
                    hasName = afterSono && afterSono.length > 0 && !afterSono.match(/^[.,!?;:]+$/);
                } else if (hasMiChiamo) {
                    const afterMiChiamo = userLower.split("mi chiamo")[1]?.trim();
                    hasName = afterMiChiamo && afterMiChiamo.length > 0 && !afterMiChiamo.match(/^[.,!?;:]+$/);
                }

                // Accept if has "Io sono" or "Mi chiamo" followed by a name
                resultStatus = ((hasIoSono || hasMiChiamo) && hasName) ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                // "Di dove sei?" (Where are you from?) context - must respond with "Sono di" + country OR "Sono" + nationality
                const hasSonoDi = userLower.includes("sono di");
                const hasSono = userLower.includes("sono") && (userLower.includes("italia") || userLower.includes("francia") || userLower.includes("spagna") || userLower.includes("stati uniti") || userLower.includes("regno unito") || userLower.includes("americano") || userLower.includes("italiano") || userLower.includes("francese") || userLower.includes("spagnolo") || userLower.includes("inglese"));

                // Check if there's a country/nationality mentioned
                const hasCountry = userLower.includes("italia") ||
                    userLower.includes("francia") ||
                    userLower.includes("spagna") ||
                    userLower.includes("stati uniti") ||
                    userLower.includes("regno unito") ||
                    userLower.includes("americano") ||
                    userLower.includes("italiano") ||
                    userLower.includes("francese") ||
                    userLower.includes("spagnolo") ||
                    userLower.includes("inglese");

                // Accept if has "Sono di" + country OR "Sono" + nationality
                if ((hasSonoDi && hasCountry) || (hasSono && hasCountry)) {
                    resultStatus = 'correct';
                } else if (hasSonoDi || hasSono) {
                    // Has "Sono di" or "Sono" but missing country/nationality
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && context.toLowerCase().includes("piacere")) {
                // Introduction context - must introduce self
                const hasIntroduction = userLower.includes("mi chiamo") ||
                    (userLower.includes("sono") && userLower.split("sono")[1].trim().length > 0) ||
                    (userLower.includes("piacere") && userLower.length > 7);
                resultStatus = hasIntroduction ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                // Polite closing context - must have polite closing
                const hasPoliteClosing = userLower.includes("grazie") ||
                    userLower.includes("arrivederci") ||
                    userLower.includes("arrivederla") ||
                    userLower.includes("a presto") ||
                    userLower.includes("buona giornata") ||
                    userLower.includes("buonasera") ||
                    userLower.includes("buongiorno");
                resultStatus = hasPoliteClosing ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                // Coffee ordering context - must have "caffè" (with correct accent è) and "per favore"
                const normalizedInput = userLower.replace(/è/g, 'e').replace(/é/g, 'e');
                const hasCaffe = normalizedInput.includes("caffe");
                const hasPerFavore = userLower.includes("per favore");
                const hasUn = normalizedInput.includes("un ") || normalizedInput.startsWith("un ");

                // Check for wrong accent (é instead of è)
                const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");

                // Accept if has "un caffè" (with correct accent è) and "per favore"
                if (hasCaffe && hasPerFavore && !hasWrongAccent) {
                    resultStatus = 'correct';
                } else if (hasCaffe && hasPerFavore && hasWrongAccent) {
                    // Has everything correct but wrong accent (é instead of è) - almost correct
                    resultStatus = 'almost';
                } else if (hasCaffe && hasUn) {
                    // Has "un caffè" but missing "per favore" - almost correct
                    resultStatus = 'almost';
                } else if (hasCaffe || hasPerFavore) {
                    // Partial: has one but not both
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else {
                // Fallback: use AI response analysis
                const aiLower = aiResponse.toLowerCase();
                const isCorrect = status === "GOAL_ACHIEVED" ||
                    aiLower.includes("correct") ||
                    aiLower.includes("good") ||
                    aiLower.includes("perfect") ||
                    aiLower.includes("bravo") ||
                    aiLower.includes("ben fatto") ||
                    aiLower.includes("ottimo") ||
                    aiLower.includes("fantastico") ||
                    aiLower.includes("perfetto");
                resultStatus = isCorrect ? 'correct' : 'incorrect';
            }

            // Always stop processing, even on success
            setIsProcessing(false);
            setIsComplete(true);

            // Set appropriate feedback with detailed, pedagogically-focused explanations
            if (resultStatus === 'correct') {
                // When correct: Explain why it's appropriate in this context
                let feedbackMsg = "Correct!";
                let explanationText = "";

                if (aiResponse && aiResponse.trim().length > 0 && !aiResponse.toLowerCase().includes("error")) {
                    // Use AI response if it's meaningful
                    explanationText = aiResponse;
                } else {
                    // Generate context-specific explanations
                    if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                        explanationText = `Perfect! You used "${userInput}" which is exactly right for greeting a friend. In Italian, "Ciao" and "Come stai?" are what you'd use with people you know well - it shows you understand when to be casual and friendly. Great job!`;
                    } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                        const isEvening = context.toLowerCase().includes("7 pm") || context.toLowerCase().includes("evening");
                        const greeting = userInput.toLowerCase().includes("buonasera") ? "Buonasera" : userInput.toLowerCase().includes("buongiorno") ? "Buongiorno" : "formal greeting";
                        explanationText = `Excellent choice! You used ${greeting}, which is perfect for this situation. ${isEvening ? "Since it's evening, 'Buonasera' is exactly what you'd say - you're really getting the hang of time-based greetings!" : "Using formal language shows respect, and you've got that down. Well done!"}`;
                    } else if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                        explanationText = `Perfect! You correctly responded to "Chi sei?" (Who are you?) with "${userInput}". Using "Io sono [name]" is exactly the right way to answer this question in Italian. You're getting the hang of introductions!`;
                    } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                        explanationText = `Perfect! You correctly answered "Di dove sei?" (Where are you from?) with "${userInput}". Using "Sono di [country]" or "Sono [nationality]" is exactly the right way to respond. Great job!`;
                    } else if (context && context.toLowerCase().includes("piacere")) {
                        explanationText = `Nice work! You responded with "${userInput}", which is perfect. When someone says "Piacere" (nice to meet you), introducing yourself with "Mi chiamo" or "Sono" is exactly the right thing to do. You're understanding the flow of Italian conversations really well!`;
                    } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                        explanationText = `Perfect! Using "${userInput}" when leaving a shop is exactly what you should do. In Italian culture, it's really important to acknowledge people politely when you're leaving - it shows good manners. You're getting the cultural side of things too, which is fantastic!`;
                    } else if (explanation) {
                        explanationText = explanation;
                    } else {
                        explanationText = "Well done! Your response is appropriate for this situation.";
                    }
                }

                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('correct', userInput, explanationText);
            } else if (resultStatus === 'almost') {
                // When almost: Explain what's right and what needs adjustment
                let feedbackMsg = "Almost!";
                let explanationText = "";

                // Generate "almost" feedback explaining what's right and what needs adjustment
                if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                    explanationText = `You're on the right track! You used an informal greeting like "Come stai?" which is perfect for a friend. However, you also used a formal greeting like "Buongiorno" or "Buonasera" at the beginning. For friends, stick with just the informal greeting - try "Ciao" or "Come stai?" without the formal part. You're getting it!`;
                } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                    explanationText = `Good effort! You used a formal greeting which is correct for this situation. However, you also mixed in an informal greeting. For someone like a professor, keep it completely formal - use just "Buongiorno" or "Buonasera" depending on the time. You're almost there!`;
                } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                    const userLowerLocal = userInput.toLowerCase();
                    const hasCaffe = userLowerLocal.includes("caffè") || userLowerLocal.includes("caffe") || userLowerLocal.includes("caffé");
                    const hasPerFavore = userLowerLocal.includes("per favore");
                    const hasUn = userLowerLocal.includes("un ") || userLowerLocal.startsWith("un ");
                    const hasWrongAccent = userLowerLocal.includes("caffé") && !userLowerLocal.includes("caffè");

                    if (hasWrongAccent && hasCaffe && hasPerFavore) {
                        explanationText = `Almost there! You have everything right - "un caffè" and "per favore" - but there's a small accent issue. The word "caffè" uses a grave accent (è), not an acute accent (é). So it should be "Un caffè per favore" with è, not é. Great attention to detail though!`;
                    } else if (hasCaffe && hasUn && !hasPerFavore) {
                        explanationText = `You're almost there! You correctly used "un caffè" (a coffee), which is perfect. To make it more polite, add "per favore" (please) at the end. So it would be "Un caffè per favore" - that's the complete, polite way to order!`;
                    } else if (hasCaffe && !hasUn) {
                        explanationText = `Good start! You mentioned "caffè" (coffee), which is correct. To order properly, use "Un caffè" (A coffee) - the article "un" is important because "caffè" is masculine. Then add "per favore" (please) to be polite. Try: "Un caffè per favore"!`;
                    } else if (!hasCaffe && hasPerFavore) {
                        explanationText = `You remembered "per favore" (please), which is great for being polite! However, you need to specify what you're ordering. Use "Un caffè per favore" (A coffee, please) - "caffè" is the word for coffee, and "un" is the masculine article. You're getting there!`;
                    } else {
                        explanationText = `To order a coffee in Italian, say "Un caffè per favore" (A coffee, please). Remember: "caffè" is masculine, so use "un" as the article. The phrase "per favore" makes it polite. Give it another try!`;
                    }
                } else {
                    explanationText = "You're close! Some parts of your answer are right, but there are a few adjustments needed. Keep trying!";
                }

                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('almost', userInput, explanationText);
            } else {
                // When incorrect: Explain why it's wrong and what would be better
                let feedbackMsg = "Incorrect.";
                let explanationText = "";

                if (aiResponse && aiResponse.trim().length > 0 && !aiResponse.toLowerCase().includes("error")) {
                    explanationText = aiResponse;
                } else {
                    // Generate context-specific explanations for why it's wrong
                    if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                        explanationText = `Almost there! When someone asks "Chi sei?" (Who are you?), you should respond with "Io sono [your name]" (I am [name]). Your answer "${userInput}" is close, but make sure you include "Io sono" followed by your name. For example: "Io sono Jeff" or "Io sono Maria". You're learning!`;
                    } else if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                        const usedFormal = userInput.toLowerCase().includes("buongiorno") || userInput.toLowerCase().includes("buonasera");
                        explanationText = `I see what happened here! ${usedFormal ? "You used a formal greeting, but since this is a friend, you'd want to use something more casual like 'Ciao' or 'Come stai?' to show you're on familiar terms. In Italian, the greeting you choose depends on how well you know the person - with friends, we keep it informal!" : "For a friend, try using something more casual like 'Ciao' (hi/bye) or 'Come stai?' (how are you?). These show you're on familiar terms, which is perfect for friends!"}`;
                    } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                        const usedInformal = userInput.toLowerCase().includes("ciao") && !userInput.toLowerCase().includes("buongiorno") && !userInput.toLowerCase().includes("buonasera");
                        const isEvening = context.toLowerCase().includes("7 pm") || context.toLowerCase().includes("evening");

                        if (usedInformal) {
                            explanationText = `I see what happened - you used an informal greeting, but this situation calls for something more formal. ${isEvening ? "Since it's evening, try 'Buonasera' (good evening) - that's the polite way to greet someone in the evening, especially someone like a professor!" : "When talking to a professor or someone in authority, we use formal greetings like 'Buongiorno' or 'Buonasera' depending on the time. It's all about showing respect - you'll get the hang of it!"}`;
                        } else {
                            explanationText = `Almost there! ${isEvening ? "Since it's 7 PM (evening), you'd want to use 'Buonasera' (good evening) instead of 'Buongiorno'. In Italian, time-based greetings matter a lot - 'Buongiorno' is for morning/daytime, while 'Buonasera' is for evening/night. Don't worry, this is a common thing to mix up!" : "For someone like a professor, we use formal greetings to show respect. Try 'Buongiorno' (good morning) or 'Buonasera' (good evening) depending on the time of day. You're learning the social side of Italian - keep going!"}`;
                        }
                    } else if (context && context.toLowerCase().includes("piacere")) {
                        explanationText = `Good try! When someone says "Piacere" (nice to meet you), the natural response is to introduce yourself. Try using "Mi chiamo [your name]" (my name is...) or "Sono [your name]" (I am...). This is how Italians do introductions - you'll get it!`;
                    } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                        explanationText = `Almost there! When leaving a shop, Italians like to end the interaction politely. Try phrases like "Arrivederci" (goodbye), "Grazie" (thank you), or "A presto" (see you soon). It's a cultural thing - showing good manners is really valued in Italy. You're learning!`;
                    } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                        const userLowerLocal = userInput.toLowerCase();
                        const hasSonoDi = userLowerLocal.includes("sono di");
                        const hasSono = userLowerLocal.includes("sono");
                        const hasCountry = userLowerLocal.includes("italia") || userLowerLocal.includes("francia") || userLowerLocal.includes("spagna") || userLowerLocal.includes("stati uniti") || userLowerLocal.includes("regno unito") || userLowerLocal.includes("americano") || userLowerLocal.includes("italiano") || userLowerLocal.includes("francese") || userLowerLocal.includes("spagnolo") || userLowerLocal.includes("inglese");

                        if (!hasSonoDi && !hasSono) {
                            explanationText = `To answer "Di dove sei?" (Where are you from?), start with "Sono di" (I'm from) followed by a country name, or "Sono" (I am) followed by a nationality. For example: "Sono di Italia" (I'm from Italy) or "Sono italiano" (I am Italian). Try again!`;
                        } else if ((hasSonoDi || hasSono) && !hasCountry) {
                            explanationText = `You used "Sono di" or "Sono" which is good, but you need to add a country name or nationality. For example: "Sono di Italia" (I'm from Italy) or "Sono italiano" (I am Italian). You're getting there!`;
                        } else {
                            explanationText = `To answer "Di dove sei?" (Where are you from?), use "Sono di [country]" (I'm from [country]) or "Sono [nationality]" (I am [nationality]). For example: "Sono di Italia" or "Sono italiano". Give it another try!`;
                        }
                    } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                        explanationText = `To order a coffee in Italian, say "Un caffè per favore" (A coffee, please). Remember: "caffè" is masculine, so use "un" as the article. The phrase "per favore" makes it polite. Give it another try!`;
                    } else if (explanation) {
                        explanationText = explanation;
                    } else {
                        explanationText = "Your response doesn't quite fit this situation. Think about the context and what would be culturally appropriate.";
                    }
                }

                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('incorrect', userInput, explanationText);
            }
        } catch (error) {
            console.error("Error in mini prompt:", error);
            // Always stop processing on error
            setIsProcessing(false);
            setIsComplete(true);

            // Provide fallback feedback
            setFeedback("Error validating response.");
            setFeedbackExplanation("Please check your answer and try again.");
            onAnswer('incorrect', userInput, "Error validating response. Please try again.");
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>

            {/* Context display */}
            {context && (
                <div className="bg-blue-50 p-4 rounded-xl border border-blue-200">
                    <p className="text-sm text-gray-600 mb-2 font-medium">Context:</p>
                    <p className="text-gray-800">{context}</p>
                </div>
            )}

            {/* Task display */}
            {task && (
                <div className="bg-yellow-50 p-4 rounded-xl border border-yellow-200">
                    <p className="text-sm text-gray-600 mb-2 font-medium">Task:</p>
                    <p className="text-lg font-bold text-gray-800">{task}</p>
                </div>
            )}

            {/* Input area */}
            <div className="space-y-3">
                <label className="block text-sm font-medium text-gray-700">
                    Your response ({targetLang.toUpperCase()}):
                </label>
                <textarea
                    ref={textareaRef}
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    disabled={isComplete || isProcessing}
                    placeholder="Type your response here..."
                    className="w-full p-4 border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:outline-none resize-none disabled:bg-gray-100 disabled:cursor-not-allowed"
                    rows={3}
                />
                {/* Accented letter chips for Italian */}
                {targetLang === 'it' && (
                    <AccentedLetterChips
                        inputRef={textareaRef}
                        value={userInput}
                        setValue={setUserInput}
                        disabled={isComplete || isProcessing}
                    />
                )}
                <button
                    onClick={handleSubmit}
                    disabled={!userInput.trim() || isComplete || isProcessing}
                    className="w-full py-4 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white rounded-xl font-bold shadow-md transition transform hover:scale-[1.02] disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                    {isProcessing ? (
                        <>
                            <Loader2 className="w-5 h-5 animate-spin" />
                            Validating...
                        </>
                    ) : isComplete ? (
                        "Submitted"
                    ) : (
                        "Submit"
                    )}
                </button>
            </div>

            {/* Feedback - removed duplicate, handled by parent ExerciseView */}

            {explanation && !isComplete && (
                <div className="bg-purple-50 p-4 rounded-xl border border-purple-200">
                    <p className="text-sm text-purple-700 font-medium mb-1">Hint:</p>
                    <p className="text-sm text-purple-800 italic">{explanation}</p>
                </div>
            )}
        </div>
    );
};

MiniPromptExercise.displayName = 'MiniPromptExercise';

export default MiniPromptExercise;
