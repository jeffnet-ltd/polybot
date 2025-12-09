/**
 * API Service Layer
 * Centralized axios client configuration
 */

import axios from 'axios';
import { API } from '../config/constants';

/**
 * Configured axios instance with base settings
 */
export const apiClient = axios.create({
    baseURL: API,
    timeout: 300000, // 5 minutes
    headers: {
        'Content-Type': 'application/json',
    },
});

// Optional: Add request interceptor for logging
apiClient.interceptors.request.use(
    (config) => {
        console.log(`[API] ${config.method.toUpperCase()} ${config.url}`);
        return config;
    },
    (error) => {
        console.error('[API] Request error:', error);
        return Promise.reject(error);
    }
);

// Optional: Add response interceptor for error handling
apiClient.interceptors.response.use(
    (response) => {
        console.log(`[API] Response OK: ${response.status}`);
        return response;
    },
    (error) => {
        console.error('[API] Response error:', error);
        return Promise.reject(error);
    }
);

export default apiClient;
