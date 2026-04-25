import React, { useState } from 'react';
import axios from 'axios';

const API = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

const SettingsView = React.memo(({ userProfile, setUserProfile, onPrivacyPolicy, onDeleteAccount, t }) => {
    const [activeTab, setActiveTab] = useState('account');
    const [editingName, setEditingName] = useState(false);
    const [nameInput, setNameInput] = useState('');
    const [nameSaving, setNameSaving] = useState(false);
    const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
    const [deleting, setDeleting] = useState(false);

    const initials = userProfile?.name
        ? userProfile.name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
        : '?';

    const handleEditName = () => {
        setNameInput(userProfile.name || '');
        setEditingName(true);
    };

    const handleSaveName = async () => {
        const trimmed = nameInput.trim();
        if (!trimmed || trimmed === userProfile.name) {
            setEditingName(false);
            return;
        }
        try {
            setNameSaving(true);
            await axios.patch(`${API}/api/user/${userProfile.user_id}`, { name: trimmed }, { withCredentials: true });
            setUserProfile(prev => ({ ...prev, name: trimmed }));
            setEditingName(false);
        } catch (err) {
            console.error('Failed to save name:', err);
        } finally {
            setNameSaving(false);
        }
    };

    const handleDeleteAccount = async () => {
        try {
            setDeleting(true);
            await axios.delete(`${API}/api/user/${userProfile.user_id}`, { withCredentials: true });
            onDeleteAccount();
        } catch (err) {
            console.error('Failed to delete account:', err);
            setDeleting(false);
            setShowDeleteConfirm(false);
        }
    };

    const tabs = [
        { id: 'account', label: 'Account' },
        { id: 'about',   label: 'About' },
        { id: 'legal',   label: 'Legal & Licenses' },
    ];

    return (
        <div className="max-w-4xl mx-auto p-6 space-y-6">
            <h2 className="text-3xl font-bold text-gray-800 mb-6">Settings</h2>

            {/* Tabs */}
            <div className="border-b border-gray-200">
                <nav className="flex space-x-8">
                    {tabs.map(tab => (
                        <button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`py-4 px-1 border-b-2 font-medium text-sm ${
                                activeTab === tab.id
                                    ? 'border-green-500 text-green-600'
                                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                            }`}
                        >
                            {tab.label}
                        </button>
                    ))}
                </nav>
            </div>

            {/* Account Tab */}
            {activeTab === 'account' && (
                <div className="space-y-6">
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
                        <h3 className="text-2xl font-bold text-gray-800 mb-6">Account</h3>

                        {/* Avatar */}
                        <div className="flex items-center space-x-4 mb-8">
                            <div className="w-16 h-16 rounded-full bg-emerald-500 flex items-center justify-center flex-shrink-0">
                                <span className="text-white text-xl font-bold">{initials}</span>
                            </div>
                            <div>
                                <p className="font-semibold text-gray-800">{userProfile.name}</p>
                                <p className="text-sm text-gray-500">{userProfile.email}</p>
                            </div>
                        </div>

                        {/* Name */}
                        <div className="mb-5">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Display Name</label>
                            {editingName ? (
                                <div className="flex items-center space-x-2">
                                    <input
                                        type="text"
                                        value={nameInput}
                                        onChange={e => setNameInput(e.target.value)}
                                        onKeyDown={e => e.key === 'Enter' && handleSaveName()}
                                        className="flex-1 border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
                                        autoFocus
                                    />
                                    <button
                                        onClick={handleSaveName}
                                        disabled={nameSaving}
                                        className="px-3 py-2 bg-emerald-500 text-white text-sm rounded-lg hover:bg-emerald-600 disabled:opacity-50 transition"
                                    >
                                        {nameSaving ? 'Saving…' : 'Save'}
                                    </button>
                                    <button
                                        onClick={() => setEditingName(false)}
                                        className="px-3 py-2 border border-gray-300 text-gray-600 text-sm rounded-lg hover:bg-gray-50 transition"
                                    >
                                        Cancel
                                    </button>
                                </div>
                            ) : (
                                <div className="flex items-center space-x-3">
                                    <span className="text-gray-800">{userProfile.name}</span>
                                    <button
                                        onClick={handleEditName}
                                        className="text-xs text-emerald-600 hover:text-emerald-700 underline"
                                    >
                                        Edit
                                    </button>
                                </div>
                            )}
                        </div>

                        {/* Email */}
                        <div className="mb-5">
                            <label className="block text-sm font-semibold text-gray-700 mb-1">Email (via Google)</label>
                            <span className="text-gray-800">{userProfile.email}</span>
                        </div>
                    </div>

                    {/* Delete Account */}
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-red-100">
                        <h3 className="text-lg font-bold text-red-700 mb-2">Danger Zone</h3>
                        <p className="text-sm text-gray-600 mb-4">
                            Permanently delete your account and all learning progress. This cannot be undone.
                        </p>
                        <button
                            onClick={() => setShowDeleteConfirm(true)}
                            className="px-4 py-2 bg-red-600 text-white text-sm rounded-lg hover:bg-red-700 transition font-medium"
                        >
                            Delete Account
                        </button>
                    </div>
                </div>
            )}

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
                                <p className="text-gray-600">2.2.2</p>
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
                            <div className="border-l-4 border-blue-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Llama 3 8B Instruct</h4>
                                <p className="text-sm text-gray-600 mb-2"><strong>License:</strong> Meta Llama 3 Community License Agreement</p>
                                <p className="text-sm text-gray-600 mb-2"><strong>Source:</strong> Meta AI</p>
                                <p className="text-sm text-gray-600">
                                    Llama 3 is licensed under Meta's custom license. See the full license at:{' '}
                                    <a href="https://llama.meta.com/llama3/license/" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                                        https://llama.meta.com/llama3/license/
                                    </a>
                                </p>
                            </div>
                            <div className="border-l-4 border-green-500 pl-4">
                                <h4 className="font-semibold text-gray-800 mb-2">Whisper</h4>
                                <p className="text-sm text-gray-600 mb-2"><strong>License:</strong> MIT License</p>
                                <p className="text-sm text-gray-600 mb-2"><strong>Source:</strong> OpenAI</p>
                                <p className="text-sm text-gray-600">Copyright (c) 2022 OpenAI. Licensed under the MIT License.</p>
                            </div>
                        </div>
                    </div>

                    {/* Privacy Policy */}
                    <div className="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
                        <h3 className="text-xl font-bold text-gray-800 mb-4">Privacy Policy</h3>
                        <p className="text-gray-600 mb-4">
                            PolyBot processes audio and text data locally or on secure cloud infrastructure.
                            All user data is handled in accordance with our privacy policy.
                        </p>
                        <button
                            onClick={onPrivacyPolicy}
                            className="px-4 py-2 bg-emerald-500 text-white text-sm rounded-lg hover:bg-emerald-600 transition font-medium"
                        >
                            View Privacy Policy
                        </button>
                        <p className="text-sm text-gray-500 mt-4">
                            For questions about data handling or licensing, contact{' '}
                            <a href="mailto:jeff.itservices@gmail.com" className="text-emerald-600 hover:underline">
                                jeff.itservices@gmail.com
                            </a>
                        </p>
                    </div>
                </div>
            )}

            {/* Delete Confirmation Modal */}
            {showDeleteConfirm && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
                    <div className="bg-white rounded-2xl p-6 max-w-md w-full shadow-xl">
                        <h3 className="text-xl font-bold text-gray-800 mb-3">Are you sure?</h3>
                        <p className="text-gray-600 mb-6">
                            This will permanently delete your account and all learning progress. This cannot be undone.
                        </p>
                        <div className="flex space-x-3">
                            <button
                                onClick={() => setShowDeleteConfirm(false)}
                                disabled={deleting}
                                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition"
                            >
                                Cancel
                            </button>
                            <button
                                onClick={handleDeleteAccount}
                                disabled={deleting}
                                className="flex-1 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 disabled:opacity-50 transition font-medium"
                            >
                                {deleting ? 'Deleting…' : 'Delete'}
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
});

SettingsView.displayName = 'SettingsView';

export default SettingsView;
