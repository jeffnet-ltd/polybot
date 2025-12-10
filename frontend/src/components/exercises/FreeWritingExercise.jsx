/**
 * FreeWritingExercise Component
 *
 * A free-form writing exercise with AI or pattern-based validation.
 * Checks for required elements and provides detailed feedback.
 */

import React, { useState, useRef } from 'react';
import { sendTutorMessage } from '../../services/tutorService';

const FreeWritingExercise = ({ prompt, context, task, targetLang, requiredElements, exampleResponse, validationMode = "ai", onAnswer, explanation }) => {
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
            if (validationMode === "ai") {
                // Use AI validation (same as mini_prompt)
                const responseData = await sendTutorMessage({
                    user_message: userInput.trim(),
                    chat_history: [],
                    target_language: targetLang,
                    native_language: "en",
                    level: "Beginner",
                    lesson_id: null
                });

                const aiResponse = responseData.text || "";
                const status = responseData.status;

                // Pattern-based validation for required elements
                const userLower = userInput.toLowerCase();
                let allElementsPresent = true;
                let missingElements = [];

                if (requiredElements) {
                    requiredElements.forEach(element => {
                        let found = false;
                        if (element === "name") {
                            found = userLower.includes("mi chiamo") || userLower.includes("sono ") || userLower.includes("io sono");
                        } else if (element === "greeting") {
                            found = userLower.includes("ciao") || userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
                        } else if (element === "origin") {
                            found = userLower.includes("sono di") || userLower.includes("di italia") || userLower.includes("di francia");
                        } else if (element === "how are you") {
                            found = userLower.includes("come stai") || userLower.includes("come va");
                        }
                        if (!found) {
                            allElementsPresent = false;
                            missingElements.push(element);
                        }
                    });
                }

                let resultStatus = 'incorrect';

                if (allElementsPresent) {
                    // All required elements are present
                    // Check if AI explicitly says it's wrong or needs improvement
                    const aiSaysWrong = aiResponse.toLowerCase().includes('incorrect') ||
                                        aiResponse.toLowerCase().includes('wrong') ||
                                        aiResponse.toLowerCase().includes('try again');

                    if (status === 'correct' ||
                        aiResponse.toLowerCase().includes('correct') ||
                        aiResponse.toLowerCase().includes('perfect') ||
                        aiResponse.toLowerCase().includes('great') ||
                        !aiSaysWrong) {
                        // AI confirms it's correct, or doesn't say it's wrong
                        resultStatus = 'correct';
                    } else {
                        // AI says there's an issue despite having all elements
                        resultStatus = 'almost';
                    }
                } else if (status === 'almost' || missingElements.length === 1) {
                    // Missing elements but close to correct
                    resultStatus = 'almost';
                }

                let explanationText = explanation || aiResponse;
                if (missingElements.length > 0) {
                    explanationText = `You're missing: ${missingElements.join(', ')}. ${explanationText}`;
                }

                setFeedback(resultStatus === 'correct' ? 'success' : resultStatus === 'almost' ? 'warning' : 'error');
                setFeedbackExplanation(explanationText);
                onAnswer(resultStatus, userInput, explanationText);
            } else {
                // Pattern-based validation only
                const userLower = userInput.toLowerCase();
                let allElementsPresent = true;
                let missingElements = [];

                if (requiredElements) {
                    requiredElements.forEach(element => {
                        let found = false;
                        if (element === "name") {
                            found = userLower.includes("mi chiamo") || userLower.includes("sono ") || userLower.includes("io sono");
                        } else if (element === "greeting") {
                            found = userLower.includes("ciao") || userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
                        } else if (element === "origin") {
                            found = userLower.includes("sono di") || userLower.includes("di italia") || userLower.includes("di francia");
                        }
                        if (!found) {
                            allElementsPresent = false;
                            missingElements.push(element);
                        }
                    });
                }

                const resultStatus = allElementsPresent ? 'correct' : 'almost';
                let explanationText = explanation || (allElementsPresent ? "Great writing!" : `You're missing: ${missingElements.join(', ')}. Try to include all required elements.`);

                setFeedback(resultStatus === 'correct' ? 'success' : 'warning');
                setFeedbackExplanation(explanationText);
                onAnswer(resultStatus, userInput, explanationText);
            }
        } catch (error) {
            console.error("Error validating writing:", error);
            // Fallback to pattern matching
            const userLower = userInput.toLowerCase();
            let allElementsPresent = true;
            if (requiredElements) {
                requiredElements.forEach(element => {
                    let found = false;
                    if (element === "name") {
                        found = userLower.includes("mi chiamo") || userLower.includes("sono ");
                    } else if (element === "greeting") {
                        found = userLower.includes("ciao") || userLower.includes("buongiorno");
                    }
                    if (!found) allElementsPresent = false;
                });
            }
            const resultStatus = allElementsPresent ? 'correct' : 'almost';
            setFeedback(resultStatus === 'correct' ? 'success' : 'warning');
            setFeedbackExplanation(explanation || "Good effort! Make sure to include all required elements.");
            onAnswer(resultStatus, userInput, explanation);
        } finally {
            setIsProcessing(false);
            setIsComplete(true);
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            {context && (
                <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                    <p className="text-sm text-gray-600 mb-2"><strong>Context:</strong> {context}</p>
                    <p className="text-sm text-gray-700"><strong>Task:</strong> {task}</p>
                    {requiredElements && (
                        <p className="text-sm text-blue-600 mt-2"><strong>Required:</strong> {requiredElements.join(', ')}</p>
                    )}
                </div>
            )}
            <textarea
                ref={textareaRef}
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Write your response here..."
                className="w-full p-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 min-h-32"
                disabled={isComplete || isProcessing}
            />
            {exampleResponse && (
                <details className="text-sm text-gray-600">
                    <summary className="cursor-pointer text-blue-600 hover:text-blue-700">Show example</summary>
                    <div className="mt-2 p-3 bg-gray-50 rounded-lg border border-gray-200">
                        <p className="font-semibold">Example:</p>
                        <p className="italic">{exampleResponse}</p>
                    </div>
                </details>
            )}
            <button
                onClick={handleSubmit}
                disabled={!userInput.trim() || isProcessing || isComplete}
                className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed shadow-md transition transform hover:scale-[1.02]"
            >
                {isProcessing ? "Checking..." : isComplete ? "Submitted" : "Submit"}
            </button>
            {feedback && (
                <div className={`p-4 rounded-xl ${feedback === 'success' ? 'bg-green-50 border-green-200' : feedback === 'warning' ? 'bg-yellow-50 border-yellow-200' : 'bg-red-50 border-red-200'}`}>
                    <p className={`font-semibold ${feedback === 'success' ? 'text-green-800' : feedback === 'warning' ? 'text-yellow-800' : 'text-red-800'}`}>
                        {feedback === 'success' ? '✓ Correct!' : feedback === 'warning' ? '⚠ Almost!' : '✗ Incorrect'}
                    </p>
                    {feedbackExplanation && (
                        <p className={`mt-2 text-sm ${feedback === 'success' ? 'text-green-700' : feedback === 'warning' ? 'text-yellow-700' : 'text-red-700'}`}>
                            {feedbackExplanation}
                        </p>
                    )}
                </div>
            )}
        </div>
    );
};

FreeWritingExercise.displayName = 'FreeWritingExercise';

export default FreeWritingExercise;
