/**
 * CurriculumView Component
 *
 * Main component for displaying lessons and modules with enhanced visual design
 * Features:
 * - Hierarchical module structure with nested lessons
 * - User profile header with progress tracking
 * - Visual distinction for next, completed, and locked lessons
 * - Desktop dashboard with progress widgets (hidden on mobile)
 */

import React, { useState, useEffect } from 'react';
import { Loader2, GraduationCap, ChevronDown, ChevronRight, CheckCircle, Lock } from 'lucide-react';
import { getModules, getLessons } from '../../services/lessonService';
import { CORE_LANGUAGES } from '../../config/constants';
import ModuleSection from './ModuleSection';
import DashboardColumn from './DashboardColumn';

const CurriculumView = React.memo(({ onSelectLesson, userProfile, t }) => {
    const [modules, setModules] = useState([]);
    const [lessons, setLessons] = useState([]);
    const [loading, setLoading] = useState(true);
    const [expandedModules, setExpandedModules] = useState({});
    const [error, setError] = useState(null);

    // MUST call hooks before any early returns (React rules)
    useEffect(() => {
        // Ensure we have required fields and userProfile
        if (!userProfile || !userProfile.target_language || !userProfile.native_language) {
            setError('Missing user profile or language configuration');
            setLoading(false);
            return;
        }

        // Try to fetch modules first (hierarchical structure)
        getModules(userProfile.target_language, userProfile.native_language)
            .then(data => {
                // Check if response contains modules with nested lessons
                if (data && data.length > 0 && data[0].type === "module" && data[0].lessons) {
                    setModules(data);
                    setLoading(false);
                } else {
                    // Fallback to /lessons endpoint for flat structure
                    getLessons(userProfile.target_language, userProfile.native_language)
                        .then(res => {
                            setLessons(res || []);
                            setLoading(false);
                        })
                        .catch(e => {
                            console.error('[CurriculumView] Error fetching lessons:', e);
                            setLoading(false);
                        });
                }
            })
            .catch(err => {
                console.error('[CurriculumView] Error fetching modules:', err);
                // Fallback to /lessons endpoint
                getLessons(userProfile.target_language, userProfile.native_language)
                    .then(res => {
                        setLessons(res || []);
                        setLoading(false);
                    })
                    .catch(e => {
                        console.error('[CurriculumView] Error fetching lessons (fallback):', e);
                        setError('Unable to load lessons');
                        setLoading(false);
                    });
            });
    }, [userProfile?.target_language, userProfile?.native_language]);

    // NOW we can do early returns AFTER all hooks
    if (!userProfile) {
        return (
            <div className="p-10 text-center">
                <p className="text-red-600 font-semibold">Error: User profile not loaded</p>
                <p className="text-gray-600 text-sm mt-2">Please try refreshing the page.</p>
            </div>
        );
    }

    const isComplete = (lessonId) => {
        if (!userProfile.progress) return false;
        return userProfile.progress.some(p =>
            p.module_id === lessonId &&
            p.target_lang === userProfile.target_language
        );
    };

    const isLessonComplete = (lessonId) => {
        if (!userProfile.progress) return false;
        return userProfile.progress.some(p =>
            (p.module_id === lessonId || p.lesson_id === lessonId) &&
            p.target_lang === userProfile.target_language
        );
    };

    const toggleModule = (moduleId) => {
        setExpandedModules(prev => ({
            ...prev,
            [moduleId]: !prev[moduleId]
        }));
    };

    const canAccessBossFight = (module) => {
        // Boss fight is unlocked if all regular lessons (non-boss) are complete
        if (!module.lessons) return false;
        const regularLessons = module.lessons.filter(l => l.type !== "boss_fight");
        return regularLessons.every(lesson => isLessonComplete(lesson.lesson_id));
    };

    // Show error if one occurred
    if (error) {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-6">
                    Chapters (A1)
                </h2>
                <div className="bg-white rounded-2xl border border-red-200 shadow-sm p-12 max-w-2xl mx-auto">
                    <p className="text-red-600 font-semibold mb-2">{error}</p>
                    <p className="text-gray-600 text-sm">
                        If this problem persists, please try refreshing the page or logging in again.
                    </p>
                </div>
            </div>
        );
    }

    if (loading) {
        return (
            <div className="p-10 text-center text-gray-500">
                <Loader2 className="w-8 h-8 animate-spin mx-auto mb-2" />
                Loading...
            </div>
        );
    }

    // Show "Content Coming Soon" for non-Italian languages
    if (userProfile.target_language !== 'it') {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-6">
                    Chapters (A1)
                </h2>
                <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-12 max-w-2xl mx-auto">
                    <GraduationCap size={64} className="text-gray-300 mx-auto mb-4" />
                    <h3 className="text-xl font-bold text-gray-800 mb-3">Content Coming Soon</h3>
                    <p className="text-gray-600 mb-2">
                        Currently, structured lessons are only available for <strong>Italian</strong>.
                    </p>
                    <p className="text-gray-600">
                        We're working on adding content for {CORE_LANGUAGES.find(l => l.code === userProfile.target_language)?.name || 'your selected language'}.
                        Check back soon!
                    </p>
                </div>
            </div>
        );
    }

    // Main render: Hierarchical modules (only reached for Italian)
    if (modules.length > 0) {
        return (
            <div className="max-w-screen-2xl mx-auto px-6 w-full">
                <div className="flex gap-6">
                    {/* Main Content Column */}
                    <div className="flex-1">
                        <div className="p-4 space-y-4">
                            <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mt-6">
                                Chapters (A1)
                            </h2>

                            <div className="space-y-3">
                                {modules.map((module) => (
                                    <ModuleSection
                                        key={module._id}
                                        module={module}
                                        isExpanded={expandedModules[module._id]}
                                        onToggle={() => toggleModule(module._id)}
                                        onSelectLesson={onSelectLesson}
                                        isLessonComplete={isLessonComplete}
                                        canAccessBossFight={canAccessBossFight}
                                    />
                                ))}
                            </div>
                        </div>
                    </div>

                    {/* Dashboard Column - Desktop Only */}
                    <div className="hidden lg:block w-80 flex-shrink-0">
                        <DashboardColumn userProfile={userProfile} modules={modules} isLessonComplete={isLessonComplete} />
                    </div>
                </div>
            </div>
        );
    }

    // Fallback: Render flat lessons (backward compatibility)
    if (lessons.length === 0) {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-6">
                    Chapters (A1)
                </h2>
                <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-12 max-w-2xl mx-auto">
                    <GraduationCap size={64} className="text-gray-300 mx-auto mb-4" />
                    <h3 className="text-xl font-bold text-gray-800 mb-3">No Lessons Available</h3>
                    <p className="text-gray-600">
                        There are no lessons available at this time.
                    </p>
                </div>
            </div>
        );
    }

    // Flat lessons fallback
    return (
        <div className="max-w-screen-2xl mx-auto px-6 w-full">
            <div className="flex gap-6">
                {/* Main Content Column */}
                <div className="flex-1">
                    <div className="p-4 space-y-4">
                        <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mt-6">
                            Chapters (A1)
                        </h2>

                        <div className="space-y-3">
                            {lessons.map((lesson, index) => {
                                const completed = isComplete(lesson._id);
                                return (
                                    <div
                                        key={lesson._id}
                                        onClick={() => onSelectLesson(lesson)}
                                        className={`flex items-center p-4 bg-white rounded-2xl border shadow-sm cursor-pointer hover:shadow-md transition group ${
                                            completed ? 'border-green-200 bg-green-50' : 'border-gray-100'
                                        }`}
                                    >
                                        <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-4 font-bold ${
                                            completed ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-400'
                                        }`}>
                                            {completed ? <CheckCircle size={20} /> : index + 1}
                                        </div>
                                        <div className="flex-grow">
                                            <h3 className="font-bold text-gray-800 group-hover:text-[#4CAF50] transition">
                                                {lesson.title}
                                            </h3>
                                            <p className="text-xs text-gray-500">{lesson.goal}</p>
                                        </div>
                                        <ChevronRight className="text-gray-300 group-hover:text-[#4CAF50]" />
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                </div>

                {/* Dashboard Column - Desktop Only */}
                <div className="hidden lg:block w-80 flex-shrink-0">
                    <DashboardColumn userProfile={userProfile} modules={[]} isLessonComplete={isLessonComplete} />
                </div>
            </div>
        </div>
    );
});

CurriculumView.displayName = 'CurriculumView';

export default CurriculumView;
