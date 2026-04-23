import React, { useState, useEffect, useCallback } from 'react';
import { CheckCircle, XCircle, RotateCcw, ChevronRight } from 'lucide-react';
import { API } from '../../config/constants';
import apiClient from '../../services/api';

const ReviewSession = ({ userProfile, onClose, onXpEarned }) => {
    const [cards, setCards] = useState([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [flipped, setFlipped] = useState(false);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [results, setResults] = useState([]);
    const [done, setDone] = useState(false);

    useEffect(() => {
        const fetchDue = async () => {
            try {
                const res = await apiClient.get(`/api/vocabulary/due?user_id=${userProfile.user_id}`);
                setCards(res.data);
            } catch (e) {
                setError('Could not load review cards.');
            } finally {
                setLoading(false);
            }
        };
        fetchDue();
    }, [userProfile.user_id]);

    const submitAnswer = useCallback(async (difficulty) => {
        const card = cards[currentIndex];
        const correct = difficulty !== 'hard';
        try {
            await apiClient.post('/api/vocabulary/review', {
                user_id: userProfile.user_id,
                term: card.term,
                target_lang: card.target_lang,
                correct,
                difficulty,
            });
        } catch (_) {}

        setResults(prev => [...prev, { card, correct, difficulty }]);

        if (currentIndex + 1 >= cards.length) {
            const xpEarned = cards.length * 5;
            if (onXpEarned) onXpEarned(xpEarned);
            setDone(true);
        } else {
            setCurrentIndex(i => i + 1);
            setFlipped(false);
        }
    }, [cards, currentIndex, userProfile.user_id, onXpEarned]);

    if (loading) {
        return (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                <div className="bg-white rounded-2xl p-8 text-center">
                    <p className="text-gray-600">Loading review cards...</p>
                </div>
            </div>
        );
    }

    if (error || cards.length === 0) {
        return (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                <div className="bg-white rounded-2xl p-8 text-center max-w-sm w-full mx-4">
                    <CheckCircle className="w-12 h-12 text-green-500 mx-auto mb-3" />
                    <h2 className="text-xl font-bold text-gray-800 mb-2">All caught up!</h2>
                    <p className="text-gray-500 mb-6">{error || 'No words are due for review right now.'}</p>
                    <button onClick={onClose} className="w-full py-3 bg-teal-600 text-white rounded-xl font-semibold hover:bg-teal-700">
                        Close
                    </button>
                </div>
            </div>
        );
    }

    if (done) {
        const correct = results.filter(r => r.correct).length;
        const weak = results.filter(r => r.card.category === 'weak').length;
        const medium = results.filter(r => r.card.category === 'medium').length;
        const strong = results.filter(r => r.card.category === 'strong').length;
        const xpEarned = cards.length * 5;

        return (
            <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                <div className="bg-white rounded-2xl p-8 max-w-sm w-full mx-4">
                    <div className="text-center mb-6">
                        <CheckCircle className="w-14 h-14 text-green-500 mx-auto mb-3" />
                        <h2 className="text-2xl font-bold text-gray-800">Session Complete!</h2>
                        <p className="text-teal-600 font-semibold mt-1">+{xpEarned} XP earned</p>
                    </div>
                    <div className="space-y-3 mb-6">
                        <div className="flex justify-between text-sm">
                            <span className="text-gray-600">Words reviewed</span>
                            <span className="font-bold">{cards.length}</span>
                        </div>
                        <div className="flex justify-between text-sm">
                            <span className="text-gray-600">Correct</span>
                            <span className="font-bold text-green-600">{correct}/{cards.length}</span>
                        </div>
                        <div className="h-px bg-gray-100" />
                        <div className="flex justify-between text-sm">
                            <span className="text-red-500">Weak words</span>
                            <span className="font-bold">{weak}</span>
                        </div>
                        <div className="flex justify-between text-sm">
                            <span className="text-yellow-500">Medium words</span>
                            <span className="font-bold">{medium}</span>
                        </div>
                        <div className="flex justify-between text-sm">
                            <span className="text-green-500">Strong words</span>
                            <span className="font-bold">{strong}</span>
                        </div>
                    </div>
                    <button onClick={onClose} className="w-full py-3 bg-teal-600 text-white rounded-xl font-semibold hover:bg-teal-700">
                        Done
                    </button>
                </div>
            </div>
        );
    }

    const card = cards[currentIndex];
    const progress = ((currentIndex) / cards.length) * 100;

    const categoryColour = { weak: 'bg-red-100 text-red-600', medium: 'bg-yellow-100 text-yellow-600', strong: 'bg-green-100 text-green-600' };

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-2xl w-full max-w-md shadow-2xl">
                {/* Header */}
                <div className="p-4 border-b flex items-center justify-between">
                    <span className="text-sm text-gray-500">{currentIndex + 1} / {cards.length}</span>
                    <span className={`text-xs font-semibold px-2 py-1 rounded-full ${categoryColour[card.category]}`}>
                        {card.category}
                    </span>
                    <button onClick={onClose} className="text-gray-400 hover:text-gray-600 text-sm">✕</button>
                </div>

                {/* Progress bar */}
                <div className="h-1 bg-gray-100">
                    <div className="h-full bg-teal-500 transition-all duration-300" style={{ width: `${progress}%` }} />
                </div>

                {/* Card */}
                <div
                    className="p-8 min-h-48 flex flex-col items-center justify-center cursor-pointer select-none"
                    onClick={() => !flipped && setFlipped(true)}
                >
                    {!flipped ? (
                        <div className="text-center">
                            <p className="text-3xl font-bold text-gray-800 mb-3">{card.term}</p>
                            <p className="text-sm text-gray-400">Tap to reveal</p>
                        </div>
                    ) : (
                        <div className="text-center">
                            <p className="text-3xl font-bold text-gray-800 mb-2">{card.term}</p>
                            <p className="text-xl text-teal-600 font-semibold mb-3">{card.translation}</p>
                            {card.context_sentence && (
                                <p className="text-sm text-gray-500 italic">"{card.context_sentence}"</p>
                            )}
                        </div>
                    )}
                </div>

                {/* Buttons */}
                {flipped ? (
                    <div className="p-4 border-t grid grid-cols-3 gap-3">
                        <button
                            onClick={() => submitAnswer('hard')}
                            className="flex flex-col items-center py-3 rounded-xl bg-red-50 hover:bg-red-100 border border-red-200 transition"
                        >
                            <XCircle className="w-5 h-5 text-red-500 mb-1" />
                            <span className="text-xs font-semibold text-red-600">Hard</span>
                        </button>
                        <button
                            onClick={() => submitAnswer('medium')}
                            className="flex flex-col items-center py-3 rounded-xl bg-yellow-50 hover:bg-yellow-100 border border-yellow-200 transition"
                        >
                            <RotateCcw className="w-5 h-5 text-yellow-500 mb-1" />
                            <span className="text-xs font-semibold text-yellow-600">Got it</span>
                        </button>
                        <button
                            onClick={() => submitAnswer('easy')}
                            className="flex flex-col items-center py-3 rounded-xl bg-green-50 hover:bg-green-100 border border-green-200 transition"
                        >
                            <ChevronRight className="w-5 h-5 text-green-500 mb-1" />
                            <span className="text-xs font-semibold text-green-600">Easy</span>
                        </button>
                    </div>
                ) : (
                    <div className="p-4 border-t">
                        <button
                            onClick={() => setFlipped(true)}
                            className="w-full py-3 bg-teal-600 text-white rounded-xl font-semibold hover:bg-teal-700"
                        >
                            Show Answer
                        </button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default ReviewSession;
