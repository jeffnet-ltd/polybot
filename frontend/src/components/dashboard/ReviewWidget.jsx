/**
 * ReviewWidget Component
 *
 * Shows number of words/content due for review and CTA button.
 */

import React from 'react';
import { BookOpen } from 'lucide-react';

const ReviewWidget = ({ wordsToReview = 0, onStartReview }) => {
    return (
        <div className="dashboard-widget animate-slide-up">
            <div className="flex items-center gap-2 mb-4">
                <BookOpen className="text-brand-indigo-600 w-5 h-5" />
                <h3 className="font-semibold text-gray-800">Review Today</h3>
            </div>

            {/* Content Count */}
            <p className="text-gray-700 mb-4 text-sm">
                {wordsToReview} words and phrases are due for practice
            </p>

            {/* CTA Button */}
            <button
                onClick={onStartReview}
                className="w-full py-3 bg-brand-indigo-600 text-white rounded-lg font-semibold hover:bg-brand-indigo-700 transition-smooth shadow-elevation-1 hover:shadow-elevation-2 active:scale-95"
            >
                Review Now
            </button>
        </div>
    );
};

ReviewWidget.displayName = 'ReviewWidget';

export default ReviewWidget;
