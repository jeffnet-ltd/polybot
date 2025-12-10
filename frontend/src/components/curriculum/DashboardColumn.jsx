/**
 * DashboardColumn Component
 *
 * Right-side dashboard for desktop view showing:
 * - Daily progress widget
 * - Learning streak
 * - Words/content to review
 * - Quick start to next lesson
 * - Optional: Community leaderboard
 *
 * Hidden on mobile, visible on lg+ breakpoint
 */

import React from 'react';
import ProgressWidget from '../dashboard/ProgressWidget';
import StreakWidget from '../dashboard/StreakWidget';
import ReviewWidget from '../dashboard/ReviewWidget';
import QuickStartWidget from '../dashboard/QuickStartWidget';

const DashboardColumn = ({ userProfile, modules, isLessonComplete }) => {
    if (!userProfile) return null;
    if (!modules || modules.length === 0) return null;

    // Calculate stats
    const completedLessons = modules.reduce((count, module) => {
        if (module && module.lessons) {
            return count + module.lessons.filter(l => isLessonComplete(l.lesson_id)).length;
        }
        return count;
    }, 0);

    const totalLessons = modules.reduce((count, module) => {
        return count + (module?.lessons?.length || 0);
    }, 0);

    // Find next lesson
    let nextLesson = null;
    for (const module of modules) {
        if (module && module.lessons) {
            const next = module.lessons.find(l => !isLessonComplete(l.lesson_id));
            if (next) {
                nextLesson = { ...next, module_name: module.title };
                break;
            }
        }
    }

    // Calculate words due for review (placeholder - would come from backend)
    const wordsDueForReview = 12;

    // Generate week data for streak (placeholder)
    const weekData = [true, true, true, true, true, false, false];

    return (
        <div className="space-y-4 sticky top-4 max-h-screen overflow-y-auto">
            {/* Daily Progress Widget */}
            <ProgressWidget
                dailyGoal={100}
                currentXP={userProfile.xp || 0}
            />

            {/* Streak Widget */}
            <StreakWidget
                streak={userProfile.streak || 0}
                weekData={weekData}
            />

            {/* Review Widget */}
            {wordsDueForReview > 0 && (
                <ReviewWidget
                    wordsToReview={wordsDueForReview}
                    onStartReview={() => {
                        // Navigate to vocabulary review
                        console.log('Review vocabulary');
                    }}
                />
            )}

            {/* Quick Start Widget */}
            {nextLesson && (
                <QuickStartWidget
                    nextLesson={nextLesson}
                    onStartLesson={(lessonId) => {
                        // Handle start lesson
                        console.log('Start lesson:', lessonId);
                    }}
                />
            )}

            {/* Stats Card */}
            <div className="bg-white rounded-xl p-6 shadow-md border border-gray-200">
                <h3 className="font-semibold text-gray-800 mb-4">Progress Overview</h3>
                <div className="space-y-3">
                    <div className="flex justify-between items-center">
                        <span className="text-sm text-gray-600">Lessons Completed</span>
                        <span className="font-bold text-lime-600">
                            {completedLessons}/{totalLessons}
                        </span>
                    </div>
                    <div className="relative h-2 bg-gray-200 rounded-full overflow-hidden">
                        <div
                            className="absolute h-full bg-gradient-to-r from-lime-400 to-lime-600 transition-all duration-500"
                            style={{ width: `${(completedLessons / totalLessons) * 100 || 0}%` }}
                        />
                    </div>
                    <div className="flex justify-between items-center text-xs text-gray-500">
                        <span>{Math.round((completedLessons / totalLessons) * 100 || 0)}% Complete</span>
                    </div>
                </div>
            </div>
        </div>
    );
};

DashboardColumn.displayName = 'DashboardColumn';

export default DashboardColumn;
