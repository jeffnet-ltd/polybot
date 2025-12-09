/**
 * LandingPage Component
 * Marketing landing page for PolyBot
 */

import React from 'react';
import { GraduationCap, Zap, Mic, CheckCircle } from 'lucide-react';
import { CORE_LANGUAGES } from '../../config/constants';

const LandingPage = ({ onGetStarted }) => {
    return (
        <div className="min-h-screen bg-gradient-to-br from-[#4CAF50] via-[#2196F3] to-[#9C27B0]">
            {/* Hero Section */}
            <div className="container mx-auto px-4 py-16">
                <div className="max-w-4xl mx-auto text-center text-white mb-16">
                    <h1 className="text-5xl md:text-6xl font-extrabold mb-6 drop-shadow-lg">
                        PolyBot
                    </h1>
                    <p className="text-2xl md:text-3xl font-semibold mb-4 drop-shadow-md">
                        Your AI-Powered Multilingual Language Tutor
                    </p>
                    <p className="text-lg md:text-xl mb-8 text-white/90 max-w-2xl mx-auto">
                        Learn in your target language while receiving explanations in your native language.
                        A True Bilingual learning experience with structured CEFR A1 curriculum.
                    </p>
                    <button
                        onClick={onGetStarted}
                        className="bg-white text-[#388E3C] px-8 py-4 rounded-[30px] font-bold text-lg shadow-2xl hover:shadow-3xl transform hover:scale-105 transition duration-300"
                    >
                        Start Learning Free
                    </button>
                </div>

                {/* Key Features Grid */}
                <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto mb-16">
                    {/* Feature 1: Structured Curriculum */}
                    <div className="bg-white/95 backdrop-blur-sm p-6 rounded-[30px] shadow-xl border border-white/20">
                        <div className="bg-[#4CAF50] p-3 rounded-full w-16 h-16 flex items-center justify-center mb-4 mx-auto">
                            <GraduationCap size={32} className="text-white" />
                        </div>
                        <h3 className="text-xl font-bold text-gray-800 mb-3 text-center">
                            Structured CEFR A1 Curriculum
                        </h3>
                        <p className="text-gray-600 text-center">
                            10-module comprehensive course with complete lessons in Module A1.1 (Greetings & Introductions) and Module A1.2 (Personal Information & Family).
                            Learn grammar, vocabulary, and conversation skills systematically.
                        </p>
                    </div>

                    {/* Feature 2: AI-Powered Learning */}
                    <div className="bg-white/95 backdrop-blur-sm p-6 rounded-[30px] shadow-xl border border-white/20">
                        <div className="bg-[#2196F3] p-3 rounded-full w-16 h-16 flex items-center justify-center mb-4 mx-auto">
                            <Zap size={32} className="text-white" />
                        </div>
                        <h3 className="text-xl font-bold text-gray-800 mb-3 text-center">
                            AI-Powered Exercises
                        </h3>
                        <p className="text-gray-600 text-center">
                            Interactive exercises including Match Pairs, Unscramble, Echo Chamber, Mini-Prompt,
                            and Boss Fight conversations. Get instant, pedagogically-focused feedback.
                        </p>
                    </div>

                    {/* Feature 3: Voice Integration */}
                    <div className="bg-white/95 backdrop-blur-sm p-6 rounded-[30px] shadow-xl border border-white/20">
                        <div className="bg-[#9C27B0] p-3 rounded-full w-16 h-16 flex items-center justify-center mb-4 mx-auto">
                            <Mic size={32} className="text-white" />
                        </div>
                        <h3 className="text-xl font-bold text-gray-800 mb-3 text-center">
                            Voice-Integrated Learning
                        </h3>
                        <p className="text-gray-600 text-center">
                            Practice pronunciation with Whisper speech-to-text transcription and Piper TTS audio playback.
                            Get phonetic scoring and pronunciation feedback.
                        </p>
                    </div>
                </div>

                {/* Languages Section */}
                <div className="bg-white/95 backdrop-blur-sm p-8 rounded-[30px] shadow-xl border border-white/20 max-w-4xl mx-auto mb-16">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
                        Learn Multiple Languages
                    </h2>
                    <p className="text-gray-600 text-center mb-8">
                        Currently supporting Italian, French, Spanish, Portuguese, Twi, and more.
                        More languages coming soon.
                    </p>
                    <div className="flex flex-wrap justify-center gap-4">
                        {CORE_LANGUAGES.map((lang) => (
                            <div
                                key={lang.code}
                                className="bg-gray-50 px-6 py-3 rounded-xl border border-gray-200 flex items-center space-x-2 shadow-sm"
                            >
                                <img
                                    src={`https://flagcdn.com/w20/${lang.country}.png`}
                                    alt={lang.name}
                                    className="w-5 h-5"
                                />
                                <span className="font-semibold text-gray-700">{lang.name}</span>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Exercise Types Section */}
                <div className="bg-white/95 backdrop-blur-sm p-8 rounded-[30px] shadow-xl border border-white/20 max-w-5xl mx-auto mb-16">
                    <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
                        Comprehensive Exercise Types
                    </h2>
                    <div className="grid md:grid-cols-2 gap-4">
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Info Cards</h4>
                                <p className="text-sm text-gray-600">Audio playback, vocabulary introduction, grammar explanations</p>
                            </div>
                        </div>
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Match Pairs</h4>
                                <p className="text-sm text-gray-600">Audio-to-text matching, interactive selection</p>
                            </div>
                        </div>
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Echo Chamber</h4>
                                <p className="text-sm text-gray-600">Voice recording with pronunciation feedback</p>
                            </div>
                        </div>
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Boss Fight</h4>
                                <p className="text-sm text-gray-600">Conversation practice with grammar and spelling feedback</p>
                            </div>
                        </div>
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Unscramble</h4>
                                <p className="text-sm text-gray-600">Drag-and-drop sentence construction</p>
                            </div>
                        </div>
                        <div className="flex items-start space-x-3 p-4 bg-gray-50 rounded-xl">
                            <CheckCircle size={24} className="text-[#4CAF50] flex-shrink-0 mt-1" />
                            <div>
                                <h4 className="font-bold text-gray-800 mb-1">Mini-Prompt</h4>
                                <p className="text-sm text-gray-600">Contextual exercises with AI validation</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* CTA Section */}
                <div className="text-center max-w-2xl mx-auto">
                    <h2 className="text-3xl md:text-4xl font-bold text-white mb-4 drop-shadow-lg">
                        Ready to Start Your Language Journey?
                    </h2>
                    <p className="text-lg text-white/90 mb-8">
                        Join PolyBot and experience a new way of learning languages with AI-powered,
                        structured lessons designed for real-world communication.
                    </p>
                    <button
                        onClick={onGetStarted}
                        className="bg-white text-[#388E3C] px-10 py-5 rounded-[30px] font-bold text-xl shadow-2xl hover:shadow-3xl transform hover:scale-105 transition duration-300"
                    >
                        Get Started Now
                    </button>
                </div>
            </div>
        </div>
    );
};

export default LandingPage;
