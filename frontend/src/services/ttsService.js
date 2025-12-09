/**
 * TTS Service
 * Handle text-to-speech API calls and voice synthesis
 */

import { apiClient } from './api';

/**
 * Synthesize text to speech
 * @param {string} text - Text to synthesize
 * @param {string} language - Language code
 * @returns {Promise<Blob>} Audio blob
 */
export const synthesizeVoice = async (text, language) => {
    try {
        const response = await apiClient.post(
            '/api/v1/voice/synthesize',
            { text, language },
            {
                responseType: 'blob',
            }
        );
        return response.data;
    } catch (error) {
        console.error('Error synthesizing voice:', error);
        throw error;
    }
};

/**
 * Analyze audio (transcribe + get phonetic score)
 * @param {FormData} formData - FormData with audio file
 * @returns {Promise<Object>} Transcription and analysis results
 */
export const analyzeAudio = async (formData) => {
    try {
        const response = await apiClient.post('/voice/analyze', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error analyzing audio:', error);
        throw error;
    }
};
