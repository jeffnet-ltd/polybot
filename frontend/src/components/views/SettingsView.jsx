/**
 * SettingsView Component
 * Displays application settings, about info, and licenses
 */

import React, { useState } from 'react';

const SettingsView = React.memo(({ userProfile, t }) => {
    const [activeTab, setActiveTab] = useState('about');

    return (
        <div className="max-w-4xl mx-auto p-6 space-y-6">
            <h2 className="text-3xl font-bold text-gray-800 mb-6">Settings</h2>

            {/* Tabs */}
            <div className="border-b border-gray-200">
                <nav className="flex space-x-8">
                    <button
                        onClick={() => setActiveTab('about')}
                        className={`py-4 px-1 border-b-2 font-medium text-sm ${
                            activeTab === 'about'
                                ? 'border-green-500 text-green-600'
                                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                        }`}
                    >
                        About
                    </button>
                    <button
                        onClick={() => setActiveTab('legal')}
                        className={`py-4 px-1 border-b-2 font-medium text-sm ${
                            activeTab === 'legal'
                                ? 'border-green-500 text-green-600'
                                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                        }`}
                    >
                        Legal & Licenses
                    </button>
                </nav>
            </div>

            {/* About Tab */}
            {activeTab === 'about' && (
                <div className="space-y-6">
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
                        <h3 className="text-2xl font-bold text-gray-800 mb-4">About PolyBot</h3>
                        <p className="text-gray-700 mb-4">
                            PolyBot is an AI-powered multilingual language learning platform that combines
                            structured CEFR A1 curriculum with interactive AI roleplay to provide a "True Bilingual"
                            learning experience.
                        </p>
                        <div className="space-y-3">
                            <div>
                                <h4 className="font-semibold text-gray-800 mb-2">Version</h4>
                                <p className="text-gray-600">2.0.0</p>
                            </div>
                            <div>
                                <h4 className="font-semibold text-gray-800 mb-2">Key Features</h4>
                                <ul className="list-disc list-inside text-gray-600 space-y-1">
                                    <li>10-module CEFR A1 Curriculum</li>
                                    <li>Interactive exercises with AI validation</li>
                                    <li>Voice-based practice with pronunciation feedback</li>
                                    <li>Scenario-based roleplay conversations</li>
                                    <li>Real-time grammar and vocabulary corrections</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Legal Tab */}
            {activeTab === 'legal' && (
                <div className="space-y-6">
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
                        <h3 className="text-2xl font-bold text-gray-800 mb-4">Open Source Licenses</h3>
                        <p className="text-gray-600 mb-6">
                            PolyBot uses the following open-source models and libraries:
                        </p>

                        <div className="space-y-6">
                            {/* Llama 3 */}
                            <div className="border-l-4 border-blue-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Llama 3 8B Instruct</h4>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>License:</strong> Meta Llama 3 Community License Agreement
                                </p>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>Source:</strong> Meta AI
                                </p>
                                <p className="text-sm text-gray-600">
                                    Llama 3 is licensed under Meta's custom license. See the full license at:{' '}
                                    <a
                                        href="https://llama.meta.com/llama3/license/"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        className="text-blue-600 hover:underline"
                                    >
                                        https://llama.meta.com/llama3/license/
                                    </a>
                                </p>
                            </div>

                            {/* Whisper */}
                            <div className="border-l-4 border-green-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Whisper</h4>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>License:</strong> MIT License
                                </p>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>Source:</strong> OpenAI
                                </p>
                                <p className="text-sm text-gray-600">
                                    Copyright (c) 2022 OpenAI. Licensed under the MIT License.
                                </p>
                            </div>

                            {/* Piper TTS */}
                            <div className="border-l-4 border-purple-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Piper TTS</h4>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>License:</strong> MIT License
                                </p>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>Source:</strong> Rhasspy
                                </p>
                                <p className="text-sm text-gray-600">
                                    Copyright (c) 2022 Michael Hansen. Licensed under the MIT License.
                                </p>
                            </div>

                            {/* AutoGPTQ */}
                            <div className="border-l-4 border-orange-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">AutoGPTQ</h4>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>License:</strong> Apache License 2.0
                                </p>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>Source:</strong> AutoGPTQ Project
                                </p>
                                <p className="text-sm text-gray-600">
                                    Licensed under the Apache License, Version 2.0.
                                </p>
                            </div>

                            {/* Transformers */}
                            <div className="border-l-4 border-yellow-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Transformers</h4>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>License:</strong> Apache License 2.0
                                </p>
                                <p className="text-sm text-gray-600 mb-2">
                                    <strong>Source:</strong> Hugging Face
                                </p>
                                <p className="text-sm text-gray-600">
                                    Copyright (c) 2018-2024 Hugging Face. Licensed under the Apache License, Version 2.0.
                                </p>
                            </div>
                        </div>
                    </div>

                    {/* Privacy & Terms */}
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
                        <h3 className="text-xl font-bold text-gray-800 mb-4">Privacy & Terms</h3>
                        <p className="text-gray-600 mb-4">
                            PolyBot processes audio and text data locally or on secure cloud infrastructure.
                            All user data is handled in accordance with our privacy policy.
                        </p>
                        <p className="text-sm text-gray-500">
                            For questions about data handling or licensing, please contact the development team.
                        </p>
                    </div>
                </div>
            )}
        </div>
    );
});

SettingsView.displayName = 'SettingsView';

export default SettingsView;
