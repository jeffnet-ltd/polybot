/**
 * LessonCardNext Component
 *
 * Highlighted lesson card for the next lesson to take.
 * Uses vibrant lime green gradient with prominent styling.
 */

import React, { useState } from 'react';
import { Play, ArrowRight } from 'lucide-react';

const LessonCardNext = ({ lesson, index, onSelect, isHighlighted = true }) => {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <div
            onClick={onSelect}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            className={`relative flex items-center p-5 cursor-pointer border-b border-gray-100 last:border-b-0 transition-all duration-200 group ${
                isHighlighted
                    ? 'bg-gradient-to-r from-lime-400 to-lime-600 text-white shadow-md hover:shadow-lg'
                    : 'bg-white hover:bg-gray-50'
            }`}
        >
            {/* Icon */}
            <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-4 flex-shrink-0 font-bold transition-all ${
                isHighlighted
                    ? 'bg-white bg-opacity-30 text-white'
                    : 'bg-blue-100 text-blue-600'
            }`}>
                <Play size={18} className="fill-current" />
            </div>

            {/* Content */}
            <div className="flex-grow">
                <h4 className={`font-semibold transition-all ${
                    isHighlighted ? 'text-white text-base' : 'text-gray-800'
                }`}>
                    {lesson.title}
                </h4>
                {lesson.focus && (
                    <p className={`text-xs transition-all ${
                        isHighlighted ? 'text-white text-opacity-80' : 'text-gray-500'
                    }`}>
                        {lesson.focus}
                    </p>
                )}
            </div>

            {/* Arrow Icon */}
            <ArrowRight
                size={20}
                className={`flex-shrink-0 transition-all duration-200 ${
                    isHighlighted
                        ? 'text-white opacity-70 group-hover:opacity-100 group-hover:translate-x-1'
                        : 'text-gray-300 group-hover:text-gray-400'
                }`}
            />

            {/* Pulsing Glow for Highlighted */}
            {isHighlighted && (
                <div className="absolute inset-0 rounded-lg pointer-events-none animate-pulse" />
            )}
        </div>
    );
};

LessonCardNext.displayName = 'LessonCardNext';

export default LessonCardNext;
