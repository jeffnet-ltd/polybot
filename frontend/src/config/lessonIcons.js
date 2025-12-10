/**
 * Lesson Icons Configuration
 * Maps lesson states to lucide-react icons
 */

import {
    CheckCircle2,
    PlayCircle,
    Lock,
    Trophy,
    BookOpen,
    Zap,
    Target,
    Flame,
    BookMarked,
    Radio,
    FileText,
    MessageSquare,
} from 'lucide-react';

/**
 * Icon mapping for lesson status states
 */
export const LESSON_STATUS_ICONS = {
    completed: CheckCircle2,
    next: PlayCircle,
    locked: Lock,
    boss_fight: Trophy,
};

/**
 * Icon mapping for lesson types
 */
export const LESSON_TYPE_ICONS = {
    conversation: MessageSquare,
    reading: FileText,
    listening: Radio,
    writing: BookMarked,
    vocabulary: BookOpen,
    boss_fight: Trophy,
    default: BookOpen,
};

/**
 * Dashboard widget icons
 */
export const DASHBOARD_ICONS = {
    progress: Target,
    streak: Flame,
    review: BookOpen,
    quickStart: Zap,
};

/**
 * Get icon component for lesson status
 * @param {string} status - 'completed', 'next', 'locked', 'boss_fight'
 * @returns {React.Component} Icon component from lucide-react
 */
export const getStatusIcon = (status) => {
    return LESSON_STATUS_ICONS[status] || LESSON_STATUS_ICONS.next;
};

/**
 * Get icon component for lesson type
 * @param {string} type - lesson type code
 * @returns {React.Component} Icon component from lucide-react
 */
export const getLessonTypeIcon = (type) => {
    return LESSON_TYPE_ICONS[type] || LESSON_TYPE_ICONS.default;
};

/**
 * Get color classes for status
 * @param {string} status - lesson status
 * @returns {string} Tailwind color classes
 */
export const getStatusColorClasses = (status) => {
    const colors = {
        completed: 'text-emerald-500 bg-emerald-50',
        next: 'text-lime-600 bg-lime-50',
        locked: 'text-gray-400 bg-gray-50',
        boss_fight: 'text-amber-500 bg-amber-50',
    };
    return colors[status] || colors.next;
};

/**
 * Get badge background color for status
 * @param {string} status - lesson status
 * @returns {string} Tailwind background class
 */
export const getStatusBadgeBackground = (status) => {
    const backgrounds = {
        completed: 'bg-emerald-100',
        next: 'bg-lime-100',
        locked: 'bg-gray-100',
        boss_fight: 'bg-amber-100',
    };
    return backgrounds[status] || backgrounds.next;
};
