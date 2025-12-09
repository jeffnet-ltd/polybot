/**
 * Global Constants
 * Centralized configuration for API, languages, UI strings, and levels
 */

// Backend API URL
export const API = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

// All supported languages with country codes for FlagCDN
export const ALL_LANGUAGES = [
    { code: 'en', name: 'English', country: 'gb' },
    { code: 'fr', name: 'French', country: 'fr' },
    { code: 'es', name: 'Spanish', country: 'es' },
    { code: 'it', name: 'Italian', country: 'it' },
    { code: 'pt', name: 'Portuguese', country: 'pt' },
    { code: 'tw', name: 'Twi', country: 'gh' },
    { code: 'de', name: 'German', country: 'de' },
    { code: 'ar', name: 'Arabic', country: 'sa' },
    { code: 'zh', name: 'Mandarin', country: 'cn' },
    { code: 'ja', name: 'Japanese', country: 'jp' },
    { code: 'ru', name: 'Russian', country: 'ru' },
    { code: 'ko', name: 'Korean', country: 'kr' },
];

// Core languages (available for learning)
export const CORE_LANGUAGES = [
    { code: 'en', name: 'English', country: 'gb' },
    { code: 'fr', name: 'French', country: 'fr' },
    { code: 'es', name: 'Spanish', country: 'es' },
    { code: 'it', name: 'Italian', country: 'it' },
    { code: 'pt', name: 'Portuguese', country: 'pt' },
    { code: 'tw', name: 'Twi', country: 'gh' },
];

// Learning levels
export const LEVELS = [];

// UI strings for localization
export const UI_STRINGS = {
    en: {
        menu: "Menu",
        lessons: "Lessons",
        practice: "Practice",
        progress: "Progress",
        vocab: "Vocabulary",
        start: "Start Learning",
        profile: "Change Profile",
        overview: "Overview",
        exercises: "Exercises"
    },
};
