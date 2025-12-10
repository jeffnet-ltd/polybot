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
        <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200 hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-2 mb-4">
                <Flame className="text-orange-500 w-5 h-5" />
                <h3 className="font-semibold text-gray-800">Learning Streak</h3>
            </div>

            {/* Streak Count */}
            <div className="text-center mb-6">
                <p className="text-4xl font-bold text-orange-600">{streak}</p>
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
                            className={`w-8 h-8 rounded-lg transition-all ${
                                displayWeekData[idx]
                                    ? 'bg-emerald-500 shadow-md'
                                    : 'bg-gray-200'
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
