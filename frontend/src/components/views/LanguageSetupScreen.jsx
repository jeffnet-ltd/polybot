/**
 * LanguageSetupScreen Component
 * Allows user to select native and target languages
 */

import React, { useState } from 'react';
import { ALL_LANGUAGES, CORE_LANGUAGES } from '../../config/constants';
import { updateUserProfile } from '../../services/userService';

const LanguageSetupScreen = ({ userProfile, setUserProfile, onComplete }) => {
    const [isSaving, setIsSaving] = useState(false);

    const handleSave = async () => {
        setIsSaving(true);
        try {
            await updateUserProfile(userProfile.user_id, {
                native_language: userProfile.native_language,
                target_language: userProfile.target_language,
                level: "Beginner"
            });
            onComplete();
        } catch (error) {
            console.error("Failed to save languages", error);
            alert("Error saving preferences. Please try again.");
        } finally {
            setIsSaving(false);
        }
    };

    return (
        <div className="polybot-background min-h-screen flex items-center justify-center p-4">
            <style jsx="true">{` .polybot-background { background: linear-gradient(135deg, #4CAF50 0%, #2196F3 50%, #9C27B0 100%); } `}</style>
            <div className="w-full max-w-md bg-white p-8 rounded-[30px] shadow-xl">
                <h1 className="text-2xl font-bold text-gray-800 mb-2">Welcome, {userProfile.name}!</h1>
                <p className="text-gray-600 mb-6">Let's set up your learning path.</p>
                <div className="space-y-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">I speak:</label>
                        <select
                            value={userProfile.native_language}
                            onChange={(e) => setUserProfile({ ...userProfile, native_language: e.target.value })}
                            className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]"
                        >
                            {ALL_LANGUAGES.map(lang => (
                                <option
                                    key={lang.code}
                                    value={lang.code}
                                    disabled={lang.code === userProfile.target_language}
                                >
                                    {lang.name}
                                </option>
                            ))}
                        </select>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">I want to learn:</label>
                        <select
                            value={userProfile.target_language}
                            onChange={(e) => setUserProfile({ ...userProfile, target_language: e.target.value })}
                            className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]"
                        >
                            {CORE_LANGUAGES.map(lang => (
                                <option
                                    key={lang.code}
                                    value={lang.code}
                                    disabled={lang.code === userProfile.native_language}
                                >
                                    {lang.name}
                                </option>
                            ))}
                        </select>
                    </div>
                </div>
                <button
                    onClick={handleSave}
                    disabled={isSaving}
                    className="w-full mt-8 p-4 text-lg font-semibold text-white rounded-xl bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 shadow-lg transition transform hover:scale-[1.02]"
                >
                    {isSaving ? "Saving..." : "Start Learning"}
                </button>
            </div>
        </div>
    );
};

export default LanguageSetupScreen;
