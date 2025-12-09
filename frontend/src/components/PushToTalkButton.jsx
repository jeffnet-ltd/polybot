import React, { useState, useRef, useEffect } from 'react';
import { Mic, MicOff } from 'lucide-react';

/**
 * PushToTalkButton Component
 * Hold-to-record button with MediaRecorder API
 * Walkie-talkie UX: one-way communication prevents interruption
 */
const PushToTalkButton = ({ onRecordingComplete, onError, disabled = false }) => {
    const [isRecording, setIsRecording] = useState(false);
    const [isProcessing, setIsProcessing] = useState(false);
    const mediaRecorderRef = useRef(null);
    const audioChunksRef = useRef([]);
    const streamRef = useRef(null);

    useEffect(() => {
        // Cleanup on unmount
        return () => {
            if (streamRef.current) {
                streamRef.current.getTracks().forEach(track => track.stop());
            }
        };
    }, []);

    const startRecording = async () => {
        if (disabled || isProcessing) return;

        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            streamRef.current = stream;

            const mediaRecorder = new MediaRecorder(stream, {
                mimeType: 'audio/webm;codecs=opus'
            });

            audioChunksRef.current = [];

            mediaRecorder.ondataavailable = (event) => {
                if (event.data.size > 0) {
                    audioChunksRef.current.push(event.data);
                }
            };

            mediaRecorder.onstop = async () => {
                const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/webm' });
                
                // Stop all tracks
                if (streamRef.current) {
                    streamRef.current.getTracks().forEach(track => track.stop());
                    streamRef.current = null;
                }

                setIsProcessing(true);
                
                try {
                    await onRecordingComplete(audioBlob);
                } catch (error) {
                    console.error('Error processing recording:', error);
                    if (onError) {
                        onError(error);
                    }
                } finally {
                    setIsProcessing(false);
                    audioChunksRef.current = [];
                }
            };

            mediaRecorder.onerror = (event) => {
                console.error('MediaRecorder error:', event);
                setIsRecording(false);
                if (streamRef.current) {
                    streamRef.current.getTracks().forEach(track => track.stop());
                    streamRef.current = null;
                }
                if (onError) {
                    onError(new Error('Recording error occurred'));
                }
            };

            mediaRecorder.start();
            mediaRecorderRef.current = mediaRecorder;
            setIsRecording(true);
        } catch (err) {
            console.error('Error accessing microphone:', err);
            setIsRecording(false);
            if (onError) {
                onError(new Error('Could not access microphone. Please check permissions.'));
            }
        }
    };

    const stopRecording = () => {
        if (mediaRecorderRef.current && isRecording) {
            mediaRecorderRef.current.stop();
            setIsRecording(false);
        }
    };

    const handleMouseDown = (e) => {
        e.preventDefault();
        startRecording();
    };

    const handleMouseUp = (e) => {
        e.preventDefault();
        stopRecording();
    };

    const handleTouchStart = (e) => {
        e.preventDefault();
        startRecording();
    };

    const handleTouchEnd = (e) => {
        e.preventDefault();
        stopRecording();
    };

    // Prevent default context menu on long press
    const handleContextMenu = (e) => {
        e.preventDefault();
    };

    const buttonState = isProcessing ? 'processing' : isRecording ? 'recording' : 'idle';

    return (
        <button
            className={`
                relative w-24 h-24 rounded-full flex items-center justify-center
                transition-all duration-200 transform
                ${disabled || isProcessing 
                    ? 'bg-gray-300 cursor-not-allowed' 
                    : isRecording 
                        ? 'bg-red-500 hover:bg-red-600 scale-110 shadow-lg' 
                        : 'bg-blue-500 hover:bg-blue-600 hover:scale-105 shadow-md'
                }
                focus:outline-none focus:ring-4 focus:ring-blue-300
                active:scale-95
            `}
            onMouseDown={handleMouseDown}
            onMouseUp={handleMouseUp}
            onMouseLeave={stopRecording} // Stop if mouse leaves button
            onTouchStart={handleTouchStart}
            onTouchEnd={handleTouchEnd}
            onContextMenu={handleContextMenu}
            disabled={disabled || isProcessing}
            aria-label={isRecording ? 'Recording... Release to send' : 'Hold to record'}
        >
            {isProcessing ? (
                <div className="w-8 h-8 border-4 border-white border-t-transparent rounded-full animate-spin" />
            ) : isRecording ? (
                <MicOff className="w-10 h-10 text-white" />
            ) : (
                <Mic className="w-10 h-10 text-white" />
            )}
            
            {/* Recording indicator pulse */}
            {isRecording && (
                <span className="absolute inset-0 rounded-full bg-red-500 animate-ping opacity-75" />
            )}
        </button>
    );
};

export default PushToTalkButton;

