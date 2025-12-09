/**
 * Lesson Service
 * Handle curriculum, lesson retrieval, and related operations
 */

import { apiClient } from './api';

/**
 * Get modules/curriculum for a target language
 * @param {string} targetLang - Target language code
 * @param {string} nativeLang - Native language code
 * @returns {Promise<Array>} List of modules
 */
export const getModules = async (targetLang, nativeLang) => {
    try {
        const response = await apiClient.get('/modules', {
            params: {
                target_lang: targetLang,
                native_lang: nativeLang,
            },
            timeout: 15000,
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching modules:', error);
        throw error;
    }
};

/**
 * Get lessons for a target language (fallback/flat structure)
 * @param {string} targetLang - Target language code
 * @param {string} nativeLang - Native language code
 * @returns {Promise<Array>} List of lessons
 */
export const getLessons = async (targetLang, nativeLang) => {
    try {
        const response = await apiClient.get('/lessons', {
            params: {
                target_lang: targetLang,
                native_lang: nativeLang,
            },
            timeout: 15000,
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching lessons:', error);
        throw error;
    }
};
