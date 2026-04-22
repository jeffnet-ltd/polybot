/**
 * RegistrationScreen Component
 * User registration with social login and email signup
 */

import React from 'react';
import { API } from '../../config/constants';

const RegistrationScreen = React.memo(() => {
    return (
        <div className="min-h-screen flex items-center justify-center p-4 bg-white">
            <div className="w-full max-w-md bg-white p-8 rounded-[30px] shadow-2xl transition duration-500">
                <h1 className="text-3xl font-extrabold text-[#388E3C] mb-2">Polybot</h1>
                <p className="text-gray-600 mb-6 font-semibold">Your private AI language tutor. Learn locally, speak globally.</p>

                <button
                    onClick={() => { window.location.href = `${API}/api/google/login`; }}
                    className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 hover:bg-gray-50"
                >
                    <img src="https://img.icons8.com/color/16/000000/google-logo.png" alt="Google" className="w-5 h-5" />
                    <span>Continue with Google</span>
                </button>
            </div>
        </div>
    );
});

RegistrationScreen.displayName = 'RegistrationScreen';

export default RegistrationScreen;
