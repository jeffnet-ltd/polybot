/**
 * QuickStartWidget Component
 *
 * Highlights the next lesson with prominent CTA button.
 * Uses lime green gradient to match primary action color.
 */

import React, { useState } from 'react';
import { Zap, ArrowRight } from 'lucide-react';

const QuickStartWidget = ({ nextLesson = null, onStartLesson }) => {
    const [isHovered, setIsHovered] = useState(false);

    if (!nextLesson) {
        return (
            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200">
                <div className="text-center py-6">
                    <Zap className="w-8 h-8 text-gray-300 mx-auto mb-2" />
                    <p className="text-sm text-gray-500">No lessons available</p>
                </div>
            </div>
        );
    }

    return (
        <div className="bg-gradient-to-br from-brand-lime-400 to-brand-lime-600 rounded-xl p-6 shadow-elevation-4 border border-brand-lime-300 text-white hover:shadow-glow-lime-strong transition-smooth animate-slide-up animate-pulse-glow">
            {/* Header */}
            <div className="flex items-center gap-2 mb-4">
                <Zap className="w-5 h-5 animate-bounce" />
                <h3 className="font-semibold">Next Lesson</h3>
            </div>

            {/* Lesson Info */}
            <div className="mb-5">
                <p className="text-lg font-bold mb-1">
                    {nextLesson.title}
                </p>
                <p className="text-sm opacity-90">
                    {nextLesson.module_name || 'Chapter'}
                </p>
            </div>

            {/* CTA Button */}
            <button
                onClick={() => onStartLesson(nextLesson.lesson_id)}
                onMouseEnter={() => setIsHovered(true)}
                onMouseLeave={() => setIsHovered(false)}
                className="w-full py-3 bg-white text-brand-lime-700 rounded-lg font-bold hover:bg-gray-50 transition-smooth shadow-elevation-2 flex items-center justify-center gap-2 group hover:scale-105 active:scale-95"
            >
                <span>Start Lesson</span>
                <ArrowRight
                    size={18}
                    className={`transition-transform ${
                        isHovered ? 'translate-x-1' : ''
                    }`}
                />
            </button>
        </div>
    );
};

QuickStartWidget.displayName = 'QuickStartWidget';

export default QuickStartWidget;
