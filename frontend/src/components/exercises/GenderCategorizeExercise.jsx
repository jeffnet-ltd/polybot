/**
 * GenderCategorizeExercise Component
 *
 * An interactive exercise for categorizing words by gender (masculine/feminine).
 * Features drag-and-drop functionality and click-based interaction for mobile devices.
 */

import React, { useState, useEffect } from 'react';
import { RefreshCcw } from 'lucide-react';

const GenderCategorizeExercise = ({ prompt, words, correctAnswers, columns, items, onAnswer }) => {
    const [maschileWords, setMaschileWords] = useState([]);
    const [femminileWords, setFemminileWords] = useState([]);
    const [bothWords, setBothWords] = useState([]);
    const [isLocked, setIsLocked] = useState(false);
    const [draggedItem, setDraggedItem] = useState(null);

    // Detect format and normalize data
    const [normalizedWords, normalizedAnswers] = React.useMemo(() => {
        // New format: columns + items
        if (items && columns) {
            const wordsList = items.map(item => item.text);
            const answersMap = {};

            items.forEach(item => {
                // Map column_id to actual category name
                if (item.column_id === 'masc') {
                    answersMap[item.text] = 'maschile';
                } else if (item.column_id === 'fem') {
                    answersMap[item.text] = 'femminile';
                } else if (item.column_id === 'both') {
                    answersMap[item.text] = 'both';
                }
            });

            return [wordsList, answersMap];
        }

        // Old format: words + correctAnswers
        return [words, correctAnswers];
    }, [words, correctAnswers, items, columns]);

    const [availableWords, setAvailableWords] = useState([...normalizedWords]);

    // Reset all state when words change (new exercise)
    useEffect(() => {
        setMaschileWords([]);
        setFemminileWords([]);
        setBothWords([]);
        setIsLocked(false);
        setDraggedItem(null);
        const shuffled = [...normalizedWords].sort(() => Math.random() - 0.5);
        setAvailableWords(shuffled);
    }, [normalizedWords]);

    const handleDragStart = (e, word, source) => {
        setDraggedItem({ word, source });
        e.dataTransfer.effectAllowed = 'move';
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    };

    const handleDrop = (e, targetColumn) => {
        e.preventDefault();
        if (!draggedItem || isLocked) return;

        const { word, source } = draggedItem;

        // Remove from source
        if (source === 'available') {
            setAvailableWords(prev => prev.filter(w => w !== word));
        } else if (source === 'maschile') {
            setMaschileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'femminile') {
            setFemminileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'both') {
            setBothWords(prev => prev.filter(w => w !== word));
        }

        // Add to target
        if (targetColumn === 'maschile') {
            setMaschileWords(prev => [...prev, word]);
        } else if (targetColumn === 'femminile') {
            setFemminileWords(prev => [...prev, word]);
        } else if (targetColumn === 'both') {
            setBothWords(prev => [...prev, word]);
        } else if (targetColumn === 'available') {
            setAvailableWords(prev => [...prev, word]);
        }

        setDraggedItem(null);
    };

    const handleClick = (word, source) => {
        if (isLocked) return;

        // Remove from source
        if (source === 'available') {
            setAvailableWords(prev => prev.filter(w => w !== word));
        } else if (source === 'maschile') {
            setMaschileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'femminile') {
            setFemminileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'both') {
            setBothWords(prev => prev.filter(w => w !== word));
        }

        // Toggle between columns or return to available
        // For simplicity, clicking moves it back to available
        setAvailableWords(prev => [...prev, word]);
    };

    const handleReset = () => {
        if (isLocked) return;
        setMaschileWords([]);
        setFemminileWords([]);
        setBothWords([]);
        const shuffled = [...normalizedWords].sort(() => Math.random() - 0.5);
        setAvailableWords(shuffled);
    };

    const checkAnswer = () => {
        let allCorrect = true;
        const mistakes = [];

        // Check all words are placed
        if (maschileWords.length + femminileWords.length + bothWords.length !== normalizedWords.length) {
            allCorrect = false;
        }

        // Check maschile words
        maschileWords.forEach(word => {
            if (normalizedAnswers[word] !== 'maschile') {
                allCorrect = false;
                const correct = normalizedAnswers[word];
                mistakes.push(`${word} should be ${correct === 'femminile' ? 'Femminile' : correct === 'both' ? 'BOTH' : 'Maschile'}`);
            }
        });

        // Check femminile words
        femminileWords.forEach(word => {
            if (normalizedAnswers[word] !== 'femminile') {
                allCorrect = false;
                const correct = normalizedAnswers[word];
                mistakes.push(`${word} should be ${correct === 'maschile' ? 'Maschile' : correct === 'both' ? 'BOTH' : 'Femminile'}`);
            }
        });

        // Check both words
        bothWords.forEach(word => {
            if (normalizedAnswers[word] !== 'both') {
                allCorrect = false;
                const correct = normalizedAnswers[word];
                mistakes.push(`${word} should be ${correct === 'maschile' ? 'Maschile' : correct === 'femminile' ? 'Femminile' : 'BOTH'}`);
            }
        });

        // Check all words are placed
        availableWords.forEach(word => {
            allCorrect = false;
            mistakes.push(`${word} needs to be placed in a column`);
        });

        onAnswer(allCorrect ? 'correct' : 'incorrect', { maschile: maschileWords, femminile: femminileWords, both: bothWords });
        setIsLocked(true);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>

            {/* Three columns layout */}
            <div className="grid grid-cols-3 gap-4">
                {/* Maschile Column */}
                <div
                    onDragOver={handleDragOver}
                    onDrop={(e) => handleDrop(e, 'maschile')}
                    className="bg-blue-50 p-6 rounded-xl min-h-[300px] border-2 border-dashed border-blue-400 transition hover:border-blue-500"
                >
                    <h4 className="text-lg font-bold text-blue-700 mb-4 text-center">Maschile</h4>
                    <div className="flex flex-col gap-2 min-h-[200px]">
                        {maschileWords.length === 0 ? (
                            <p className="text-gray-400 text-sm text-center mt-8">Drag words here</p>
                        ) : (
                            maschileWords.map((word, idx) => (
                                <span
                                    key={idx}
                                    draggable={!isLocked}
                                    onDragStart={(e) => handleDragStart(e, word, 'maschile')}
                                    onClick={() => handleClick(word, 'maschile')}
                                    className="px-4 py-3 bg-blue-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-blue-600 transition text-center"
                                >
                                    {word}
                                </span>
                            ))
                        )}
                    </div>
                </div>

                {/* Femminile Column */}
                <div
                    onDragOver={handleDragOver}
                    onDrop={(e) => handleDrop(e, 'femminile')}
                    className="bg-pink-50 p-6 rounded-xl min-h-[300px] border-2 border-dashed border-pink-400 transition hover:border-pink-500"
                >
                    <h4 className="text-lg font-bold text-pink-700 mb-4 text-center">Femminile</h4>
                    <div className="flex flex-col gap-2 min-h-[200px]">
                        {femminileWords.length === 0 ? (
                            <p className="text-gray-400 text-sm text-center mt-8">Drag words here</p>
                        ) : (
                            femminileWords.map((word, idx) => (
                                <span
                                    key={idx}
                                    draggable={!isLocked}
                                    onDragStart={(e) => handleDragStart(e, word, 'femminile')}
                                    onClick={() => handleClick(word, 'femminile')}
                                    className="px-4 py-3 bg-pink-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-pink-600 transition text-center"
                                >
                                    {word}
                                </span>
                            ))
                        )}
                    </div>
                </div>

                {/* Both Column */}
                <div
                    onDragOver={handleDragOver}
                    onDrop={(e) => handleDrop(e, 'both')}
                    className="bg-indigo-50 p-6 rounded-xl min-h-[300px] border-2 border-dashed border-indigo-400 transition hover:border-indigo-500"
                >
                    <h4 className="text-lg font-bold text-indigo-700 mb-4 text-center">BOTH</h4>
                    <div className="flex flex-col gap-2 min-h-[200px]">
                        {bothWords.length === 0 ? (
                            <p className="text-gray-400 text-sm text-center mt-8">Drag words here</p>
                        ) : (
                            bothWords.map((word, idx) => (
                                <span
                                    key={idx}
                                    draggable={!isLocked}
                                    onDragStart={(e) => handleDragStart(e, word, 'both')}
                                    onClick={() => handleClick(word, 'both')}
                                    className="px-4 py-3 bg-indigo-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-indigo-600 transition text-center"
                                >
                                    {word}
                                </span>
                            ))
                        )}
                    </div>
                </div>
            </div>

            {/* Available words in center */}
            {availableWords.length > 0 && (
                <div className="space-y-2">
                    <p className="text-sm text-gray-500 font-medium text-center">Drag words to the correct column:</p>
                    <div className="flex flex-wrap gap-2 justify-center">
                        {availableWords.map((word, idx) => (
                            <span
                                key={idx}
                                draggable={!isLocked}
                                onDragStart={(e) => handleDragStart(e, word, 'available')}
                                onClick={() => handleClick(word, 'available')}
                                className="px-4 py-2 bg-white border-2 border-gray-300 text-gray-800 rounded-lg font-medium shadow-sm cursor-move hover:bg-gray-50 hover:border-blue-400 transition"
                            >
                                {word}
                            </span>
                        ))}
                    </div>
                </div>
            )}

            {/* Controls */}
            <div className="flex gap-3">
                <button
                    onClick={handleReset}
                    disabled={isLocked}
                    className="p-3 text-gray-500 hover:bg-gray-100 rounded-xl transition disabled:opacity-50"
                >
                    <RefreshCcw size={20} />
                </button>
                <button
                    onClick={checkAnswer}
                    disabled={isLocked || (maschileWords.length === 0 && femminileWords.length === 0 && bothWords.length === 0)}
                    className="flex-grow py-3 bg-[#4CAF50] text-white rounded-xl font-bold shadow-md hover:bg-[#388E3C] transition disabled:bg-gray-500 disabled:cursor-not-allowed"
                >
                    Check Answer
                </button>
            </div>
        </div>
    );
};

GenderCategorizeExercise.displayName = 'GenderCategorizeExercise';

export default GenderCategorizeExercise;
