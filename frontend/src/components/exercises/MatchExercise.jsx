/**
 * MatchExercise Component
 *
 * A vocabulary matching exercise pairing target language with native language.
 * Features click-to-match interaction with audio pronunciation support.
 */

import React, { useState, useEffect, useMemo } from 'react';
import { speakText } from '../../utils/audio';

const MatchExercise = ({ pairs, onAnswer, targetLang }) => {
    const [selectedLeft, setSelectedLeft] = useState(null);
    const [matchedPairs, setMatchedPairs] = useState([]);
    const [failedPairs, setFailedPairs] = useState([]); // Stores items that were matched incorrectly
    const [isLocked, setIsLocked] = useState(false);

    // Ensure Italian (target language) is on the left, English on the right
    // Data structure: pairs = [[Italian, English], ...] based on a1_1_module_data.py
    // So p[0] is Italian (left), p[1] is English (right)
    const leftSide = useMemo(() => {
        if (!pairs || !Array.isArray(pairs) || pairs.length === 0) return [];
        return pairs.map(p => p[0]).filter(Boolean);
    }, [pairs]); // Italian on left
    const rightSide = useMemo(() => {
        if (!pairs || !Array.isArray(pairs) || pairs.length === 0) return [];
        return pairs.map(p => p[1]).filter(Boolean).sort(() => Math.random() - 0.5);
    }, [pairs]); // English on right

    // Reset state when pairs change (new exercise)
    useEffect(() => {
        setSelectedLeft(null);
        setMatchedPairs([]);
        setFailedPairs([]);
        setIsLocked(false);
    }, [pairs]);

    // Effect: Check for completion
    useEffect(() => {
        const totalItems = pairs.length * 2;
        const processed = matchedPairs.length + failedPairs.length;

        if (totalItems > 0 && processed === totalItems && !isLocked) {
            setIsLocked(true);
            const isPerfect = failedPairs.length === 0;
            onAnswer(isPerfect ? 'correct' : 'incorrect', isPerfect ? "All matched!" : "Completed with errors.");
        }
    }, [matchedPairs, failedPairs, pairs, isLocked, onAnswer]);

    const handleLeftClick = (item) => {
        if (isLocked) return;
        // Allow click only if not already matched AND not failed
        if (!matchedPairs.includes(item) && !failedPairs.includes(item)) {
            setSelectedLeft(item);
            speakText(item, targetLang);
        }
    };

    const handleRightClick = (item) => {
        if (isLocked) return;
        if (matchedPairs.includes(item) || failedPairs.includes(item)) return;

        if (selectedLeft) {
            // Check if selectedLeft (Italian, p[0]) matches item (English, p[1])
            const isMatch = pairs.find(p => p[0] === selectedLeft && p[1] === item);

            if (isMatch) {
                setMatchedPairs(prev => [...prev, selectedLeft, item]);
            } else {
                // Mismatch: Add both to failedPairs, locking them out (red)
                setFailedPairs(prev => [...prev, selectedLeft, item]);
            }
            setSelectedLeft(null);
        }
    };

    return (
        <div className="space-y-4">
            <h3 className="text-xl font-semibold text-gray-800 text-center">Match Pairs</h3>
            <div className="grid grid-cols-2 gap-4">
                <div className="flex flex-col gap-3">
                    {leftSide.map((item, idx) => {
                        const isMatched = matchedPairs.includes(item);
                        const isFailed = failedPairs.includes(item);
                        const isSelected = selectedLeft === item;

                        let baseClass = "p-4 rounded-xl border text-left font-medium transition flex justify-between ";

                        if (isMatched) {
                            baseClass += "bg-green-50 border-green-200 text-green-800 opacity-50 cursor-not-allowed";
                        } else if (isFailed) {
                            baseClass += "bg-red-50 border-red-200 text-red-800 opacity-60 cursor-not-allowed";
                        } else if (isSelected) {
                            baseClass += "bg-blue-50 border-blue-500 text-blue-700 ring-2 ring-blue-200 cursor-pointer";
                        } else {
                            baseClass += "bg-white border-gray-200 hover:bg-gray-50 cursor-pointer";
                        }

                        return (
                            <button
                                key={idx}
                                onClick={(e) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    handleLeftClick(item);
                                }}
                                disabled={isMatched || isFailed || isLocked}
                                className={baseClass}
                                type="button"
                            >
                                {item}
                            </button>
                        );
                    })}
                </div>
                <div className="flex flex-col gap-3">
                    {rightSide.map((item, idx) => {
                        const isMatched = matchedPairs.includes(item);
                        const isFailed = failedPairs.includes(item);

                        let baseClass = "p-4 rounded-xl border text-left font-medium transition ";
                        if (isMatched) {
                            baseClass += "bg-green-50 border-green-200 text-green-800 opacity-50 cursor-not-allowed";
                        } else if (isFailed) {
                            baseClass += "bg-red-50 border-red-200 text-red-800 opacity-60 cursor-not-allowed";
                        } else {
                            baseClass += "bg-white border-gray-200 hover:bg-gray-50 cursor-pointer";
                        }

                        return (
                            <button
                                key={idx}
                                onClick={(e) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    handleRightClick(item);
                                }}
                                disabled={isMatched || isFailed || isLocked}
                                className={baseClass}
                                type="button"
                            >
                                {item}
                            </button>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

MatchExercise.displayName = 'MatchExercise';

export default MatchExercise;
