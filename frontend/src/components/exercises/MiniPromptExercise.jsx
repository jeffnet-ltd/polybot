/**
 * MiniPromptExercise Component
 *
 * A context-based language exercise where users respond to specific scenarios. It
 * features intelligent, client-side validation for various contexts like greetings,
 * introductions, and ordering, providing instant and pedagogically-focused feedback.
 */
import React, { useState, useRef, useCallback } from 'react';
import { Loader2 } from 'lucide-react';
import AccentedLetterChips from '../common/AccentedLetterChips';
import { sendTutorMessage } from '../../services/tutorService';

const MiniPromptExercise = ({ prompt, context, task, targetLang, nativeLang, onAnswer, explanation }) => {
    const [userInput, setUserInput] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);
    const [isComplete, setIsComplete] = useState(false);
    const textareaRef = useRef(null);

    const validateResponse = useCallback((input, validationContext, validationTask) => {
        const userLower = input.toLowerCase().trim();
        const contextLower = (validationContext || '').toLowerCase();
        const taskLower = (validationTask || '').toLowerCase();

        // --- Context-Specific Validation Rules ---

        if (contextLower.includes("piacere")) { // Introduction
            const hasMiChiamo = userLower.includes("mi chiamo");
            const hasSonoIntro = userLower.startsWith("sono ") || (userLower.includes("sono ") && userLower.indexOf("sono ") < 5);
            const hasPiacere = userLower.includes("piacere");

            let hasMiChiamoWithName = false;
            if (hasMiChiamo) {
                const afterMiChiamo = userLower.split("mi chiamo")[1]?.trim();
                hasMiChiamoWithName = afterMiChiamo && afterMiChiamo.length > 0 && !afterMiChiamo.match(/^[.,!?;:]+$/);
            }

            const hasValidIntroduction = hasMiChiamoWithName || hasSonoIntro || (hasPiacere && userLower.length > 7);
            if (hasValidIntroduction) {
                return { status: 'correct', explanation: `Great! You included your name and greeting. Perfect introduction.` };
            }
            return { status: 'incorrect', explanation: `When someone says "Piacere", you should introduce yourself. Try "Mi chiamo [your name]" or "Sono [your name]".` };
        }

        if (contextLower.includes("friend") && taskLower.includes("greet")) { // Informal Greeting
            const hasInformal = userLower.includes("ciao") || userLower.includes("come stai") || userLower.includes("come va");
            const hasFormal = userLower.includes("buongiorno") || userLower.includes("buonasera");

            if (hasInformal && !hasFormal) {
                return { status: 'correct', explanation: `Perfect! "${userInput}" is a great informal greeting for a friend.` };
            }
            if (hasInformal && hasFormal) {
                return { status: 'almost', explanation: `You're close! You used both formal and informal greetings. With friends, just stick to informal ones like "Ciao".` };
            }
            return { status: 'incorrect', explanation: `For a friend, use an informal greeting like "Ciao" or "Come stai?".` };
        }

        if (contextLower.includes("professor") || contextLower.includes("dr.") || contextLower.includes("7 pm")) { // Formal Greeting
            const hasFormal = userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
            const hasInformal = userLower.includes("ciao") && !userLower.includes("buongiorno");

            if (hasFormal && !hasInformal) {
                return { status: 'correct', explanation: `Excellent! Using a formal greeting like "${userInput}" is perfect for this situation.` };
            }
            if (hasFormal && hasInformal) {
                return { status: 'almost', explanation: `Good effort, but you mixed formal and informal greetings. Stick to just the formal one in this context.` };
            }
            return { status: 'incorrect', explanation: `This situation requires a formal greeting like "Buongiorno" or "Buonasera".` };
        }

        if (contextLower.includes("café") && taskLower.includes("order")) { // Ordering Coffee
            const hasCaffe = userLower.includes("caffè");
            const hasWrongAccent = userLower.includes("caffé");
            const hasPerFavore = userLower.includes("per favore");

            if (hasCaffe && hasPerFavore) {
                return { status: 'correct', explanation: `Perfect! "Un caffè per favore" is exactly how you order a coffee politely.` };
            }
            if (hasCaffe && !hasPerFavore) {
                return { status: 'almost', explanation: `You're so close! You ordered the coffee, but remember to add "per favore" to be polite.` };
            }
            if (hasWrongAccent) {
                return { status: 'almost', explanation: `Great try! Just a small correction: the accent on "caffè" goes the other way (è, not é).` };
            }
            return { status: 'incorrect', explanation: `To order a coffee, you can say "Un caffè per favore".` };
        }

        if (contextLower.includes("di dove") || contextLower.includes("where") || contextLower.includes("from")) { // Origin/Location Question
            const hasSonoDi = userLower.includes("sono di");
            const hasVengoDa = userLower.includes("vengo da");
            const hasCountryMention = userLower.length > 10; // Rough check for country name

            if ((hasSonoDi || hasVengoDa) && hasCountryMention) {
                return { status: 'correct', explanation: `Perfect! You correctly answered where you're from using "${userInput}".` };
            }
            if (hasSonoDi || hasVengoDa) {
                return { status: 'almost', explanation: `Good! You used the right structure. Make sure to include the country name.` };
            }
            return { status: 'incorrect', explanation: `To answer where you're from, use "Sono di [country]" or "Vengo da [country]".` };
        }

        // Fallback if no specific context matches
        return { status: 'ai_required', explanation: null };
    }, []);

    const handleSubmit = async () => {
        if (!userInput.trim() || isProcessing || isComplete) {
            return;
        }

        setIsProcessing(true);

        try {
            let validationResult = validateResponse(userInput, context, task);

            // If client-side validation is inconclusive, call the AI
            if (validationResult.status === 'ai_required') {
                const responseData = await sendTutorMessage({
                    user_message: userInput.trim(),
                    chat_history: [],
                    target_language: targetLang,
                    native_language: nativeLang,
                    level: "Beginner",
                    lesson_id: null
                });

                const aiResponse = responseData.text || "";
                const aiStatus = responseData.status;
                const aiLower = aiResponse.toLowerCase();
                const isCorrect = aiStatus === "GOAL_ACHIEVED" || ["correct", "good", "perfect", "bravo", "ottimo"].some(word => aiLower.includes(word));

                validationResult = {
                    status: isCorrect ? 'correct' : 'incorrect',
                    explanation: aiResponse || (isCorrect ? "Well done!" : "That's not quite right. Please try again.")
                };
            }

            setIsProcessing(false);
            setIsComplete(true);
            // Pass the result up to the parent ExerciseView
            onAnswer(validationResult.status, userInput, validationResult.explanation);
        } catch (error) {
            console.error("Error in mini prompt:", error);
            setIsProcessing(false);
            setIsComplete(true);
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
