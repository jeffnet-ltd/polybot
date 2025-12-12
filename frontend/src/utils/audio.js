/**
 * Audio Utilities
 * TTS (Text-to-Speech), audio playback, and audio context management
 */

import { API } from '../config/constants';

let audioUnlocked = false;

/**
 * Unlock audio context for autoplay on iOS/Safari
 * Creates a dummy audio context and resumes it to enable autoplay
 */
export const unlockAudio = () => {
    if (!audioUnlocked) {
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            if (audioContext.state === 'suspended') {
                audioContext.resume();
            }
            audioUnlocked = true;
            console.log("[Audio] Audio unlocked for autoplay");
        } catch (err) {
            console.error("[Audio] Failed to unlock audio:", err);
        }
    }
};

// Set up audio unlock on first user interaction
if (typeof window !== 'undefined') {
    const unlockOnInteraction = () => {
        unlockAudio();
        document.removeEventListener('click', unlockOnInteraction);
        document.removeEventListener('touchstart', unlockOnInteraction);
    };
    document.addEventListener('click', unlockOnInteraction, { once: true });
    document.addEventListener('touchstart', unlockOnInteraction, { once: true });
}

/**
 * Get TTS audio blob from backend
 * @param {string} text - Text to convert to speech
 * @param {string} langCode - Language code (e.g., 'it', 'en')
 * @param {string} characterName - Optional character name for gendered voices
 * @returns {Promise<Blob>} Audio blob
 */
export const getTTSAudioBlob = async (text, langCode, characterName = null) => {
    if (!text) return null;

    try {
        const payload = { text, language: langCode };
        if (characterName) {
            payload.character_name = characterName;
        }

        const response = await fetch(`${API}/api/v1/voice/synthesize`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error("[TTS] Request failed:", response.status, errorText);
            throw new Error(`TTS Error: ${response.status} - ${errorText}`);
        }

        const blob = await response.blob();
        console.log(`[TTS] Received audio blob, size: ${blob.size} bytes, type: ${blob.type}`);

        if (blob.size === 0) {
            throw new Error("TTS Error: Received empty audio");
        }

        return blob;
    } catch (err) {
        console.error("[TTS] Error getting audio blob:", err);
        throw err;
    }
};

/**
 * Backend-powered TTS using Azure Speech Services
 * Handles full audio playback with error recovery
 * @param {string} text - Text to speak
 * @param {string} langCode - Language code
 * @param {string} characterName - Optional character name for gendered voices
 */
export const speakText = async (text, langCode, characterName = null) => {
    if (!text) return;
    try {
        unlockAudio();

        console.log(`[TTS] Requesting audio for: "${text}" in language: ${langCode}${characterName ? ` (character: ${characterName})` : ''}`);
        console.log(`[TTS] API URL: ${API}/api/v1/voice/synthesize`);

        // Check if backend is reachable
        try {
            const healthCheck = await fetch(`${API}/health`);
            console.log(`[TTS] Backend health check: ${healthCheck.status}`);
        } catch (healthErr) {
            console.error("[TTS] Backend health check failed:", healthErr);
            alert(`Cannot reach backend at ${API}. Is the backend running?`);
            return;
        }

        const blob = await getTTSAudioBlob(text, langCode, characterName);
        if (!blob) return;

        // Create audio element and play
        const url = URL.createObjectURL(blob);
        const audio = new Audio(url);

        // Set up event handlers
        const cleanup = () => {
            URL.revokeObjectURL(url);
        };

        audio.onerror = (e) => {
            console.error("[TTS] Audio playback error:", e, audio.error);
            cleanup();
        };

        audio.onended = () => {
            console.log("[TTS] Audio playback completed");
            cleanup();
        };

        // Improved playback logic
        const playAudio = async () => {
            try {
                audio.volume = 1.0;
                const playPromise = audio.play();

                if (playPromise !== undefined) {
                    await playPromise;
                    console.log("[TTS] Audio playback started successfully");
                }
            } catch (playError) {
                console.log("[TTS] Initial play blocked:", playError.name);

                // Wait for audio to be ready
                const waitForReady = () => {
                    return new Promise((resolve, reject) => {
                        if (audio.readyState >= 2) {
                            // HAVE_CURRENT_DATA
                            resolve();
                        } else {
                            audio.oncanplaythrough = () => resolve();
                            audio.onerror = () => reject(new Error("Audio load failed"));
                            setTimeout(() => reject(new Error("Audio load timeout")), 5000);
                        }
                    });
                };

                try {
                    await waitForReady();
                    console.log("[TTS] Audio ready, attempting playback");
                    await audio.play();
                    console.log("[TTS] Audio playback started after waiting");
                } catch (playError2) {
                    console.error("[TTS] Play failed:", playError2);
                    // If still blocked, set up click handler
                    const playOnClick = () => {
                        audio.play().catch(e => console.error("[TTS] Retry play failed:", e));
                        document.removeEventListener('click', playOnClick);
                        document.removeEventListener('touchstart', playOnClick);
                    };
                    document.addEventListener('click', playOnClick, { once: true });
                    document.addEventListener('touchstart', playOnClick, { once: true });
                }
            }
        };

        audio.load();
        playAudio();
    } catch (err) {
        console.error("[TTS] Error in speakText:", err);
        if (err.name === 'TypeError' && err.message.includes('fetch')) {
            alert(
                `TTS Error: Cannot connect to backend at ${API}. Please check:\n1. Backend is running\n2. Backend URL is correct\n3. No firewall blocking the connection`
            );
        } else {
            alert(`TTS Error: ${err.message}`);
        }
    }
};

/**
 * Play audio at a slower speed with pitch correction
 * Used for listening comprehension exercises
 * @param {Blob} audioBlob - Audio blob to play
 * @param {number} playbackRate - Playback rate (0.5 = half speed, 1.0 = normal)
 */
export const playAudioSlow = (audioBlob, playbackRate = 0.75) => {
    try {
        const url = URL.createObjectURL(audioBlob);
        const audio = new Audio(url);
        audio.playbackRate = playbackRate;
        audio.volume = 1.0;

        const cleanup = () => {
            URL.revokeObjectURL(url);
        };

        audio.onerror = (e) => {
            console.error("[Audio] Slow playback error:", e);
            cleanup();
        };

        audio.onended = () => {
            cleanup();
        };

        audio.play().catch(err => {
            console.error("[Audio] Failed to play slow audio:", err);
            cleanup();
        });
    } catch (err) {
        console.error("[Audio] Error in playAudioSlow:", err);
    }
};
