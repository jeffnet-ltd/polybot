/**
 * ProgressWidget Component
 *
 * Displays daily XP progress towards daily goal.
 */

import React, { useEffect, useState } from 'react';
import { Target } from 'lucide-react';

const ProgressWidget = ({ dailyGoal = 100, currentXP = 0 }) => {
    const [displayedXP, setDisplayedXP] = useState(0);
    const percentage = (currentXP / dailyGoal) * 100;

    // Animate the progress on load
    useEffect(() => {
        const timer = setTimeout(() => {
            setDisplayedXP(percentage);
        }, 100);
        return () => clearTimeout(timer);
    }, [percentage]);

    return (
        <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200 hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-2 mb-4">
                <Target className="text-lime-600 w-5 h-5" />
                <h3 className="font-semibold text-gray-800">Daily Goal</h3>
            </div>

            {/* Progress Bar */}
            <div className="relative h-3 bg-gray-200 rounded-full overflow-hidden mb-3">
                <div
                    className="absolute h-full bg-gradient-to-r from-lime-400 to-lime-600 transition-all duration-1000 ease-out rounded-full"
                    style={{ width: `${displayedXP}%` }}
                />
            </div>

            {/* Progress Text */}
            <div className="flex justify-between items-center">
                <p className="text-sm font-medium text-gray-700">
                    {Math.round(currentXP)} / {dailyGoal} XP
                </p>
                <p className="text-sm font-semibold text-lime-600">
                    {Math.round(percentage)}%
                </p>
            </div>
        </div>
    );
};

ProgressWidget.displayName = 'ProgressWidget';

export default ProgressWidget;
