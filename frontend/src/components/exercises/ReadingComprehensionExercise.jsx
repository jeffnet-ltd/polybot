/**
 * ReadingComprehensionExercise Component
 *
 * A reading comprehension exercise with text passage and multiple-choice questions.
 * Features vocabulary highlighting for learning support.
 */

import React, { useState } from 'react';

const ReadingComprehensionExercise = ({ prompt, text, question, options, correctAnswer, highlightVocab, onAnswer, explanation }) => {
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [hasAnswered, setHasAnswered] = useState(false);

    const highlightText = (text, vocab) => {
        if (!vocab || vocab.length === 0) return text;
        let highlighted = text;
        vocab.forEach(word => {
            const regex = new RegExp(`\\b${word}\\b`, 'gi');
            highlighted = highlighted.replace(regex, `<mark class="bg-yellow-200 font-semibold">${word}</mark>`);
        });
        return highlighted;
    };

    const handleSelect = (option) => {
        if (hasAnswered) return;
        setSelectedAnswer(option);
        setHasAnswered(true);
        const isCorrect = option === correctAnswer;
        onAnswer(isCorrect ? 'correct' : 'incorrect', option, explanation);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-blue-50 rounded-2xl p-6 border border-blue-200">
                <div
                    className="text-lg text-gray-800 whitespace-pre-line leading-relaxed"
                    dangerouslySetInnerHTML={{ __html: highlightText(text, highlightVocab) }}
                />
            </div>
            <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                <p className="font-semibold text-gray-800 mb-4">{question}</p>
                <div className="space-y-3">
                    {options.map((opt, idx) => (
                        <button
                            key={idx}
                            onClick={() => handleSelect(opt)}
                            disabled={hasAnswered}
                            className={`w-full p-4 text-left rounded-xl border transition-all ${hasAnswered
                                    ? opt === correctAnswer
                                        ? 'bg-green-100 border-green-300 text-green-800'
                                        : opt === selectedAnswer
                                            ? 'bg-red-100 border-red-300 text-red-800'
                                            : 'bg-gray-50 border-gray-200 text-gray-600'
                                    : 'bg-white border-gray-200 hover:bg-gray-50 cursor-pointer'
                                }`}
                        >
                            {opt}
                        </button>
                    ))}
                </div>
            </div>
        </div>
    );
};

ReadingComprehensionExercise.displayName = 'ReadingComprehensionExercise';

export default ReadingComprehensionExercise;
