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

import React, { useState, useEffect } from 'react';
import ProgressWidget from '../dashboard/ProgressWidget';
import StreakWidget from '../dashboard/StreakWidget';
import ReviewWidget from '../dashboard/ReviewWidget';
import QuickStartWidget from '../dashboard/QuickStartWidget';
import ReviewSession from '../views/ReviewSession';
import apiClient from '../../services/api';

const DashboardColumn = ({ userProfile, modules, isLessonComplete }) => {
    const [wordsDue, setWordsDue] = useState(0);
    const [showReview, setShowReview] = useState(false);

    useEffect(() => {
        if (!userProfile?.user_id) return;
        apiClient.get(`/api/vocabulary/due?user_id=${userProfile.user_id}`)
            .then(res => setWordsDue(res.data.length))
            .catch(() => {});
    }, [userProfile?.user_id]);

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

    const wordsDueForReview = wordsDue;

    // Build weekData from streak + last_active so active days light up correctly.
    // Index 0 = Monday, index 6 = Sunday (matching the widget's Mon–Sun layout).
    const weekData = (() => {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const streak = userProfile.streak || 0;
        const lastActiveStr = userProfile.last_active;

        const data = Array(7).fill(false);
        if (!lastActiveStr || streak === 0) return data;

        const lastActive = new Date(lastActiveStr);
        lastActive.setHours(0, 0, 0, 0);

        // Day-of-week index (0=Sun→6=Sat), convert to Mon-based (0=Mon→6=Sun)
        const toMonIndex = (d) => (d.getDay() + 6) % 7;

        let cursor = new Date(lastActive);
        for (let i = 0; i < streak && i < 7; i++) {
            const idx = toMonIndex(cursor);
            data[idx] = true;
            cursor.setDate(cursor.getDate() - 1);
        }
        return data;
    })();

    return (
        <div className="space-y-4">
            {/* Daily Progress Widget */}
            <ProgressWidget
                dailyGoal={100}
                currentXP={userProfile.daily_xp || 0}
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
                    onStartReview={() => setShowReview(true)}
                />
            )}

            {/* Review Session Modal */}
            {showReview && (
                <ReviewSession
                    userProfile={userProfile}
                    onClose={() => { setShowReview(false); setWordsDue(0); }}
                    onXpEarned={(xp) => console.log(`Review earned ${xp} XP`)}
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
