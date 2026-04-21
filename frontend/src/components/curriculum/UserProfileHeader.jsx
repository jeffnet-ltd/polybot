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

    // Level thresholds: 1→0-100, 2→101-300, 3→301-600, 4→601-1000, 5→1000+
    const LEVELS = [
        { level: 1, min: 0,   max: 100,  label: 'Novice' },
        { level: 2, min: 101, max: 300,  label: 'Beginner' },
        { level: 3, min: 301, max: 600,  label: 'Elementary' },
        { level: 4, min: 601, max: 1000, label: 'Intermediate' },
        { level: 5, min: 1001,max: Infinity, label: 'Advanced' },
    ];
    const xp = userProfile.xp || 0;
    const currentLevel = LEVELS.find(l => xp >= l.min && xp <= l.max) || LEVELS[LEVELS.length - 1];
    const nextLevel = LEVELS.find(l => l.level === currentLevel.level + 1);
    const levelGoal = nextLevel ? nextLevel.min - currentLevel.min : 1;
    const xpProgress = nextLevel ? xp - currentLevel.min : levelGoal;
    const progressPercentage = Math.min((xpProgress / levelGoal) * 100, 100);

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
                        <p className="text-xs text-gray-500">Level {currentLevel.level} · {currentLevel.label}</p>
                    </div>
                </div>

                {/* Language Flag and Level Badge */}
                <div className="flex items-center gap-3">
                    <span className="text-3xl">{getLanguageFlag(userProfile.target_language)}</span>
                    <div className="bg-gradient-to-br from-brand-lime-50 to-emerald-50 px-3 py-1 rounded-lg border border-brand-lime-200">
                        <p className="text-xs font-semibold text-brand-lime-700">Lv.{currentLevel.level}</p>
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
                    <span className="font-medium">Lv.{currentLevel.level} {currentLevel.label}</span>
                    {nextLevel && <>
                        <span className="text-gray-400 mx-2">→</span>
                        <span className="font-medium text-gray-400">Lv.{nextLevel.level} {nextLevel.label}</span>
                    </>}
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
