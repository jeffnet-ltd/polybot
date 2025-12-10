/**
 * ReviewWidget Component
 *
 * Shows number of words/content due for review and CTA button.
 */

import React from 'react';
import { BookOpen } from 'lucide-react';

const ReviewWidget = ({ wordsToReview = 0, onStartReview }) => {
    return (
        <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200 hover:shadow-lg transition-shadow">
            <div className="flex items-center gap-2 mb-4">
                <BookOpen className="text-indigo-600 w-5 h-5" />
                <h3 className="font-semibold text-gray-800">Review Today</h3>
            </div>

            {/* Content Count */}
            <p className="text-gray-700 mb-4 text-sm">
                {wordsToReview} words and phrases are due for practice
            </p>

            {/* CTA Button */}
            <button
                onClick={onStartReview}
                className="w-full py-3 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700 transition-colors shadow-sm hover:shadow-md"
            >
                Review Now
            </button>
        </div>
    );
};

ReviewWidget.displayName = 'ReviewWidget';

export default ReviewWidget;
