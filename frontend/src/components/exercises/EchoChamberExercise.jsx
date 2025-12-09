/**
 * EchoChamberExercise Component
 *
 * A pronunciation practice exercise using speech recognition.
 * Records user audio, analyzes pronunciation, and provides detailed feedback.
 * Features include playback, re-recording, and skip functionality.
 */

import React, { useState, useEffect, useRef } from 'react';
import { Volume2, Mic, RefreshCcw, CheckSquare, Loader2 } from 'lucide-react';
import { speakText } from '../../utils/audio';
import { analyzeAudio } from '../../services/ttsService';

const EchoChamberExercise = ({ prompt, targetPhrase, targetLang, onAnswer, explanation, onComplete }) => {
    const [isRecording, setIsRecording] = useState(false);
    const [isProcessing, setIsProcessing] = useState(false);
    const [transcription, setTranscription] = useState(null);
    const [confidence, setConfidence] = useState(null);
    const [phoneticScore, setPhoneticScore] = useState(null);
    const [isComplete, setIsComplete] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioChunks, setAudioChunks] = useState([]);
    const [recordedBlob, setRecordedBlob] = useState(null);
    const [audioUrl, setAudioUrl] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const audioRef = useRef(null);
    const playbackAudioRef = useRef(null);

    // Reset all state when targetPhrase changes (new exercise)
    useEffect(() => {
        // Reset all state when moving to a new exercise
        setTranscription(null);
        setConfidence(null);
        setPhoneticScore(null);
        setIsComplete(false);
        setIsRecording(false);
        setIsProcessing(false);
        setRecordedBlob(null);
        setAudioChunks([]);
        setIsPlaying(false);

        // Clean up previous recording
        if (audioUrl) {
            URL.revokeObjectURL(audioUrl);
            setAudioUrl(null);
        }

        // Stop any active recording
        if (mediaRecorder && mediaRecorder.state !== 'inactive') {
            try {
                mediaRecorder.stop();
            } catch (e) {
                console.log("MediaRecorder already stopped");
            }
        }
        setMediaRecorder(null);

        // Stop any audio playback
        if (playbackAudioRef.current) {
            playbackAudioRef.current.pause();
            playbackAudioRef.current.currentTime = 0;
        }
    }, [targetPhrase]);

    // Auto-play target phrase on mount (only once per phrase)
    const lastPlayedPhraseRef = useRef(null);
    useEffect(() => {
        // Only play if this is a new phrase (different from last one)
        if (targetPhrase && lastPlayedPhraseRef.current !== targetPhrase) {
            lastPlayedPhraseRef.current = targetPhrase;
            speakText(targetPhrase, targetLang);
        }
    }, [targetPhrase, targetLang]); // speakText is a stable global function, no need to include in deps

    // Cleanup audio URL on unmount
    useEffect(() => {
        return () => {
            if (audioUrl) {
                URL.revokeObjectURL(audioUrl);
            }
        };
    }, [audioUrl]);

    const startRecording = async () => {
        try {
            // Clean up previous recording
            if (audioUrl) {
                URL.revokeObjectURL(audioUrl);
                setAudioUrl(null);
            }
            setRecordedBlob(null);
            setTranscription(null);
            setConfidence(null);
            setPhoneticScore(null);
            setIsComplete(false);

            // Enhanced audio constraints for better quality
            const audioConstraints = {
                audio: {
                    echoCancellation: true,
                    noiseSuppression: true,
                    autoGainControl: true,
                    sampleRate: 44100,
                    channelCount: 1,
                    // Request specific audio input device if available
                    googEchoCancellation: true,
                    googAutoGainControl: true,
                    googNoiseSuppression: true,
                    googHighpassFilter: true,
                    googTypingNoiseDetection: true
                }
            };

            const stream = await navigator.mediaDevices.getUserMedia(audioConstraints);

            // Log audio track info for debugging
            const audioTracks = stream.getAudioTracks();
            if (audioTracks.length > 0) {
                const track = audioTracks[0];
                console.log("[Recording] Audio track:", {
                    label: track.label,
                    enabled: track.enabled,
                    muted: track.muted,
                    readyState: track.readyState,
                    settings: track.getSettings()
                });
            }

            // Determine best mimeType for MediaRecorder
            let mimeType = 'audio/webm';
            if (MediaRecorder.isTypeSupported('audio/webm;codecs=opus')) {
                mimeType = 'audio/webm;codecs=opus';
            } else if (MediaRecorder.isTypeSupported('audio/webm')) {
                mimeType = 'audio/webm';
            } else if (MediaRecorder.isTypeSupported('audio/mp4')) {
                mimeType = 'audio/mp4';
            } else if (MediaRecorder.isTypeSupported('audio/ogg;codecs=opus')) {
                mimeType = 'audio/ogg;codecs=opus';
            }

            console.log("[Recording] Using mimeType:", mimeType);

            const recorderOptions = {
                mimeType: mimeType,
                audioBitsPerSecond: 128000 // Higher quality
            };

            const recorder = new MediaRecorder(stream, recorderOptions);
            const chunks = [];

            recorder.ondataavailable = (e) => {
                console.log("[Recording] Data available:", e.data.size, "bytes");
                if (e.data.size > 0) {
                    chunks.push(e.data);
                }
            };

            recorder.onerror = (e) => {
                console.error("[Recording] MediaRecorder error:", e);
                alert("Recording error occurred. Please try again.");
                setIsRecording(false);
            };

            recorder.onstop = () => {
                console.log("[Recording] Stopped. Total chunks:", chunks.length, "Total size:", chunks.reduce((sum, chunk) => sum + chunk.size, 0), "bytes");
                const audioBlob = new Blob(chunks, { type: mimeType });
                setAudioChunks(chunks);
                setRecordedBlob(audioBlob);
                // Create URL for playback
                const url = URL.createObjectURL(audioBlob);
                setAudioUrl(url);
                stream.getTracks().forEach(track => {
                    track.stop();
                    console.log("[Recording] Stopped track:", track.label);
                });
            };

            // Start recording with timeslice to ensure data is captured
            recorder.start(100); // Collect data every 100ms
            setMediaRecorder(recorder);
            setIsRecording(true);
            console.log("[Recording] Started with mimeType:", mimeType);
        } catch (error) {
            console.error("Error accessing microphone:", error);
            let errorMessage = "Could not access microphone. ";
            if (error.name === 'NotAllowedError') {
                errorMessage += "Please allow microphone access in your browser settings.";
            } else if (error.name === 'NotFoundError') {
                errorMessage += "No microphone found. Please connect a microphone.";
            } else if (error.name === 'NotReadableError') {
                errorMessage += "Microphone is being used by another application.";
            } else {
                errorMessage += `Error: ${error.message}`;
            }
            alert(errorMessage);
        }
    };

    const stopRecording = () => {
        if (mediaRecorder && isRecording) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    };

    const playRecording = () => {
        if (audioUrl && playbackAudioRef.current) {
            console.log("[Playback] Playing recording, URL:", audioUrl);
            playbackAudioRef.current.play()
                .then(() => {
                    console.log("[Playback] Playback started");
                    setIsPlaying(true);
                })
                .catch(err => {
                    console.error("[Playback] Error playing recording:", err);
                    alert("Could not play recording. The audio file may be corrupted or the format is not supported.");
                    setIsPlaying(false);
                });
        } else {
            console.warn("[Playback] Cannot play - audioUrl:", audioUrl, "ref:", playbackAudioRef.current);
        }
    };

    const handlePlaybackEnded = () => {
        setIsPlaying(false);
    };

    const handleReRecord = () => {
        // Clean up current recording
        if (audioUrl) {
            URL.revokeObjectURL(audioUrl);
            setAudioUrl(null);
        }
        setRecordedBlob(null);
        setTranscription(null);
        setConfidence(null);
        setPhoneticScore(null);
        setIsComplete(false);
        // Start new recording
        startRecording();
    };

    const handleSubmit = async () => {
        if (!recordedBlob) return;

        setIsProcessing(true);
        await analyzeAudioFile(recordedBlob);
    };

    const analyzeAudioFile = async (audioBlob) => {
        try {
            const formData = new FormData();
            formData.append('file', audioBlob, 'recording.webm');
            // Always send language and target_phrase if available
            if (targetLang) {
                formData.append('language', targetLang);
                console.log("[Analyze] Sending language:", targetLang);
            }
            if (targetPhrase) {
                formData.append('target_phrase', targetPhrase);
                console.log("[Analyze] Sending target_phrase:", targetPhrase);
            }

            const responseData = await analyzeAudio(formData);

            const { text, confidence: conf, phonetic_score } = responseData;
            setTranscription(text);
            setConfidence(conf);
            setPhoneticScore(phonetic_score);

            // Check if transcription seems completely wrong (very low phonetic score)
            const isTranscriptionValid = phonetic_score > 0.1 || conf > 0.3;

            // Determine if answer is correct (phonetic score > 0.7 or high confidence)
            const isCorrect = phonetic_score >= 0.7 || conf >= 0.8;

            // If transcription is clearly wrong, don't mark as complete - allow re-recording
            if (!isTranscriptionValid && phonetic_score < 0.2) {
                setIsProcessing(false);
                setIsComplete(false);
                // Don't call onAnswer yet - let user re-record
                return;
            }

            setIsComplete(true);
            setIsProcessing(false);
            onAnswer(isCorrect ? 'correct' : 'incorrect', text);
        } catch (error) {
            console.error("Error analyzing audio:", error);
            alert("Error analyzing audio. Please try again.");
            setIsProcessing(false);
        }
    };

    const handleReplay = () => {
        if (targetPhrase) {
            speakText(targetPhrase, targetLang);
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt || "Repeat after me"}</h3>

            {/* Target phrase display */}
            <div className="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center">
                <p className="text-2xl font-bold text-blue-800 mb-2">{targetPhrase}</p>
                <button
                    onClick={handleReplay}
                    className="inline-flex items-center gap-2 px-4 py-2 bg-blue-100 text-blue-700 rounded-lg hover:bg-blue-200 transition"
                >
                    <Volume2 size={20} />
                    Replay
                </button>
            </div>

            {/* Recording controls */}
            <div className="flex flex-col items-center gap-4">
                {!isRecording && !recordedBlob && !isProcessing && (
                    <>
                        <button
                            onClick={startRecording}
                            className="px-8 py-4 bg-red-500 text-white rounded-full font-bold shadow-lg hover:bg-red-600 transition flex items-center gap-3"
                        >
                            <Mic size={24} />
                            Start Recording
                        </button>
                        <div className="mt-4 text-center">
                            <p className="text-xs text-gray-500 mb-2">Don't have a mic? Click here to skip this lesson and come back later</p>
                            <button
                                onClick={() => {
                                    if (onComplete) {
                                        onComplete();
                                    }
                                }}
                                className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300 transition"
                            >
                                Skip
                            </button>
                        </div>
                    </>
                )}

                {isRecording && (
                    <div className="flex flex-col items-center gap-4">
                        <div className="flex items-center gap-3">
                            <div className="w-4 h-4 bg-red-500 rounded-full animate-pulse"></div>
                            <span className="text-red-600 font-bold">Recording...</span>
                        </div>
                        <button
                            onClick={stopRecording}
                            className="px-8 py-4 bg-gray-600 text-white rounded-full font-bold shadow-lg hover:bg-gray-700 transition"
                        >
                            Stop Recording
                        </button>
                    </div>
                )}

                {/* Playback and submit controls after recording */}
                {recordedBlob && !isComplete && (
                    <div className="flex flex-col items-center gap-4 w-full">
                        <p className="text-sm text-gray-600 font-medium">Review your recording:</p>
                        <audio
                            ref={playbackAudioRef}
                            src={audioUrl}
                            onEnded={handlePlaybackEnded}
                            onError={(e) => {
                                console.error("Audio playback error:", e);
                                setIsPlaying(false);
                            }}
                            onLoadedData={() => {
                                console.log("[Playback] Audio loaded, duration:", playbackAudioRef.current?.duration);
                            }}
                            className="hidden"
                        />
                        <div className="flex gap-3">
                            <button
                                onClick={playRecording}
                                disabled={isPlaying || isProcessing}
                                className="px-6 py-3 bg-blue-500 text-white rounded-lg font-semibold shadow-md hover:bg-blue-600 transition disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
                            >
                                <Volume2 size={20} />
                                {isPlaying ? "Playing..." : "Play Recording"}
                            </button>
                            <button
                                onClick={handleReRecord}
                                disabled={isProcessing}
                                className="px-6 py-3 bg-gray-500 text-white rounded-lg font-semibold shadow-md hover:bg-gray-600 transition disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
                            >
                                <RefreshCcw size={20} />
                                Re-record
                            </button>
                            <button
                                onClick={handleSubmit}
                                disabled={isProcessing}
                                className="px-6 py-3 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white rounded-lg font-semibold shadow-md transition transform hover:scale-[1.02] disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center gap-2"
                            >
                                {isProcessing ? (
                                    <>
                                        <Loader2 className="w-5 h-5 animate-spin" />
                                        Analyzing...
                                    </>
                                ) : (
                                    <>
                                        <CheckSquare size={20} />
                                        Submit
                                    </>
                                )}
                            </button>
                        </div>
                        <div className="mt-4 text-center">
                            <p className="text-xs text-gray-500 mb-2">Don't have a mic? Click here to skip this lesson and come back later</p>
                            <button
                                onClick={() => {
                                    if (onComplete) {
                                        onComplete();
                                    }
                                }}
                                className="px-6 py-2 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300 transition"
                            >
                                Skip
                            </button>
                        </div>
                    </div>
                )}

                {isProcessing && !recordedBlob && (
                    <div className="flex items-center gap-3 text-gray-600">
                        <Loader2 className="w-6 h-6 animate-spin" />
                        <span>Analyzing your pronunciation...</span>
                    </div>
                )}
            </div>

            {/* Results */}
            {transcription && (
                <div className={`p-6 rounded-xl border space-y-3 ${phoneticScore < 0.2 ? 'bg-red-50 border-red-200' :
                        isComplete && phoneticScore >= 0.7 ? 'bg-green-50 border-green-200' :
                            'bg-gray-50 border-gray-200'
                    }`}>
                    <div>
                        <p className="text-sm text-gray-500 mb-1">Your transcription:</p>
                        <p className="text-lg font-semibold text-gray-800">{transcription}</p>
                        {phoneticScore < 0.2 && (
                            <p className="text-sm text-red-600 mt-2 font-medium">
                                ⚠️ Transcription may be incorrect. Please try recording again.
                            </p>
                        )}
                        {isComplete && phoneticScore >= 0.7 && (
                            <div className="mt-3">
                                <p className="text-sm text-green-600 font-medium mb-2">
                                    ✓ Excellent pronunciation!
                                </p>
                                <p className="text-sm text-gray-700">
                                    {targetPhrase === "Come stai?" && "Great job! I can hear you're really getting those vowel sounds right. The 'o' in 'Come' and the 'ai' in 'stai' are coming through clearly - you've got this!"}
                                    {targetPhrase === "Arrivederci" && "Wow, nice work! That rolled 'r' and soft 'c' in 'Arrivederci' can be tricky, but you're handling them really well. Keep it up!"}
                                    {targetPhrase === "Piacere" && "Perfect! You nailed that soft 'c' sound (like 'ch' in English 'church'). That's exactly how it should sound - you're doing great!"}
                                    {targetPhrase === "Mi chiamo" && "Excellent! You got that hard 'ch' sound right (like 'k' in English). I know it's confusing because 'ch' in Italian sounds different from English, but you're getting it!"}
                                    {targetPhrase === "A presto" && "Nice work! You handled that 'pre' cluster really well. The 'r' has that nice roll to it, and your 'e' sounds clear and open - perfect!"}
                                    {!["Come stai?", "Arrivederci", "Piacere", "Mi chiamo", "A presto"].includes(targetPhrase) && explanation && explanation}
                                </p>
                            </div>
                        )}
                        {isComplete && phoneticScore >= 0.4 && phoneticScore < 0.7 && (
                            <div className="mt-3">
                                <p className="text-sm text-yellow-600 font-medium mb-2">
                                    Good attempt! Your pronunciation is close.
                                </p>
                                <p className="text-sm text-gray-700">
                                    {targetPhrase === "Come stai?" && "You're really close! Try opening your mouth a bit more for those vowel sounds - 'Come' has a nice open 'o', and 'stai' ends with a clear 'ai' sound. You've got this!"}
                                    {targetPhrase === "Arrivederci" && "Good effort! The 'r' in 'Arrivederci' needs a bit of a roll - try placing your tongue near the roof of your mouth and letting it vibrate. Also, remember the 'c' should be soft (like 'ch'). Keep practicing!"}
                                    {targetPhrase === "Piacere" && "You're on the right track! The 'c' in 'Piacere' should be soft (like 'ch' in 'church'), not hard. Try listening to the example one more time - you'll hear that soft 'c' sound. You're almost there!"}
                                    {targetPhrase === "Mi chiamo" && "Almost there! Remember, the 'ch' in 'chiamo' makes a hard 'k' sound (like in 'key'), not a soft 'ch'. Think 'kee-AH-mo' - you can do it!"}
                                    {targetPhrase === "A presto" && "Good try! Focus on that 'pre' cluster - the 'r' should have a slight roll, and make sure both syllables come through clearly: 'PREH-sto'. Keep at it!"}
                                    {!["Come stai?", "Arrivederci", "Piacere", "Mi chiamo", "A presto"].includes(targetPhrase) && `Try to match: "${targetPhrase}". ${explanation || 'Focus on pronunciation clarity.'}`}
                                </p>
                            </div>
                        )}
                        {isComplete && phoneticScore < 0.4 && phoneticScore >= 0.2 && (
                            <div className="mt-3">
                                <p className="text-sm text-orange-600 font-medium mb-2">
                                    Your pronunciation needs improvement.
                                </p>
                                <p className="text-sm text-gray-700">
                                    {targetPhrase === "Come stai?" && "Don't worry, let's work on this together! Italian vowels are more open than English ones, so try opening your mouth wider. Also, remember to raise your voice at the end of 'stai?' to make it sound like a question. Listen to the example and give it another try - you will get it!"}
                                    {targetPhrase === "Arrivederci" && "This one's a bit tricky, but we'll get there! The rolled 'r' takes practice - try vibrating your tongue. And remember, the 'c' should be soft (like 'ch'), not hard. Break it down slowly: 'ah-ree-veh-DEHR-chee'. You've got this!"}
                                    {targetPhrase === "Piacere" && "Let's work on this together! The 'c' in 'Piacere' is soft (like 'ch' in 'church'), so it should sound like 'pyah-CHEH-reh'. Make sure you're not using a hard 'k' sound. Listen carefully and try again - I believe in you!"}
                                    {targetPhrase === "Mi chiamo" && "I know this can be confusing! Remember: 'ch' in Italian makes a 'k' sound, not 'ch'. So 'chiamo' sounds like 'kee-AH-mo'. Make sure both words are clear: 'mee kee-AH-mo'. You're learning, and that's what matters!"}
                                    {targetPhrase === "A presto" && "Let's break this down together! Focus on: 1) Getting that 'r' to roll slightly, 2) Making sure both syllables are clear: 'PREH-sto', 3) Keeping that 'e' open and clear. Listen to the example and try again - practice makes perfect!"}
                                    {!["Come stai?", "Arrivederci", "Piacere", "Mi chiamo", "A presto"].includes(targetPhrase) && `Try to match: "${targetPhrase}". ${explanation || 'Listen carefully and try again.'}`}
                                </p>
                            </div>
                        )}
                    </div>
                    <div className="grid grid-cols-2 gap-4">
                        <div>
                            <p className="text-xs text-gray-500 mb-1">Confidence</p>
                            <p className="text-xl font-bold text-blue-600">{(confidence * 100).toFixed(0)}%</p>
                        </div>
                        <div>
                            <p className="text-xs text-gray-500 mb-1">Phonetic Score</p>
                            <p className={`text-xl font-bold ${phoneticScore >= 0.7 ? 'text-green-600' :
                                    phoneticScore >= 0.4 ? 'text-yellow-600' :
                                        'text-red-600'
                                }`}>
                                {(phoneticScore * 100).toFixed(0)}%
                            </p>
                        </div>
                    </div>
                    {explanation && (
                        <p className="text-sm text-gray-600 italic">{explanation}</p>
                    )}
                    {phoneticScore < 0.2 && !isComplete && (
                        <button
                            onClick={handleReRecord}
                            className="w-full mt-4 px-6 py-3 bg-red-500 text-white rounded-lg font-semibold shadow-md hover:bg-red-600 transition flex items-center justify-center gap-2"
                        >
                            <RefreshCcw size={20} />
                            Re-record (Transcription seems incorrect)
                        </button>
                    )}
                </div>
            )}
        </div>
    );
};

EchoChamberExercise.displayName = 'EchoChamberExercise';

export default EchoChamberExercise;
