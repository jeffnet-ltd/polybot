/**
 * SelfAssessmentExercise Component
 *
 * A self-reflection exercise for learners to assess their understanding.
 * No wrong answers - helps track learner confidence and progress.
 */

import React, { useState } from 'react';

const SelfAssessmentExercise = ({ prompt, assessmentType, questions, skipAllowed = true, onAnswer }) => {
    const [responses, setResponses] = useState({});
    const [isComplete, setIsComplete] = useState(false);

    const handleResponse = (questionIndex, response) => {
        setResponses(prev => ({ ...prev, [questionIndex]: response }));
    };

    const handleSubmit = () => {
        setIsComplete(true);
        // Store responses (could be sent to backend for tracking)
        console.log("Self-assessment responses:", responses);
        // Don't call onAnswer with score - just move to next exercise
        // The parent component should handle moving to next exercise
        onAnswer('correct', responses, "Thank you for your self-assessment!");
    };

    const handleSkip = () => {
        onAnswer('correct', {}, "Assessment skipped");
    };

    return (
        <div className="space-y-6">
            <div className="bg-purple-50 rounded-2xl p-6 border-2 border-purple-200">
                <h3 className="text-xl font-semibold text-gray-800 text-center mb-2">{prompt}</h3>
                <p className="text-sm text-gray-600 text-center">This helps you track your progress. No wrong answers!</p>
            </div>
            <div className="space-y-4">
                {questions.map((q, idx) => (
                    <div key={idx} className="bg-white p-4 rounded-xl border border-gray-200">
                        <p className="font-medium text-gray-800 mb-3">{q.question}</p>
                        <div className="space-y-2">
                            {q.options.map((opt, optIdx) => (
                                <button
                                    key={optIdx}
                                    onClick={() => handleResponse(idx, opt)}
                                    className={`w-full p-3 text-left rounded-lg border transition-all ${responses[idx] === opt
                                            ? 'bg-purple-100 border-purple-300 text-purple-800'
                                            : 'bg-gray-50 border-gray-200 hover:bg-gray-100'
                                        }`}
                                >
                                    {opt}
                                </button>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
            <div className="flex gap-3">
                {skipAllowed && (
                    <button
                        onClick={handleSkip}
                        className="flex-1 py-3 rounded-xl font-semibold text-gray-700 bg-gray-100 hover:bg-gray-200 transition"
                    >
                        Skip
                    </button>
                )}
                <button
                    onClick={handleSubmit}
                    disabled={isComplete || Object.keys(responses).length < questions.length}
                    className="flex-1 py-3 rounded-xl font-bold text-white bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition"
                >
                    {isComplete ? "Submitted" : "Submit"}
                </button>
            </div>
        </div>
    );
};

SelfAssessmentExercise.displayName = 'SelfAssessmentExercise';

export default SelfAssessmentExercise;
