/**
 * UnscrambleExercise Component
 *
 * An interactive exercise where users unscramble words/blocks to form correct sentences.
 * Features drag-and-drop and click-based interaction with intelligent answer validation.
 */

import React, { useState, useEffect } from 'react';
import { RefreshCcw } from 'lucide-react';

const UnscrambleExercise = ({ prompt, blocks, correctAnswer, onAnswer }) => {
    const [draggedBlocks, setDraggedBlocks] = useState([]);
    const [availableBlocks, setAvailableBlocks] = useState([...blocks]);
    const [isLocked, setIsLocked] = useState(false);
    const [draggedItem, setDraggedItem] = useState(null);

    // Reset all state when blocks change (new exercise)
    useEffect(() => {
        setDraggedBlocks([]);
        setIsLocked(false);
        setDraggedItem(null);
        const shuffled = [...blocks].sort(() => Math.random() - 0.5);
        setAvailableBlocks(shuffled);
    }, [blocks]);

    const handleDragStart = (e, block, source) => {
        setDraggedItem({ block, source });
        e.dataTransfer.effectAllowed = 'move';
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    };

    const handleDrop = (e, targetArea) => {
        e.preventDefault();
        if (!draggedItem || isLocked) return;

        const { block, source } = draggedItem;

        if (source === 'available' && targetArea === 'answer') {
            // Move from available to answer area
            setAvailableBlocks(prev => prev.filter(b => b !== block));
            setDraggedBlocks(prev => [...prev, block]);
        } else if (source === 'answer' && targetArea === 'available') {
            // Move from answer back to available
            setDraggedBlocks(prev => prev.filter(b => b !== block));
            setAvailableBlocks(prev => [...prev, block]);
        }

        setDraggedItem(null);
    };

    const handleClick = (block, source) => {
        if (isLocked) return;
        if (source === 'available') {
            setAvailableBlocks(prev => prev.filter(b => b !== block));
            setDraggedBlocks(prev => [...prev, block]);
        } else {
            setDraggedBlocks(prev => prev.filter(b => b !== block));
            setAvailableBlocks(prev => [...prev, block]);
        }
    };

    const handleReset = () => {
        if (isLocked) return;
        setDraggedBlocks([]);
        const shuffled = [...blocks].sort(() => Math.random() - 0.5);
        setAvailableBlocks(shuffled);
    };

    const checkAnswer = () => {
        const attempt = draggedBlocks.join(" ");
        // Normalize both strings: lowercase, trim, normalize multiple spaces
        // Remove all punctuation (including commas) and extra spaces for comparison
        // This makes the validation more lenient - accepts answers with or without commas
        const normalize = (str) => {
            return str.toLowerCase()
                .trim()
                .replace(/\s+/g, ' ')  // Replace multiple spaces with single space
                .replace(/[,.!?;:]/g, '')  // Remove all punctuation including commas
                .trim();
        };
        const normalizedAttempt = normalize(attempt);
        const normalizedCorrect = normalize(correctAnswer);
        const isCorrect = normalizedAttempt === normalizedCorrect;
        onAnswer(isCorrect ? 'correct' : 'incorrect', attempt);
        setIsLocked(true);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>

            {/* Answer area (drop zone) */}
            <div
                onDragOver={handleDragOver}
                onDrop={(e) => handleDrop(e, 'answer')}
                className="bg-gray-50 p-6 rounded-xl min-h-[80px] flex flex-wrap gap-3 border-2 border-dashed border-blue-300 items-center justify-center transition hover:border-blue-400"
            >
                {draggedBlocks.length === 0 ? (
                    <p className="text-gray-400 text-sm">Drag words here to build your sentence</p>
                ) : (
                    draggedBlocks.map((block, idx) => (
                        <span
                            key={idx}
                            draggable={!isLocked}
                            onDragStart={(e) => handleDragStart(e, block, 'answer')}
                            onClick={() => handleClick(block, 'answer')}
                            className="px-4 py-3 bg-blue-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-blue-600 transition"
                        >
                            {block}
                        </span>
                    ))
                )}
            </div>

            {/* Available blocks */}
            <div className="space-y-2">
                <p className="text-sm text-gray-500 font-medium">Available words:</p>
                <div className="flex flex-wrap gap-2">
                    {availableBlocks.map((block, idx) => (
                        <span
                            key={idx}
                            draggable={!isLocked}
                            onDragStart={(e) => handleDragStart(e, block, 'available')}
                            onClick={() => handleClick(block, 'available')}
                            className="px-4 py-2 bg-white border-2 border-gray-300 text-gray-800 rounded-lg font-medium shadow-sm cursor-move hover:bg-gray-50 hover:border-blue-400 transition"
                        >
                            {block}
                        </span>
                    ))}
                </div>
            </div>

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
                    disabled={isLocked || draggedBlocks.length === 0}
                    className="flex-grow py-3 bg-[#4CAF50] text-white rounded-xl font-bold shadow-md hover:bg-[#388E3C] transition disabled:bg-gray-500 disabled:cursor-not-allowed"
                >
                    Check Answer
                </button>
            </div>
        </div>
    );
};

UnscrambleExercise.displayName = 'UnscrambleExercise';

export default UnscrambleExercise;
