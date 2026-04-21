/**
 * ProgressView Component
 * Displays user progress with XP, words learned, and streak
 */

import React, { useMemo } from 'react';
import { Zap, BookOpen, Trophy } from 'lucide-react';
import ProgressCard from '../common/ProgressCard';

const ProgressView = React.memo(({ userProfile }) => {
    const vocabBreakdown = useMemo(() => {
        const vocab = (userProfile.vocabulary_list || []).filter(v => !v.is_header);
        return {
            weak:   vocab.filter(v => v.proficiency < 40).length,
            medium: vocab.filter(v => v.proficiency >= 40 && v.proficiency <= 70).length,
            strong: vocab.filter(v => v.proficiency > 70).length,
            total:  vocab.length,
        };
    }, [userProfile.vocabulary_list]);

    return (
    <div className="p-4 space-y-6">
        <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">Your Progress</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <ProgressCard icon={Zap} title="Total XP" value={userProfile.xp} color="bg-yellow-500" subtitle={`Today: ${userProfile.daily_xp || 0} XP`} />
            <ProgressCard icon={BookOpen} title="Words" value={userProfile.words_learned} color="bg-green-500" />
            <ProgressCard icon={Trophy} title="Streak" value={userProfile.streak} color="bg-red-500" />
        </div>

        {vocabBreakdown.total > 0 && (
            <div className="bg-white rounded-xl p-5 shadow border border-gray-100">
                <h3 className="font-semibold text-gray-800 mb-4">Vocabulary Breakdown</h3>
                <div className="space-y-3">
                    {[
                        { label: 'Strong', count: vocabBreakdown.strong, colour: 'bg-green-500', text: 'text-green-600' },
                        { label: 'Medium', count: vocabBreakdown.medium, colour: 'bg-yellow-400', text: 'text-yellow-600' },
                        { label: 'Weak',   count: vocabBreakdown.weak,   colour: 'bg-red-400',   text: 'text-red-600'   },
                    ].map(({ label, count, colour, text }) => (
                        <div key={label}>
                            <div className="flex justify-between text-sm mb-1">
                                <span className={`font-medium ${text}`}>{label}</span>
                                <span className="text-gray-500">{count} / {vocabBreakdown.total}</span>
                            </div>
                            <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                                <div
                                    className={`h-full ${colour} rounded-full transition-all duration-500`}
                                    style={{ width: `${vocabBreakdown.total ? (count / vocabBreakdown.total) * 100 : 0}%` }}
                                />
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        )}
    </div>
    );
});

ProgressView.displayName = 'ProgressView';

export default ProgressView;
