/**
 * StreakWidget Component
 *
 * Displays learning streak and weekly activity.
 */

import React from 'react';
import { Flame } from 'lucide-react';

const StreakWidget = ({ streak = 0, weekData = [] }) => {
    const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const displayWeekData = weekData.length > 0 ? weekData : Array(7).fill(false);

    return (
        <div className="dashboard-widget animate-slide-up">
            <div className="flex items-center gap-2 mb-4">
                <Flame className="text-orange-500 w-5 h-5 animate-bounce" />
                <h3 className="font-semibold text-gray-800">Learning Streak</h3>
            </div>

            {/* Streak Count */}
            <div className="text-center mb-6">
                <p className="text-4xl font-bold text-orange-600 animate-bounce-scale">{streak}</p>
                <p className="text-sm text-gray-600 mt-1">
                    {streak === 1 ? 'day' : 'days'} in a row
                </p>
            </div>

            {/* Week Activity Grid */}
            <div className="grid grid-cols-7 gap-2">
                {days.map((day, idx) => (
                    <div key={day} className="text-center">
                        <p className="text-xs text-gray-500 font-medium mb-1">{day}</p>
                        <div
                            className={`w-8 h-8 rounded-lg transition-smooth ${
                                displayWeekData[idx]
                                    ? 'bg-emerald-500 shadow-elevation-1 hover:shadow-elevation-2 animate-slide-up'
                                    : 'bg-gray-200 hover:bg-gray-300'
                            }`}
                        />
                    </div>
                ))}
            </div>
        </div>
    );
};

StreakWidget.displayName = 'StreakWidget';

export default StreakWidget;
