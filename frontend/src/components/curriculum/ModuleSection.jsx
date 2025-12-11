/**
 * ModuleSection Component
 *
 * Displays a collapsible module with nested lessons.
 * Shows:
 * - Module title and goal
 * - Progress indicator (X/Y lessons completed)
 * - Expandable list of lessons with different states (next, completed, locked)
 */

import React from 'react';
import { ChevronDown, CheckCircle, Lock, Play } from 'lucide-react';
import { getModuleIcon } from '../../utils/imageUtils';
import LessonCardNext from './LessonCardNext';
import LessonCardCompleted from './LessonCardCompleted';
import LessonCardLocked from './LessonCardLocked';

const ModuleSection = ({
    module,
    isExpanded,
    onToggle,
    onSelectLesson,
    isLessonComplete,
    canAccessBossFight
}) => {
    if (!module || !module.lessons) return null;

    const completedCount = module.lessons.filter(l => isLessonComplete(l.lesson_id)).length;
    const totalCount = module.lessons.length;
    const moduleComplete = completedCount === totalCount;

    return (
        <div className="bg-white rounded-2xl border border-gray-200 shadow-elevation-2 overflow-hidden hover:shadow-elevation-3 transition-smooth mb-4 card-stagger">
            {/* Module Header */}
            <div
                onClick={onToggle}
                className={`module-header flex items-center p-5 cursor-pointer hover:bg-gray-50 transition-smooth ${
                    moduleComplete ? 'border-b border-emerald-200 bg-emerald-50' : 'border-b border-gray-100'
                }`}
            >
                {/* Module Icon/Status */}
                {moduleComplete ? (
                    <div className={`w-12 h-12 rounded-full flex items-center justify-center mr-4 font-bold text-lg flex-shrink-0 bg-emerald-500 text-white shadow-elevation-2`}>
                        <CheckCircle size={24} />
                    </div>
                ) : (
                    <img
                        src={getModuleIcon(module.title)}
                        alt={module.title}
                        className="w-12 h-12 rounded-full object-cover mr-4 flex-shrink-0 shadow-elevation-1"
                    />
                )}

                {/* Module Info */}
                <div className="flex-grow">
                    <h3 className="font-bold text-gray-800 text-lg">{module.title}</h3>
                    <p className="text-sm text-gray-600 mt-1">{module.goal}</p>
                </div>

                {/* Progress Indicator */}
                <div className="flex items-center gap-3 mr-3">
                    <div className="text-right">
                        <p className="text-sm font-semibold text-gray-700">
                            {completedCount}/{totalCount}
                        </p>
                        <p className="text-xs text-gray-500">lessons</p>
                    </div>
                </div>

                {/* Expand/Collapse Indicator */}
                <ChevronDown
                    size={20}
                    className={`text-gray-400 transition-transform flex-shrink-0 ${
                        isExpanded ? 'rotate-180' : ''
                    }`}
                />
            </div>

            {/* Nested Lessons */}
            {isExpanded && (
                <div className="border-t border-gray-100 bg-gray-50 p-5">
                    {module.lessons.map((lesson, idx) => {
                        const lessonCompleted = isLessonComplete(lesson.lesson_id);
                        const isBossFight = lesson.type === "boss_fight";
                        const isLocked = isBossFight && !canAccessBossFight(module);
                        const isNext = !lessonCompleted && !isLocked && idx < module.lessons.length - 1;

                        // Render appropriate card variant
                        if (lessonCompleted) {
                            return (
                                <LessonCardCompleted
                                    key={lesson.lesson_id}
                                    lesson={lesson}
                                    index={idx}
                                    onSelect={() => onSelectLesson({ ...lesson, moduleTitle: module.title })}
                                />
                            );
                        }

                        if (isLocked) {
                            return (
                                <LessonCardLocked
                                    key={lesson.lesson_id}
                                    lesson={lesson}
                                    index={idx}
                                />
                            );
                        }

                        return (
                            <LessonCardNext
                                key={lesson.lesson_id}
                                lesson={lesson}
                                index={idx}
                                onSelect={() => onSelectLesson({ ...lesson, moduleTitle: module.title })}
                                isHighlighted={isNext}
                            />
                        );
                    })}
                </div>
            )}
        </div>
    );
};

ModuleSection.displayName = 'ModuleSection';

export default ModuleSection;
