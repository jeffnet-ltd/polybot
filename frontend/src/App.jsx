import React, { useState, useCallback, useEffect, useMemo, useRef } from 'react';
import axios from 'axios';
import { Menu, MessageSquare, GraduationCap, Zap, BookOpen, Trophy, Send, X, User, Loader2, Lock, ChevronRight, CheckCircle, AlertCircle, ArrowLeft, Volume2, RefreshCcw, CheckSquare, Target, ChevronDown, Mic } from 'lucide-react';

// --- Global Constants ---
const API = process.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

// Updated with 'country' code for FlagCDN
const ALL_LANGUAGES = [
    { code: 'en', name: 'English', country: 'gb' }, 
    { code: 'fr', name: 'French', country: 'fr' }, 
    { code: 'es', name: 'Spanish', country: 'es' },
    { code: 'it', name: 'Italian', country: 'it' }, 
    { code: 'pt', name: 'Portuguese', country: 'pt' }, 
    { code: 'tw', name: 'Twi', country: 'gh' }, 
    { code: 'de', name: 'German', country: 'de' }, 
    { code: 'ar', name: 'Arabic', country: 'sa' }, 
    { code: 'zh', name: 'Mandarin', country: 'cn' },
    { code: 'ja', name: 'Japanese', country: 'jp' }, 
    { code: 'ru', name: 'Russian', country: 'ru' }, 
    { code: 'ko', name: 'Korean', country: 'kr' },
];

const CORE_LANGUAGES = [
    { code: 'en', name: 'English', country: 'gb' }, 
    { code: 'fr', name: 'French', country: 'fr' }, 
    { code: 'es', name: 'Spanish', country: 'es' },
    { code: 'it', name: 'Italian', country: 'it' }, 
    { code: 'pt', name: 'Portuguese', country: 'pt' }, 
    { code: 'tw', name: 'Twi', country: 'gh' }, 
];

const LEVELS = []; 

const UI_STRINGS = {
    en: { menu: "Menu", lessons: "Lessons", practice: "Practice", progress: "Progress", vocab: "Vocabulary", start: "Start Learning", profile: "Change Profile", overview: "Overview", exercises: "Exercises" },
};

const getT = (langCode) => (key) => UI_STRINGS['en'][key] || key; 

const uuidv4 = () => {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
};

// Audio unlock mechanism for autoplay
let audioUnlocked = false;
const unlockAudio = () => {
    if (!audioUnlocked) {
        // Create a dummy audio context and resume it to unlock autoplay
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        if (audioContext.state === 'suspended') {
            audioContext.resume();
        }
        audioUnlocked = true;
        console.log("[Audio] Audio unlocked for autoplay");
    }
};

// Unlock audio on first user interaction
if (typeof window !== 'undefined') {
    const unlockOnInteraction = () => {
        unlockAudio();
        document.removeEventListener('click', unlockOnInteraction);
        document.removeEventListener('touchstart', unlockOnInteraction);
    };
    document.addEventListener('click', unlockOnInteraction, { once: true });
    document.addEventListener('touchstart', unlockOnInteraction, { once: true });
}

// Backend-powered TTS using Edge-TTS (Microsoft)
const speakText = async (text, langCode) => {
    if (!text) return;
    try {
        // Unlock audio if not already unlocked
        unlockAudio();
        
        console.log(`[TTS] Requesting audio for: "${text}" in language: ${langCode}`);
        console.log(`[TTS] API URL: ${API}/api/v1/voice/synthesize`);
        
        // First check if backend is reachable
        try {
            const healthCheck = await fetch(`${API}/health`);
            console.log(`[TTS] Backend health check: ${healthCheck.status}`);
        } catch (healthErr) {
            console.error("[TTS] Backend health check failed:", healthErr);
            alert(`Cannot reach backend at ${API}. Is the backend running?`);
            return;
        }
        
        const response = await fetch(`${API}/api/v1/voice/synthesize`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text, language: langCode }),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error("[TTS] Request failed:", response.status, errorText);
            alert(`TTS Error: ${response.status} - ${errorText}`);
            return;
        }

        const blob = await response.blob();
        console.log(`[TTS] Received audio blob, size: ${blob.size} bytes, type: ${blob.type}`);
        
        if (blob.size === 0) {
            console.error("[TTS] Received empty audio blob");
            alert("TTS Error: Received empty audio");
            return;
        }

        // Create audio element and play
        const url = URL.createObjectURL(blob);
        const audio = new Audio(url);
        
        // Set up event handlers
        const cleanup = () => {
            URL.revokeObjectURL(url);
        };
        
        audio.onerror = (e) => {
            console.error("[TTS] Audio playback error:", e, audio.error);
            cleanup();
        };
        
        audio.onended = () => {
            console.log("[TTS] Audio playback completed");
            cleanup();
        };
        
        // Improved playback logic
        const playAudio = async () => {
            try {
                // Set volume and ensure audio is ready
                audio.volume = 1.0;
                
                // Try to play immediately
                const playPromise = audio.play();
                
                if (playPromise !== undefined) {
                    await playPromise;
                    console.log("[TTS] Audio playback started successfully");
                }
            } catch (playError) {
                console.log("[TTS] Initial play blocked:", playError.name);
                
                // Wait for audio to be ready
                const waitForReady = () => {
                    return new Promise((resolve, reject) => {
                        if (audio.readyState >= 2) { // HAVE_CURRENT_DATA
                            resolve();
                        } else {
                            audio.oncanplaythrough = () => resolve();
                            audio.onerror = () => reject(new Error("Audio load failed"));
                            // Timeout after 5 seconds
                            setTimeout(() => reject(new Error("Audio load timeout")), 5000);
                        }
                    });
                };
                
                try {
                    await waitForReady();
                    console.log("[TTS] Audio ready, attempting playback");
                    await audio.play();
                    console.log("[TTS] Audio playback started after waiting");
                } catch (playError2) {
                    console.error("[TTS] Play failed:", playError2);
                    // If still blocked, set up click handler
                    const playOnClick = () => {
                        audio.play().catch(e => console.error("[TTS] Retry play failed:", e));
                        document.removeEventListener('click', playOnClick);
                        document.removeEventListener('touchstart', playOnClick);
                    };
                    document.addEventListener('click', playOnClick, { once: true });
                    document.addEventListener('touchstart', playOnClick, { once: true });
                }
            }
        };
        
        // Load and attempt to play
        audio.load();
        playAudio();
        
    } catch (err) {
        console.error("[TTS] Error in speakText:", err);
        // More detailed error message
        if (err.name === 'TypeError' && err.message.includes('fetch')) {
            alert(`TTS Error: Cannot connect to backend at ${API}. Please check:\n1. Backend is running\n2. Backend URL is correct\n3. No firewall blocking the connection`);
        } else {
            alert(`TTS Error: ${err.message}`);
        }
    }
};

// --- UTILITY FUNCTION FOR PARSING CORRECTION ---
const parseCorrectionData = (data) => {
    if (!data || data === "NO_ERROR" || !data.includes("CORRECTED:")) return null;
    
    const correctedMatch = data.match(/CORRECTED:\s*([^E]+)/); 
    const explanationMatch = data.match(/EXPLANATION:\s*([^\n]+)/); 
    
    if (correctedMatch && explanationMatch) {
        return {
            corrected: correctedMatch[1].trim().replace(/\[|\]/g, ''),
            explanation: explanationMatch[1].trim().replace(/\[|\]/g, '')
        };
    }
    if (data.length > 100 || data.includes("ERROR")) return { corrected: "Formatting Error", explanation: "AI output corrupted. Check backend logs." }
    return null; 
};

// --- HELPER: Render Flag Image ---
const FlagIcon = ({ countryCode, className = "w-5 h-4" }) => (
    <img 
        src={`https://flagcdn.com/${countryCode}.svg`} 
        alt={countryCode} 
        className={`object-cover rounded-sm border border-gray-200 ${className}`} 
    />
);

// --- NEW COMPONENT: Language Switcher Dropdown ---
const LanguageSwitcher = ({ currentLang, nativeLang, onSwitch }) => {
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef(null);

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const currentLangObj = CORE_LANGUAGES.find(l => l.code === currentLang) || CORE_LANGUAGES[0];

    return (
        <div className="relative" ref={dropdownRef}>
            <button 
                onClick={() => setIsOpen(!isOpen)} 
                className="flex items-center space-x-2 bg-white hover:bg-gray-50 px-3 py-2 rounded-full transition duration-200 border border-gray-200 shadow-sm"
            >
                <FlagIcon countryCode={currentLangObj.country} className="w-6 h-4" />
                <span className="font-semibold text-sm text-gray-700 hidden sm:inline">{currentLangObj.name}</span>
                <ChevronDown size={16} className={`text-gray-500 transition-transform ${isOpen ? 'rotate-180' : ''}`} />
            </button>

            {isOpen && (
                <div className="absolute right-0 mt-2 w-56 bg-white rounded-xl shadow-xl border border-gray-100 overflow-hidden z-50 animate-fade-in">
                    <div className="max-h-80 overflow-y-auto py-1">
                        {CORE_LANGUAGES.map((lang) => {
                            const isNative = lang.code === nativeLang;
                            return (
                                <button
                                    key={lang.code}
                                    disabled={isNative}
                                    onClick={() => {
                                        if (!isNative) {
                                            onSwitch(lang.code);
                                            setIsOpen(false);
                                        }
                                    }}
                                    className={`w-full text-left px-4 py-3 flex items-center space-x-3 transition ${currentLang === lang.code ? 'bg-blue-50' : 'hover:bg-gray-50'} ${isNative ? 'opacity-50 cursor-not-allowed bg-gray-50' : ''}`}
                                >
                                    <FlagIcon countryCode={lang.country} className="w-6 h-4" />
                                    <span className={`text-sm font-medium ${currentLang === lang.code ? 'text-blue-600' : 'text-gray-700'}`}>
                                        {lang.name} {isNative && "(Native)"}
                                    </span>
                                    {currentLang === lang.code && <CheckCircle size={16} className="ml-auto text-blue-500" />}
                                </button>
                            );
                        })}
                    </div>
                </div>
            )}
        </div>
    );
};

// --- Sub-Components ---

const ProgressCard = ({ icon: Icon, title, value, color }) => (
    <div className="flex items-center justify-between p-3 bg-white rounded-xl shadow-lg border border-gray-100 transition duration-300 hover:shadow-xl">
        <div className={`p-2 rounded-full text-white ${color}`}><Icon size={20} /></div>
        <div className="text-right"><p className="text-xs text-gray-500 font-medium">{title}</p><p className="text-2xl font-bold text-gray-800">{value}</p></div>
    </div>
);

const SidebarMenu = React.memo(({ isSidebarOpen, setIsSidebarOpen, setMainContentView, setView, userProfile, t }) => {
    const handleNavigation = (content) => { setMainContentView(content); setIsSidebarOpen(false); };
    
    // Helper to get flag from code
    const getLang = (code) => ALL_LANGUAGES.find(l => l.code === code) || ALL_LANGUAGES[0];

    return (
        <div className={`fixed inset-y-0 right-0 z-50 transform transition-transform duration-300 ease-in-out ${isSidebarOpen ? 'translate-x-0' : 'translate-x-full'} w-64 bg-white shadow-2xl md:static md:translate-x-0 md:shadow-none md:w-auto`}>
            <div className="p-4 md:hidden flex justify-between items-center border-b"><h3 className="text-xl font-bold text-gray-800">{t('menu')}</h3><button onClick={() => setIsSidebarOpen(false)} className="text-gray-500 hover:text-gray-900"><X size={24} /></button></div>
            <nav className="p-4 space-y-2">
                {/* UPDATED PROFILE SECTION WITH FLAGS */}
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
                
                <button onClick={() => handleNavigation('curriculum')} className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"><GraduationCap size={20} /><span className="font-medium">{t('lessons')}</span></button>
                <button onClick={() => handleNavigation('tutor')} className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"><MessageSquare size={20} /><span className="font-medium">{t('practice')} (AI)</span></button>
                <button onClick={() => handleNavigation('progress')} className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"><Trophy size={20} /><span className="font-medium">{t('progress')}</span></button>
                <button onClick={() => handleNavigation('vocabulary')} className="flex items-center space-x-3 w-full p-3 rounded-lg text-gray-700 hover:bg-gray-100 transition"><BookOpen size={20} /><span className="font-medium">{t('vocab')}</span></button>
                <div className="p-4 border-t mt-auto"><button onClick={() => setView('register')} className="flex items-center space-x-2 text-sm text-red-500 hover:text-red-700 transition"><User size={18} /><span>{t('profile')}</span></button></div>
            </nav>
        </div>
    );
});

// --- ONBOARDING & LOGIN SCREENS ---

const LanguageSetupScreen = ({ userProfile, setUserProfile, onComplete }) => {
    const [isSaving, setIsSaving] = useState(false);
    
    const handleSave = async () => {
        setIsSaving(true);
        try {
            await axios.patch(`${API}/user/${userProfile.user_id}`, {
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
                        <select value={userProfile.native_language} onChange={(e) => setUserProfile({...userProfile, native_language: e.target.value})} className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]">
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
                        <select value={userProfile.target_language} onChange={(e) => setUserProfile({...userProfile, target_language: e.target.value})} className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]">
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
                <button onClick={handleSave} disabled={isSaving} className="w-full mt-8 p-4 text-lg font-semibold text-white rounded-xl bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 shadow-lg transition transform hover:scale-[1.02]">
                    {isSaving ? "Saving..." : "Start Learning"}
                </button>
            </div>
        </div>
    );
};

const RegistrationScreen = React.memo(({ userProfile, setUserProfile, handleRegister, errorMessage }) => {
    const [isRegistering, setIsRegistering] = useState(false);
    const handleInputChange = useCallback((e) => { const { name, value } = e.target; setUserProfile(prev => ({ ...prev, [name]: value })); }, [setUserProfile]);
    
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
                    <button onClick={() => handleSocialLogin('Google')} className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 hover:bg-gray-50">
                        <img src="https://img.icons8.com/color/16/000000/google-logo.png" alt="Google" className="w-5 h-5"/><span>Continue with Google</span>
                    </button>
                    <button onClick={() => handleSocialLogin('Apple')} className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 bg-black text-white hover:bg-gray-800">
                        <img src="https://img.icons8.com/ios-filled/16/ffffff/mac-os.png" alt="Apple" className="w-5 h-5"/><span>Continue with Apple</span>
                    </button>
                    <button onClick={() => handleSocialLogin('Facebook')} className="w-full p-3 border border-gray-300 rounded-xl font-semibold flex items-center justify-center space-x-3 transition duration-150 bg-blue-600 text-white hover:bg-blue-700">
                        <img src="https://img.icons8.com/ios-filled/16/ffffff/facebook-new.png" alt="Facebook" className="w-5 h-5"/><span>Continue with Facebook</span>
                    </button>
                </div>

                <div className="text-center my-4 text-gray-400 text-sm">— OR SIGN UP WITH EMAIL —</div>

                <div className="space-y-4">
                    <input type="text" name="name" placeholder="Name" value={userProfile.name} onChange={handleInputChange} className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]" required />
                    <input type="email" name="email" placeholder="Email" value={userProfile.email} onChange={handleInputChange} className="w-full p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50]" required />
                </div>
                {errorMessage && <p className="mt-4 text-sm text-red-600 font-semibold p-3 bg-red-50 rounded-lg border border-red-200">{errorMessage}</p>}
                
                <button onClick={submitRegistration} disabled={isRegistering} className="w-full mt-6 p-4 text-lg font-semibold text-white rounded-xl transition duration-300 shadow-md bg-gradient-to-r from-[#4CAF50] to-[#388E3C] hover:from-[#388E3C] hover:to-[#2E7D32] hover:shadow-xl disabled:bg-gray-500">
                    {isRegistering ? '...' : 'Create Account & Start'}
                </button>
            </div>
        </div>
    );
});

// --- CORE VIEWS ---

const ProgressView = React.memo(({ userProfile }) => (
    <div className="p-4 space-y-6">
        <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">Your Progress</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <ProgressCard icon={Zap} title="XP Points" value={userProfile.xp} color="bg-yellow-500" />
            <ProgressCard icon={BookOpen} title="Words" value={userProfile.words_learned} color="bg-green-500" />
            <ProgressCard icon={Trophy} title="Streak" value={userProfile.streak} color="bg-red-500" />
        </div>
    </div>
));

const VocabularyView = React.memo(({ userProfile, targetLang }) => {
    const filteredVocab = userProfile.vocabulary_list.filter(word => 
        word.target_lang === targetLang
    );

    return (
        <div className="p-4 space-y-6">
            <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">My Vocabulary</h2>
            {!filteredVocab || filteredVocab.length === 0 ? (
                <div className="bg-white p-6 rounded-2xl shadow-xl border border-gray-100 min-h-64 flex items-center justify-center">
                    <p className="text-gray-500 text-lg">Complete lessons to build your vocabulary!</p>
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {filteredVocab.map((word, idx) => (
                        // NEW: Render Section Header if present
                        word.is_header ? (
                            <div key={idx} className="col-span-full mt-4 mb-2">
                                <h3 className="text-lg font-bold text-gray-700 border-b pb-1">{word.term.replace(/---/g, '').trim()}</h3>
                            </div>
                        ) : (
                            <div key={idx} className="bg-white p-4 rounded-xl border border-gray-200 shadow-sm flex justify-between items-center">
                                <div>
                                    <p className="text-xl font-bold text-gray-800">{word.term}</p>
                                    <p className="text-sm text-gray-500">{word.translation}</p>
                                    <div className="mt-2 w-32 h-2 bg-gray-100 rounded-full overflow-hidden">
                                        <div className="h-full bg-green-500" style={{ width: `${word.proficiency}%` }}></div>
                                    </div>
                                    <p className="text-xs text-green-600 mt-1">{Math.round(word.proficiency)}% Proficiency</p>
                                </div>
                                <button onClick={() => speakText(word.term, targetLang)} className="p-2 text-gray-400 hover:text-blue-500 hover:bg-blue-50 rounded-full transition"><Volume2 size={20} /></button>
                            </div>
                        )
                    ))}
                </div>
            )}
        </div>
    );
});

// --- Exercises ---

// Reusable component for accented letter chips (Italian)
const AccentedLetterChips = ({ inputRef, value, setValue, disabled }) => {
    const lowercaseLetters = ['à', 'è', 'é', 'ì', 'ò', 'ù'];
    const uppercaseLetters = ['À', 'È', 'É', 'Ì', 'Ò', 'Ù'];
    
    const handleInsert = (letter) => {
        if (disabled || !inputRef?.current) return;
        
        const input = inputRef.current;
        const start = input.selectionStart || 0;
        const end = input.selectionEnd || 0;
        const newValue = (value || '').substring(0, start) + letter + (value || '').substring(end);
        
        if (setValue) {
            setValue(newValue);
        } else {
            // Fallback: directly update the input value
            input.value = newValue;
            input.dispatchEvent(new Event('input', { bubbles: true }));
        }
        
        // Set cursor position after inserted letter
        setTimeout(() => {
            input.focus();
            input.setSelectionRange(start + 1, start + 1);
        }, 0);
    };
    
    return (
        <div className="space-y-2">
            <p className="text-xs text-gray-500 w-full mb-1">Click to insert accented letters:</p>
            {/* Lowercase letters row */}
            <div className="flex flex-wrap gap-2">
                {lowercaseLetters.map((letter) => (
                    <button
                        key={letter}
                        type="button"
                        onClick={() => handleInsert(letter)}
                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-lg text-lg font-medium text-gray-700 transition hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={disabled}
                    >
                        {letter}
                    </button>
                ))}
            </div>
            {/* Uppercase letters row */}
            <div className="flex flex-wrap gap-2">
                {uppercaseLetters.map((letter) => (
                    <button
                        key={letter}
                        type="button"
                        onClick={() => handleInsert(letter)}
                        className="px-3 py-2 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-lg text-lg font-medium text-gray-700 transition hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed"
                        disabled={disabled}
                    >
                        {letter}
                    </button>
                ))}
            </div>
        </div>
    );
};

const ConversationExercise = ({ dialogue, options, onAnswer }) => {
    const [userAnswers, setUserAnswers] = useState({}); 
    const [availableWords, setAvailableWords] = useState(options);
    const [isChecked, setIsChecked] = useState(false);

    useEffect(() => {
        setUserAnswers({});
        setAvailableWords(options);
        setIsChecked(false);
    }, [dialogue, options]);

    const handleWordClick = (word) => {
        if (isChecked) return;
        const emptyIndex = dialogue.findIndex((line, idx) => line.missing_word && !userAnswers[idx]);
        
        if (emptyIndex !== -1) {
            setUserAnswers(prev => ({ ...prev, [emptyIndex]: word }));
            setAvailableWords(prev => {
                const idx = prev.indexOf(word);
                if (idx > -1) {
                    const newArr = [...prev];
                    newArr.splice(idx, 1);
                    return newArr;
                }
                return prev;
            });
        }
    };

    const handleSlotClick = (idx, word) => {
        if (isChecked || !word) return;
        setUserAnswers(prev => {
            const next = { ...prev };
            delete next[idx];
            return next;
        });
        setAvailableWords(prev => [...prev, word]);
    };

    const checkAnswers = () => {
        setIsChecked(true);
        const allCorrect = dialogue.every((line, idx) => {
            if (!line.missing_word) return true; 
            return userAnswers[idx] === line.missing_word;
        });
        onAnswer(allCorrect ? 'correct' : 'incorrect', allCorrect ? "Conversation completed!" : "Some words are wrong.");
    };

    const isFull = dialogue.filter(l => l.missing_word).length === Object.keys(userAnswers).length;

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-bold text-gray-800 text-center">Complete the Conversation</h3>
            <div className="space-y-4 max-h-96 overflow-y-auto p-2">
                {dialogue.map((line, idx) => {
                    const isMe = line.speaker === 'B'; 
                    const parts = line.text.split('___');
                    const hasGap = line.missing_word;
                    const userAnswer = userAnswers[idx];
                    
                    let gapStyle = "inline-block w-24 border-b-2 border-dashed border-gray-400 text-center mx-1 cursor-pointer text-blue-600 font-bold";
                    if (isChecked) {
                        if (userAnswer === line.missing_word) gapStyle = "inline-block px-2 py-1 rounded bg-green-100 text-green-700 font-bold border border-green-300";
                        else gapStyle = "inline-block px-2 py-1 rounded bg-red-100 text-red-700 font-bold border border-red-300";
                    }

                    return (
                        <div key={idx} className={`flex ${isMe ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-[85%] p-4 rounded-2xl ${isMe ? 'bg-blue-50 border-blue-100 rounded-br-none' : 'bg-gray-100 border-gray-200 rounded-tl-none'} border shadow-sm`}>
                                <p className="text-gray-800">
                                    {parts[0]}
                                    {hasGap && (
                                        <span className={gapStyle} onClick={() => handleSlotClick(idx, userAnswer)}>
                                            {userAnswer || (isChecked ? line.missing_word : "___")}
                                        </span>
                                    )}
                                    {parts[1]}
                                </p>
                                <p className="text-xs text-gray-400 mt-1">{line.translation}</p>
                            </div>
                        </div>
                    );
                })}
            </div>
            <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                <p className="text-xs text-gray-500 mb-2 text-center uppercase font-bold tracking-wider">Word Bank</p>
                <div className="flex flex-wrap gap-2 justify-center min-h-[50px]">
                    {availableWords.map((word, i) => (
                        <button key={i} onClick={() => handleWordClick(word)} disabled={isChecked} className="px-3 py-2 bg-white border border-gray-300 rounded-lg shadow-sm text-gray-800 font-semibold hover:bg-blue-50 hover:border-blue-300 transition disabled:opacity-70 disabled:text-gray-800">{word || ''}</button>
                    ))}
                </div>
            </div>
            <button onClick={checkAnswers} disabled={!isFull || isChecked} className={`w-full py-4 rounded-2xl font-bold text-white shadow-lg transition ${isFull && !isChecked ? 'bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 transform hover:scale-[1.02]' : 'bg-gray-300 cursor-not-allowed'}`}>Check Answers</button>
        </div>
    );
};

const ArrangeExercise = ({ prompt, options, correctAnswer, onAnswer }) => {
    const [currentOrder, setCurrentOrder] = useState([]);
    const [availableOptions, setAvailableOptions] = useState(options);
    const [isLocked, setIsLocked] = useState(false); 

    const handleSelect = (word) => { 
        if (isLocked) return; 
        setCurrentOrder([...currentOrder, word]); 
        setAvailableOptions(availableOptions.filter(w => w !== word)); 
    };
    
    const handleReset = () => { 
        if (isLocked) return; 
        setCurrentOrder([]); 
        setAvailableOptions(options); 
    };

    const checkAnswer = () => { 
        const attempt = currentOrder.join(" "); 
        onAnswer(attempt === correctAnswer ? 'correct' : 'incorrect', attempt); 
        setIsLocked(true); 
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-gray-50 p-4 rounded-xl min-h-[60px] flex flex-wrap gap-2 border-2 border-dashed border-gray-300 items-center justify-center">
                {currentOrder.map((word, idx) => 
                    <span key={idx} className="px-3 py-2 bg-blue-100 text-blue-700 rounded-lg font-bold shadow-sm">{word}</span>
                )}
            </div>
            <div className="flex flex-wrap gap-2 justify-center">
                {availableOptions.map((word, idx) => 
                    <button 
                        key={idx} 
                        onClick={() => handleSelect(word)} 
                        disabled={isLocked}
                        className={`px-4 py-2 bg-white border border-gray-300 text-gray-800 rounded-xl shadow-sm hover:bg-gray-50 font-medium transition ${isLocked ? 'opacity-70 cursor-not-allowed text-gray-800' : ''}`}
                    >
                        {word || ''}
                    </button>
                )}
            </div>
            <div className="flex gap-3">
                <button onClick={handleReset} disabled={isLocked} className="p-3 text-gray-500 hover:bg-gray-100 rounded-xl transition disabled:opacity-50"><RefreshCcw size={20} /></button>
                <button 
                    onClick={checkAnswer} 
                    disabled={isLocked}
                    className="flex-grow py-3 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white rounded-xl font-bold shadow-md transition transform hover:scale-[1.02] disabled:bg-gray-500"
                >
                    Check
                </button>
            </div>
        </div>
    );
};

const GenderCategorizeExercise = ({ prompt, words, correctAnswers, onAnswer }) => {
    const [maschileWords, setMaschileWords] = useState([]);
    const [femminileWords, setFemminileWords] = useState([]);
    const [availableWords, setAvailableWords] = useState([...words]);
    const [isLocked, setIsLocked] = useState(false);
    const [draggedItem, setDraggedItem] = useState(null);

    // Reset all state when words change (new exercise)
    useEffect(() => {
        setMaschileWords([]);
        setFemminileWords([]);
        setIsLocked(false);
        setDraggedItem(null);
        const shuffled = [...words].sort(() => Math.random() - 0.5);
        setAvailableWords(shuffled);
    }, [words]);

    const handleDragStart = (e, word, source) => {
        setDraggedItem({ word, source });
        e.dataTransfer.effectAllowed = 'move';
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    };

    const handleDrop = (e, targetColumn) => {
        e.preventDefault();
        if (!draggedItem || isLocked) return;

        const { word, source } = draggedItem;

        // Remove from source
        if (source === 'available') {
            setAvailableWords(prev => prev.filter(w => w !== word));
        } else if (source === 'maschile') {
            setMaschileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'femminile') {
            setFemminileWords(prev => prev.filter(w => w !== word));
        }

        // Add to target
        if (targetColumn === 'maschile') {
            setMaschileWords(prev => [...prev, word]);
        } else if (targetColumn === 'femminile') {
            setFemminileWords(prev => [...prev, word]);
        } else if (targetColumn === 'available') {
            setAvailableWords(prev => [...prev, word]);
        }

        setDraggedItem(null);
    };

    const handleClick = (word, source) => {
        if (isLocked) return;
        
        // Remove from source
        if (source === 'available') {
            setAvailableWords(prev => prev.filter(w => w !== word));
        } else if (source === 'maschile') {
            setMaschileWords(prev => prev.filter(w => w !== word));
        } else if (source === 'femminile') {
            setFemminileWords(prev => prev.filter(w => w !== word));
        }

        // Toggle between columns or return to available
        // For simplicity, clicking moves it back to available
        setAvailableWords(prev => [...prev, word]);
    };

    const handleReset = () => {
        if (isLocked) return;
        setMaschileWords([]);
        setFemminileWords([]);
        const shuffled = [...words].sort(() => Math.random() - 0.5);
        setAvailableWords(shuffled);
    };

    const checkAnswer = () => {
        let allCorrect = true;
        const mistakes = [];

        // Check all words are placed
        if (maschileWords.length + femminileWords.length !== words.length) {
            allCorrect = false;
        }

        // Check maschile words
        maschileWords.forEach(word => {
            if (correctAnswers[word] !== 'maschile') {
                allCorrect = false;
                mistakes.push(`${word} should be ${correctAnswers[word] === 'femminile' ? 'Femminile' : 'Maschile'}`);
            }
        });

        // Check femminile words
        femminileWords.forEach(word => {
            if (correctAnswers[word] !== 'femminile') {
                allCorrect = false;
                mistakes.push(`${word} should be ${correctAnswers[word] === 'maschile' ? 'Maschile' : 'Femminile'}`);
            }
        });

        // Check all words are placed
        availableWords.forEach(word => {
            allCorrect = false;
            mistakes.push(`${word} needs to be placed in a column`);
        });

        onAnswer(allCorrect ? 'correct' : 'incorrect', { maschile: maschileWords, femminile: femminileWords });
        setIsLocked(true);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            
            {/* Two columns layout */}
            <div className="grid grid-cols-2 gap-4">
                {/* Maschile Column */}
                <div
                    onDragOver={handleDragOver}
                    onDrop={(e) => handleDrop(e, 'maschile')}
                    className="bg-blue-50 p-6 rounded-xl min-h-[300px] border-2 border-dashed border-blue-400 transition hover:border-blue-500"
                >
                    <h4 className="text-lg font-bold text-blue-700 mb-4 text-center">Maschile</h4>
                    <div className="flex flex-col gap-2 min-h-[200px]">
                        {maschileWords.length === 0 ? (
                            <p className="text-gray-400 text-sm text-center mt-8">Drag words here</p>
                        ) : (
                            maschileWords.map((word, idx) => (
                                <span
                                    key={idx}
                                    draggable={!isLocked}
                                    onDragStart={(e) => handleDragStart(e, word, 'maschile')}
                                    onClick={() => handleClick(word, 'maschile')}
                                    className="px-4 py-3 bg-blue-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-blue-600 transition text-center"
                                >
                                    {word}
                                </span>
                            ))
                        )}
                    </div>
                </div>

                {/* Femminile Column */}
                <div
                    onDragOver={handleDragOver}
                    onDrop={(e) => handleDrop(e, 'femminile')}
                    className="bg-pink-50 p-6 rounded-xl min-h-[300px] border-2 border-dashed border-pink-400 transition hover:border-pink-500"
                >
                    <h4 className="text-lg font-bold text-pink-700 mb-4 text-center">Femminile</h4>
                    <div className="flex flex-col gap-2 min-h-[200px]">
                        {femminileWords.length === 0 ? (
                            <p className="text-gray-400 text-sm text-center mt-8">Drag words here</p>
                        ) : (
                            femminileWords.map((word, idx) => (
                                <span
                                    key={idx}
                                    draggable={!isLocked}
                                    onDragStart={(e) => handleDragStart(e, word, 'femminile')}
                                    onClick={() => handleClick(word, 'femminile')}
                                    className="px-4 py-3 bg-pink-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-pink-600 transition text-center"
                                >
                                    {word}
                                </span>
                            ))
                        )}
                    </div>
                </div>
            </div>

            {/* Available words in center */}
            {availableWords.length > 0 && (
                <div className="space-y-2">
                    <p className="text-sm text-gray-500 font-medium text-center">Drag words to the correct column:</p>
                    <div className="flex flex-wrap gap-2 justify-center">
                        {availableWords.map((word, idx) => (
                            <span
                                key={idx}
                                draggable={!isLocked}
                                onDragStart={(e) => handleDragStart(e, word, 'available')}
                                onClick={() => handleClick(word, 'available')}
                                className="px-4 py-2 bg-white border-2 border-gray-300 text-gray-800 rounded-lg font-medium shadow-sm cursor-move hover:bg-gray-50 hover:border-blue-400 transition"
                            >
                                {word}
                            </span>
                        ))}
                    </div>
                </div>
            )}

            {/* Controls */}
            <div className="flex gap-3">
                <button
                    onClick={handleReset}
                    disabled={isLocked}
                    className="p-3 text-gray-500 hover:bg-gray-100 rounded-xl transition disabled:opacity-50"
                >
                    <RefreshCcw size={20} />
                </button>
                <button
                    onClick={checkAnswer}
                    disabled={isLocked || (maschileWords.length === 0 && femminileWords.length === 0)}
                    className="flex-grow py-3 bg-[#4CAF50] text-white rounded-xl font-bold shadow-md hover:bg-[#388E3C] transition disabled:bg-gray-500 disabled:cursor-not-allowed"
                >
                    Check Answer
                </button>
            </div>
        </div>
    );
};

const UnscrambleExercise = ({ prompt, blocks, correctAnswer, onAnswer }) => {
    const [draggedBlocks, setDraggedBlocks] = useState([]);
    const [availableBlocks, setAvailableBlocks] = useState([...blocks]);
    const [isLocked, setIsLocked] = useState(false);
    const [draggedItem, setDraggedItem] = useState(null);

    // Reset all state when blocks change (new exercise)
    useEffect(() => {
        setDraggedBlocks([]);
        setIsLocked(false);
        setDraggedItem(null);
        const shuffled = [...blocks].sort(() => Math.random() - 0.5);
        setAvailableBlocks(shuffled);
    }, [blocks]);

    const handleDragStart = (e, block, source) => {
        setDraggedItem({ block, source });
        e.dataTransfer.effectAllowed = 'move';
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    };

    const handleDrop = (e, targetArea) => {
        e.preventDefault();
        if (!draggedItem || isLocked) return;

        const { block, source } = draggedItem;

        if (source === 'available' && targetArea === 'answer') {
            // Move from available to answer area
            setAvailableBlocks(prev => prev.filter(b => b !== block));
            setDraggedBlocks(prev => [...prev, block]);
        } else if (source === 'answer' && targetArea === 'available') {
            // Move from answer back to available
            setDraggedBlocks(prev => prev.filter(b => b !== block));
            setAvailableBlocks(prev => [...prev, block]);
        }

        setDraggedItem(null);
    };

    const handleClick = (block, source) => {
        if (isLocked) return;
        if (source === 'available') {
            setAvailableBlocks(prev => prev.filter(b => b !== block));
            setDraggedBlocks(prev => [...prev, block]);
        } else {
            setDraggedBlocks(prev => prev.filter(b => b !== block));
            setAvailableBlocks(prev => [...prev, block]);
        }
    };

    const handleReset = () => {
        if (isLocked) return;
        setDraggedBlocks([]);
        const shuffled = [...blocks].sort(() => Math.random() - 0.5);
        setAvailableBlocks(shuffled);
    };

    const checkAnswer = () => {
        const attempt = draggedBlocks.join(" ");
        // Normalize both strings: lowercase, trim, normalize multiple spaces
        // Remove all punctuation (including commas) and extra spaces for comparison
        // This makes the validation more lenient - accepts answers with or without commas
        const normalize = (str) => {
            return str.toLowerCase()
                .trim()
                .replace(/\s+/g, ' ')  // Replace multiple spaces with single space
                .replace(/[,.!?;:]/g, '')  // Remove all punctuation including commas
                .trim();
        };
        const normalizedAttempt = normalize(attempt);
        const normalizedCorrect = normalize(correctAnswer);
        const isCorrect = normalizedAttempt === normalizedCorrect;
        onAnswer(isCorrect ? 'correct' : 'incorrect', attempt);
        setIsLocked(true);
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            
            {/* Answer area (drop zone) */}
            <div
                onDragOver={handleDragOver}
                onDrop={(e) => handleDrop(e, 'answer')}
                className="bg-gray-50 p-6 rounded-xl min-h-[80px] flex flex-wrap gap-3 border-2 border-dashed border-blue-300 items-center justify-center transition hover:border-blue-400"
            >
                {draggedBlocks.length === 0 ? (
                    <p className="text-gray-400 text-sm">Drag words here to build your sentence</p>
                ) : (
                    draggedBlocks.map((block, idx) => (
                        <span
                            key={idx}
                            draggable={!isLocked}
                            onDragStart={(e) => handleDragStart(e, block, 'answer')}
                            onClick={() => handleClick(block, 'answer')}
                            className="px-4 py-3 bg-blue-500 text-white rounded-lg font-bold shadow-md cursor-move hover:bg-blue-600 transition"
                        >
                            {block}
                        </span>
                    ))
                )}
            </div>

            {/* Available blocks */}
            <div className="space-y-2">
                <p className="text-sm text-gray-500 font-medium">Available words:</p>
                <div className="flex flex-wrap gap-2">
                    {availableBlocks.map((block, idx) => (
                        <span
                            key={idx}
                            draggable={!isLocked}
                            onDragStart={(e) => handleDragStart(e, block, 'available')}
                            onClick={() => handleClick(block, 'available')}
                            className="px-4 py-2 bg-white border-2 border-gray-300 text-gray-800 rounded-lg font-medium shadow-sm cursor-move hover:bg-gray-50 hover:border-blue-400 transition"
                        >
                            {block}
                        </span>
                    ))}
                </div>
            </div>

            {/* Controls */}
            <div className="flex gap-3">
                <button
                    onClick={handleReset}
                    disabled={isLocked}
                    className="p-3 text-gray-500 hover:bg-gray-100 rounded-xl transition disabled:opacity-50"
                >
                    <RefreshCcw size={20} />
                </button>
                <button
                    onClick={checkAnswer}
                    disabled={isLocked || draggedBlocks.length === 0}
                    className="flex-grow py-3 bg-[#4CAF50] text-white rounded-xl font-bold shadow-md hover:bg-[#388E3C] transition disabled:bg-gray-500 disabled:cursor-not-allowed"
                >
                    Check Answer
                </button>
            </div>
        </div>
    );
};

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
    }, [targetPhrase, targetLang]);

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
        await analyzeAudio(recordedBlob);
    };

    const analyzeAudio = async (audioBlob) => {
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

            const response = await axios.post(`${API}/voice/analyze`, formData, {
                headers: { 'Content-Type': 'multipart/form-data' },
                timeout: 30000
            });

            const { text, confidence: conf, phonetic_score } = response.data;
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
                <div className={`p-6 rounded-xl border space-y-3 ${
                    phoneticScore < 0.2 ? 'bg-red-50 border-red-200' : 
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
                            <p className={`text-xl font-bold ${
                                phoneticScore >= 0.7 ? 'text-green-600' : 
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

const MiniPromptExercise = ({ prompt, context, task, targetLang, nativeLang, onAnswer, explanation }) => {
    const [userInput, setUserInput] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);
    const [feedback, setFeedback] = useState(null);
    const [feedbackExplanation, setFeedbackExplanation] = useState(null);
    const [isComplete, setIsComplete] = useState(false);
    const textareaRef = useRef(null);

    const handleSubmit = async () => {
        if (!userInput.trim() || isProcessing || isComplete) return;

        setIsProcessing(true);
        setFeedback(null);

        try {
            // Use /tutor endpoint for AI validation
            const response = await axios.post(`${API}/tutor`, {
                user_message: userInput.trim(),
                chat_history: [],
                target_language: targetLang,
                native_language: nativeLang,
                level: "Beginner",
                lesson_id: null
            }, { timeout: 30000 });

            const aiResponse = response.data.text || "";
            const status = response.data.status;

            // Improved validation logic for mini-prompt exercises
            // Check for appropriate responses based on context and task
            const userLower = userInput.toLowerCase().trim();
            let resultStatus = 'incorrect'; // 'correct', 'almost', or 'incorrect'
            
            // Context-specific validation
            if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                // Informal greeting context - check for informal Italian greetings
                // Accept: Ciao, Come stai, Come va, etc.
                const hasInformalGreeting = userLower.includes("ciao") || 
                                           userLower.includes("come stai") ||
                                           userLower.includes("come va") ||
                                           (userLower.includes("salve") && !userLower.includes("buongiorno") && !userLower.includes("buonasera"));
                // Reject if uses formal greetings
                const usesFormalGreeting = userLower.includes("buongiorno") || userLower.includes("buonasera");
                
                if (hasInformalGreeting && !usesFormalGreeting) {
                    resultStatus = 'correct';
                } else if (hasInformalGreeting && usesFormalGreeting) {
                    // Partial: Has informal but also formal - this is "almost"
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                // Formal context - check for formal greetings
                const hasFormalGreeting = userLower.includes("buongiorno") || 
                                        userLower.includes("buonasera") ||
                                        userLower.includes("salve");
                // Reject if uses informal greeting
                const usesInformalGreeting = userLower.includes("ciao") && !userLower.includes("buongiorno") && !userLower.includes("buonasera");
                
                if (hasFormalGreeting && !usesInformalGreeting) {
                    resultStatus = 'correct';
                } else if (hasFormalGreeting && usesInformalGreeting) {
                    // Partial: Has formal but also informal
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                // "Chi sei?" (Who are you?) context - must respond with "Io sono" + name
                // Check for "Io sono" pattern (with or without "Io")
                const hasIoSono = userLower.includes("io sono") || 
                                 (userLower.startsWith("sono ") && userLower.split("sono ")[1]?.trim().length > 0);
                // Also accept "Mi chiamo" as alternative
                const hasMiChiamo = userLower.includes("mi chiamo");
                
                // For "Io sono" - check if there's text after it (the name)
                let hasName = false;
                if (userLower.includes("io sono")) {
                    const afterIoSono = userLower.split("io sono")[1]?.trim();
                    hasName = afterIoSono && afterIoSono.length > 0 && !afterIoSono.match(/^[.,!?;:]+$/);
                } else if (userLower.startsWith("sono ")) {
                    const afterSono = userLower.split("sono ")[1]?.trim();
                    hasName = afterSono && afterSono.length > 0 && !afterSono.match(/^[.,!?;:]+$/);
                } else if (hasMiChiamo) {
                    const afterMiChiamo = userLower.split("mi chiamo")[1]?.trim();
                    hasName = afterMiChiamo && afterMiChiamo.length > 0 && !afterMiChiamo.match(/^[.,!?;:]+$/);
                }
                
                // Accept if has "Io sono" or "Mi chiamo" followed by a name
                resultStatus = ((hasIoSono || hasMiChiamo) && hasName) ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                // "Di dove sei?" (Where are you from?) context - must respond with "Sono di" + country OR "Sono" + nationality
                const hasSonoDi = userLower.includes("sono di");
                const hasSono = userLower.includes("sono") && (userLower.includes("italia") || userLower.includes("francia") || userLower.includes("spagna") || userLower.includes("stati uniti") || userLower.includes("regno unito") || userLower.includes("americano") || userLower.includes("italiano") || userLower.includes("francese") || userLower.includes("spagnolo") || userLower.includes("inglese"));
                
                // Check if there's a country/nationality mentioned
                const hasCountry = userLower.includes("italia") || 
                                  userLower.includes("francia") || 
                                  userLower.includes("spagna") || 
                                  userLower.includes("stati uniti") ||
                                  userLower.includes("regno unito") ||
                                  userLower.includes("americano") ||
                                  userLower.includes("italiano") ||
                                  userLower.includes("francese") ||
                                  userLower.includes("spagnolo") ||
                                  userLower.includes("inglese");
                
                // Accept if has "Sono di" + country OR "Sono" + nationality
                if ((hasSonoDi && hasCountry) || (hasSono && hasCountry)) {
                    resultStatus = 'correct';
                } else if (hasSonoDi || hasSono) {
                    // Has "Sono di" or "Sono" but missing country/nationality
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else if (context && context.toLowerCase().includes("piacere")) {
                // Introduction context - must introduce self
                const hasIntroduction = userLower.includes("mi chiamo") || 
                                      (userLower.includes("sono") && userLower.split("sono")[1].trim().length > 0) ||
                                      (userLower.includes("piacere") && userLower.length > 7);
                resultStatus = hasIntroduction ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                // Polite closing context - must have polite closing
                const hasPoliteClosing = userLower.includes("grazie") || 
                                        userLower.includes("arrivederci") || 
                                        userLower.includes("arrivederla") ||
                                        userLower.includes("a presto") || 
                                        userLower.includes("buona giornata") ||
                                        userLower.includes("buonasera") ||
                                        userLower.includes("buongiorno");
                resultStatus = hasPoliteClosing ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                // Coffee ordering context - must have "caffè" (with correct accent è) and "per favore"
                const normalizedInput = userLower.replace(/è/g, 'e').replace(/é/g, 'e');
                const hasCaffe = normalizedInput.includes("caffe");
                const hasPerFavore = userLower.includes("per favore");
                const hasUn = normalizedInput.includes("un ") || normalizedInput.startsWith("un ");
                
                // Check for wrong accent (é instead of è)
                const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");
                
                // Accept if has "un caffè" (with correct accent è) and "per favore"
                if (hasCaffe && hasPerFavore && !hasWrongAccent) {
                    resultStatus = 'correct';
                } else if (hasCaffe && hasPerFavore && hasWrongAccent) {
                    // Has everything correct but wrong accent (é instead of è) - almost correct
                    resultStatus = 'almost';
                } else if (hasCaffe && hasUn) {
                    // Has "un caffè" but missing "per favore" - almost correct
                    resultStatus = 'almost';
                } else if (hasCaffe || hasPerFavore) {
                    // Partial: has one but not both
                    resultStatus = 'almost';
                } else {
                    resultStatus = 'incorrect';
                }
            } else {
                // Fallback: use AI response analysis
                const aiLower = aiResponse.toLowerCase();
                const isCorrect = status === "GOAL_ACHIEVED" || 
                            aiLower.includes("correct") ||
                            aiLower.includes("good") ||
                            aiLower.includes("perfect") ||
                            aiLower.includes("bravo") ||
                            aiLower.includes("ben fatto") ||
                            aiLower.includes("ottimo") ||
                            aiLower.includes("fantastico") ||
                            aiLower.includes("perfetto");
                resultStatus = isCorrect ? 'correct' : 'incorrect';
            }

            // Always stop processing, even on success
            setIsProcessing(false);
            setIsComplete(true);
            
            // Set appropriate feedback with detailed, pedagogically-focused explanations
            if (resultStatus === 'correct') {
                // When correct: Explain why it's appropriate in this context
                let feedbackMsg = "Correct!";
                let explanationText = "";
                
                if (aiResponse && aiResponse.trim().length > 0 && !aiResponse.toLowerCase().includes("error")) {
                    // Use AI response if it's meaningful
                    explanationText = aiResponse;
                } else {
                    // Generate context-specific explanations
                    if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                        explanationText = `Perfect! You used "${userInput}" which is exactly right for greeting a friend. In Italian, "Ciao" and "Come stai?" are what you'd use with people you know well - it shows you understand when to be casual and friendly. Great job!`;
                    } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                        const isEvening = context.toLowerCase().includes("7 pm") || context.toLowerCase().includes("evening");
                        const greeting = userInput.toLowerCase().includes("buonasera") ? "Buonasera" : userInput.toLowerCase().includes("buongiorno") ? "Buongiorno" : "formal greeting";
                        explanationText = `Excellent choice! You used ${greeting}, which is perfect for this situation. ${isEvening ? "Since it's evening, 'Buonasera' is exactly what you'd say - you're really getting the hang of time-based greetings!" : "Using formal language shows respect, and you've got that down. Well done!"}`;
                    } else if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                        explanationText = `Perfect! You correctly responded to "Chi sei?" (Who are you?) with "${userInput}". Using "Io sono [name]" is exactly the right way to answer this question in Italian. You're getting the hang of introductions!`;
                    } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                        explanationText = `Perfect! You correctly answered "Di dove sei?" (Where are you from?) with "${userInput}". Using "Sono di [country]" or "Sono [nationality]" is exactly the right way to respond. Great job!`;
                    } else if (context && context.toLowerCase().includes("piacere")) {
                        explanationText = `Nice work! You responded with "${userInput}", which is perfect. When someone says "Piacere" (nice to meet you), introducing yourself with "Mi chiamo" or "Sono" is exactly the right thing to do. You're understanding the flow of Italian conversations really well!`;
                    } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                        explanationText = `Perfect! Using "${userInput}" when leaving a shop is exactly what you should do. In Italian culture, it's really important to acknowledge people politely when you're leaving - it shows good manners. You're getting the cultural side of things too, which is fantastic!`;
                    } else if (explanation) {
                        explanationText = explanation;
                    } else {
                        explanationText = "Well done! Your response is appropriate for this situation.";
                    }
                }
                
                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('correct', userInput, explanationText);
            } else if (resultStatus === 'almost') {
                // When almost: Explain what's right and what needs adjustment
                let feedbackMsg = "Almost!";
                let explanationText = "";
                
                // Generate "almost" feedback explaining what's right and what needs adjustment
                if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                    explanationText = `You're on the right track! You used an informal greeting like "Come stai?" which is perfect for a friend. However, you also used a formal greeting like "Buongiorno" or "Buonasera" at the beginning. For friends, stick with just the informal greeting - try "Ciao" or "Come stai?" without the formal part. You're getting it!`;
                } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                    explanationText = `Good effort! You used a formal greeting which is correct for this situation. However, you also mixed in an informal greeting. For someone like a professor, keep it completely formal - use just "Buongiorno" or "Buonasera" depending on the time. You're almost there!`;
                } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                    const userLower = userInput.toLowerCase();
                    const hasCaffe = userLower.includes("caffè") || userLower.includes("caffe") || userLower.includes("caffé");
                    const hasPerFavore = userLower.includes("per favore");
                    const hasUn = userLower.includes("un ") || userLower.startsWith("un ");
                    const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");
                    
                    if (hasWrongAccent && hasCaffe && hasPerFavore) {
                        explanationText = `Almost there! You have everything right - "un caffè" and "per favore" - but there's a small accent issue. The word "caffè" uses a grave accent (è), not an acute accent (é). So it should be "Un caffè per favore" with è, not é. Great attention to detail though!`;
                    } else if (hasCaffe && hasUn && !hasPerFavore) {
                        explanationText = `You're almost there! You correctly used "un caffè" (a coffee), which is perfect. To make it more polite, add "per favore" (please) at the end. So it would be "Un caffè per favore" - that's the complete, polite way to order!`;
                    } else if (hasCaffe && !hasUn) {
                        explanationText = `Good start! You mentioned "caffè" (coffee), which is correct. To order properly, use "Un caffè" (A coffee) - the article "un" is important because "caffè" is masculine. Then add "per favore" (please) to be polite. Try: "Un caffè per favore"!`;
                    } else if (!hasCaffe && hasPerFavore) {
                        explanationText = `You remembered "per favore" (please), which is great for being polite! However, you need to specify what you're ordering. Use "Un caffè per favore" (A coffee, please) - "caffè" is the word for coffee, and "un" is the masculine article. You're getting there!`;
                    } else {
                        explanationText = `To order a coffee in Italian, say "Un caffè per favore" (A coffee, please). Remember: "caffè" is masculine, so use "un" as the article. The phrase "per favore" makes it polite. Give it another try!`;
                    }
                } else {
                    explanationText = "You're close! Some parts of your answer are right, but there are a few adjustments needed. Keep trying!";
                }
                
                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('almost', userInput, explanationText);
            } else {
                // When incorrect: Explain why it's wrong and what would be better
                let feedbackMsg = "Incorrect.";
                let explanationText = "";
                
                if (aiResponse && aiResponse.trim().length > 0 && !aiResponse.toLowerCase().includes("error")) {
                    explanationText = aiResponse;
                } else {
                    // Generate context-specific explanations for why it's wrong
                    if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                        explanationText = `Almost there! When someone asks "Chi sei?" (Who are you?), you should respond with "Io sono [your name]" (I am [name]). Your answer "${userInput}" is close, but make sure you include "Io sono" followed by your name. For example: "Io sono Jeff" or "Io sono Maria". You're learning!`;
                    } else if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                        const usedFormal = userInput.toLowerCase().includes("buongiorno") || userInput.toLowerCase().includes("buonasera");
                        explanationText = `I see what happened here! ${usedFormal ? "You used a formal greeting, but since this is a friend, you'd want to use something more casual like 'Ciao' or 'Come stai?' to show you're on familiar terms. In Italian, the greeting you choose depends on how well you know the person - with friends, we keep it informal!" : "For a friend, try using something more casual like 'Ciao' (hi/bye) or 'Come stai?' (how are you?). These show you're on familiar terms, which is perfect for friends!"}`;
                    } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                        const usedInformal = userInput.toLowerCase().includes("ciao") && !userInput.toLowerCase().includes("buongiorno") && !userInput.toLowerCase().includes("buonasera");
                        const isEvening = context.toLowerCase().includes("7 pm") || context.toLowerCase().includes("evening");
                        
                        if (usedInformal) {
                            explanationText = `I see what happened - you used an informal greeting, but this situation calls for something more formal. ${isEvening ? "Since it's evening, try 'Buonasera' (good evening) - that's the polite way to greet someone in the evening, especially someone like a professor!" : "When talking to a professor or someone in authority, we use formal greetings like 'Buongiorno' or 'Buonasera' depending on the time. It's all about showing respect - you'll get the hang of it!"}`;
                        } else {
                            explanationText = `Almost there! ${isEvening ? "Since it's 7 PM (evening), you'd want to use 'Buonasera' (good evening) instead of 'Buongiorno'. In Italian, time-based greetings matter a lot - 'Buongiorno' is for morning/daytime, while 'Buonasera' is for evening/night. Don't worry, this is a common thing to mix up!" : "For someone like a professor, we use formal greetings to show respect. Try 'Buongiorno' (good morning) or 'Buonasera' (good evening) depending on the time of day. You're learning the social side of Italian - keep going!"}`;
                        }
                    } else if (context && context.toLowerCase().includes("piacere")) {
                        explanationText = `Good try! When someone says "Piacere" (nice to meet you), the natural response is to introduce yourself. Try using "Mi chiamo [your name]" (my name is...) or "Sono [your name]" (I am...). This is how Italians do introductions - you'll get it!`;
                    } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                        explanationText = `Almost there! When leaving a shop, Italians like to end the interaction politely. Try phrases like "Arrivederci" (goodbye), "Grazie" (thank you), or "A presto" (see you soon). It's a cultural thing - showing good manners is really valued in Italy. You're learning!`;
                    } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                        const userLower = userInput.toLowerCase();
                        const hasSonoDi = userLower.includes("sono di");
                        const hasSono = userLower.includes("sono");
                        const hasCountry = userLower.includes("italia") || userLower.includes("francia") || userLower.includes("spagna") || userLower.includes("stati uniti") || userLower.includes("regno unito") || userLower.includes("americano") || userLower.includes("italiano") || userLower.includes("francese") || userLower.includes("spagnolo") || userLower.includes("inglese");
                        
                        if (!hasSonoDi && !hasSono) {
                            explanationText = `To answer "Di dove sei?" (Where are you from?), start with "Sono di" (I'm from) followed by a country name, or "Sono" (I am) followed by a nationality. For example: "Sono di Italia" (I'm from Italy) or "Sono italiano" (I am Italian). Try again!`;
                        } else if ((hasSonoDi || hasSono) && !hasCountry) {
                            explanationText = `You used "Sono di" or "Sono" which is good, but you need to add a country name or nationality. For example: "Sono di Italia" (I'm from Italy) or "Sono italiano" (I am Italian). You're getting there!`;
                        } else {
                            explanationText = `To answer "Di dove sei?" (Where are you from?), use "Sono di [country]" (I'm from [country]) or "Sono [nationality]" (I am [nationality]). For example: "Sono di Italia" or "Sono italiano". Give it another try!`;
                        }
                    } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                        const userLower = userInput.toLowerCase();
                        const hasCaffe = userLower.includes("caffè") || userLower.includes("caffe") || userLower.includes("caffé");
                        const hasPerFavore = userLower.includes("per favore");
                        const hasUn = userLower.includes("un ") || userLower.startsWith("un ");
                        const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");
                        
                        if (hasWrongAccent && hasCaffe && hasPerFavore) {
                            explanationText = `Almost there! You have everything right - "un caffè" and "per favore" - but there's a small accent issue. The word "caffè" uses a grave accent (è), not an acute accent (é). So it should be "Un caffè per favore" with è, not é. Great attention to detail though!`;
                        } else if (hasCaffe && hasUn && !hasPerFavore) {
                            explanationText = `You're almost there! You correctly used "un caffè" (a coffee), which is perfect. To make it more polite, add "per favore" (please) at the end. So it would be "Un caffè per favore" - that's the complete, polite way to order!`;
                        } else if (hasCaffe && !hasUn) {
                            explanationText = `Good start! You mentioned "caffè" (coffee), which is correct. To order properly, use "Un caffè" (A coffee) - the article "un" is important because "caffè" is masculine. Then add "per favore" (please) to be polite. Try: "Un caffè per favore"!`;
                        } else if (!hasCaffe && hasPerFavore) {
                            explanationText = `You remembered "per favore" (please), which is great for being polite! However, you need to specify what you're ordering. Use "Un caffè per favore" (A coffee, please) - "caffè" is the word for coffee, and "un" is the masculine article. You're getting there!`;
                        } else {
                            explanationText = `To order a coffee in Italian, say "Un caffè per favore" (A coffee, please). Remember: "caffè" is masculine, so use "un" as the article. The phrase "per favore" makes it polite. Give it another try!`;
                        }
                    } else if (explanation) {
                        explanationText = explanation;
                    } else {
                        explanationText = "Your response doesn't quite fit this situation. Think about the context and what would be culturally appropriate.";
                    }
                }
                
                setFeedback(feedbackMsg);
                setFeedbackExplanation(explanationText);
                onAnswer('incorrect', userInput, explanationText);
            }
        } catch (error) {
            console.error("Error in mini prompt:", error);
            // Always stop processing on error
            setIsProcessing(false);
            
            // If API fails, try to validate locally as fallback
            const userLower = userInput.toLowerCase().trim();
            let fallbackStatus = 'incorrect'; // 'correct', 'almost', or 'incorrect'
            
            // Apply same validation logic as fallback
            if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                const hasInformalGreeting = userLower.includes("ciao") || 
                                           userLower.includes("come stai") ||
                                           userLower.includes("come va");
                const usesFormalGreeting = userLower.includes("buongiorno") || userLower.includes("buonasera");
                
                if (hasInformalGreeting && !usesFormalGreeting) {
                    fallbackStatus = 'correct';
                } else if (hasInformalGreeting && usesFormalGreeting) {
                    fallbackStatus = 'almost';
                } else {
                    fallbackStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                const hasFormalGreeting = userLower.includes("buongiorno") || 
                                        userLower.includes("buonasera") ||
                                        userLower.includes("salve");
                const usesInformalGreeting = userLower.includes("ciao") && !userLower.includes("buongiorno") && !userLower.includes("buonasera");
                
                if (hasFormalGreeting && !usesInformalGreeting) {
                    fallbackStatus = 'correct';
                } else if (hasFormalGreeting && usesInformalGreeting) {
                    fallbackStatus = 'almost';
                } else {
                    fallbackStatus = 'incorrect';
                }
            } else if (context && context.toLowerCase().includes("piacere")) {
                // Check for "Chi sei?" context
                if (context && (context.toLowerCase().includes("chi sei") || context.toLowerCase().includes("who are you"))) {
                    const hasIoSono = userLower.includes("io sono") || 
                                     (userLower.startsWith("sono ") && userLower.split("sono ")[1]?.trim().length > 0);
                    const hasMiChiamo = userLower.includes("mi chiamo");
                    
                    let hasName = false;
                    if (userLower.includes("io sono")) {
                        const afterIoSono = userLower.split("io sono")[1]?.trim();
                        hasName = afterIoSono && afterIoSono.length > 0 && !afterIoSono.match(/^[.,!?;:]+$/);
                    } else if (userLower.startsWith("sono ")) {
                        const afterSono = userLower.split("sono ")[1]?.trim();
                        hasName = afterSono && afterSono.length > 0 && !afterSono.match(/^[.,!?;:]+$/);
                    } else if (hasMiChiamo) {
                        const afterMiChiamo = userLower.split("mi chiamo")[1]?.trim();
                        hasName = afterMiChiamo && afterMiChiamo.length > 0 && !afterMiChiamo.match(/^[.,!?;:]+$/);
                    }
                    
                    fallbackStatus = ((hasIoSono || hasMiChiamo) && hasName) ? 'correct' : 'incorrect';
                } else {
                    const hasIntroduction = userLower.includes("mi chiamo") || 
                                          (userLower.includes("sono") && userLower.split("sono")[1].trim().length > 0) ||
                                          (userLower.includes("piacere") && userLower.length > 7);
                    fallbackStatus = hasIntroduction ? 'correct' : 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                const hasPoliteClosing = userLower.includes("grazie") || 
                                        userLower.includes("arrivederci") || 
                                        userLower.includes("arrivederla") ||
                                        userLower.includes("a presto") || 
                                        userLower.includes("buona giornata") ||
                                        userLower.includes("buonasera") ||
                                        userLower.includes("buongiorno");
                fallbackStatus = hasPoliteClosing ? 'correct' : 'incorrect';
            } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                // "Di dove sei?" (Where are you from?) context - must respond with "Sono di" + country OR "Sono" + nationality
                const hasSonoDi = userLower.includes("sono di");
                const hasSono = userLower.includes("sono") && (userLower.includes("italia") || userLower.includes("francia") || userLower.includes("spagna") || userLower.includes("stati uniti") || userLower.includes("regno unito") || userLower.includes("americano") || userLower.includes("italiano") || userLower.includes("francese") || userLower.includes("spagnolo") || userLower.includes("inglese"));
                
                // Check if there's a country/nationality mentioned
                const hasCountry = userLower.includes("italia") || 
                                  userLower.includes("francia") || 
                                  userLower.includes("spagna") || 
                                  userLower.includes("stati uniti") ||
                                  userLower.includes("regno unito") ||
                                  userLower.includes("americano") ||
                                  userLower.includes("italiano") ||
                                  userLower.includes("francese") ||
                                  userLower.includes("spagnolo") ||
                                  userLower.includes("inglese");
                
                // Accept if has "Sono di" + country OR "Sono" + nationality
                if ((hasSonoDi && hasCountry) || (hasSono && hasCountry)) {
                    fallbackStatus = 'correct';
                } else if (hasSonoDi || hasSono) {
                    // Has "Sono di" or "Sono" but missing country/nationality
                    fallbackStatus = 'almost';
                } else {
                    fallbackStatus = 'incorrect';
                }
            } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                // Coffee ordering context - must have "caffè" (with correct accent è) and "per favore"
                const normalizedInput = userLower.replace(/è/g, 'e').replace(/é/g, 'e');
                const hasCaffe = normalizedInput.includes("caffe");
                const hasPerFavore = userLower.includes("per favore");
                const hasUn = normalizedInput.includes("un ") || normalizedInput.startsWith("un ");
                
                // Check for wrong accent (é instead of è)
                const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");
                
                // Accept if has "un caffè" (with correct accent è) and "per favore"
                if (hasCaffe && hasPerFavore && !hasWrongAccent) {
                    fallbackStatus = 'correct';
                } else if (hasCaffe && hasPerFavore && hasWrongAccent) {
                    // Has everything correct but wrong accent (é instead of è) - almost correct
                    fallbackStatus = 'almost';
                } else if (hasCaffe && hasUn) {
                    // Has "un caffè" but missing "per favore" - almost correct
                    fallbackStatus = 'almost';
                } else if (hasCaffe || hasPerFavore) {
                    // Partial: has one but not both
                    fallbackStatus = 'almost';
                } else {
                    fallbackStatus = 'incorrect';
                }
            }
            
            setIsComplete(true);
            let feedbackMsg = "";
            let explanationText = "";
            
            if (fallbackStatus === 'correct') {
                feedbackMsg = "Correct!";
                
                // Generate context-specific explanations
                if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                    explanationText = `Perfect! You used an informal greeting ("${userInput}"), which is appropriate when greeting a friend. In Italian, "Ciao" and "Come stai?" are used with people you know well, showing familiarity and closeness.`;
                } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                    const isEvening = context.toLowerCase().includes("7 pm") || context.toLowerCase().includes("evening");
                    explanationText = `Excellent! You correctly used a formal greeting, which is required when addressing a professor or someone in authority. ${isEvening ? "Since it's evening (7 PM), 'Buonasera' is the appropriate time-based greeting." : "Using formal language (Lei form) shows respect in professional or academic settings."}`;
                } else if (context && context.toLowerCase().includes("piacere")) {
                    explanationText = `Well done! You correctly introduced yourself using "${userInput}". In Italian, when someone says "Piacere", the appropriate response is to introduce yourself.`;
                } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                    explanationText = `Perfect! You correctly answered "Di dove sei?" (Where are you from?) with "${userInput}". Using "Sono di [country]" or "Sono [nationality]" is exactly the right way to respond. Great job!`;
                } else if (context && (context.toLowerCase().includes("shop") || context.toLowerCase().includes("leaving"))) {
                    explanationText = `Perfect! You used a polite closing phrase ("${userInput}"), which is essential when leaving a shop. In Italian culture, it's important to acknowledge the interaction politely.`;
                } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                    explanationText = `Perfect! You correctly ordered a coffee using "${userInput}". In Italian, "Un caffè per favore" (A coffee, please) is the standard way to order. You used the masculine article "un" with "caffè" which is correct - great job!`;
                } else if (explanation) {
                    explanationText = explanation;
                } else {
                    explanationText = "Well done!";
                }
            } else if (fallbackStatus === 'almost') {
                feedbackMsg = "Almost!";
                
                // Generate "almost" feedback
                if (context && context.toLowerCase().includes("friend") && task && task.toLowerCase().includes("greet")) {
                    explanationText = `You're on the right track! You used an informal greeting like "Come stai?" which is perfect for a friend. However, you also used a formal greeting like "Buongiorno" or "Buonasera" at the beginning. For friends, stick with just the informal greeting - try "Ciao" or "Come stai?" without the formal part. You're getting it!`;
                } else if (context && (context.toLowerCase().includes("professor") || context.toLowerCase().includes("dr.") || context.toLowerCase().includes("7 pm"))) {
                    explanationText = `Good effort! You used a formal greeting which is correct for this situation. However, you also mixed in an informal greeting. For someone like a professor, keep it completely formal - use just "Buongiorno" or "Buonasera" depending on the time. You're almost there!`;
                } else if (context && (context.toLowerCase().includes("di dove") || context.toLowerCase().includes("where are you from"))) {
                    const userLower = userInput.toLowerCase();
                    const hasSonoDi = userLower.includes("sono di");
                    const hasSono = userLower.includes("sono");
                    const hasCountry = userLower.includes("italia") || userLower.includes("francia") || userLower.includes("spagna") || userLower.includes("stati uniti") || userLower.includes("regno unito") || userLower.includes("americano") || userLower.includes("italiano") || userLower.includes("francese") || userLower.includes("spagnolo") || userLower.includes("inglese");
                    
                    if ((hasSonoDi || hasSono) && !hasCountry) {
                        explanationText = `You're almost there! You used "Sono di" or "Sono" which is correct, but you need to add a country name or nationality. For example: "Sono di Italia" (I'm from Italy) or "Sono italiano" (I am Italian). Try again!`;
                    } else {
                        explanationText = `To answer "Di dove sei?" (Where are you from?), use "Sono di [country]" (I'm from [country]) or "Sono [nationality]" (I am [nationality]). For example: "Sono di Italia" or "Sono italiano". Give it another try!`;
                    }
                } else if (context && (context.toLowerCase().includes("café") || context.toLowerCase().includes("cafe") || context.toLowerCase().includes("coffee")) && task && task.toLowerCase().includes("order")) {
                    const userLower = userInput.toLowerCase();
                    const hasCaffe = userLower.includes("caffè") || userLower.includes("caffe") || userLower.includes("caffé");
                    const hasPerFavore = userLower.includes("per favore");
                    const hasUn = userLower.includes("un ") || userLower.startsWith("un ");
                    const hasWrongAccent = userLower.includes("caffé") && !userLower.includes("caffè");
                    
                    if (hasWrongAccent && hasCaffe && hasPerFavore) {
                        explanationText = `Almost there! You have everything right - "un caffè" and "per favore" - but there's a small accent issue. The word "caffè" uses a grave accent (è), not an acute accent (é). So it should be "Un caffè per favore" with è, not é. Great attention to detail though!`;
                    } else if (hasCaffe && hasUn && !hasPerFavore) {
                        explanationText = `You're almost there! You correctly used "un caffè" (a coffee), which is perfect. To make it more polite, add "per favore" (please) at the end. So it would be "Un caffè per favore" - that's the complete, polite way to order!`;
                    } else if (hasCaffe && !hasUn) {
                        explanationText = `Good start! You mentioned "caffè" (coffee), which is correct. To order properly, use "Un caffè" (A coffee) - the article "un" is important because "caffè" is masculine. Then add "per favore" (please) to be polite. Try: "Un caffè per favore"!`;
                    } else if (!hasCaffe && hasPerFavore) {
                        explanationText = `You remembered "per favore" (please), which is great for being polite! However, you need to specify what you're ordering. Use "Un caffè per favore" (A coffee, please) - "caffè" is the word for coffee, and "un" is the masculine article. You're getting there!`;
                    } else {
                        explanationText = `To order a coffee in Italian, say "Un caffè per favore" (A coffee, please). Remember: "caffè" is masculine, so use "un" as the article. The phrase "per favore" makes it polite. Give it another try!`;
                    }
                } else {
                    explanationText = "You're close! Some parts of your answer are right, but there are a few adjustments needed. Keep trying!";
                }
            } else {
                feedbackMsg = "Error validating response.";
                explanationText = "Please check your answer and try again.";
                if (explanation) {
                    explanationText = explanation;
                }
            }
            
            setFeedback(feedbackMsg);
            setFeedbackExplanation(explanationText);
            onAnswer(fallbackStatus, userInput, explanationText);
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            
            {/* Context display */}
            {context && (
                <div className="bg-blue-50 p-4 rounded-xl border border-blue-200">
                    <p className="text-sm text-gray-600 mb-2 font-medium">Context:</p>
                    <p className="text-gray-800">{context}</p>
                </div>
            )}

            {/* Task display */}
            {task && (
                <div className="bg-yellow-50 p-4 rounded-xl border border-yellow-200">
                    <p className="text-sm text-gray-600 mb-2 font-medium">Task:</p>
                    <p className="text-lg font-bold text-gray-800">{task}</p>
                </div>
            )}

            {/* Input area */}
            <div className="space-y-3">
                <label className="block text-sm font-medium text-gray-700">
                    Your response ({targetLang.toUpperCase()}):
                </label>
                <textarea
                    ref={textareaRef}
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    disabled={isComplete || isProcessing}
                    placeholder="Type your response here..."
                    className="w-full p-4 border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:outline-none resize-none disabled:bg-gray-100 disabled:cursor-not-allowed"
                    rows={3}
                />
                {/* Accented letter chips for Italian */}
                {targetLang === 'it' && (
                    <AccentedLetterChips 
                        inputRef={textareaRef}
                        value={userInput}
                        setValue={setUserInput}
                        disabled={isComplete || isProcessing}
                    />
                )}
                <button
                    onClick={handleSubmit}
                    disabled={!userInput.trim() || isComplete || isProcessing}
                    className="w-full py-4 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white rounded-xl font-bold shadow-md transition transform hover:scale-[1.02] disabled:bg-gray-400 disabled:cursor-not-allowed flex items-center justify-center gap-2"
                >
                    {isProcessing ? (
                        <>
                            <Loader2 className="w-5 h-5 animate-spin" />
                            Validating...
                        </>
                    ) : isComplete ? (
                        "Submitted"
                    ) : (
                        "Submit"
                    )}
                </button>
            </div>

            {/* Feedback - removed duplicate, handled by parent ExerciseView */}

            {explanation && !isComplete && (
                <div className="bg-purple-50 p-4 rounded-xl border border-purple-200">
                    <p className="text-sm text-purple-700 font-medium mb-1">💡 Hint:</p>
                    <p className="text-sm text-purple-800 italic">{explanation}</p>
                </div>
            )}
        </div>
    );
};

// ========== PRIORITY 1: NEW EXERCISE COMPONENTS ==========

// Listening Comprehension Exercise
const ListeningComprehensionExercise = ({ prompt, audioUrl, audioText, options, correctAnswer, allowReplay = true, maxPlays = 3, onAnswer, explanation, targetLang = "it" }) => {
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const [playCount, setPlayCount] = useState(0);
    const [hasAnswered, setHasAnswered] = useState(false);

    // Use audio_text if provided, otherwise fall back to audioUrl or correctAnswer
    const textToSpeak = audioText || (audioUrl ? null : correctAnswer);

    useEffect(() => {
        // Auto-play on mount using TTS
        if (textToSpeak && playCount === 0) {
            speakText(textToSpeak, targetLang);
            setPlayCount(1);
            setIsPlaying(true);
            // Simulate playing state for TTS (estimate based on text length)
            const estimatedDuration = Math.max(2000, textToSpeak.length * 150);
            setTimeout(() => setIsPlaying(false), estimatedDuration);
        }
    }, []);

    const handlePlay = () => {
        if (playCount >= maxPlays || !textToSpeak) return;
        
        // Always use TTS
        speakText(textToSpeak, targetLang);
        setPlayCount(p => p + 1);
        setIsPlaying(true);
        // Simulate playing state for TTS
        const estimatedDuration = Math.max(2000, textToSpeak.length * 150);
        setTimeout(() => setIsPlaying(false), estimatedDuration);
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
                <div className="flex items-center justify-center gap-4 mb-4">
                    <button
                        onClick={handlePlay}
                        disabled={playCount >= maxPlays || isPlaying}
                        className="px-6 py-3 bg-blue-600 text-white rounded-xl font-semibold hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition flex items-center gap-2"
                    >
                        <Volume2 size={20} />
                        {isPlaying ? 'Playing...' : allowReplay ? `Play Audio (${playCount}/${maxPlays})` : 'Play Audio'}
                    </button>
                </div>
                {playCount >= maxPlays && (
                    <p className="text-sm text-gray-600 text-center">Maximum plays reached. Select your answer below.</p>
                )}
            </div>
            <div className="space-y-3">
                {options.map((opt, idx) => (
                    <button
                        key={idx}
                        onClick={() => handleSelect(opt)}
                        disabled={hasAnswered || playCount === 0}
                        className={`w-full p-4 text-left rounded-xl border transition-all ${
                            hasAnswered
                                ? opt === correctAnswer
                                    ? 'bg-green-100 border-green-300 text-green-800'
                                    : opt === selectedAnswer
                                    ? 'bg-red-100 border-red-300 text-red-800'
                                    : 'bg-gray-50 border-gray-200 text-gray-600'
                                : 'bg-white border-gray-200 hover:bg-gray-50 cursor-pointer'
                        } ${playCount === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        {opt}
                    </button>
                ))}
            </div>
        </div>
    );
};

// Free Writing Exercise
const FreeWritingExercise = ({ prompt, context, task, targetLang, requiredElements, exampleResponse, validationMode = "ai", onAnswer, explanation }) => {
    const [userInput, setUserInput] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);
    const [feedback, setFeedback] = useState(null);
    const [feedbackExplanation, setFeedbackExplanation] = useState(null);
    const [isComplete, setIsComplete] = useState(false);
    const textareaRef = useRef(null);

    const handleSubmit = async () => {
        if (!userInput.trim() || isProcessing || isComplete) return;

        setIsProcessing(true);
        setFeedback(null);

        try {
            if (validationMode === "ai") {
                // Use AI validation (same as mini_prompt)
                const response = await axios.post(`${API}/tutor`, {
                    user_message: userInput.trim(),
                    chat_history: [],
                    target_language: targetLang,
                    native_language: "en",
                    level: "Beginner",
                    lesson_id: null
                }, { timeout: 30000 });

                const aiResponse = response.data.text || "";
                const status = response.data.status;

                // Pattern-based validation for required elements
                const userLower = userInput.toLowerCase();
                let allElementsPresent = true;
                let missingElements = [];

                if (requiredElements) {
                    requiredElements.forEach(element => {
                        let found = false;
                        if (element === "name") {
                            found = userLower.includes("mi chiamo") || userLower.includes("sono ") || userLower.includes("io sono");
                        } else if (element === "greeting") {
                            found = userLower.includes("ciao") || userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
                        } else if (element === "origin") {
                            found = userLower.includes("sono di") || userLower.includes("di italia") || userLower.includes("di francia");
                        } else if (element === "how are you") {
                            found = userLower.includes("come stai") || userLower.includes("come va");
                        }
                        if (!found) {
                            allElementsPresent = false;
                            missingElements.push(element);
                        }
                    });
                }

                let resultStatus = 'incorrect';
                if (allElementsPresent && (status === 'correct' || aiResponse.toLowerCase().includes('correct'))) {
                    resultStatus = 'correct';
                } else if (allElementsPresent || status === 'almost') {
                    resultStatus = 'almost';
                }

                let explanationText = explanation || aiResponse;
                if (missingElements.length > 0) {
                    explanationText = `You're missing: ${missingElements.join(', ')}. ${explanationText}`;
                }

                setFeedback(resultStatus === 'correct' ? 'success' : resultStatus === 'almost' ? 'warning' : 'error');
                setFeedbackExplanation(explanationText);
                onAnswer(resultStatus, userInput, explanationText);
            } else {
                // Pattern-based validation only
                const userLower = userInput.toLowerCase();
                let allElementsPresent = true;
                let missingElements = [];

                if (requiredElements) {
                    requiredElements.forEach(element => {
                        let found = false;
                        if (element === "name") {
                            found = userLower.includes("mi chiamo") || userLower.includes("sono ") || userLower.includes("io sono");
                        } else if (element === "greeting") {
                            found = userLower.includes("ciao") || userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
                        } else if (element === "origin") {
                            found = userLower.includes("sono di") || userLower.includes("di italia") || userLower.includes("di francia");
                        }
                        if (!found) {
                            allElementsPresent = false;
                            missingElements.push(element);
                        }
                    });
                }

                const resultStatus = allElementsPresent ? 'correct' : 'almost';
                let explanationText = explanation || (allElementsPresent ? "Great writing!" : `You're missing: ${missingElements.join(', ')}. Try to include all required elements.`);
                
                setFeedback(resultStatus === 'correct' ? 'success' : 'warning');
                setFeedbackExplanation(explanationText);
                onAnswer(resultStatus, userInput, explanationText);
            }
        } catch (error) {
            console.error("Error validating writing:", error);
            // Fallback to pattern matching
            const userLower = userInput.toLowerCase();
            let allElementsPresent = true;
            if (requiredElements) {
                requiredElements.forEach(element => {
                    let found = false;
                    if (element === "name") {
                        found = userLower.includes("mi chiamo") || userLower.includes("sono ");
                    } else if (element === "greeting") {
                        found = userLower.includes("ciao") || userLower.includes("buongiorno");
                    }
                    if (!found) allElementsPresent = false;
                });
            }
            const resultStatus = allElementsPresent ? 'correct' : 'almost';
            setFeedback(resultStatus === 'correct' ? 'success' : 'warning');
            setFeedbackExplanation(explanation || "Good effort! Make sure to include all required elements.");
            onAnswer(resultStatus, userInput, explanation);
        } finally {
            setIsProcessing(false);
            setIsComplete(true);
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            {context && (
                <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                    <p className="text-sm text-gray-600 mb-2"><strong>Context:</strong> {context}</p>
                    <p className="text-sm text-gray-700"><strong>Task:</strong> {task}</p>
                    {requiredElements && (
                        <p className="text-sm text-blue-600 mt-2"><strong>Required:</strong> {requiredElements.join(', ')}</p>
                    )}
                </div>
            )}
            <textarea
                ref={textareaRef}
                value={userInput}
                onChange={(e) => setUserInput(e.target.value)}
                placeholder="Write your response here..."
                className="w-full p-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 min-h-32"
                disabled={isComplete || isProcessing}
            />
            {exampleResponse && (
                <details className="text-sm text-gray-600">
                    <summary className="cursor-pointer text-blue-600 hover:text-blue-700">Show example</summary>
                    <div className="mt-2 p-3 bg-gray-50 rounded-lg border border-gray-200">
                        <p className="font-semibold">Example:</p>
                        <p className="italic">{exampleResponse}</p>
                    </div>
                </details>
            )}
            <button
                onClick={handleSubmit}
                disabled={!userInput.trim() || isProcessing || isComplete}
                className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed shadow-md transition transform hover:scale-[1.02]"
            >
                {isProcessing ? "Checking..." : isComplete ? "Submitted" : "Submit"}
            </button>
            {feedback && (
                <div className={`p-4 rounded-xl ${feedback === 'success' ? 'bg-green-50 border-green-200' : feedback === 'warning' ? 'bg-yellow-50 border-yellow-200' : 'bg-red-50 border-red-200'}`}>
                    <p className={`font-semibold ${feedback === 'success' ? 'text-green-800' : feedback === 'warning' ? 'text-yellow-800' : 'text-red-800'}`}>
                        {feedback === 'success' ? '✓ Correct!' : feedback === 'warning' ? '⚠ Almost!' : '✗ Incorrect'}
                    </p>
                    {feedbackExplanation && (
                        <p className={`mt-2 text-sm ${feedback === 'success' ? 'text-green-700' : feedback === 'warning' ? 'text-yellow-700' : 'text-red-700'}`}>
                            {feedbackExplanation}
                        </p>
                    )}
                </div>
            )}
        </div>
    );
};

// Reading Comprehension Exercise
const ReadingComprehensionExercise = ({ prompt, text, question, options, correctAnswer, highlightVocab, onAnswer, explanation }) => {
    const [selectedAnswer, setSelectedAnswer] = useState(null);
    const [hasAnswered, setHasAnswered] = useState(false);

    const highlightText = (text, vocab) => {
        if (!vocab || vocab.length === 0) return text;
        let highlighted = text;
        vocab.forEach(word => {
            const regex = new RegExp(`\\b${word}\\b`, 'gi');
            highlighted = highlighted.replace(regex, `<mark class="bg-yellow-200 font-semibold">${word}</mark>`);
        });
        return highlighted;
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
                <div 
                    className="text-lg text-gray-800 whitespace-pre-line leading-relaxed"
                    dangerouslySetInnerHTML={{ __html: highlightText(text, highlightVocab) }}
                />
            </div>
            <div className="bg-gray-50 p-4 rounded-xl border border-gray-200">
                <p className="font-semibold text-gray-800 mb-4">{question}</p>
                <div className="space-y-3">
                    {options.map((opt, idx) => (
                        <button
                            key={idx}
                            onClick={() => handleSelect(opt)}
                            disabled={hasAnswered}
                            className={`w-full p-4 text-left rounded-xl border transition-all ${
                                hasAnswered
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
        </div>
    );
};

// ========== PRIORITY 2: FORM FILLING & VOCAB REVIEW ==========

// Form Fill Exercise
const FormFillExercise = ({ prompt, formFields, targetLang, onAnswer, explanation }) => {
    const [formData, setFormData] = useState({});
    const [hasSubmitted, setHasSubmitted] = useState(false);
    const [validationErrors, setValidationErrors] = useState({});

    const handleFieldChange = (fieldLabel, value) => {
        setFormData(prev => ({ ...prev, [fieldLabel]: value }));
        // Clear validation error for this field
        if (validationErrors[fieldLabel]) {
            setValidationErrors(prev => {
                const newErrors = { ...prev };
                delete newErrors[fieldLabel];
                return newErrors;
            });
        }
    };

    const validateField = (field, value) => {
        if (field.required && !value) {
            return `${field.label} is required`;
        }
        if (field.validation === "name" && value) {
            const hasName = value.toLowerCase().includes("mi chiamo") || value.toLowerCase().includes("sono ") || value.toLowerCase().includes("io sono");
            if (!hasName) return "Use 'Mi chiamo [name]' or 'Sono [name]' format";
        }
        if (field.validation === "origin" && value) {
            const hasOrigin = value.toLowerCase().includes("sono di") || value.toLowerCase().includes("di italia") || value.toLowerCase().includes("di francia");
            if (!hasOrigin) return "Use 'Sono di [country]' format";
        }
        return null;
    };

    const handleSubmit = () => {
        const errors = {};
        let allValid = true;

        formFields.forEach(field => {
            const value = formData[field.label] || '';
            const error = validateField(field, value);
            if (error) {
                errors[field.label] = error;
                allValid = false;
            }
        });

        setValidationErrors(errors);
        setHasSubmitted(true);

        if (allValid) {
            // Check if all required fields are filled
            const allRequiredFilled = formFields.every(field => !field.required || formData[field.label]);
            onAnswer(allRequiredFilled ? 'correct' : 'almost', formData, explanation || "Perfect! All fields filled correctly.");
        } else {
            onAnswer('incorrect', formData, "Please fill all required fields correctly.");
        }
    };

    return (
        <div className="space-y-6">
            <h3 className="text-xl font-semibold text-gray-800 text-center">{prompt}</h3>
            <div className="bg-white border-2 border-gray-300 rounded-2xl p-6 space-y-4">
                {formFields.map((field, idx) => (
                    <div key={idx} className="space-y-2">
                        <label className="block text-sm font-medium text-gray-700">
                            {field.label}
                            {field.required && <span className="text-red-500 ml-1">*</span>}
                        </label>
                        {field.type === "text" ? (
                            <input
                                type="text"
                                value={formData[field.label] || ''}
                                onChange={(e) => handleFieldChange(field.label, e.target.value)}
                                placeholder={field.hint || ""}
                                disabled={hasSubmitted}
                                className={`w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 ${
                                    validationErrors[field.label] ? 'border-red-300' : 'border-gray-300'
                                }`}
                            />
                        ) : field.type === "select" ? (
                            <select
                                value={formData[field.label] || ''}
                                onChange={(e) => handleFieldChange(field.label, e.target.value)}
                                disabled={hasSubmitted}
                                className={`w-full p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 ${
                                    validationErrors[field.label] ? 'border-red-300' : 'border-gray-300'
                                }`}
                            >
                                <option value="">Select...</option>
                                {field.options.map((opt, optIdx) => (
                                    <option key={optIdx} value={opt}>{opt}</option>
                                ))}
                            </select>
                        ) : null}
                        {field.hint && !validationErrors[field.label] && (
                            <p className="text-xs text-gray-500">{field.hint}</p>
                        )}
                        {validationErrors[field.label] && (
                            <p className="text-xs text-red-600">{validationErrors[field.label]}</p>
                        )}
                    </div>
                ))}
            </div>
            <button
                onClick={handleSubmit}
                disabled={hasSubmitted}
                className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed shadow-md transition transform hover:scale-[1.02]"
            >
                {hasSubmitted ? "Submitted" : "Submit Form"}
            </button>
        </div>
    );
};

// ========== PRIORITY 3: SELF-ASSESSMENT ==========

// Self Assessment Exercise
const SelfAssessmentExercise = ({ prompt, assessmentType, questions, skipAllowed = true, onAnswer }) => {
    const [responses, setResponses] = useState({});
    const [isComplete, setIsComplete] = useState(false);

    const handleResponse = (questionIndex, response) => {
        setResponses(prev => ({ ...prev, [questionIndex]: response }));
    };

    const handleSubmit = () => {
        setIsComplete(true);
        // Store responses (could be sent to backend for tracking)
        console.log("Self-assessment responses:", responses);
        // Don't call onAnswer with score - just move to next exercise
        // The parent component should handle moving to next exercise
        onAnswer('correct', responses, "Thank you for your self-assessment!");
    };

    const handleSkip = () => {
        onAnswer('correct', {}, "Assessment skipped");
    };

    return (
        <div className="space-y-6">
            <div className="bg-purple-50 rounded-2xl p-6 border-2 border-purple-200">
                <h3 className="text-xl font-semibold text-gray-800 text-center mb-2">{prompt}</h3>
                <p className="text-sm text-gray-600 text-center">This helps you track your progress. No wrong answers!</p>
            </div>
            <div className="space-y-4">
                {questions.map((q, idx) => (
                    <div key={idx} className="bg-white p-4 rounded-xl border border-gray-200">
                        <p className="font-medium text-gray-800 mb-3">{q.question}</p>
                        <div className="space-y-2">
                            {q.options.map((opt, optIdx) => (
                                <button
                                    key={optIdx}
                                    onClick={() => handleResponse(idx, opt)}
                                    className={`w-full p-3 text-left rounded-lg border transition-all ${
                                        responses[idx] === opt
                                            ? 'bg-purple-100 border-purple-300 text-purple-800'
                                            : 'bg-gray-50 border-gray-200 hover:bg-gray-100'
                                    }`}
                                >
                                    {opt}
                                </button>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
            <div className="flex gap-3">
                {skipAllowed && (
                    <button
                        onClick={handleSkip}
                        className="flex-1 py-3 rounded-xl font-semibold text-gray-700 bg-gray-100 hover:bg-gray-200 transition"
                    >
                        Skip
                    </button>
                )}
                <button
                    onClick={handleSubmit}
                    disabled={isComplete || Object.keys(responses).length < questions.length}
                    className="flex-1 py-3 rounded-xl font-bold text-white bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition"
                >
                    {isComplete ? "Submitted" : "Submit"}
                </button>
            </div>
        </div>
    );
};

const MatchExercise = ({ pairs, onAnswer, targetLang }) => {
    const [selectedLeft, setSelectedLeft] = useState(null);
    const [matchedPairs, setMatchedPairs] = useState([]);
    const [failedPairs, setFailedPairs] = useState([]); // Stores items that were matched incorrectly
    const [isLocked, setIsLocked] = useState(false); 

    // Ensure Italian (target language) is on the left, English on the right
    // Data structure: pairs = [[Italian, English], ...] based on a1_1_module_data.py
    // So p[0] is Italian (left), p[1] is English (right)
    const leftSide = useMemo(() => {
        if (!pairs || !Array.isArray(pairs) || pairs.length === 0) return [];
        return pairs.map(p => p[0]).filter(Boolean);
    }, [pairs]); // Italian on left
    const rightSide = useMemo(() => {
        if (!pairs || !Array.isArray(pairs) || pairs.length === 0) return [];
        return pairs.map(p => p[1]).filter(Boolean).sort(() => Math.random() - 0.5);
    }, [pairs]); // English on right

    // Reset state when pairs change (new exercise)
    useEffect(() => {
        setSelectedLeft(null);
        setMatchedPairs([]);
        setFailedPairs([]);
        setIsLocked(false);
    }, [pairs]); 

    // Effect: Check for completion
    useEffect(() => {
        const totalItems = pairs.length * 2;
        const processed = matchedPairs.length + failedPairs.length;

        if (totalItems > 0 && processed === totalItems && !isLocked) {
            setIsLocked(true);
            const isPerfect = failedPairs.length === 0;
            onAnswer(isPerfect ? 'correct' : 'incorrect', isPerfect ? "All matched!" : "Completed with errors.");
        }
    }, [matchedPairs, failedPairs, pairs, isLocked, onAnswer]);

    const handleLeftClick = (item) => { 
        if (isLocked) return; 
        // Allow click only if not already matched AND not failed
        if (!matchedPairs.includes(item) && !failedPairs.includes(item)) { 
            setSelectedLeft(item); 
            speakText(item, targetLang); 
        }
    };

    const handleRightClick = (item) => {
        if (isLocked) return;
        if (matchedPairs.includes(item) || failedPairs.includes(item)) return;

        if (selectedLeft) {
            // Check if selectedLeft (Italian, p[0]) matches item (English, p[1])
            const isMatch = pairs.find(p => p[0] === selectedLeft && p[1] === item);
            
            if (isMatch) {
                setMatchedPairs(prev => [...prev, selectedLeft, item]);
            } else { 
                // Mismatch: Add both to failedPairs, locking them out (red)
                setFailedPairs(prev => [...prev, selectedLeft, item]);
            }
            setSelectedLeft(null);
        }
    };

    return (
        <div className="space-y-4">
             <h3 className="text-xl font-semibold text-gray-800 text-center">Match Pairs</h3>
             <div className="grid grid-cols-2 gap-4">
                <div className="flex flex-col gap-3">
                    {leftSide.map((item, idx) => {
                        const isMatched = matchedPairs.includes(item);
                        const isFailed = failedPairs.includes(item);
                        const isSelected = selectedLeft === item;
                        
                        let baseClass = "p-4 rounded-xl border text-left font-medium transition flex justify-between ";
                        
                        if (isMatched) {
                            baseClass += "bg-green-50 border-green-200 text-green-800 opacity-50 cursor-not-allowed";
                        } else if (isFailed) {
                            baseClass += "bg-red-50 border-red-200 text-red-800 opacity-60 cursor-not-allowed";
                        } else if (isSelected) {
                            baseClass += "bg-blue-50 border-blue-500 text-blue-700 ring-2 ring-blue-200 cursor-pointer";
                        } else {
                            baseClass += "bg-white border-gray-200 hover:bg-gray-50 cursor-pointer";
                        }

                        return (
                            <button 
                                key={idx} 
                                onClick={(e) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    handleLeftClick(item);
                                }} 
                                disabled={isMatched || isFailed || isLocked}
                                className={baseClass}
                                type="button"
                            >
                                {item}
                            </button>
                        );
                    })}
                </div>
                <div className="flex flex-col gap-3">
                    {rightSide.map((item, idx) => {
                        const isMatched = matchedPairs.includes(item);
                        const isFailed = failedPairs.includes(item);
                        
                        let baseClass = "p-4 rounded-xl border text-left font-medium transition ";
                        if (isMatched) {
                            baseClass += "bg-green-50 border-green-200 text-green-800 opacity-50 cursor-not-allowed";
                        } else if (isFailed) {
                            baseClass += "bg-red-50 border-red-200 text-red-800 opacity-60 cursor-not-allowed";
                        } else {
                            baseClass += "bg-white border-gray-200 hover:bg-gray-50 cursor-pointer";
                        }

                        return (
                            <button 
                                key={idx} 
                                onClick={(e) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    handleRightClick(item);
                                }} 
                                disabled={isMatched || isFailed || isLocked}
                                className={baseClass}
                                type="button"
                            >
                                {item}
                            </button>
                        );
                    })}
                </div>
            </div>
        </div>
    );
};

const CelebrationScreen = ({ score, total, onContinue, isSelfAssessment = false }) => {
    const [isStarting, setIsStarting] = useState(false);
    const handleClick = () => { setIsStarting(true); onContinue(); };

    // For self-assessment lessons, show a different message
    if (isSelfAssessment) {
        return (
            <div className="text-center space-y-8 py-10 animate-fade-in">
                <div className="text-6xl">🎉</div>
                <h2 className="text-4xl font-extrabold text-gray-800">Lesson Complete!</h2>
                <div className="bg-white p-8 rounded-3xl shadow-xl border border-gray-100 max-w-sm mx-auto">
                    <p className="text-lg text-gray-700 mb-4">Thanks for that! We'll adjust your learning to your level.</p>
                </div>
                <button onClick={handleClick} disabled={isStarting} className={`px-10 py-4 text-white text-xl font-bold rounded-2xl shadow-lg transition transform hover:scale-105 ${isStarting ? 'bg-gray-400 cursor-not-allowed' : 'bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700'}`}>
                    {isStarting ? <span className="flex items-center gap-2"><Loader2 className="w-6 h-6 animate-spin" /> Loading...</span> : "Continue to Next Lesson"}
                </button>
            </div>
        );
    }

    return (
        <div className="text-center space-y-8 py-10 animate-fade-in">
            <div className="text-6xl">🎉</div>
            <h2 className="text-4xl font-extrabold text-gray-800">Lesson Complete!</h2>
            <div className="bg-white p-8 rounded-3xl shadow-xl border border-gray-100 max-w-sm mx-auto">
                <p className="text-gray-500 mb-2">You scored</p>
                <p className="text-6xl font-bold text-[#4CAF50]">{score}/{total}</p>
                <p className="text-sm text-gray-400 mt-4">Vocabulary updated!</p>
            </div>
            <button onClick={handleClick} disabled={isStarting} className={`px-10 py-4 text-white text-xl font-bold rounded-2xl shadow-lg transition transform hover:scale-105 ${isStarting ? 'bg-gray-400 cursor-not-allowed' : 'bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700'}`}>
                {isStarting ? <span className="flex items-center gap-2"><Loader2 className="w-6 h-6 animate-spin" /> Loading...</span> : "Continue to Next Lesson"}
            </button>
        </div>
    );
};

const ExerciseView = ({ exercises, onComplete, targetLang, userProfile }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const [feedback, setFeedback] = useState(null);
    const [score, setScore] = useState(0);
    const [showCelebration, setShowCelebration] = useState(false);
    const hasAutoPlayedRef = useRef(false);

    if (!exercises || exercises.length === 0) return <div className="p-6 text-center text-gray-500">No exercises available.</div>;
    const currentExercise = exercises[currentIndex];
    const isLast = currentIndex === exercises.length - 1;

    // Auto-play audio for info_card and flashcard exercises
    useEffect(() => {
        // Reset the ref when exercise index changes
        hasAutoPlayedRef.current = false;
        
        // Use a small delay to ensure the component has fully rendered
        const timer = setTimeout(() => {
            if (currentExercise && (currentExercise.type === 'info_card' || currentExercise.type === 'flashcard')) {
                // Skip section headers (Topic cards)
                const isSectionHeader = currentExercise.prompt === "Topic" || currentExercise.prompt === "Next Group" || currentExercise.prompt === "Final Number";
                if (!isSectionHeader && currentExercise.correct_answer && !hasAutoPlayedRef.current) {
                    hasAutoPlayedRef.current = true;
                    console.log(`[Auto-play] Playing: "${currentExercise.correct_answer}" for exercise type: ${currentExercise.type}, index: ${currentIndex}`);
                    speakText(currentExercise.correct_answer, targetLang).catch(err => {
                        console.error("[Auto-play] Failed to play audio:", err);
                    });
                }
            }
        }, 100); // Minimal delay for instant auto-play
        
        return () => clearTimeout(timer);
    }, [currentIndex, targetLang]); // Depend on currentIndex and targetLang only

    const handleAnswer = (resultStatus, userAnswer, customExplanation = null) => {
        // resultStatus can be 'correct', 'almost', or 'incorrect' (or boolean for backward compatibility)
        // Handle backward compatibility: convert boolean to string
        if (typeof resultStatus === 'boolean') {
            resultStatus = resultStatus ? 'correct' : 'incorrect';
        }
        
        const isCorrect = resultStatus === 'correct';
        const isAlmost = resultStatus === 'almost';
        
        if (isCorrect) setScore(s => s + 1);
        // Optionally give partial credit for "almost" - uncomment if desired
        // if (isAlmost) setScore(s => s + 0.5);
        
        // Generate detailed feedback messages
        let feedbackMsg = '';
        let explanationText = '';
        let feedbackType = 'error'; // default
        
        // Use custom explanation if provided (from MiniPromptExercise)
        if (customExplanation) {
            if (isCorrect) {
                feedbackMsg = 'Correct!';
                feedbackType = 'success';
            } else if (isAlmost) {
                feedbackMsg = 'Almost!';
                feedbackType = 'warning';
            } else {
                feedbackMsg = 'Incorrect.';
                feedbackType = 'error';
            }
            explanationText = customExplanation;
        } else if (isCorrect) {
            // When correct: Explain why it's correct
            feedbackMsg = 'Correct!';
            feedbackType = 'success';
            // Generate specific feedback based on exercise type
            if (currentExercise.type === 'unscramble') {
                explanationText = `Great job! You put the words together perfectly to make "${currentExercise.correct_answer}". You're really getting the hang of how Italian sentences are structured - that's awesome!`;
            } else if (currentExercise.type === 'match') {
                explanationText = "Perfect! You matched everything correctly! I can see you're really understanding what these Italian words mean - keep it up!";
            } else if (currentExercise.type === 'gender_categorize') {
                explanationText = "Excellent! You correctly identified the gender of all nouns. Remember: -o/-è endings indicate masculine (maschile) nouns, while -a endings indicate feminine (femminile) nouns. This pattern will help you with many Italian nouns!";
            } else if (currentExercise.type === 'multiple_choice' || currentExercise.type === 'fill_blank') {
                explanationText = `Nice work! "${currentExercise.correct_answer}" is exactly right. ${currentExercise.explanation && !currentExercise.explanation.toLowerCase().includes('test') ? currentExercise.explanation : "You're doing great!"}`;
            } else {
                explanationText = currentExercise.explanation || 'Well done!';
            }
        } else if (isAlmost) {
            // When almost: Explain what's right and what needs adjustment
            feedbackMsg = 'Almost!';
            feedbackType = 'warning';
            // Generate almost feedback
            if (currentExercise.type === 'unscramble') {
                explanationText = `You're really close! The correct sentence is "${currentExercise.correct_answer}". You had most of it right - just a small adjustment needed. Keep going!`;
            } else if (currentExercise.type === 'match') {
                explanationText = "You matched most pairs correctly! Just a couple need to be adjusted. Think about the meanings and you'll get it!";
            } else {
                explanationText = currentExercise.explanation || "You're almost there! Just a small adjustment needed.";
            }
        } else {
            // When incorrect: Show correct answer and explain why their answer was wrong
            feedbackMsg = 'Incorrect.';
            feedbackType = 'error';
            
            // Check for common mistakes first (Priority 3 enhancement)
            let foundCommonMistake = false;
            if (currentExercise.common_mistakes && Array.isArray(currentExercise.common_mistakes)) {
                const userAnswerLower = (userAnswer || '').toLowerCase();
                for (const mistake of currentExercise.common_mistakes) {
                    if (mistake.pattern && userAnswerLower.includes(mistake.pattern.toLowerCase())) {
                        explanationText = mistake.explanation || currentExercise.explanation || 'Please try again.';
                        foundCommonMistake = true;
                        break;
                    }
                }
            }
            
            // If no common mistake found, use default feedback
            if (!foundCommonMistake) {
                if (currentExercise.type === 'match') {
                    explanationText = "Not quite - some pairs need to be matched differently. Think about what each Italian word means and find its English partner. You'll get it!";
                } else if (currentExercise.type === 'gender_categorize') {
                    explanationText = "Not quite - some words are in the wrong column. Remember: words ending in -o or -è are usually masculine (maschile), and words ending in -a are usually feminine (femminile). Check each word's ending to help you decide!";
                } else if (currentExercise.type === 'unscramble') {
                    explanationText = `The correct sentence is "${currentExercise.correct_answer}". Italian has a specific word order that can be tricky at first - subjects, verbs, and objects go in certain places. Take a look at the correct order and see if you can spot the pattern. You're learning!`;
                } else if (currentExercise.type === 'multiple_choice' || currentExercise.type === 'fill_blank') {
                    explanationText = `The correct answer is "${currentExercise.correct_answer}". ${currentExercise.explanation ? 'Think about why this one works better - you are getting there!' : "Don't worry, let's review this together!"}`;
                } else {
                    explanationText = currentExercise.explanation || 'Please try again.';
                }
            }
        }
        
        setFeedback({ type: feedbackType, msg: feedbackMsg, explanation: explanationText });
        if(isCorrect && currentExercise.type !== 'flashcard') speakText("Correct", "en"); 
    };
    
    const handleSimpleNext = () => {
        setFeedback(null);
        if (isLast) setShowCelebration(true);
        else setCurrentIndex(c => c + 1);
    };

    const handleNext = () => { 
        setFeedback(null); 
        if (isLast) setShowCelebration(true); 
        else setCurrentIndex(c => c + 1); 
    };

    if (showCelebration) {
        const gradedQuestions = exercises.filter(e => 
            e.type !== 'info_card' && 
            e.type !== 'flashcard' && 
            e.type !== 'boss_fight' && 
            e.type !== 'self_assessment'
        ).length;
        // Check if this is a self-assessment lesson (all exercises are self_assessment)
        const isSelfAssessmentLesson = exercises.length > 0 && exercises.every(e => e.type === 'self_assessment');
        return <CelebrationScreen score={score} total={gradedQuestions} onContinue={() => onComplete(score, gradedQuestions)} isSelfAssessment={isSelfAssessmentLesson} />;
    }

    const renderExerciseBody = () => {
        switch (currentExercise.type) {
            case 'info_card': 
                // Section Header Rendering
                const isSectionHeader = currentExercise.prompt === "Topic" || currentExercise.prompt === "Next Group" || currentExercise.prompt === "Final Number";
                if (isSectionHeader) {
                     return (
                        <div className="space-y-6 text-center py-10">
                            <h3 className="text-3xl font-extrabold text-gray-800">{currentExercise.correct_answer}</h3>
                            <p className="text-xl text-gray-600">{currentExercise.explanation}</p>
                            <button onClick={handleSimpleNext} className="mt-6 px-8 py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 shadow-md transition transform hover:scale-[1.02]">Start</button>
                        </div>
                     );
                }
                // Cultural note enhancement
                const isCulturalNote = currentExercise.cultural_note === true;
                return (
                    <div className="space-y-6 text-center">
                        <h3 className="text-gray-500 font-medium text-lg">{currentExercise.prompt}</h3>
                        <div className={`py-6 rounded-2xl border ${
                            isCulturalNote 
                                ? 'bg-yellow-50 border-yellow-200' 
                                : 'bg-blue-50 border-blue-100'
                        }`}>
                            {isCulturalNote && (
                                <div className="mb-3 flex items-center justify-center gap-2">
                                    <span className="text-2xl">🌍</span>
                                    <span className="text-sm font-semibold text-yellow-800">Cultural Note</span>
                                </div>
                            )}
                            <p className={`text-4xl font-extrabold mb-2 ${
                                isCulturalNote ? 'text-yellow-800' : 'text-blue-800'
                            }`}>{currentExercise.correct_answer}</p>
                            <p className={`text-xl mb-4 whitespace-pre-line ${
                                isCulturalNote ? 'text-yellow-700' : 'text-blue-600'
                            }`}>{currentExercise.explanation}</p>
                            {currentExercise.sub_text && <p className="text-sm text-gray-500 italic">{currentExercise.sub_text}</p>}
                        </div>
                        {currentExercise.audio_url && (
                            <button onClick={() => speakText(currentExercise.correct_answer, targetLang)} className="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition"><Volume2 size={24} /> Replay</button>
                        )}
                        <button onClick={handleSimpleNext} className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 shadow-md transition transform hover:scale-[1.02] mt-4">Continue</button>
                    </div>
                );
            case 'listening_comprehension':
                return <ListeningComprehensionExercise 
                    prompt={currentExercise.prompt}
                    audioUrl={currentExercise.audio_url}
                    audioText={currentExercise.audio_text}
                    options={currentExercise.options}
                    correctAnswer={currentExercise.correct_answer}
                    allowReplay={currentExercise.allow_replay !== false}
                    maxPlays={currentExercise.max_plays || 3}
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                    targetLang={targetLang}
                />;
            case 'free_writing':
                return <FreeWritingExercise 
                    prompt={currentExercise.prompt}
                    context={currentExercise.context}
                    task={currentExercise.task}
                    targetLang={targetLang}
                    requiredElements={currentExercise.required_elements}
                    exampleResponse={currentExercise.example_response}
                    validationMode={currentExercise.validation_mode || "ai"}
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                />;
            case 'reading_comprehension':
                return <ReadingComprehensionExercise 
                    prompt={currentExercise.prompt}
                    text={currentExercise.text}
                    question={currentExercise.question}
                    options={currentExercise.options}
                    correctAnswer={currentExercise.correct_answer}
                    highlightVocab={currentExercise.highlight_vocab}
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                />;
            case 'form_fill':
                return <FormFillExercise 
                    prompt={currentExercise.prompt}
                    formFields={currentExercise.form_fields}
                    targetLang={targetLang}
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                />;
            case 'self_assessment':
                return <SelfAssessmentExercise 
                    prompt={currentExercise.prompt}
                    assessmentType={currentExercise.assessment_type}
                    questions={currentExercise.questions}
                    skipAllowed={currentExercise.skip_allowed !== false}
                    onAnswer={(responses, msg, explanation) => {
                        // Self-assessment doesn't count toward score
                        handleSimpleNext();
                    }}
                />;
            case 'conversation':
                return <ConversationExercise dialogue={currentExercise.dialogue} options={currentExercise.options} onAnswer={handleAnswer} />;
            case 'arrange':
                return <ArrangeExercise prompt={currentExercise.prompt} options={currentExercise.options} correctAnswer={currentExercise.correct_answer} onAnswer={handleAnswer} />;
            case 'unscramble':
                return <UnscrambleExercise prompt={currentExercise.prompt} blocks={currentExercise.blocks} correctAnswer={currentExercise.correct_answer} onAnswer={handleAnswer} />;
            case 'match':
                return <MatchExercise pairs={currentExercise.pairs} targetLang={targetLang} onAnswer={handleAnswer} />;
            case 'gender_categorize':
                return <GenderCategorizeExercise 
                    prompt={currentExercise.prompt} 
                    words={currentExercise.words} 
                    correctAnswers={currentExercise.correct_answers} 
                    onAnswer={handleAnswer} 
                />;
            case 'echo_chamber':
                return <EchoChamberExercise 
                    prompt={currentExercise.prompt} 
                    targetPhrase={currentExercise.target_phrase} 
                    targetLang={targetLang} 
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                    onComplete={handleSimpleNext}
                />;
            case 'mini_prompt':
                return <MiniPromptExercise 
                    prompt={currentExercise.prompt}
                    context={currentExercise.context}
                    task={currentExercise.task}
                    targetLang={targetLang}
                    nativeLang={userProfile?.native_language || "en"}
                    onAnswer={handleAnswer}
                    explanation={currentExercise.explanation}
                />;
            case 'flashcard':
                return (
                     <div className="space-y-8 text-center">
                         <h3 className="text-gray-500 font-medium text-lg">{currentExercise.prompt}</h3>
                         <div className="py-6">
                             <p className="text-5xl font-extrabold text-blue-600 mb-6">{currentExercise.correct_answer}</p>
                             <button onClick={() => speakText(currentExercise.correct_answer, targetLang)} className="inline-flex items-center gap-2 px-6 py-3 bg-blue-50 text-blue-700 rounded-full hover:bg-blue-100 transition shadow-sm border border-blue-200"><Volume2 size={24} /> Replay</button>
                         </div>
                         <div className="pt-4"><button onClick={handleSimpleNext} className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 shadow-md transition transform hover:scale-[1.02]">{isLast ? "Finish Exercises" : "Continue"}</button></div>
                     </div>
                );
            case 'boss_fight':
                // Get round information to display both scenarios
                const round1 = currentExercise.conversation_flow?.find(r => r.round === 1);
                const round2 = currentExercise.conversation_flow?.find(r => r.round === 2);
                return (
                    <div className="space-y-6 text-center">
                        <div className="bg-gradient-to-br from-purple-50 to-blue-50 p-8 rounded-2xl border-2 border-purple-200">
                            <h3 className="text-2xl font-bold text-gray-800 mb-4">⚔️ Boss Fight</h3>
                            {currentExercise.explanation && (
                                <p className="text-sm text-gray-600 italic mb-6">{currentExercise.explanation}</p>
                            )}
                            <div className="bg-white/60 p-4 rounded-lg border border-purple-200">
                                <p className="text-sm font-semibold text-purple-800 mb-2">Your Mission:</p>
                                <p className="text-sm text-gray-700 mb-2">
                                    Complete <strong>2 rounds</strong> of conversations using the greetings you've learned:
                                </p>
                                <ul className="text-sm text-gray-700 text-left space-y-1 mt-2">
                                    <li className="flex items-start">
                                        <span className="font-semibold mr-2">Round 1:</span>
                                        <span className="flex-1">{round1?.round_description || "Have a casual conversation with your neighbor Signora Rossi"}</span>
                                    </li>
                                    <li className="flex items-start">
                                        <span className="font-semibold mr-2">Round 2:</span>
                                        <span className="flex-1">{round2?.round_description || "Have a formal conversation with Professor Bianchi"}</span>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <button 
                            onClick={() => {
                                // Don't call handleAnswer - it triggers the "Correct" sound
                                // Just transition directly to tutor mode
                                setTimeout(() => {
                                    onComplete(0, 1); // Pass minimal score to trigger handleExercisesComplete
                                }, 100);
                            }}
                            className="w-full py-4 rounded-2xl font-bold text-white bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-700 hover:to-blue-700 shadow-lg transition transform hover:scale-[1.02]"
                        >
                            Start Boss Fight ⚔️
                        </button>
                    </div>
                );
            default: // Multiple choice, fill blank (if not handled above)
                return (
                    <div className="space-y-3">
                        <h3 className="text-xl font-semibold text-gray-800 mb-6">{currentExercise.prompt}</h3>
                        {currentExercise.options.map((opt, idx) => (
                            <button 
                                key={idx} 
                                onClick={() => { 
                                    if(!feedback) { 
                                        const isC = opt === currentExercise.correct_answer; 
                                        let feedbackMsg = '';
                                        let explanationText = '';
                                        
                                        if (isC) {
                                            feedbackMsg = 'Correct!';
                                            if (currentExercise.type === 'multiple_choice' || currentExercise.type === 'fill_blank') {
                                                explanationText = `"${opt}" is exactly right! ${currentExercise.explanation && !currentExercise.explanation.toLowerCase().includes('test') ? currentExercise.explanation : "You're doing great!"}`;
                                            } else {
                                                explanationText = currentExercise.explanation || 'Well done!';
                                            }
                                        } else {
                                            feedbackMsg = 'Incorrect.';
                                            if (currentExercise.correct_answer) {
                                                explanationText = `The correct answer is "${currentExercise.correct_answer}". ${currentExercise.explanation ? "Think about why this one works better - you're getting there!" : "Don't worry, let's review this together!"}`;
                                            } else {
                                                explanationText = currentExercise.explanation || 'Please try again.';
                                            }
                                        }
                                        setFeedback(isC ? { type:'success', msg: feedbackMsg, explanation: explanationText} : {type:'error', msg: feedbackMsg, explanation: explanationText}); 
                                        if(isC) setScore(s=>s+1); 
                                    } 
                                }} 
                                className={`w-full p-4 text-left rounded-xl border transition-all ${feedback ? 'cursor-default' : 'hover:bg-gray-50'}`} 
                                disabled={!!feedback} // LOCKED BY GLOBAL FEEDBACK STATE
                            >
                                {opt}
                            </button>
                        ))}
                    </div>
                );
        }
    };

    // Check for extension activity
    const isExtension = currentExercise.extension === true;
    const isOptional = currentExercise.optional === true;

    return (
        <div className="max-w-2xl mx-auto bg-white p-6 rounded-2xl shadow-lg mt-4">
            <div className="w-full bg-gray-200 rounded-full h-2 mb-6"><div className="bg-[#4CAF50] h-2 rounded-full transition-all duration-500" style={{ width: `${((currentIndex) / exercises.length) * 100}%` }}></div></div>
            {isExtension && (
                <div className="mb-4 px-4 py-3 bg-purple-100 border border-purple-300 rounded-lg flex items-center justify-between">
                    <span className="text-purple-800 font-semibold flex items-center gap-2">
                        <span>🌟</span>
                        <span>Optional Challenge</span>
                    </span>
                    {isOptional && (
                        <button 
                            onClick={handleSimpleNext} 
                            className="text-purple-600 hover:text-purple-700 underline text-sm font-medium"
                        >
                            Skip
                        </button>
                    )}
                </div>
            )}
            {renderExerciseBody()}
            {feedback && (
                <div className="mt-6 animate-fade-in">
                    <div className={`p-4 rounded-xl mb-4 flex items-center ${
                        feedback.type === 'success' 
                            ? 'bg-green-50 text-green-800 border border-green-100' 
                            : feedback.type === 'warning'
                            ? 'bg-amber-50 text-amber-800 border border-amber-200'
                            : 'bg-red-50 text-red-800 border border-red-100'
                    }`}>
                        {feedback.type === 'success' ? <CheckCircle className="mr-3" /> : 
                         feedback.type === 'warning' ? <AlertCircle className="mr-3" /> : 
                         <AlertCircle className="mr-3" />}
                        <div>
                            <p className="font-bold">{feedback.msg}</p>
                            {feedback.explanation && <p className="text-sm mt-1">{feedback.explanation}</p>}
                        </div>
                    </div>
                    <button onClick={handleNext} className="w-full py-3 rounded-xl font-bold text-white bg-blue-600 hover:bg-blue-700 shadow-md transition">{isLast ? "Finish" : "Continue"}</button>
                </div>
            )}
        </div>
    );
};

const LessonDetailView = ({ lesson, onStartChat, onBack, targetLang, t, onCompleteExercises, userProfile }) => {
    const [step, setStep] = useState('overview');
    return (
        <div className="p-4 max-w-4xl mx-auto h-full flex flex-col">
            <button onClick={onBack} className="flex items-center text-gray-500 hover:text-gray-800 mb-4"><ArrowLeft size={20} className="mr-1" /> Back</button>
            {step === 'overview' && (
                <>
                    <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 mb-6"><h1 className="text-3xl font-extrabold text-gray-800 mb-2">{lesson.title}</h1><p className="text-gray-600">{lesson.goal}</p></div>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                        {lesson.vocabulary && lesson.vocabulary.map((vocab, idx) => {
                            // Handle both string arrays and vocabulary objects
                            let vocabItem;
                            if (typeof vocab === 'string') {
                                // Convert string to vocabulary object
                                vocabItem = { term: vocab, translation: "" };
                            } else {
                                vocabItem = vocab;
                            }
                            
                            // UPDATED: Render Header or Card based on is_header flag
                            if (vocabItem.is_header) {
                                return (
                                    <div key={idx} className="col-span-full mt-6 mb-2">
                                        <h3 className="text-lg font-bold text-gray-700 border-b pb-2 uppercase tracking-wider">{vocabItem.term.replace(/---/g, '').trim()}</h3>
                                    </div>
                                );
                            } else {
                                return (
                                    <div key={idx} className="bg-white p-4 rounded-xl border border-gray-200 flex justify-between items-center hover:shadow-md transition">
                                        <div>
                                            <p className="text-lg font-bold text-gray-800">{vocabItem.term}</p>
                                            {vocabItem.translation && <p className="text-sm text-[#4CAF50]">{vocabItem.translation}</p>}
                                        </div>
                                        <button onClick={() => speakText(vocabItem.term, targetLang)} className="p-2 text-gray-400 hover:text-blue-500 hover:bg-blue-50 rounded-full transition"><Volume2 size={20} /></button>
                                    </div>
                                );
                            }
                        })}
                    </div>
                    <div className="text-center mt-8"><button onClick={() => setStep('exercises')} className="px-8 py-4 bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white text-lg font-bold rounded-2xl shadow-lg transition transform hover:scale-[1.02]">{t('exercises')}</button></div>
                </>
            )}
            {step === 'exercises' && (
                <ExerciseView 
                    exercises={lesson.exercises} 
                    targetLang={targetLang} 
                    userProfile={userProfile}
                    onComplete={(score, total) => {
                        onCompleteExercises(score, total); 
                    }} 
                />
            )}
        </div>
    );
};

const CurriculumView = React.memo(({ onSelectLesson, userProfile, t }) => {
    const [modules, setModules] = useState([]);
    const [lessons, setLessons] = useState([]);
    const [loading, setLoading] = useState(true);
    const [expandedModules, setExpandedModules] = useState({});
    
    useEffect(() => {
        // Try to fetch modules first (hierarchical structure)
        axios.get(`${API}/modules`, { params: { target_lang: userProfile.target_language, native_lang: userProfile.native_language }, timeout: 15000 })
            .then(res => {
                const data = res.data;
                // Check if response contains modules with nested lessons
                if (data.length > 0 && data[0].type === "module" && data[0].lessons) {
                    setModules(data);
                    setLoading(false);
                } else {
                    // Fallback to /lessons endpoint for flat structure
                    axios.get(`${API}/lessons`, { params: { target_lang: userProfile.target_language, native_lang: userProfile.native_language }, timeout: 15000 })
                        .then(res => { setLessons(res.data); setLoading(false); })
                        .catch(e => { setLoading(false); });
                }
            })
            .catch(err => {
                // Fallback to /lessons endpoint
                axios.get(`${API}/lessons`, { params: { target_lang: userProfile.target_language, native_lang: userProfile.native_language }, timeout: 15000 })
                    .then(res => { setLessons(res.data); setLoading(false); })
                    .catch(e => { setLoading(false); });
            });
    }, [userProfile]);

    const isComplete = (lessonId) => {
        if (!userProfile.progress) return false;
        return userProfile.progress.some(p => 
            p.module_id === lessonId && 
            p.target_lang === userProfile.target_language
        );
    };

    const isLessonComplete = (lessonId) => {
        if (!userProfile.progress) return false;
        return userProfile.progress.some(p => 
            (p.module_id === lessonId || p.lesson_id === lessonId) && 
            p.target_lang === userProfile.target_language
        );
    };

    const toggleModule = (moduleId) => {
        setExpandedModules(prev => ({
            ...prev,
            [moduleId]: !prev[moduleId]
        }));
    };

    const canAccessBossFight = (module) => {
        // Boss fight is unlocked if all regular lessons (non-boss) are complete
        if (!module.lessons) return false;
        const regularLessons = module.lessons.filter(l => l.type !== "boss_fight");
        return regularLessons.every(lesson => isLessonComplete(lesson.lesson_id));
    };

    if (loading) return <div className="p-10 text-center text-gray-500"><Loader2 className="w-8 h-8 animate-spin mx-auto mb-2" />Loading...</div>;
    
    // Show "Content Coming Soon" for non-Italian languages - check this FIRST
    if (userProfile.target_language !== 'it') {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-6">{t('lessons')} (A1)</h2>
                <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-12 max-w-2xl mx-auto">
                    <GraduationCap size={64} className="text-gray-300 mx-auto mb-4" />
                    <h3 className="text-xl font-bold text-gray-800 mb-3">Content Coming Soon</h3>
                    <p className="text-gray-600 mb-2">
                        Currently, structured lessons are only available for <strong>Italian</strong>.
                    </p>
                    <p className="text-gray-600">
                        We're working on adding content for {CORE_LANGUAGES.find(l => l.code === userProfile.target_language)?.name || 'your selected language'}. 
                        Check back soon!
                    </p>
                </div>
            </div>
        );
    }
    
    // Render hierarchical modules (only reached for Italian)
    if (modules.length > 0) {
        return (
            <div className="p-4 space-y-4">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">{t('lessons')} (A1)</h2>
                <div className="space-y-3">
                    {modules.map((module) => {
                        const isExpanded = expandedModules[module._id];
                        const moduleCompleted = module.lessons && module.lessons.every(lesson => isLessonComplete(lesson.lesson_id));
                        
                        return (
                            <div key={module._id} className="bg-white rounded-2xl border shadow-sm overflow-hidden">
                                {/* Module Header */}
                                <div 
                                    onClick={() => toggleModule(module._id)}
                                    className={`flex items-center p-4 cursor-pointer hover:bg-gray-50 transition ${moduleCompleted ? 'border-green-200 bg-green-50' : 'border-gray-100'}`}
                                >
                                    <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-4 font-bold ${moduleCompleted ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-400'}`}>
                                        {moduleCompleted ? <CheckCircle size={20} /> : <ChevronDown size={20} className={isExpanded ? 'rotate-180' : ''} />}
                                    </div>
                                    <div className="flex-grow">
                                        <h3 className="font-bold text-gray-800">{module.title}</h3>
                                        <p className="text-xs text-gray-500">{module.goal}</p>
                                    </div>
                                    <ChevronDown className={`text-gray-300 transition-transform ${isExpanded ? 'rotate-180' : ''}`} />
                                </div>
                                
                                {/* Nested Lessons */}
                                {isExpanded && module.lessons && (
                                    <div className="border-t border-gray-100 bg-gray-50">
                                        {module.lessons.map((lesson, idx) => {
                                            const lessonCompleted = isLessonComplete(lesson.lesson_id);
                                            const isBossFight = lesson.type === "boss_fight";
                                            const isLocked = isBossFight && !canAccessBossFight(module);
                                            
                                            return (
                                                <div
                                                    key={lesson.lesson_id}
                                                    onClick={() => !isLocked && onSelectLesson(lesson)}
                                                    className={`flex items-center p-4 border-b border-gray-100 last:border-b-0 cursor-pointer hover:bg-white transition ${
                                                        isLocked ? 'opacity-50 cursor-not-allowed' : ''
                                                    } ${lessonCompleted ? 'bg-green-50' : ''}`}
                                                >
                                                    <div className={`w-8 h-8 rounded-full flex items-center justify-center mr-3 font-bold text-sm ${
                                                        lessonCompleted ? 'bg-green-500 text-white' : isLocked ? 'bg-gray-300' : 'bg-blue-100 text-blue-600'
                                                    }`}>
                                                        {lessonCompleted ? <CheckCircle size={16} /> : isLocked ? <Lock size={16} /> : idx + 1}
                                                    </div>
                                                    <div className="flex-grow">
                                                        <h4 className="font-semibold text-gray-800">{lesson.title}</h4>
                                                        {lesson.focus && <p className="text-xs text-gray-500">{lesson.focus}</p>}
                                                    </div>
                                                    {!isLocked && <ChevronRight className="text-gray-300" size={18} />}
                                                </div>
                                            );
                                        })}
                                    </div>
                                )}
                            </div>
                        );
                    })}
                </div>
            </div>
        );
    }
    
    // Fallback: Render flat lessons (backward compatibility) - only for Italian
    if (lessons.length === 0) {
        return (
            <div className="p-10 text-center">
                <h2 className="text-2xl font-bold text-gray-800 border-b pb-2 mb-6">{t('lessons')} (A1)</h2>
                <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-12 max-w-2xl mx-auto">
                    <GraduationCap size={64} className="text-gray-300 mx-auto mb-4" />
                    <h3 className="text-xl font-bold text-gray-800 mb-3">No Lessons Available</h3>
                    <p className="text-gray-600">
                        There are no lessons available at this time.
                    </p>
                </div>
            </div>
        );
    }
    
    return (
        <div className="p-4 space-y-4">
            <h2 className="text-2xl font-bold text-gray-800 border-b pb-2">{t('lessons')} (A1)</h2>
            <div className="space-y-3">{lessons.map((module, index) => {
                const completed = isComplete(module._id);
                return (
                    <div key={module._id} onClick={() => onSelectLesson(module)} className={`flex items-center p-4 bg-white rounded-2xl border shadow-sm cursor-pointer hover:shadow-md transition group ${completed ? 'border-green-200 bg-green-50' : 'border-gray-100'}`}>
                        <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-4 font-bold ${completed ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-400'}`}>
                            {completed ? <CheckCircle size={20} /> : index + 1}
                        </div>
                        <div className="flex-grow">
                            <h3 className="font-bold text-gray-800 group-hover:text-[#4CAF50] transition">{module.title}</h3>
                            <p className="text-xs text-gray-500">{module.goal}</p>
                        </div>
                        <ChevronRight className="text-gray-300 group-hover:text-[#4CAF50]" />
                    </div>
                );
            })}</div>
        </div>
    );
});

const BossFightHints = ({ activeLesson, chatHistory, currentTurn, currentRound }) => {
    if (!activeLesson || activeLesson.type !== "boss_fight") return null;
    
    // Extract conversation flow from boss fight exercise
    const bossExercise = activeLesson.exercises?.find(ex => ex.type === "boss_fight");
    if (!bossExercise || !bossExercise.conversation_flow) return null;
    
    // Calculate round and turn within round
    // ALWAYS prioritize currentRound prop - it's the source of truth from backend
    // Only use fallback calculation if currentRound is explicitly undefined/null
    // Round 1 = turns 1-4, Round 2 = turns 5-8
    let round = currentRound;
    if (round === undefined || round === null) {
        // Only calculate from currentTurn if currentRound is truly not set
        if (currentTurn) {
            round = Math.floor((currentTurn - 1) / 4) + 1;
        } else {
            round = 1; // Default to round 1
        }
    }
    // Ensure round is valid (1 or 2) - but don't override if currentRound was explicitly set
    const validRound = Math.max(1, Math.min(2, round || 1));
    const turnInRound = currentTurn ? ((currentTurn - 1) % 4) + 1 : 1;
    
    // Get current round data using validRound
    const currentRoundData = bossExercise.conversation_flow.find(r => r.round === validRound);
    if (!currentRoundData) {
        console.warn(`[BossFightHints] Round ${validRound} not found. Available rounds:`, bossExercise.conversation_flow.map(r => r.round));
        return null;
    }
    
    // Get current turn's data
    const currentTurnData = currentRoundData.turns?.find(t => t.turn === turnInRound);
    if (!currentTurnData || !currentTurnData.required_words) {
        console.warn(`[BossFightHints] Turn ${turnInRound} not found in round ${validRound}`);
        return null;
    }
    
    // Use hints array for display (filtered by formality), but required_words for validation
    // Always prefer hints array if it exists, as it's filtered for formality
    const hintWords = currentTurnData.hints && currentTurnData.hints.length > 0 
        ? currentTurnData.hints 
        : currentTurnData.required_words;
    const requiredWords = currentTurnData.required_words;
    const roundName = currentRoundData.round_name || `Round ${validRound}`;
    
    // Debug logging for round 2, turn 4
    if (validRound === 2 && turnInRound === 4) {
        console.log(`[BossFightHints] Round 2, Turn 4 - hints:`, hintWords, 'required_words:', requiredWords);
    }
    
    // Only check words used in the CURRENT turn's user messages
    const userMessages = chatHistory.filter(msg => msg.role === 'user');
    
    // Determine which user message(s) belong to the current turn
    // For round-based: turn 1-4 = round 1, turn 5-8 = round 2
    const currentTurnUserMessages = [];
    if (currentTurn >= 1 && userMessages.length >= 1 && currentTurn <= userMessages.length) {
        currentTurnUserMessages.push(userMessages[currentTurn - 1].text.toLowerCase());
    }
    
    const currentTurnText = currentTurnUserMessages.join(' ').toLowerCase();
    
    // Determine if we need ALL words (AND) or ANY word (OR) based on user_requirement
    const userRequirement = currentTurnData.user_requirement || "";
    const requiresAll = userRequirement.toLowerCase().includes(" and ");
    
    // Check which required words were used (for validation)
    const usedRequiredWords = requiredWords.filter(word => {
        const wordLower = word.toLowerCase();
        // Handle multi-word phrases like "Come stai?"
        if (wordLower.includes(' ')) {
            return currentTurnText.includes(wordLower);
        }
        // Handle single words - check for word boundaries
        return new RegExp(`\\b${wordLower}\\b`).test(currentTurnText);
    });
    
    // Determine if requirement is met
    const requirementMet = requiresAll 
        ? usedRequiredWords.length === requiredWords.length
        : usedRequiredWords.length > 0;
    
    // Check which hint words were used (for display)
    const usedHintWords = hintWords.filter(word => {
        const wordLower = word.toLowerCase();
        // Check if this hint word matches any used required word
        const matchesUsed = usedRequiredWords.some(used => {
            const usedLower = used.toLowerCase();
            if (wordLower.includes(' ') || usedLower.includes(' ')) {
                return usedLower.includes(wordLower) || wordLower.includes(usedLower);
            }
            return new RegExp(`\\b${wordLower}\\b`).test(usedLower);
        });
        if (matchesUsed) return true;
        
        // Also check directly in the text
        if (wordLower.includes(' ')) {
            return currentTurnText.includes(wordLower);
        }
        return new RegExp(`\\b${wordLower}\\b`).test(currentTurnText);
    });
    
    // Determine how many hints are required based on user_requirement
    // (userRequirement and requiresAll already declared above)
    const requiredCount = requiresAll ? hintWords.length : 1;
    const instructionText = requiredCount === 1 
        ? "Use any of the following:"
        : requiredCount === 2
        ? "Use 2 of the following:"
        : `Use ${requiredCount} of the following:`;
    
    return (
        <div className="bg-purple-50 border border-purple-200 rounded-xl p-4 mb-4">
            <h3 className="text-sm font-bold text-purple-800 mb-2 flex items-center gap-2">
                <span>💡</span> {roundName}
            </h3>
            <p className="text-xs text-purple-600 mb-3">Turn {turnInRound} of 4</p>
            <p className="text-xs text-purple-700 mb-2 font-semibold italic">{instructionText}</p>
            <div className="space-y-2">
                {hintWords.map((word, idx) => {
                    const isUsed = usedHintWords.includes(word);
                    return (
                        <div 
                            key={idx} 
                            className={`flex items-center gap-2 text-sm ${
                                isUsed ? 'text-green-700' : 'text-gray-700'
                            }`}
                        >
                            {isUsed ? (
                                <span className="text-green-600 font-bold">✓</span>
                            ) : (
                                <span className="text-gray-400">○</span>
                            )}
                            <span className={isUsed ? 'line-through opacity-60' : ''}>
                                {word}
                            </span>
                        </div>
                    );
                })}
            </div>
            {requirementMet && (
                <p className="text-xs text-green-700 font-semibold mt-3">
                    ✓ Requirement met!
                </p>
            )}
        </div>
    );
};

const ChatTutorView = React.memo(({ chatHistory, inputMessage, setInputMessage, handleSendMessage, targetLang, isLoading, setIsLoading, activeLesson, lessonGoal, onBack, onCompleteLesson, goalAchieved, userProfile, setChatHistory, setGoalAchieved }) => {
    const messagesEndRef = React.useRef(null);
    const inputRef = React.useRef(null);
    const [hoverCorrection, setHoverCorrection] = useState(null);
    const [isRecording, setIsRecording] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioChunks, setAudioChunks] = useState([]);
    const hasPlayedInitialRef = React.useRef(false);
    const [currentTurn, setCurrentTurn] = useState(1);
    const [currentRound, setCurrentRound] = useState(1);
    const [roundFeedback, setRoundFeedback] = useState(null);
    const [pronunciationScores, setPronunciationScores] = useState([]);
    const [lastTranscription, setLastTranscription] = useState(null);
    const [lastPronunciationScore, setLastPronunciationScore] = useState(null);
    const [roundMistakes, setRoundMistakes] = useState([]);
    const [waitingForRound2, setWaitingForRound2] = useState(false);
    
    // Expose setCurrentTurn to handleSendMessage via ref or make it available
    const currentTurnRef = React.useRef(1);
    React.useEffect(() => {
        currentTurnRef.current = currentTurn;
    }, [currentTurn]);
    
    // Check if this is a boss fight
    const isBossFight = activeLesson && (activeLesson.type === "boss_fight" || activeLesson.lesson_id === "A1.1.BOSS");
    
    // Update turn based on user messages (each user message advances turn if valid)
    // Note: This is just an estimate - the actual turn comes from the backend response
    // But respect currentRound - if we're in round 2, adjust turn calculation accordingly
    useEffect(() => {
        if (isBossFight) {
            const userMessageCount = chatHistory.filter(msg => msg.role === 'user').length;
            // Turn starts at 1, each valid user response advances to next turn
            // If we're in round 2, the turn should be 5-8, not 1-4
            if (currentRound === 2 && userMessageCount > 0) {
                // In round 2, turns are 5-8, so add 4 to the count
                setCurrentTurn(userMessageCount + 4 + 1);
            } else if (userMessageCount > 0) {
                // Round 1: turns 1-4
                setCurrentTurn(userMessageCount + 1);
            }
        }
    }, [chatHistory, isBossFight, currentRound]);
    
    useEffect(() => { messagesEndRef.current?.scrollIntoView({ behavior: "smooth" }); }, [chatHistory]);
    
    // Reset ref when activeLesson changes (new boss fight starts)
    useEffect(() => {
        hasPlayedInitialRef.current = false;
    }, [activeLesson]);
    
    // Play initial prompt when it first appears in chat
    useEffect(() => {
        // Check if this is the initial message (first polybot message, no user messages yet)
        const isInitialMessage = chatHistory.length === 1 && 
            chatHistory[0]?.role === 'polybot' && 
            !hasPlayedInitialRef.current;
            
        if (isInitialMessage) {
            hasPlayedInitialRef.current = true;
            const initialMessage = chatHistory[0].text;
            
            if (initialMessage && initialMessage.trim()) {
                // Delay to ensure the message is rendered in the DOM
                setTimeout(() => {
                    console.log("[Initial Prompt TTS] Playing initial message:", initialMessage);
                    unlockAudio(); // Ensure audio is unlocked
                    speakText(initialMessage, targetLang).catch(err => {
                        console.error("[Initial Prompt TTS] Failed to play audio:", err);
                    });
                }, 800); // Increased delay to ensure rendering
            }
        }
        
        // Reset the ref when chat history is cleared (new conversation starts)
        if (chatHistory.length === 0) {
            hasPlayedInitialRef.current = false;
        }
    }, [chatHistory, targetLang]);
    
    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const recorder = new MediaRecorder(stream);
            const chunks = [];
            
            recorder.ondataavailable = (e) => {
                if (e.data.size > 0) {
                    chunks.push(e.data);
                }
            };
            
            recorder.onstop = async () => {
                const blob = new Blob(chunks, { type: 'audio/webm' });
                await handleVoiceMessage(blob);
                stream.getTracks().forEach(track => track.stop());
            };
            
            recorder.start();
            setMediaRecorder(recorder);
            setAudioChunks(chunks);
            setIsRecording(true);
        } catch (err) {
            console.error("Error accessing microphone:", err);
            alert("Could not access microphone. Please check permissions.");
        }
    };

    const stopRecording = () => {
        if (mediaRecorder && isRecording) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    };

    const handleVoiceMessage = async (audioBlob) => {
        setIsLoading(true);
        const formData = new FormData();
        formData.append('file', audioBlob, 'recording.webm');
        formData.append('target_language', targetLang);
        formData.append('native_language', userProfile.native_language);
        formData.append('level', userProfile.level || 'Beginner');
        formData.append('lesson_id', activeLesson ? activeLesson._id : '');
        formData.append('chat_history', JSON.stringify(chatHistory));
        
        try {
            // First transcribe
            const transcribeResponse = await fetch(`${API}/api/v1/voice/transcribe`, {
                method: 'POST',
                body: formData,
            });
            
            if (!transcribeResponse.ok) {
                throw new Error(`Transcription failed: ${transcribeResponse.status}`);
            }
            
            const transcribeResult = await transcribeResponse.json();
            const transcript = transcribeResult.text || '';
            
            console.log("[Voice Chat] Transcript received:", transcript);
            
            // For boss fights, also analyze pronunciation
            if (isBossFight && transcript.trim()) {
                // Get the expected phrase for current turn
                const bossExercise = activeLesson.exercises?.find(ex => ex.type === "boss_fight");
                const round = currentRound || Math.floor((currentTurn - 1) / 4) + 1;
                const turnInRound = ((currentTurn - 1) % 4) + 1;
                const roundData = bossExercise?.conversation_flow?.find(r => r.round === round);
                const turnData = roundData?.turns?.find(t => t.turn === turnInRound);
                const expectedPhrase = turnData?.required_words?.join(' ') || transcript;
                
                // Analyze pronunciation
                const analyzeFormData = new FormData();
                analyzeFormData.append('file', audioBlob, 'recording.webm');
                analyzeFormData.append('language', targetLang);
                analyzeFormData.append('target_phrase', expectedPhrase);
                
                try {
                    const analyzeResponse = await fetch(`${API}/voice/analyze`, {
                        method: 'POST',
                        body: analyzeFormData,
                    });
                    
                    if (analyzeResponse.ok) {
                        const analyzeResult = await analyzeResponse.json();
                        const phoneticScore = analyzeResult.phonetic_score || 0;
                        
                        // Store pronunciation score for round completion feedback
                        setPronunciationScores(prev => [...prev, phoneticScore]);
                        
                        // Store transcription and score to add when message is sent
                        setLastTranscription(transcript);
                        setLastPronunciationScore(phoneticScore);
                    }
                } catch (analyzeError) {
                    console.error("Pronunciation analysis error:", analyzeError);
                }
            }
            
            // Populate the text input with the transcribed text so user can review/edit
            if (transcript && transcript.trim()) {
                setInputMessage(transcript);
                console.log("[Voice Chat] Set input message to:", transcript);
            } else {
                console.warn("[Voice Chat] Empty transcript received");
                alert("Could not transcribe audio. Please try again.");
            }
            
            setIsLoading(false);
            
        } catch (error) {
            console.error("Voice transcription error:", error);
            alert("Error transcribing audio. Please try again.");
            setIsLoading(false);
        }
    };
    
    // Extract scenario from boss fight exercise - use round description if available
    // Use useMemo to recalculate when currentRound or activeLesson changes
    const bossScenario = React.useMemo(() => {
        if (!isBossFight || !activeLesson) return null;
        const bossExercise = activeLesson.exercises?.find(ex => ex.type === "boss_fight");
        if (!bossExercise || !bossExercise.conversation_flow) return null;
        
        // Always use round description from conversation_flow - don't fallback to prompt
        const roundData = bossExercise.conversation_flow.find(r => r.round === currentRound);
        if (roundData && roundData.round_description) {
            return roundData.round_description;
        }
        
        // If round description not found, return null (don't use prompt as it's round 1 specific)
        console.warn(`[BossScenario] Round ${currentRound} - No round_description found. Available rounds:`, 
            bossExercise.conversation_flow.map(r => ({ round: r.round, description: r.round_description })));
        return null;
    }, [isBossFight, activeLesson, currentRound]);
    
    // Local handleSendMessage for boss fights that updates turn
    const localHandleSendMessage = useCallback(async () => {
        if (!inputMessage.trim() || isLoading) return;
        
        // Create user message with transcription and pronunciation if available
        const userMsg = { 
            role: 'user', 
            text: inputMessage.trim(),
            ...(lastTranscription && lastTranscription !== inputMessage.trim() && { transcription: lastTranscription }),
            ...(lastPronunciationScore !== null && { pronunciationScore: lastPronunciationScore })
        };
        
        // Clear transcription data after using it
        setLastTranscription(null);
        setLastPronunciationScore(null);
        
        // Add user message to local state for display
        setChatHistory(prev => [...prev, userMsg]);
        setInputMessage('');
        setIsLoading(true);
        
        try {
            // Use boss fight endpoint if in boss fight mode
            // Note: Send chatHistory BEFORE adding userMsg, so backend can calculate turn correctly
            const endpoint = isBossFight ? `${API}/tutor/boss` : `${API}/tutor`;
            const response = await axios.post(endpoint, {
                user_message: userMsg.text,
                chat_history: chatHistory, // This is the OLD chatHistory (before userMsg was added)
                target_language: userProfile.target_language,
                native_language: userProfile.native_language,
                level: userProfile.level,
                lesson_id: activeLesson ? (activeLesson.lesson_id || activeLesson._id) : null
            }, { timeout: 300000 });
            
            // Track mistakes for end-of-round feedback
            // Only track mistakes for the current round to prevent mixing Round 1 and Round 2 mistakes
            if (isBossFight && response.data.had_mistake && response.data.mistake_info) {
                const mistakeInfo = response.data.mistake_info;
                // Only add mistake if it's from the current round (or if round is not specified, assume current round)
                if (!mistakeInfo.round || mistakeInfo.round === currentRound) {
                    setRoundMistakes(prev => [...prev, mistakeInfo]);
                }
            }
            
            // Update turn and round if boss fight
            if (isBossFight && response.data.turn_number) {
                // If we're already in round 2, calculate the correct turn number
                // Backend might calculate wrong turn because chat history was cleared
                let actualTurn = response.data.turn_number;
                if (currentRound === 2 && actualTurn <= 4) {
                    // We're in round 2, but backend thinks we're in round 1
                    // Adjust turn: if backend says turn 1, we're actually on turn 5, etc.
                    actualTurn = actualTurn + 4;
                }
                setCurrentTurn(actualTurn);
                
                if (response.data.round_number) {
                    const newRound = response.data.round_number;
                    // If moving to a new round, clear mistakes from previous round
                    if (newRound !== currentRound && newRound > currentRound) {
                        setRoundMistakes([]);
                        setWaitingForRound2(false); // Clear waiting state when round changes
                    }
                    // Only update round if backend says we're in round 2, or if we're not already in round 2
                    // This prevents backend from incorrectly resetting us to round 1 when chat history was cleared
                    if (newRound === 2 || currentRound !== 2) {
                        setCurrentRound(newRound);
                    }
                } else {
                    // Calculate round from turn if backend didn't provide it
                    // Use the actual turn we calculated above
                    const calculatedRound = Math.floor((actualTurn - 1) / 4) + 1;
                    // Only update if we're not already in round 2 (to prevent reset)
                    if (calculatedRound === 2 || currentRound !== 2) {
                        setCurrentRound(calculatedRound);
                    }
                }
            }
            
            // Check if round 1 is complete and waiting for round 2
            if (isBossFight && response.data.round_complete && response.data.next_round && !response.data.all_rounds_complete) {
                setWaitingForRound2(true);
            }
            
            // Check if round is complete
            if (isBossFight && response.data.round_complete) {
                // Show feedback immediately - no AI grammar check for boss fights (static mode)
                const bossExercise = activeLesson.exercises?.find(ex => ex.type === "boss_fight");
                const roundData = bossExercise?.conversation_flow?.find(r => r.round === currentRound);
                const avgPronunciation = pronunciationScores.length > 0
                    ? pronunciationScores.reduce((a, b) => a + b, 0) / pronunciationScores.length
                    : null;
                
                // Show feedback immediately - skip AI grammar check for boss fights
                setRoundFeedback({
                    round: currentRound,
                    roundName: roundData?.round_name || `Round ${currentRound}`,
                    grammar: null, // No AI grammar check for static boss fights
                    pronunciation: avgPronunciation,
                    allComplete: response.data.all_rounds_complete || false,
                    mistakes: roundMistakes,
                    loadingGrammar: false // No grammar check, so not loading
                });
                
                // If all rounds complete, set goal achieved to show mission complete screen
                if (response.data.all_rounds_complete) {
                    setGoalAchieved(true);
                }
                
                // Clear pronunciation scores and mistakes for next round
                if (!response.data.all_rounds_complete) {
                    setPronunciationScores([]);
                    setRoundMistakes([]);
                }
            }
            
            const correctionObj = parseCorrectionData(response.data.correction_data);
            if (response.data.status === "GOAL_ACHIEVED") {
                setChatHistory(prev => {
                    const newHistory = [...prev];
                    const lastUserIndex = newHistory.length - 1;
                    if (newHistory[lastUserIndex].role === 'user') {
                        // Don't add corrections in boss fight mode
                        // Note: Transcription and pronunciation are already in userMsg when created
                        if (!isBossFight) {
                            newHistory[lastUserIndex].correction = correctionObj;
                        }
                    }
                    const botMessage = { role: 'polybot', text: response.data.text, explanation: "Mission Complete!" };
                    newHistory.push(botMessage);
                    
                    // Play TTS for boss fight responses
                    if (isBossFight && response.data.text) {
                        setTimeout(() => {
                            unlockAudio();
                            speakText(response.data.text, targetLang).catch(err => {
                                console.error("[Boss Fight TTS] Error:", err);
                            });
                        }, 300);
                    }
                    
                    return newHistory;
                });
                setGoalAchieved(true);
            } else {
                setChatHistory(prev => {
                    const newHistory = [...prev];
                    const lastUserIndex = newHistory.length - 1;
                    if (newHistory[lastUserIndex].role === 'user') {
                        // Don't add corrections in boss fight mode
                        // Note: Transcription and pronunciation are already in userMsg when created
                        if (!isBossFight) {
                            newHistory[lastUserIndex].correction = correctionObj;
                        }
                    }
                    const botMessage = { role: 'polybot', text: response.data.text };
                    newHistory.push(botMessage);
                    
                    // Play TTS for boss fight responses
                    if (isBossFight && response.data.text) {
                        setTimeout(() => {
                            unlockAudio();
                            speakText(response.data.text, targetLang).catch(err => {
                                console.error("[Boss Fight TTS] Error:", err);
                            });
                        }, 300);
                    }
                    
                    return newHistory;
                });
            }
        } catch (error) {
            setChatHistory(prev => [...prev, { role: 'polybot', text: "Error connecting to tutor.", explanation: "Try again." }]);
        } finally {
            setIsLoading(false);
        }
    }, [inputMessage, isLoading, userProfile, activeLesson, chatHistory, isBossFight, currentRound, pronunciationScores, lastTranscription, lastPronunciationScore, targetLang, roundMistakes]);
    
    // Use local handler for boss fights, parent handler for regular mode
    const effectiveHandleSendMessage = isBossFight ? localHandleSendMessage : handleSendMessage;
    
    return (
        <div className="flex flex-col h-full bg-white rounded-xl shadow-xl border border-gray-100">
            {/* Header */}
            <div className="p-4 border-b bg-gray-50 rounded-t-xl flex flex-col gap-2">
                <div className="flex items-center justify-between">
                    <div className="flex items-center">
                        {onBack && <button onClick={onBack} className="mr-3 p-2 hover:bg-gray-200 rounded-full text-gray-500"><ArrowLeft size={20} /></button>}
                        <div><p className="font-semibold text-gray-800 text-lg">{activeLesson ? "Boss Fight" : "Free Tutor Mode"}</p></div>
                    </div>
                </div>
                {/* SCENARIO BANNER */}
                {isBossFight && bossScenario ? (
                    <div className="bg-blue-600 text-white p-3 rounded-lg flex items-center shadow-inner animate-fade-in">
                        <Target size={20} className="mr-2 text-yellow-300" />
                        <span className="text-sm font-bold">Scenario: {bossScenario}</span>
                    </div>
                ) : lessonGoal ? (
                    <div className="bg-blue-600 text-white p-3 rounded-lg flex items-center shadow-inner animate-fade-in">
                        <Target size={20} className="mr-2 text-yellow-300" />
                        <span className="text-sm font-bold">Mission: {lessonGoal}</span>
                    </div>
                ) : null}
            </div>

            {/* Main Content Area - Flex layout with chat and hints sidebar */}
            <div className="flex flex-grow min-h-0">
                {/* Chat Area */}
                <div className="flex-grow overflow-y-auto p-4 space-y-4 min-h-0 bg-white">
                <div className="chat-messages-container" style={{ opacity: 1 }}>
                <div className="text-center text-sm text-gray-400 p-2">Conversation Started</div>
                {chatHistory.map((msg, index) => (
                    <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div 
                            className={`max-w-3/4 p-4 rounded-2xl shadow-sm border relative ${msg.role === 'user' ? 'bg-blue-600 text-white border-blue-600 rounded-br-none' : 'bg-gray-100 text-gray-800 border-gray-200 rounded-tl-none'}`}
                            onMouseEnter={() => msg.role === 'user' && msg.correction && setHoverCorrection(index)}
                            onMouseLeave={() => msg.role === 'user' && msg.correction && setHoverCorrection(null)}
                        >
                            <p className="whitespace-pre-wrap">{msg.text}</p>
                            {msg.explanation && <div className="mt-3 pt-2 border-t border-gray-300/50 text-xs italic opacity-80">{msg.explanation}</div>}
                            
                            {/* CORRECTION ICON & HOVER-OVER POPUP */}
                            {msg.role === 'user' && msg.correction && (
                                <div className="absolute top-0 right-0 transform translate-x-1/2 -translate-y-1/2 cursor-help text-red-300 hover:text-red-100">
                                    <AlertCircle size={16} />
                                    
                                    {/* HOVER POPUP */}
                                    {hoverCorrection === index && (
                                        <div className="absolute z-50 bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-max max-w-xs p-3 bg-red-800 text-white rounded-lg shadow-2xl border border-red-600 animate-fade-in">
                                            <p className="font-bold text-sm border-b border-red-600 mb-1">Correction:</p>
                                            <p className="text-sm font-semibold italic mb-1">{msg.correction.corrected}</p>
                                            <p className="text-xs">{msg.correction.explanation}</p>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    </div>
                ))}
                </div>
                {isLoading && <div className="flex justify-start"><div className="p-4 rounded-2xl bg-gray-50 text-gray-400 rounded-tl-none flex items-center gap-2"><Loader2 className="w-4 h-4 animate-spin" /> Thinking...</div></div>}
                {isRecording && <div className="flex justify-end"><div className="p-4 rounded-2xl bg-red-100 text-red-700 rounded-br-none flex items-center gap-2"><div className="w-3 h-3 bg-red-500 rounded-full animate-pulse"></div> Recording...</div></div>}
                
                {/* ROUND COMPLETION FEEDBACK */}
                {roundFeedback && (
                    <div className="flex justify-center my-4 animate-fade-in">
                        <div className="bg-gradient-to-br from-purple-50 to-blue-50 border-2 border-purple-300 p-6 rounded-xl text-left shadow-lg max-w-2xl w-full">
                            <h3 className="text-xl font-bold text-purple-800 mb-4 flex items-center gap-2">
                                <span>🎯</span> {roundFeedback.roundName} Complete!
                            </h3>
                            
                            {/* Grammar & Spelling Feedback */}
                            {roundFeedback.loadingGrammar ? (
                                <div className="mb-4">
                                    <h4 className="font-semibold text-gray-800 mb-2">Grammar & Spelling:</h4>
                                    <div className="p-3 rounded-lg bg-gray-50 border border-gray-200">
                                        <p className="text-sm text-gray-600 flex items-center gap-2">
                                            <Loader2 className="w-4 h-4 animate-spin" />
                                            Analyzing your responses...
                                        </p>
                                    </div>
                                </div>
                            ) : roundFeedback.grammar && (
                                <div className="mb-4">
                                    <h4 className="font-semibold text-gray-800 mb-2">Grammar & Spelling:</h4>
                                    <div className={`p-3 rounded-lg ${roundFeedback.grammar.has_errors ? 'bg-amber-50 border border-amber-200' : 'bg-green-50 border border-green-200'}`}>
                                        <p className={`text-sm ${roundFeedback.grammar.has_errors ? 'text-amber-800' : 'text-green-800'}`}>
                                            {roundFeedback.grammar.feedback}
                                        </p>
                                        {roundFeedback.grammar.errors && roundFeedback.grammar.errors.length > 0 && (
                                            <ul className="mt-2 text-xs text-amber-700 list-disc list-inside">
                                                {roundFeedback.grammar.errors.map((error, idx) => (
                                                    <li key={idx}>{error}</li>
                                                ))}
                                            </ul>
                                        )}
                                        {roundFeedback.grammar.suggestions && roundFeedback.grammar.suggestions.length > 0 && (
                                            <ul className="mt-2 text-xs text-blue-700 list-disc list-inside">
                                                {roundFeedback.grammar.suggestions.map((suggestion, idx) => (
                                                    <li key={idx}>{suggestion}</li>
                                                ))}
                                            </ul>
                                        )}
                                        <div className="mt-2 flex gap-4 text-xs">
                                            <span>Spelling: {(roundFeedback.grammar.spelling_score * 100).toFixed(0)}%</span>
                                            <span>Grammar: {(roundFeedback.grammar.grammar_score * 100).toFixed(0)}%</span>
                                        </div>
                                    </div>
                                </div>
                            )}
                            
                            {/* Pronunciation Feedback */}
                            {roundFeedback.pronunciation !== null && (
                                <div className="mb-4">
                                    <h4 className="font-semibold text-gray-800 mb-2">Pronunciation:</h4>
                                    <div className={`p-3 rounded-lg ${roundFeedback.pronunciation >= 0.7 ? 'bg-green-50 border border-green-200' : roundFeedback.pronunciation >= 0.4 ? 'bg-amber-50 border border-amber-200' : 'bg-red-50 border border-red-200'}`}>
                                        <p className={`text-sm ${roundFeedback.pronunciation >= 0.7 ? 'text-green-800' : roundFeedback.pronunciation >= 0.4 ? 'text-amber-800' : 'text-red-800'}`}>
                                            {roundFeedback.pronunciation >= 0.7 
                                                ? "Excellent pronunciation! Your accent is clear and natural."
                                                : roundFeedback.pronunciation >= 0.4
                                                ? "Good effort! Keep practicing to improve your accent clarity."
                                                : "Your pronunciation needs more practice. Focus on vowel sounds and word stress."}
                                        </p>
                                        <p className="text-xs mt-2 text-gray-600">
                                            Score: {(roundFeedback.pronunciation * 100).toFixed(0)}%
                                        </p>
                                    </div>
                                </div>
                            )}
                            
                            {/* Mistakes Feedback */}
                            {roundFeedback.mistakes && roundFeedback.mistakes.length > 0 && (
                                <div className="mb-4">
                                    <h4 className="font-semibold text-gray-800 mb-2">Areas to Improve:</h4>
                                    <div className="bg-amber-50 border border-amber-200 p-3 rounded-lg">
                                        <p className="text-sm text-amber-800 mb-2">
                                            You had {roundFeedback.mistakes.length} turn{roundFeedback.mistakes.length > 1 ? 's' : ''} where you missed some required words. Here's what to focus on:
                                        </p>
                                        <div className="space-y-2">
                                            {roundFeedback.mistakes
                                                .filter(mistake => !mistake.round || mistake.round === roundFeedback.round)
                                                .map((mistake, idx) => (
                                                <div key={idx} className="text-xs bg-white p-2 rounded border border-amber-200">
                                                    <p className="font-semibold text-amber-900 mb-1">Turn {mistake.turn}:</p>
                                                    <p className="text-amber-700 mb-1">You said: "{mistake.user_message}"</p>
                                                    <p className="text-amber-800 mb-1">Required: {mistake.user_requirement}</p>
                                                    {mistake.missing_words && mistake.missing_words.length > 0 && (
                                                        <p className="text-amber-900 font-semibold">
                                                            Missing: {mistake.missing_words.map(word => {
                                                                // Normalize capitalization: "E Lei?" -> "e Lei?" (only capitalize proper nouns)
                                                                // For phrases starting with "E " or "E?", make the "e" lowercase
                                                                if (word.match(/^E\s+[A-Z]/)) {
                                                                    return word.replace(/^E\s+/, 'e ');
                                                                }
                                                                return word;
                                                            }).join(', ')}
                                                        </p>
                                                    )}
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                            )}
                            
                            {/* Summary message if no specific feedback sections */}
                            {!roundFeedback.grammar && roundFeedback.pronunciation === null && (!roundFeedback.mistakes || roundFeedback.mistakes.length === 0) && (
                                <div className="mb-4">
                                    <div className="bg-green-50 border border-green-200 p-3 rounded-lg">
                                        <p className="text-sm text-green-800">
                                            Great job completing this round! You used all the required words correctly.
                                        </p>
                                    </div>
                                </div>
                            )}
                            
                            {roundFeedback.allComplete && (
                                <div className="mt-4 p-4 bg-gradient-to-r from-yellow-100 to-green-100 border-2 border-yellow-400 rounded-lg text-center shadow-lg">
                                    <p className="text-3xl mb-2">🎉</p>
                                    <p className="font-bold text-yellow-900 text-lg mb-1">Mission Complete!</p>
                                    <p className="text-sm text-yellow-800">You've successfully completed both conversations!</p>
                                </div>
                            )}
                            
                            {/* Button to proceed to next round - appears below all feedback */}
                            {waitingForRound2 && !roundFeedback.allComplete && (
                                <div className="mt-4">
                                    <button
                                        onClick={async () => {
                                            // Get first message of round 2
                                            const bossExercise = activeLesson.exercises?.find(ex => ex.type === "boss_fight");
                                            const round2Data = bossExercise?.conversation_flow?.find(r => r.round === 2);
                                            if (round2Data) {
                                                const firstTurnRound2 = round2Data.turns?.find(t => t.turn === 1);
                                                if (firstTurnRound2 && firstTurnRound2.ai_message) {
                                                    // Fade out current chat
                                                    const chatContainer = document.querySelector('.chat-messages-container');
                                                    if (chatContainer) {
                                                        chatContainer.style.transition = 'opacity 0.3s ease-out';
                                                        chatContainer.style.opacity = '0';
                                                    }
                                                    
                                                    // Wait for fade out, then clear chat and fade in
                                                    setTimeout(() => {
                                                        // Clear chat history and add round 2 first message
                                                        setChatHistory([{
                                                            role: 'polybot',
                                                            text: firstTurnRound2.ai_message
                                                        }]);
                                                        
                                                        // Update round and clear waiting state
                                                        setCurrentRound(2);
                                                        setCurrentTurn(5); // Turn 5 = first turn of round 2
                                                        setWaitingForRound2(false);
                                                        setRoundFeedback(null); // Clear round 1 feedback
                                                        setPronunciationScores([]); // Clear pronunciation scores
                                                        setRoundMistakes([]); // Clear mistakes
                                                        
                                                        // Fade in new chat
                                                        setTimeout(() => {
                                                            if (chatContainer) {
                                                                chatContainer.style.transition = 'opacity 0.3s ease-in';
                                                                chatContainer.style.opacity = '1';
                                                            }
                                                        }, 50);
                                                        
                                                        // Play TTS for round 2 first message
                                                        setTimeout(() => {
                                                            unlockAudio();
                                                            speakText(firstTurnRound2.ai_message, targetLang).catch(err => {
                                                                console.error("[Boss Fight TTS] Error:", err);
                                                            });
                                                        }, 400);
                                                    }, 300);
                                                }
                                            }
                                        }}
                                        className="w-full py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-bold rounded-xl hover:from-purple-700 hover:to-blue-700 shadow-lg transition transform hover:scale-[1.02] flex items-center justify-center gap-2"
                                    >
                                        <span>➡️</span> Continue to Formal Conversation
                                    </button>
                                </div>
                            )}
                            
                        </div>
                    </div>
                )}
                
                {/* GOAL ACHIEVED BANNER IN CHAT */}
                {goalAchieved && (
                    <div className="flex justify-center my-4 animate-bounce">
                        <div className="bg-yellow-100 border border-yellow-300 p-4 rounded-xl text-center shadow-lg">
                            <p className="text-2xl">🏆</p>
                            <p className="font-bold text-yellow-800">Mission Accomplished!</p>
                            <p className="text-sm text-yellow-700">XP Awarded!</p>
                        </div>
                    </div>
                )}
                <div ref={messagesEndRef} />
                </div>
                
                {/* Hints Sidebar - Only show for boss fights */}
                {isBossFight && (
                    <div className="w-64 border-l border-gray-200 bg-gray-50 overflow-y-auto p-4">
                        <BossFightHints 
                            activeLesson={activeLesson} 
                            chatHistory={chatHistory} 
                            currentTurn={currentTurn}
                            currentRound={currentRound}
                        />
                    </div>
                )}
            </div>

            {/* Input Area / Completion Button */}
            <div className="p-4 border-t bg-gray-50 rounded-b-xl">
                {goalAchieved ? (
                    <button onClick={onCompleteLesson} className="w-full py-4 bg-gradient-to-r from-green-600 to-blue-600 text-white font-bold text-lg rounded-xl hover:from-green-700 hover:to-blue-700 shadow-lg transition transform hover:scale-[1.02] flex items-center justify-center gap-2">
                         <CheckSquare size={24} /> Complete Lesson & Return
                    </button>
                ) : waitingForRound2 ? (
                    <div className="text-center">
                        <p className="text-sm text-gray-600 mb-2">Review your feedback above, then continue to the formal conversation.</p>
                    </div>
                ) : (
                    <div className="space-y-3">
                        <div className="flex space-x-3">
                            <input 
                                ref={inputRef}
                                type="text" 
                                placeholder="Type or speak your response here" 
                                value={inputMessage} 
                                onChange={(e) => setInputMessage(e.target.value)} 
                                onKeyDown={(e) => { if (e.key === 'Enter') effectiveHandleSendMessage(); }} 
                                className="flex-grow p-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-[#4CAF50] outline-none" 
                                disabled={isLoading || isRecording} 
                            />
                            {/* Microphone button */}
                            <button 
                            onClick={isRecording ? stopRecording : startRecording}
                            className={`p-3 rounded-xl text-white shadow-md transition ${
                                isRecording 
                                    ? 'bg-red-500 hover:bg-red-600 animate-pulse' 
                                    : isLoading 
                                        ? 'bg-gray-300 cursor-not-allowed' 
                                        : 'bg-blue-500 hover:bg-blue-600'
                            }`}
                            disabled={isLoading}
                            title={isRecording ? "Stop recording" : "Record voice message"}
                        >
                            <Mic size={24} />
                        </button>
                        <button 
                            onClick={effectiveHandleSendMessage} 
                            className={`p-3 rounded-xl text-white shadow-md transition transform hover:scale-[1.02] ${isLoading || isRecording ? 'bg-gray-300 cursor-not-allowed' : 'bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700'}`} 
                            disabled={isLoading || isRecording}
                        >
                            <Send size={24} />
                        </button>
                        </div>
                        {/* Accented letter chips for Italian */}
                        {targetLang === 'it' && (
                            <AccentedLetterChips 
                                inputRef={inputRef}
                                value={inputMessage}
                                setValue={setInputMessage}
                                disabled={isLoading || isRecording}
                            />
                        )}
                    </div>
                )}
            </div>
        </div>
    );
});

// --- MAIN SCREEN ---
const MainScreen = React.memo(({ userProfile, setUserProfile, setView, chatHistory, setChatHistory, inputMessage, setInputMessage, handleSendMessage, isLoading, setIsLoading, mainContentView, setMainContentView, activeLesson, setActiveLesson, lessonGoal, setLessonGoal, goalAchieved, setGoalAchieved }) => {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    const [tempScore, setTempScore] = useState({ score: 0, total: 0 });
    const t = getT(userProfile.native_language); 

    const handleLessonSelect = (lesson) => { setActiveLesson(lesson); setMainContentView('lesson_detail'); };
    
    // Handle Language Switch with Redirect
    const handleLanguageSwitch = async (newLangCode) => {
        setUserProfile(prev => ({ ...prev, target_language: newLangCode }));
        // Redirect to lessons
        setMainContentView('curriculum'); 
        try {
            await axios.patch(`${API}/user/${userProfile.user_id}`, {
                target_language: newLangCode
            });
        } catch (e) {
            console.error("Failed to switch language", e);
        }
    };

    const handleExercisesComplete = async (score, total) => {
        setTempScore({ score, total });
        
        // Check if this is a boss fight lesson - only boss fights go to tutor mode
        const isBossFight = activeLesson && (activeLesson.type === "boss_fight" || activeLesson.lesson_id === "A1.1.BOSS");
        
        if (isBossFight) {
            // Boss fight: go to tutor/chat mode
            setMainContentView('tutor');
            setChatHistory([]);
            setGoalAchieved(false);
            setLessonGoal("Loading..."); 
            
            if (activeLesson) {
                try {
                    const response = await axios.post(`${API}/tutor/initiate`, {
                        target_language: userProfile.target_language,
                        native_language: userProfile.native_language,
                        level: userProfile.level,
                        lesson_id: activeLesson.lesson_id || activeLesson._id || "A1.1.BOSS"
                    });
                    
                    const initialMessage = response.data.text;
                    setChatHistory([{ role: 'polybot', text: initialMessage, explanation: response.data.explanation }]);
                    setLessonGoal(response.data.communicative_goal);

                } catch (error) {
                    console.error("Init failed", error);
                    setChatHistory([{ role: 'polybot', text: "Hello! (Connection Error)", explanation: "Start talking." }]);
                }
            }
        } else {
            // Regular lesson: save progress and return to curriculum
            if (activeLesson) {
                try {
                    const response = await axios.post(`${API}/user/complete_lesson`, {
                        user_id: userProfile.user_id,
                        lesson_id: activeLesson.lesson_id || activeLesson._id,
                        score: score,
                        total_questions: total
                    });
                    
                    // Update local state with the returned PROGRESS list
                    setUserProfile(prev => ({ 
                        ...prev, 
                        xp: response.data.new_xp, 
                        words_learned: response.data.words_learned, 
                        vocabulary_list: response.data.vocabulary_list || prev.vocabulary_list,
                        progress: response.data.progress || prev.progress 
                    }));
                    
                    // Return to curriculum view to see next lesson
                    setMainContentView('curriculum');
                    setActiveLesson(null);
                } catch (error) {
                    console.error("Failed to save progress", error);
                    // Still return to curriculum even if save fails
                    setMainContentView('curriculum');
                    setActiveLesson(null);
                }
            } else {
                // No active lesson, just return to curriculum
                setMainContentView('curriculum');
                setActiveLesson(null);
            }
        }
    };

    const handleFinalCompletion = async () => {
        if (!activeLesson) {
            // No active lesson, just return to curriculum
            setMainContentView('curriculum');
            setActiveLesson(null);
            setGoalAchieved(false);
            setChatHistory([]);
            return;
        }
        try {
            const response = await axios.post(`${API}/user/complete_lesson`, {
                user_id: userProfile.user_id,
                lesson_id: activeLesson.lesson_id || activeLesson._id,
                score: tempScore.score,
                total_questions: tempScore.total
            });
            
            // FIX: Update local state with the returned PROGRESS list
            setUserProfile(prev => ({ 
                ...prev, 
                xp: response.data.new_xp, 
                words_learned: response.data.words_learned, 
                vocabulary_list: response.data.vocabulary_list || prev.vocabulary_list,
                progress: response.data.progress || prev.progress 
            }));
        } catch (error) {
            console.error("Failed to save progress", error);
        } finally {
            // Always navigate back to curriculum/lessons screen
            setMainContentView('curriculum');
            setActiveLesson(null);
            setGoalAchieved(false);
            setChatHistory([]);
        }
    };

    const ContentView = useMemo(() => {
        switch (mainContentView) {
            case 'progress': return <ProgressView userProfile={userProfile} />;
            case 'vocabulary': return <VocabularyView userProfile={userProfile} targetLang={userProfile.target_language} />;
            case 'curriculum': return <CurriculumView onSelectLesson={handleLessonSelect} userProfile={userProfile} t={t} />;
            case 'lesson_detail': return activeLesson ? <LessonDetailView lesson={activeLesson} onStartChat={() => {}} onCompleteExercises={handleExercisesComplete} onBack={() => setMainContentView('curriculum')} targetLang={userProfile.target_language} t={t} userProfile={userProfile} /> : <CurriculumView onSelectLesson={handleLessonSelect} userProfile={userProfile} t={t} />;
            case 'tutor': default: 
                return <ChatTutorView 
                    chatHistory={chatHistory} 
                    inputMessage={inputMessage} 
                    setInputMessage={setInputMessage} 
                    handleSendMessage={handleSendMessage} 
                    targetLang={userProfile.target_language} 
                    isLoading={isLoading}
                    setIsLoading={setIsLoading}
                    activeLesson={activeLesson} 
                    lessonGoal={lessonGoal}
                    goalAchieved={goalAchieved}
                    onBack={() => setMainContentView(activeLesson ? 'lesson_detail' : 'curriculum')} 
                    onCompleteLesson={handleFinalCompletion}
                    userProfile={userProfile}
                    setChatHistory={setChatHistory}
                    setGoalAchieved={setGoalAchieved}
                />;
        }
    }, [mainContentView, userProfile, chatHistory, inputMessage, setInputMessage, handleSendMessage, isLoading, setIsLoading, activeLesson, lessonGoal, goalAchieved, setChatHistory, setGoalAchieved]);

    return (
        <div className="polybot-background min-h-screen flex flex-col">
            <style jsx="true">{` .polybot-background { background: linear-gradient(135deg, #4CAF50 0%, #2196F3 50%, #9C27B0 100%); } `}</style>
            <header className="bg-white shadow-md p-4 flex justify-between items-center z-10">
                <div className="flex items-center space-x-4"><button onClick={() => setIsSidebarOpen(true)} className="p-2 rounded-full hover:bg-gray-100 md:hidden"><Menu size={24} /></button><h1 className="text-xl font-extrabold text-[#388E3C]">Polybot</h1></div>
                
                <div className="flex items-center space-x-4">
                     <div className="hidden md:flex space-x-2 text-sm font-medium">
                        <button onClick={() => setMainContentView('curriculum')} className="px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-600">{t('lessons')}</button>
                        <button onClick={() => setMainContentView('tutor')} className="px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-600">{t('practice')}</button>
                    </div>
                    
                    {/* Language Switcher */}
                    <LanguageSwitcher 
                        currentLang={userProfile.target_language} 
                        nativeLang={userProfile.native_language} // Pass nativeLang to disable button
                        onSwitch={handleLanguageSwitch} 
                    />
                </div>
            </header>
            <div className="flex flex-grow overflow-hidden p-4">
                {/* Desktop Menu (Always visible on desktop, responsible for the left column) */}
                <div className="hidden md:block md:w-72 mr-4">
                    <div className="bg-white rounded-2xl shadow-lg h-full overflow-hidden">
                        <SidebarMenu 
                            isSidebarOpen={true} 
                            setIsSidebarOpen={setIsSidebarOpen} 
                            setMainContentView={setMainContentView} 
                            setView={setView} 
                            userProfile={userProfile} 
                            t={t} 
                        />
                    </div>
                </div>
                <div className="flex-grow overflow-y-auto h-full">{ContentView}</div>
            </div>
            
            {/* Mobile Menu Overlay and Component (Only rendered when the menu is actively open) */}
            {isSidebarOpen && (
                <>
                    <div className="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden" onClick={() => setIsSidebarOpen(false)}></div>
                    <SidebarMenu 
                        isSidebarOpen={isSidebarOpen} 
                        setIsSidebarOpen={setIsSidebarOpen} 
                        setMainContentView={setMainContentView} 
                        setView={setView} 
                        userProfile={userProfile} 
                        t={t} 
                    />
                </>
            )}
            
        </div>
    );
});

// --- APP COMPONENT ---
// Landing Page Component
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
                            10-module comprehensive course with 7 complete lessons in Module A1.1 (Greetings & Introductions). 
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
                            Practice pronunciation with Whisper speech-to-text transcription and Edge-TTS audio playback. 
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

export default function App() { 
    const [view, setView] = useState('landing'); 
    const [userProfile, setUserProfile] = useState({ user_id: '', name: '', email: '', native_language: 'en', target_language: 'es', level: 'Beginner', xp: 0, words_learned: 0, streak: 0 });
    const [chatHistory, setChatHistory] = useState([]);
    const [inputMessage, setInputMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const [mainContentView, setMainContentView] = useState('curriculum'); 
    const [activeLesson, setActiveLesson] = useState(null); 
    
    const [lessonGoal, setLessonGoal] = useState("");
    const [goalAchieved, setGoalAchieved] = useState(false);

    // --- CHECK FOR OAUTH RETURN ---
    useEffect(() => {
        const query = new URLSearchParams(window.location.search);
        const userId = query.get('user_id');
        const isNewUser = query.get('new_user') === 'true';
        
        // CAPTURE ERROR FROM URL (New)
        const error = query.get('error');
        if (error) {
            setErrorMessage(`Login Failed: ${error.replace(/_/g, ' ')}`);
        }

        if (userId) {
            const email = query.get('email');
            const name = query.get('name');
            
            // Clear URL param
            window.history.replaceState({}, document.title, "/");

            if (isNewUser) {
                setUserProfile(prev => ({ ...prev, user_id: userId, email, name }));
                setView('language_setup');
            } else {
                // Load full profile for returning user
                handleLoadProfile(email);
            }
        }
    }, []); // Removed handleLoadProfile from deps to prevent loop, defined below

    const handleLoadProfile = useCallback(async (email) => { 
        try { 
            const response = await axios.get(`${API}/user/profile?email=${encodeURIComponent(email)}`); 
            setUserProfile(prev => ({ ...prev, ...response.data })); 
            setView('main'); 
            return true; 
        } catch (error) { return false; } 
    }, []);

    const handleRegister = useCallback(async (isManual = false) => { 
        if (!userProfile.name || !userProfile.email) { setErrorMessage("Fill all fields."); return; } 
        setErrorMessage(''); 
        const userId = userProfile.user_id || uuidv4(); 
        
        try { 
            await axios.post(`${API}/user/register`, { ...userProfile, user_id: userId }); 
            setUserProfile(prev => ({ ...prev, user_id: userId })); 
            
            if (isManual) setView('language_setup'); 
            else setView('main'); 
        } catch (error) { 
            if (error.response?.status === 409) {
                const loaded = await handleLoadProfile(userProfile.email);
                if (!loaded) setErrorMessage("User exists but couldn't load.");
            } else { setErrorMessage("Error registering."); } 
        } 
    }, [userProfile, handleLoadProfile]);
    
    const handleSendMessage = useCallback(async () => { 
        if (!inputMessage.trim() || isLoading) return; 
        const userMsg = { role: 'user', text: inputMessage.trim() }; 
        setChatHistory(prev => [...prev, userMsg]); 
        setInputMessage(''); 
        setIsLoading(true); 
        
        const isBossFight = activeLesson && (activeLesson.type === "boss_fight" || activeLesson.lesson_id === "A1.1.BOSS");
        
        try { 
            // Use boss fight endpoint if in boss fight mode
            const endpoint = isBossFight ? `${API}/tutor/boss` : `${API}/tutor`;
            const response = await axios.post(endpoint, { 
                user_message: userMsg.text, 
                chat_history: chatHistory, 
                target_language: userProfile.target_language, 
                native_language: userProfile.native_language, 
                level: userProfile.level, 
                lesson_id: activeLesson ? (activeLesson.lesson_id || activeLesson._id) : null 
            }, { timeout: 300000 });
            
            // Update turn if boss fight
            if (isBossFight && response.data.turn_number) {
                setCurrentTurn(response.data.turn_number);
                currentTurnRef.current = response.data.turn_number;
            }
            
            const correctionObj = parseCorrectionData(response.data.correction_data);
            if (response.data.status === "GOAL_ACHIEVED") {
                setChatHistory(prev => { 
                    const newHistory = [...prev]; 
                    const lastUserIndex = newHistory.length - 1; 
                    if (newHistory[lastUserIndex].role === 'user') {
                        // Don't add corrections in boss fight mode
                        if (!isBossFight) {
                            newHistory[lastUserIndex].correction = correctionObj;
                        }
                    }
                    newHistory.push({ role: 'polybot', text: response.data.text, explanation: "Mission Complete!" }); 
                    return newHistory; 
                });
                setGoalAchieved(true);
            } else {
                setChatHistory(prev => { 
                    const newHistory = [...prev]; 
                    const lastUserIndex = newHistory.length - 1; 
                    if (newHistory[lastUserIndex].role === 'user') {
                        // Don't add corrections in boss fight mode
                        if (!isBossFight) {
                            newHistory[lastUserIndex].correction = correctionObj;
                        }
                    }
                    newHistory.push({ role: 'polybot', text: response.data.text }); 
                    return newHistory; 
                });
            }
        } catch (error) { 
            setChatHistory(prev => [...prev, { role: 'polybot', text: "Error connecting to tutor.", explanation: "Try again." }]); 
        } finally { setIsLoading(false); } 
    }, [inputMessage, isLoading, userProfile, activeLesson, chatHistory]);

    // Handler for landing page "Get Started" button
    const handleGetStarted = () => {
        if (!userProfile.name || !userProfile.native_language || !userProfile.target_language) {
            setView('register');
        } else {
            setView('main');
        }
    };

    if (view === 'landing') return <LandingPage onGetStarted={handleGetStarted} />;
    if (view === 'register') return <RegistrationScreen userProfile={userProfile} setUserProfile={setUserProfile} handleRegister={handleRegister} errorMessage={errorMessage} />;
    if (view === 'language_setup') return <LanguageSetupScreen userProfile={userProfile} setUserProfile={setUserProfile} onComplete={() => setView('main')} />;
    if (view === 'main') return <MainScreen userProfile={userProfile} setUserProfile={setUserProfile} setView={setView} chatHistory={chatHistory} setChatHistory={setChatHistory} inputMessage={inputMessage} setInputMessage={setInputMessage} handleSendMessage={handleSendMessage} isLoading={isLoading} setIsLoading={setIsLoading} mainContentView={mainContentView} setMainContentView={setMainContentView} activeLesson={activeLesson} setActiveLesson={setActiveLesson} lessonGoal={lessonGoal} setLessonGoal={setLessonGoal} goalAchieved={goalAchieved} setGoalAchieved={setGoalAchieved} />;
}