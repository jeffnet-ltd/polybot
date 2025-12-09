/**
 * ListeningComprehensionExercise Component
 *
 * A listening comprehension exercise with multiple-choice questions.
 * Features normal and slow playback options with play count limits.
 */

import React, { useState } from 'react';
import { Volume2 } from 'lucide-react';
import { speakText, getTTSAudioBlob, unlockAudio } from '../../utils/audio';

const ListeningComprehensionExercise = ({ prompt, audioUrl, audioText, options, correctAnswer, allowReplay = true, maxPlays = 3, onAnswer, explanation, targetLang = "it" }) => {
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const [isPlayingSlow, setIsPlayingSlow] = useState(false);
    const [playCount, setPlayCount] = useState(0);
    const [slowPlayCount, setSlowPlayCount] = useState(0);
    const [hasAnswered, setHasAnswered] = useState(false);

    // Use audio_text if provided, otherwise fall back to audioUrl or correctAnswer
    const textToSpeak = audioText || (audioUrl ? null : correctAnswer);

    const handlePlay = async () => {
        if (playCount >= maxPlays || !textToSpeak || isPlaying || isPlayingSlow) return;

        // Always use TTS
        speakText(textToSpeak, targetLang);
        setPlayCount(p => p + 1);
        setIsPlaying(true);
        // Simulate playing state for TTS
        const estimatedDuration = Math.max(2000, textToSpeak.length * 150);
        setTimeout(() => setIsPlaying(false), estimatedDuration);
    };

    const handlePlaySlow = async () => {
        if (slowPlayCount >= maxPlays || !textToSpeak || isPlaying || isPlayingSlow) return;

        try {
            setIsPlayingSlow(true);
            setSlowPlayCount(p => p + 1);

            // Split text into words and play each word with a pause between them
            const words = textToSpeak.trim().split(/\s+/).filter(word => word.length > 0);
            const pauseDuration = 300; // 300ms pause between words

            for (let i = 0; i < words.length; i++) {
                const word = words[i];

                // Get audio for this word
                const audioBlob = await getTTSAudioBlob(word, targetLang);

                // Play the word
                await new Promise((resolve, reject) => {
                    const url = URL.createObjectURL(audioBlob);
                    const audio = new Audio(url);

                    audio.onended = () => {
                        URL.revokeObjectURL(url);
                        resolve();
                    };

                    audio.onerror = (error) => {
                        URL.revokeObjectURL(url);
                        reject(error);
                    };

                    unlockAudio();
                    audio.play().catch(reject);
                });

                // Add pause between words (except after the last word)
                if (i < words.length - 1) {
                    await new Promise(resolve => setTimeout(resolve, pauseDuration));
                }
            }
        } catch (error) {
            console.error('Error playing slow audio:', error);
            alert('Failed to play slow audio. Please try again.');
        } finally {
            setIsPlayingSlow(false);
        }
    };

    const handleSelect = (option) => {
        if (hasAnswered) return;
        setSelectedAnswer(option);
        setHasAnswered(true);
        const isCorrect = option === correctAnswer;
        onAnswer(isCorrect ? 'correct' : 'incorrect', option, explanation);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-blue-50 rounded-2xl p-6 border border-blue-200">
                <div className="flex items-center justify-center gap-4 mb-4 flex-wrap">
                    <button
                        onClick={handlePlay}
                        disabled={playCount >= maxPlays || isPlaying || isPlayingSlow}
                        className="px-6 py-3 bg-blue-600 text-white rounded-xl font-semibold hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition flex items-center gap-2"
                    >
                        <Volume2 size={20} />
                        {isPlaying ? 'Playing...' : allowReplay ? `Play Audio (${playCount}/${maxPlays})` : 'Play Audio'}
                    </button>
                    <button
                        onClick={handlePlaySlow}
                        disabled={slowPlayCount >= maxPlays || isPlaying || isPlayingSlow}
                        className="px-6 py-3 bg-purple-600 text-white rounded-xl font-semibold hover:bg-purple-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition flex items-center gap-2"
                    >
                        <Volume2 size={20} />
                        {isPlayingSlow ? 'Playing...' : allowReplay ? `Play Slow (${slowPlayCount}/${maxPlays})` : 'Play Slow'}
                    </button>
                </div>
                {playCount >= maxPlays && slowPlayCount >= maxPlays && (
                    <p className="text-sm text-gray-600 text-center">Maximum plays reached. Select your answer below.</p>
                )}
            </div>
            <div className="space-y-3">
                {options.map((opt, idx) => (
                    <button
                        key={idx}
                        onClick={() => handleSelect(opt)}
                        disabled={hasAnswered}
                        className={`w-full p-4 text-left rounded-xl border transition-all ${hasAnswered
                                ? opt === correctAnswer
                                    ? 'bg-green-100 border-green-300 text-green-800'
                                    : opt === selectedAnswer
                                        ? 'bg-red-100 border-red-300 text-red-800'
                                        : 'bg-gray-50 border-gray-200 text-gray-600'
                                : 'bg-white border-gray-200 hover:bg-gray-50 cursor-pointer'
                            }`}
                    >
                        {opt}
                    </button>
                ))}
            </div>
        </div>
    );
};

ListeningComprehensionExercise.displayName = 'ListeningComprehensionExercise';

export default ListeningComprehensionExercise;
