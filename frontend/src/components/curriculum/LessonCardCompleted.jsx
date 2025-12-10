/**
 * LessonCardCompleted Component
 *
 * Lesson card for completed lessons.
 * Uses soft green background with muted styling.
 */

import React, { useState } from 'react';
import { CheckCircle2, ChevronRight } from 'lucide-react';

const LessonCardCompleted = ({ lesson, index, onSelect }) => {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div
            onClick={onSelect}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            className="lesson-card flex items-center p-5 cursor-pointer rounded-xl mb-3 bg-emerald-50 hover:shadow-elevation-2 transition-smooth group"
        >
            {/* Checkmark Icon */}
            <div className="w-10 h-10 rounded-full flex items-center justify-center mr-4 flex-shrink-0 bg-emerald-500 text-white shadow-elevation-1">
                <CheckCircle2 size={20} />
            </div>

            {/* Content */}
            <div className="flex-grow">
                <h4 className="font-medium text-gray-700">
                    {lesson.title}
                </h4>
                {lesson.focus && (
                    <p className="text-xs text-gray-500 mt-0.5">
                        {lesson.focus}
                    </p>
                )}
            </div>

            {/* Chevron Icon */}
            <ChevronRight
                size={18}
                className="text-gray-400 flex-shrink-0 group-hover:text-emerald-500 transition-smooth"
            />
        </div>
    );
};

LessonCardCompleted.displayName = 'LessonCardCompleted';

export default LessonCardCompleted;
