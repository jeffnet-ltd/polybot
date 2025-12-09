/**
 * ArrangeExercise Component
 *
 * An interactive word arrangement exercise where users arrange words in the correct order.
 * Features drag-and-drop or click-to-select interface with visual feedback.
 */

import React, { useState } from 'react';
import { RefreshCcw } from 'lucide-react';

const ArrangeExercise = ({ prompt, options, correctAnswer, onAnswer }) => {
    const [currentOrder, setCurrentOrder] = useState([]);
    const [availableOptions, setAvailableOptions] = useState(options);
    const [isLocked, setIsLocked] = useState(false);

    const handleSelect = (word) => {
        if (isLocked) return;
        setCurrentOrder([...currentOrder, word]);
        setAvailableOptions(availableOptions.filter(w => w !== word));
    };

    const handleReset = () => {
        if (isLocked) return;
        setCurrentOrder([]);
        setAvailableOptions(options);
    };

    const checkAnswer = () => {
        const attempt = currentOrder.join(" ");
        onAnswer(attempt === correctAnswer ? 'correct' : 'incorrect', attempt);
        setIsLocked(true);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-gray-50 p-4 rounded-xl min-h-[60px] flex flex-wrap gap-2 border-2 border-dashed border-gray-300 items-center justify-center">
                {currentOrder.map((word, idx) =>
                    <span key={idx} className="px-3 py-2 bg-blue-100 text-blue-700 rounded-lg font-bold shadow-sm">{word}</span>
                )}
            </div>
            <div className="flex flex-wrap gap-2 justify-center">
                {availableOptions.map((word, idx) =>
                    <button
                        key={idx}
                        onClick={() => handleSelect(word)}
                        disabled={isLocked}
                        className={`px-4 py-2 bg-white border border-gray-300 text-gray-800 rounded-xl shadow-sm hover:bg-gray-50 font-medium transition ${isLocked ? 'opacity-70 cursor-not-allowed text-gray-800' : ''}`}
                    >
                        {word || ''}
                    </button>
                )}
            </div>
            <div className="flex gap-3">
                <button onClick={handleReset} disabled={isLocked} className="p-3 text-gray-500 hover:bg-gray-100 rounded-xl transition disabled:opacity-50"><RefreshCcw size={20} /></button>
                <button
                    onClick={checkAnswer}
                    disabled={isLocked}
                    className="flex-grow py-3 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white rounded-xl font-bold shadow-md transition transform hover:scale-[1.02] disabled:bg-gray-500"
                >
                    Check
                </button>
            </div>
        </div>
    );
};

ArrangeExercise.displayName = 'ArrangeExercise';

export default ArrangeExercise;
