/**
 * RegistrationScreen Component
 * User registration with social login and email signup
 */

import React, { useState, useCallback } from 'react';
import { API } from '../../config/constants';

const RegistrationScreen = React.memo(({ userProfile, setUserProfile, handleRegister, errorMessage }) => {
    const [isRegistering, setIsRegistering] = useState(false);

    const handleInputChange = useCallback((e) => {
        const { name, value } = e.target;
        setUserProfile(prev => ({ ...prev, [name]: value }));
    }, [setUserProfile]);

    const submitRegistration = async () => {
        if (!userProfile.name || !userProfile.email) return;
        setIsRegistering(true);
        await handleRegister(true);
        setIsRegistering(false);
    };

    const handleSocialLogin = (provider) => {
        window.location.href = `${API}/api/${provider.toLowerCase()}/login`;
    };

    return (
        <div className="polybot-background min-h-screen flex items-center justify-center p-4">
            <style jsx="true">{` .polybot-background { background: linear-gradient(135deg, #4CAF50 0%, #2196F3 50%, #9C27B0 100%); } `}</style>
            <div className="w-full max-w-md bg-white p-8 rounded-[30px] shadow-2xl transition duration-500">
                <h1 className="text-3xl font-extrabold text-[#388E3C] mb-2">Polybot</h1>
                <p className="text-gray-600 mb-6 font-semibold">Your private AI language tutor. Learn locally, speak globally.</p>

                <div className="space-y-3 mb-6">
                    <button
                        onClick={() => handleSocialLogin('Google')}
                        className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 hover:bg-gray-50"
                    >
                        <img src="https://img.icons8.com/color/16/000000/google-logo.png" alt="Google" className="w-5 h-5" />
                        <span>Continue with Google</span>
                    </button>
                    <button
                        onClick={() => handleSocialLogin('Apple')}
                        className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 bg-black text-white hover:bg-gray-800"
                    >
                        <img src="https://img.icons8.com/ios-filled/16/ffffff/mac-os.png" alt="Apple" className="w-5 h-5" />
                        <span>Continue with Apple</span>
                    </button>
                    <button
                        onClick={() => handleSocialLogin('Facebook')}
                        className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 bg-blue-600 text-white hover:bg-blue-700"
                    >
                        <img src="https://img.icons8.com/ios-filled/16/ffffff/facebook-new.png" alt="Facebook" className="w-5 h-5" />
                        <span>Continue with Facebook</span>
                    </button>
                </div>

                <div className="text-center my-4 text-gray-400 text-sm">— OR SIGN UP WITH EMAIL —</div>

                <div className="space-y-4">
                    <input
                        type="text"
                        name="name"
                        placeholder="Name"
                        value={userProfile.name}
                        onChange={handleInputChange}
                        className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]"
                        required
                    />
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={userProfile.email}
                        onChange={handleInputChange}
                        className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]"
                        required
                    />
                </div>
                {errorMessage && (
                    <p className="mt-4 text-sm text-red-600 font-semibold p-3 bg-red-50 rounded-lg border border-red-200">
                        {errorMessage}
                    </p>
                )}

                <button
                    onClick={submitRegistration}
                    disabled={isRegistering}
                    className="w-full mt-6 p-4 text-lg font-semibold text-white rounded-xl transition duration-300 shadow-md bg-gradient-to-r from-[#4CAF50] to-[#388E3C] hover:from-[#388E3C] hover:to-[#2E7D32] hover:shadow-xl disabled:bg-gray-500"
                >
                    {isRegistering ? '...' : 'Create Account & Start'}
                </button>
            </div>
        </div>
    );
});

RegistrationScreen.displayName = 'RegistrationScreen';

export default RegistrationScreen;
