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

    // Italian number word to digit mapping (ages 0-99)
    const italianNumberMap = {
        'zero': 0, 'uno': 1, 'un': 1, 'due': 2, 'tre': 3, 'quattro': 4,
        'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10,
        'undici': 11, 'dodici': 12, 'tredici': 13, 'quattordici': 14,
        'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18,
        'diciannove': 19, 'venti': 20, 'ventuno': 21, 'ventidue': 22,
        'ventitre': 23, 'ventiquattro': 24, 'venticinque': 25, 'ventisei': 26,
        'ventisette': 27, 'ventotto': 28, 'ventinove': 29, 'trenta': 30,
        'trentuno': 31, 'trentadue': 32, 'trentatre': 33, 'trentaquattro': 34,
        'trentacinque': 35, 'trentasei': 36, 'trentasette': 37, 'trentotto': 38,
        'trentanove': 39, 'quaranta': 40, 'cinquanta': 50, 'sessanta': 60,
        'settanta': 70, 'ottanta': 80, 'novanta': 90
    };

    /**
     * Normalizes Italian number words to digits for comparison
     * Accepts both "nove" and "9" as valid
     */
    const normalizeItalianNumbers = (text) => {
        let normalized = text.toLowerCase().trim();

        // Replace Italian number words with digits
        Object.entries(italianNumberMap).forEach(([word, digit]) => {
            const regex = new RegExp(`\\b${word}\\b`, 'gi');
            normalized = normalized.replace(regex, digit.toString());
        });

        return normalized;
    };

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

        // Age-related exercises (e.g., "You are roleplaying as a 9-year-old")
        if (contextLower.includes("year") || contextLower.includes("old") ||
            contextLower.includes("roleplaying as a") || contextLower.includes("anni") ||
            taskLower.includes("years old") || taskLower.includes("age")) {

            // Normalize numbers in user input (converts "nove" → "9")
            const normalizedInput = normalizeItalianNumbers(userLower);

            // Check for age statement pattern: "ho [number] anni"
            const hasHo = normalizedInput.includes("ho ");
            const hasAnni = userLower.includes("anni");

            // Extract any number (word or digit) from input
            const numberMatch = normalizedInput.match(/\b(\d+)\b/);
            const hasNumber = numberMatch !== null;

            if (targetLang === 'it') {
                // Italian validation
                if (hasHo && hasAnni && hasNumber) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly stated your age: "Ho ${numberMatch[1]} anni."`
                    };
                }

                // Provide helpful feedback for common mistakes
                if (!hasHo) {
                    return {
                        status: 'incorrect',
                        explanation: `Remember to start with "Ho" (I have). Try: "Ho [number] anni."`
                    };
                }
                if (!hasAnni) {
                    return {
                        status: 'incorrect',
                        explanation: `Don't forget "anni" (years). Try: "Ho [number] anni."`
                    };
                }
                if (!hasNumber) {
                    return {
                        status: 'incorrect',
                        explanation: `Include your age as a number. Try: "Ho [number] anni."`
                    };
                }
            }

            // For other languages, check for basic age pattern
            if (hasNumber) {
                return {
                    status: 'correct',
                    explanation: `Great! You stated your age.`
                };
            }

            return {
                status: 'incorrect',
                explanation: `Try stating your age with a number.`
            };
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
