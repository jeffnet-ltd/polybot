/**
 * SidebarMenu Component
 * Navigation sidebar for main app
 */

import React, { useCallback } from 'react';
import { Menu, MessageSquare, GraduationCap, Trophy, BookOpen, Settings, User, X } from 'lucide-react';
import { ALL_LANGUAGES } from '../../config/constants';
import FlagIcon from './FlagIcon';

const SidebarMenu = React.memo(({ isSidebarOpen, setIsSidebarOpen, setMainContentView, setView, userProfile, t }) => {
    const handleNavigation = (content) => {
        setMainContentView(content);
        setIsSidebarOpen(false);
    };

    // Helper to get flag from code
    const getLang = (code) => ALL_LANGUAGES.find(l => l.code === code) || ALL_LANGUAGES[0];

    return (
        <div className={`fixed inset-y-0 left-0 z-50 transform transition-transform duration-300 ease-in-out ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'} w-64 bg-white shadow-2xl md:static md:translate-x-0 md:shadow-none md:w-auto`}>
            <div className="p-4 md:hidden flex justify-between items-center border-b">
                <h3 className="text-xl font-bold text-gray-800">{t('menu')}</h3>
                <button onClick={() => setIsSidebarOpen(false)} className="text-gray-500 hover:text-gray-900">
                    <X size={24} />
                </button>
            </div>
            <nav className="p-4 space-y-2">
                {/* PROFILE SECTION WITH FLAGS */}
                <div className="p-3 bg-gray-50 rounded-xl border border-gray-100 mb-4">
                    <p className="text-sm font-bold text-gray-800">{userProfile.name}</p>
                    <div className="flex items-center text-xs text-gray-500 mt-2 space-x-2">
                        <div className="flex items-center space-x-1 bg-white px-2 py-1 rounded border">
                            <FlagIcon countryCode={getLang(userProfile.target_language).country} />
                            <span>{getLang(userProfile.target_language).code.toUpperCase()}</span>
                        </div>
                        <span>from</span>
                        <div className="flex items-center space-x-1 bg-white px-2 py-1 rounded border">
                            <FlagIcon countryCode={getLang(userProfile.native_language).country} />
                            <span>{getLang(userProfile.native_language).code.toUpperCase()}</span>
                        </div>
                    </div>
                </div>

                <button
                    onClick={() => handleNavigation('curriculum')}
                    className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"
                >
                    <GraduationCap size={20} />
                    <span className="font-medium">{t('lessons')}</span>
                </button>

                <button
                    onClick={() => handleNavigation('scenario_selection')}
                    className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"
                >
                    <MessageSquare size={20} />
                    <span className="font-medium">{t('practice')} Scenarios</span>
                </button>

                <button
                    onClick={() => handleNavigation('progress')}
                    className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"
                >
                    <Trophy size={20} />
                    <span className="font-medium">{t('progress')}</span>
                </button>

                <button
                    onClick={() => handleNavigation('vocabulary')}
                    className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"
                >
                    <BookOpen size={20} />
                    <span className="font-medium">{t('vocab')}</span>
                </button>

                <button
                    onClick={() => handleNavigation('settings')}
                    className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"
                >
                    <Settings size={20} />
                    <span className="font-medium">Settings</span>
                </button>

                <div className="p-4 border-t mt-auto">
                    <button
                        onClick={() => setView('register')}
                        className="flex items-center space-x-2 text-sm text-red-500 hover:text-red-700 transition"
                    >
                        <User size={18} />
                        <span>{t('profile')}</span>
                    </button>
                </div>
            </nav>
        </div>
    );
});

SidebarMenu.displayName = 'SidebarMenu';

export default SidebarMenu;
