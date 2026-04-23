/**
 * VocabularyView Component
 * Displays user's learned vocabulary with proficiency levels
 */

import React, { useState, useEffect } from 'react';
import { Volume2, RotateCcw } from 'lucide-react';
import { speakText } from '../../utils/audio';
import apiClient from '../../services/api';
import ReviewSession from './ReviewSession';

const VocabularyView = React.memo(({ userProfile, targetLang }) => {
    const [wordsDue, setWordsDue] = useState(0);
    const [showReview, setShowReview] = useState(false);

    useEffect(() => {
        if (!userProfile?.user_id) return;
        apiClient.get(`/api/vocabulary/due?user_id=${userProfile.user_id}`)
            .then(res => setWordsDue(res.data.length))
            .catch(() => {});
    }, [userProfile?.user_id]);

    const filteredVocab = userProfile.vocabulary_list.filter(word =>
        word.target_lang === targetLang
    );

    return (
        <div className="p-4 space-y-6">
            <div className="flex items-center justify-between border-b pb-2">
                <h2 className="text-2xl font-bold text-gray-800">My Vocabulary</h2>
                {wordsDue > 0 && (
                    <button
                        onClick={() => setShowReview(true)}
                        className="flex items-center gap-2 px-4 py-2 bg-teal-600 text-white rounded-xl font-semibold text-sm hover:bg-teal-700 transition"
                    >
                        <RotateCcw size={15} />
                        Review {wordsDue} word{wordsDue !== 1 ? 's' : ''}
                    </button>
                )}
            </div>

            {showReview && (
                <ReviewSession
                    userProfile={userProfile}
                    onClose={() => { setShowReview(false); setWordsDue(0); }}
                    onXpEarned={(xp) => console.log(`Review earned ${xp} XP`)}
                />
            )}

            {!filteredVocab || filteredVocab.length === 0 ? (
                <div className="bg-white p-6 rounded-2xl shadow-xl border border-gray-100 min-h-64 flex items-center justify-center">
                    <p className="text-gray-500 text-lg">Complete lessons to build your vocabulary!</p>
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {filteredVocab.map((word, idx) => (
                        // Render Section Header if present
                        word.is_header ? (
                            <div key={idx} className="col-span-full mt-4 mb-2">
                                <h3 className="text-lg font-bold text-gray-700 border-b pb-1">
                                    {word.term.replace(/---/g, '').trim()}
                                </h3>
                            </div>
                        ) : (
                            <div key={idx} className="bg-white p-4 rounded-xl border border-gray-200 shadow-sm flex justify-between items-center">
                                <div>
                                    <p className="text-xl font-bold text-gray-800">{word.term}</p>
                                    <p className="text-sm text-gray-500">{word.translation}</p>
                                    <div className="mt-2 w-32 h-2 bg-gray-100 rounded-full overflow-hidden">
                                        <div className="h-full bg-green-500" style={{ width: `${word.proficiency}%` }}></div>
                                    </div>
                                    <p className="text-xs text-green-600 mt-1">{Math.round(word.proficiency)}% Proficiency</p>
                                </div>
                                <button
                                    onClick={() => speakText(word.term, targetLang)}
                                    className="p-2 text-gray-400 hover:text-blue-500 hover:bg-blue-50 rounded-full transition"
                                >
                                    <Volume2 size={20} />
                                </button>
                            </div>
                        )
                    ))}
                </div>
            )}
        </div>
    );
});

VocabularyView.displayName = 'VocabularyView';

export default VocabularyView;
