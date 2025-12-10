/**
 * LessonCardLocked Component
 *
 * Lesson card for locked lessons (e.g., boss fights not yet unlocked).
 * Uses gray background with reduced opacity and lock icon.
 * Includes "Set Lesson" button for future functionality.
 */

import React, { useState } from 'react';
import { Lock } from 'lucide-react';

const LessonCardLocked = ({ lesson, index, onSetLesson }) => {
    const [showTooltip, setShowTooltip] = useState(false);

    const handleSetLesson = (e) => {
        e.stopPropagation();
        if (onSetLesson) {
            onSetLesson(lesson.lesson_id);
        }
    };

    return (
        <div className="flex items-center p-5 border-b border-gray-100 last:border-b-0 bg-gray-100 opacity-60 cursor-not-allowed">
            {/* Lock Icon */}
            <div className="w-10 h-10 rounded-full flex items-center justify-center mr-4 flex-shrink-0 bg-gray-300 text-gray-600">
                <Lock size={18} />
            </div>

            {/* Content */}
            <div className="flex-grow">
                <h4 className="font-semibold text-gray-700">
                    {lesson.title}
                </h4>
                <p className="text-xs text-gray-500 mt-1">
                    Complete all regular lessons to unlock this challenge
                </p>
            </div>

            {/* "Set Lesson" Button */}
            <button
                onClick={handleSetLesson}
                onMouseEnter={() => setShowTooltip(true)}
                onMouseLeave={() => setShowTooltip(false)}
                className="ml-4 px-4 py-2 bg-amber-500 text-white text-sm font-semibold rounded-lg hover:bg-amber-600 transition-all whitespace-nowrap shadow-sm"
            >
                Set Lesson
            </button>

            {/* Tooltip */}
            {showTooltip && (
                <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-3 py-2 bg-gray-800 text-white text-xs rounded-lg whitespace-nowrap shadow-lg">
                    Unlock by completing previous lessons
                </div>
            )}
        </div>
    );
};

LessonCardLocked.displayName = 'LessonCardLocked';

export default LessonCardLocked;
