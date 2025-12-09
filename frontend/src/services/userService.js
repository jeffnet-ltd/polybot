/**
 * User Service
 * Handle user authentication, profile management, and progress tracking
 */

import { apiClient } from './api';

/**
 * Get user profile by email
 * @param {string} email - User email
 * @returns {Promise<Object>} User profile data
 */
export const getUserProfile = async (email) => {
    try {
        // Note: Axios automatically encodes URL parameters, so don't use encodeURIComponent
        const response = await apiClient.get(`/user/profile`, {
            params: { email },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching user profile:', error);
        throw error;
    }
};

/**
 * Register a new user
 * @param {Object} userProfile - User profile data
 * @returns {Promise<Object>} Registration response
 */
export const registerUser = async (userProfile) => {
    try {
        const response = await apiClient.post('/user/register', userProfile);
        return response.data;
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
};

/**
 * Update user profile (e.g., language preferences, settings)
 * @param {string} userId - User ID
 * @param {Object} updates - Fields to update
 * @returns {Promise<Object>} Updated profile
 */
export const updateUserProfile = async (userId, updates) => {
    try {
        const response = await apiClient.patch(`/user/${userId}`, updates);
        return response.data;
    } catch (error) {
        console.error('Error updating user profile:', error);
        throw error;
    }
};

/**
 * Mark a lesson as complete and save progress
 * @param {string} userId - User ID
 * @param {string} lessonId - Lesson ID
 * @param {number} score - Exercise score
 * @param {number} total - Total exercises
 * @returns {Promise<Object>} Updated progress
 */
export const completeLessonProgress = async (userId, lessonId, score, total) => {
    try {
        const response = await apiClient.post('/user/complete_lesson', {
            user_id: userId,
            lesson_id: lessonId,
            score,
            total,
        });
        return response.data;
    } catch (error) {
        console.error('Error saving lesson progress:', error);
        throw error;
    }
};
