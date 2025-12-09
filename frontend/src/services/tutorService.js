/**
 * Tutor Service
 * Handle AI tutor interactions, including chat, boss fights, and initiations
 */

import { apiClient } from './api';

/**
 * Send a regular chat message to the tutor
 * @param {Object} payload - Message payload
 * @returns {Promise<Object>} Tutor response
 */
export const sendTutorMessage = async (payload) => {
    try {
        const response = await apiClient.post('/tutor', payload);
        return response.data;
    } catch (error) {
        console.error('Error sending tutor message:', error);
        throw error;
    }
};

/**
 * Initiate tutor for a lesson (setup conversation)
 * @param {Object} payload - Initiation payload
 * @returns {Promise<Object>} Initial tutor response
 */
export const initiateTutor = async (payload) => {
    try {
        const response = await apiClient.post('/tutor/initiate', payload);
        return response.data;
    } catch (error) {
        console.error('Error initiating tutor:', error);
        throw error;
    }
};

/**
 * Send a message during boss fight conversation
 * @param {Object} payload - Boss fight message payload
 * @returns {Promise<Object>} Boss fight response
 */
export const sendBossFightMessage = async (payload) => {
    try {
        const response = await apiClient.post('/tutor/boss', payload);
        return response.data;
    } catch (error) {
        console.error('Error sending boss fight message:', error);
        throw error;
    }
};
