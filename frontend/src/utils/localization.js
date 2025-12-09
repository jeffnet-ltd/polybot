/**
 * Localization Utilities
 * Translation and language utilities
 */

import { UI_STRINGS } from '../config/constants';

/**
 * Get translation function for a given language
 * Returns a function that translates keys to strings in the specified language
 * Falls back to English if key not found
 * @param {string} langCode - Language code (e.g., 'en', 'it')
 * @returns {Function} Translation function that takes a key and returns a string
 */
export const getT = (langCode) => (key) => {
    return UI_STRINGS[langCode]?.[key] || UI_STRINGS['en'][key] || key;
};
