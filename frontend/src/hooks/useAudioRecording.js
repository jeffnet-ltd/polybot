import { useState, useCallback } from 'react';

/**
 * Custom hook for managing audio recording functionality
 *
 * This hook provides audio recording capabilities using the browser's MediaRecorder API.
 * It manages the recording state, audio chunks, and provides methods to start, stop,
 * and clear recordings.
 *
 * @param {Object} params - Hook parameters
 * @param {Function} params.onRecordingComplete - Callback function called when recording stops with audio blob
 *
 * @returns {Object} - Object containing recording state and control functions
 * @returns {boolean} returns.isRecording - Whether recording is currently active
 * @returns {Function} returns.startRecording - Function to start recording
 * @returns {Function} returns.stopRecording - Function to stop recording
 * @returns {Function} returns.clearRecording - Function to clear recording data
 * @returns {Array} returns.audioChunks - Array of audio data chunks
 */
const useAudioRecording = ({ onRecordingComplete } = {}) => {
    const [isRecording, setIsRecording] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioChunks, setAudioChunks] = useState([]);

    /**
     * Starts audio recording
     *
     * Requests microphone access and starts recording audio.
     * Handles browser compatibility and permissions.
     */
    const startRecording = useCallback(async () => {
        try {
            // Request microphone access
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const recorder = new MediaRecorder(stream);
            const chunks = [];

            // Handle incoming audio data
            recorder.ondataavailable = (e) => {
                if (e.data.size > 0) {
                    chunks.push(e.data);
                }
            };

            // Handle recording stop
            recorder.onstop = async () => {
                const blob = new Blob(chunks, { type: 'audio/webm' });

                // Call the callback if provided
                if (onRecordingComplete) {
                    await onRecordingComplete(blob);
                }

                // Stop all audio tracks to release microphone
                stream.getTracks().forEach(track => track.stop());
            };

            // Start recording
            recorder.start();
            setMediaRecorder(recorder);
            setAudioChunks(chunks);
            setIsRecording(true);
        } catch (err) {
            console.error("Error accessing microphone:", err);
            alert("Could not access microphone. Please check permissions.");
        }
    }, [onRecordingComplete]);

    /**
     * Stops audio recording
     *
     * Stops the current recording and triggers the onstop event
     * which will process the recorded audio.
     */
    const stopRecording = useCallback(() => {
        if (mediaRecorder && isRecording) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    }, [mediaRecorder, isRecording]);

    /**
     * Clears recording data
     *
     * Resets the audio chunks and media recorder state.
     */
    const clearRecording = useCallback(() => {
        setAudioChunks([]);
        setMediaRecorder(null);
    }, []);

    return {
        isRecording,
        startRecording,
        stopRecording,
        clearRecording,
        audioChunks
    };
};

export default useAudioRecording;
