/**
 * UserProfileHeader Component
 *
 * Enhanced profile header showing:
 * - User greeting with name
 * - XP progress bar
 * - Current level and target level
 * - Learning streak
 * - Target language flag
 */

import React from 'react';
import { Flame } from 'lucide-react';

const UserProfileHeader = ({ userProfile, t }) => {
    if (!userProfile) return null;

    // Calculate XP progress (this would come from backend in a real app)
    const levelGoal = 1000; // XP needed per level
    const xpProgress = (userProfile.xp || 0) % levelGoal;
    const progressPercentage = (xpProgress / levelGoal) * 100;

    const getLanguageFlag = (langCode) => {
        const flags = {
            it: '🇮🇹',
            es: '🇪🇸',
            fr: '🇫🇷',
            de: '🇩🇪',
            pt: '🇵🇹',
            ja: '🇯🇵',
            ko: '🇰🇷',
            zh: '🇨🇳',
        };
        return flags[langCode] || '🌍';
    };

    return (
        <div className="bg-white rounded-2xl p-6 shadow-elevation-3 mb-6 border border-gray-100 animate-slide-up">
            {/* Header Row: Avatar, Name, Level Badge */}
            <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-4">
                    {/* Avatar - Brand Teal Gradient */}
                    <div className="w-12 h-12 rounded-full bg-gradient-to-br from-brand-lime-400 to-brand-lime-600 flex items-center justify-center text-white font-bold text-lg shadow-elevation-2 hover:shadow-elevation-3 transition-smooth-fast">
                        {userProfile.name ? userProfile.name[0].toUpperCase() : 'U'}
                    </div>

                    {/* Name and Greeting */}
                    <div>
                        <h2 className="text-lg font-semibold text-gray-800">
                            Hi, {userProfile.name?.split(' ')[0] || 'Learner'}
                        </h2>
                        <p className="text-xs text-gray-500">A1 Beginner</p>
                    </div>
                </div>

                {/* Language Flag and Level Badge */}
                <div className="flex items-center gap-3">
                    <span className="text-3xl">{getLanguageFlag(userProfile.target_language)}</span>
                    <div className="bg-gradient-to-br from-brand-lime-50 to-emerald-50 px-3 py-1 rounded-lg border border-brand-lime-200">
                        <p className="text-xs font-semibold text-brand-lime-700">A1</p>
                    </div>
                </div>
            </div>

            {/* Progress Bar */}
            <div className="mb-4">
                <div className="flex items-center justify-between mb-2">
                    <p className="text-xs font-medium text-gray-600">Daily Progress</p>
                    <p className="text-xs text-gray-500">{Math.round(progressPercentage)}%</p>
                </div>
                <div className="relative h-2 bg-gray-200 rounded-full overflow-hidden">
                    <div
                        className="absolute h-full bg-gradient-to-r from-brand-lime-400 to-brand-lime-600 transition-smooth"
                        style={{ width: `${progressPercentage}%` }}
                    />
                </div>
            </div>

            {/* Footer Row: Level progression and streak */}
            <div className="flex items-center justify-between">
                <div className="text-sm text-gray-700">
                    <span className="font-medium">A1 Beginner</span>
                    <span className="text-gray-400 mx-2">→</span>
                    <span className="font-medium">A1 Tiropót</span>
                </div>

                {/* Streak */}
                <div className="flex items-center gap-1">
                    <Flame className="w-4 h-4 text-orange-500 animate-bounce" />
                    <span className="text-sm font-semibold text-orange-600">
                        {userProfile.streak || 0} days
                    </span>
                </div>
            </div>
        </div>
    );
};

UserProfileHeader.displayName = 'UserProfileHeader';

export default UserProfileHeader;
