/**
 * ProgressView Component
 * Displays user progress with XP, words learned, and streak
 */

import React from 'react';
import { Zap, BookOpen, Trophy } from 'lucide-react';
import ProgressCard from '../common/ProgressCard';

const ProgressView = React.memo(({ userProfile }) => (
    <div className="p-4 space-y-6">
        <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">Your Progress</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <ProgressCard icon={Zap} title="Total XP" value={userProfile.xp} color="bg-yellow-500" subtitle={`Today: ${userProfile.daily_xp || 0} XP`} />
            <ProgressCard icon={BookOpen} title="Words" value={userProfile.words_learned} color="bg-green-500" />
            <ProgressCard icon={Trophy} title="Streak" value={userProfile.streak} color="bg-red-500" />
        </div>
    </div>
));

ProgressView.displayName = 'ProgressView';

export default ProgressView;
