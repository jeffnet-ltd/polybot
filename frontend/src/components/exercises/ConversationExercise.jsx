/**
 * ConversationExercise Component
 * Fill-in-the-blank conversation exercise with word bank selection
 */

import React, { useState, useEffect } from 'react';

const ConversationExercise = ({ dialogue, options, onAnswer }) => {
    const [userAnswers, setUserAnswers] = useState({});
    const [availableWords, setAvailableWords] = useState(options);
    const [isChecked, setIsChecked] = useState(false);

    useEffect(() => {
        setUserAnswers({});
        setAvailableWords(options);
        setIsChecked(false);
    }, [dialogue, options]);

    const handleWordClick = (word) => {
        if (isChecked) return;
        const emptyIndex = dialogue.findIndex((line, idx) => line.missing_word && !userAnswers[idx]);

        if (emptyIndex !== -1) {
            setUserAnswers(prev => ({ ...prev, [emptyIndex]: word }));
            setAvailableWords(prev => {
                const idx = prev.indexOf(word);
                if (idx > -1) {
                    const newArr = [...prev];
                    newArr.splice(idx, 1);
                    return newArr;
                }
                return prev;
            });
        }
    };

    const handleSlotClick = (idx, word) => {
        if (isChecked || !word) return;
        setUserAnswers(prev => {
            const next = { ...prev };
            delete next[idx];
            return next;
        });
        setAvailableWords(prev => [...prev, word]);
    };

    const checkAnswers = () => {
        setIsChecked(true);
        const allCorrect = dialogue.every((line, idx) => {
            if (!line.missing_word) return true;
            return userAnswers[idx] === line.missing_word;
        });
        onAnswer(allCorrect ? 'correct' : 'incorrect', allCorrect ? "Conversation completed!" : "Some words are wrong.");
    };

    const isFull = dialogue.filter(l => l.missing_word).length === Object.keys(userAnswers).length;

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-bold text-gray-800 text-center">Complete the Conversation</h3>
            <div className="space-y-4 max-h-96 overflow-y-auto p-2">
                {dialogue.map((line, idx) => {
                    const isMe = line.speaker === 'B';
                    const parts = line.text.split('___');
                    const hasGap = line.missing_word;
                    const userAnswer = userAnswers[idx];

                    let gapStyle = "inline-block w-24 border-b-2 border-dashed border-gray-400 text-center mx-1 cursor-pointer text-blue-600 font-bold";
                    if (isChecked) {
                        if (userAnswer === line.missing_word) gapStyle = "inline-block px-2 py-1 rounded bg-green-100 text-green-700 font-bold border border-green-300";
                        else gapStyle = "inline-block px-2 py-1 rounded bg-red-100 text-red-700 font-bold border border-red-300";
                    }

                    return (
                        <div key={idx} className={`flex ${isMe ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-[85%] p-4 rounded-2xl ${isMe ? 'bg-blue-50 border-blue-100 rounded-br-none' : 'bg-gray-100 border-gray-200 rounded-tl-none'} border shadow-sm`}>
                                <p className="text-gray-800">
                                    {parts[0]}
                                    {hasGap && (
                                        <span className={gapStyle} onClick={() => handleSlotClick(idx, userAnswer)}>
                                            {userAnswer || (isChecked ? line.missing_word : "___")}
                                        </span>
                                    )}
                                    {parts[1]}
                                </p>
                                <p className="text-xs text-gray-400 mt-1">{line.translation}</p>
                            </div>
                        </div>
                    );
                })}
            </div>
            <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                <p className="text-xs text-gray-500 mb-2 text-center uppercase font-bold tracking-wider">Word Bank</p>
                <div className="flex flex-wrap gap-2 justify-center min-h-[50px]">
                    {availableWords.map((word, i) => (
                        <button key={i} onClick={() => handleWordClick(word)} disabled={isChecked} className="px-3 py-2 bg-white border border-gray-300 rounded-lg shadow-sm text-gray-800 font-semibold hover:bg-blue-50 hover:border-blue-300 transition disabled:opacity-70 disabled:text-gray-800">{word || ''}</button>
                    ))}
                </div>
            </div>
            <button onClick={checkAnswers} disabled={!isFull || isChecked} className={`w-full py-4 rounded-2xl font-bold text-white shadow-lg transition ${isFull && !isChecked ? 'bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 transform hover:scale-[1.02]' : 'bg-gray-300 cursor-not-allowed'}`}>Check Answers</button>
        </div>
    );
};

ConversationExercise.displayName = 'ConversationExercise';

export default ConversationExercise;
