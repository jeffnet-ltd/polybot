import React, { useState, useCallback, useEffect, useMemo, useRef } from 'react';
import { Menu, MessageSquare, GraduationCap, Zap, BookOpen, Trophy, Send, X, User, Loader2, Lock, ChevronRight, CheckCircle, AlertCircle, ArrowLeft, Volume2, RefreshCcw, CheckSquare, Target, ChevronDown, Mic, Settings } from 'lucide-react';
import ScenarioSelectionView from './components/ScenarioSelectionView';
import ScenarioPracticeView from './components/ScenarioPracticeView';

// Phase 2 Components - Common UI
import FlagIcon from './components/common/FlagIcon';
import ProgressCard from './components/common/ProgressCard';
import AccentedLetterChips from './components/common/AccentedLetterChips';
import SidebarMenu from './components/common/SidebarMenu';

// Phase 2 Components - Views
import LandingPage from './components/views/LandingPage';
import RegistrationScreen from './components/views/RegistrationScreen';
import LanguageSetupScreen from './components/views/LanguageSetupScreen';
import ProgressView from './components/views/ProgressView';
import VocabularyView from './components/views/VocabularyView';
import SettingsView from './components/views/SettingsView';

// Phase 5 Components - Curriculum (New Design)
import CurriculumView from './components/curriculum/CurriculumView';

// Phase 3 Components - Exercises
import {
    ConversationExercise,
    ArrangeExercise,
    GenderCategorizeExercise,
    UnscrambleExercise,
    EchoChamberExercise,
    MiniPromptExercise,
    ListeningComprehensionExercise,
    FreeWritingExercise,
    ReadingComprehensionExercise,
    FormFillExercise,
    SelfAssessmentExercise,
    MatchExercise
} from './components/exercises';

// Phase 4 Hooks - Custom orchestration and utility hooks
import { useLessonCompletion, useLanguageSwitch, useAudioRecording } from './hooks';

// Constants
import { API, ALL_LANGUAGES, CORE_LANGUAGES, LEVELS, UI_STRINGS } from './config/constants';

// Utilities
import { unlockAudio, speakText } from './utils/audio';
import { parseCorrectionData } from './utils/parsing';
import { uuidv4 } from './utils/uuid';
import { getT } from './utils/localization';
import { getNextModuleImage } from './utils/imageUtils';

// Services
import { getUserProfile, registerUser, updateUserProfile, completeLessonProgress } from './services/userService';
import { getModules, getLessons } from './services/lessonService';
import { sendTutorMessage, initiateTutor, sendBossFightMessage } from './services/tutorService';
import { synthesizeVoice, analyzeAudio } from './services/ttsService';

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

const ExerciseView = ({ exercises, onComplete, targetLang, userProfile, moduleTitle }) => {
    const [currentIndex, setCurrentIndex] = useState(0);
    const [feedback, setFeedback] = useState(null);
    const [score, setScore] = useState(0);
    const [showCelebration, setShowCelebration] = useState(false);
    const [usedImages, setUsedImages] = useState(new Set());
    const hasAutoPlayedRef = useRef(false);

    // Calculate these before early return so they're available in useEffect
    const currentExercise = exercises && exercises.length > 0 ? exercises[currentIndex] : null;
    const isLast = exercises && exercises.length > 0 ? currentIndex === exercises.length - 1 : false;

    // Auto-play audio for info_card and flashcard exercises
    // MUST be before early return to follow React Hooks rules
    useEffect(() => {
        if (!exercises || exercises.length === 0 || !currentExercise) return;
        
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
    }, [currentIndex, targetLang, currentExercise]); // Added currentExercise to deps

    // Track used images to avoid repetition within lesson
    useEffect(() => {
        if (currentExercise && currentExercise.type === 'info_card' && moduleTitle) {
            const imageUrl = getNextModuleImage(moduleTitle, usedImages);
            if (imageUrl && !usedImages.has(imageUrl)) {
                setUsedImages(prev => new Set([...prev, imageUrl]));
            }
        }
    }, [currentIndex, moduleTitle]);

    // Define handleAnswer BEFORE early return - React Hooks must come before early returns
    const handleAnswer = React.useCallback((resultStatus, userAnswer, customExplanation = null) => {
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
                feedbackType = 'success'; // e.g., "Great! You included..."
            } else if (isAlmost) {
                feedbackMsg = 'Almost!';
                feedbackType = 'warning'; // e.g., "You're close, but..."
            } else {
                feedbackMsg = 'Incorrect.';
                feedbackType = 'error'; // e.g., "For this situation, try..."
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
    }, [currentExercise, speakText]);

    // Early return AFTER all hooks
    if (!exercises || exercises.length === 0) return <div className="p-6 text-center text-gray-500">No exercises available.</div>;

    const handleSimpleNext = () => {
        setFeedback(null);
        if (isLast) setShowCelebration(true);
        else setCurrentIndex(c => c + 1);
    };

    const handleNext = () => {
        setFeedback(null);
        if (isLast) {
            setShowCelebration(true);
        } else {
            setCurrentIndex(c => c + 1);
        }
    };

    if (showCelebration) {
        const gradedQuestions = exercises.filter(e => 
            e.type !== 'info_card' && 
            e.type !== 'flashcard' && 
            e.type !== 'conversation_challenge' && 
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
                // Get next unused image for this lesson
                // For info cards with specific answers (numbers, vocab), use correct_answer to select images
                // Fall back to moduleTitle for other info cards (grammar, phrases)
                const currentImageUrl = currentExercise.correct_answer ?
                    getNextModuleImage(currentExercise.correct_answer, usedImages) :
                    (moduleTitle ? getNextModuleImage(moduleTitle, usedImages) : null);

                return (
                    <div className="space-y-6 text-center">
                        <h3 className="text-gray-500 font-medium text-lg">{currentExercise.prompt}</h3>

                        {/* Blue/Yellow Box - now contains image + content */}
                        <div className={`p-6 rounded-2xl border ${
                            isCulturalNote
                                ? 'bg-yellow-50 border-yellow-200'
                                : 'bg-blue-50 border-blue-100'
                        }`}>
                            {/* Category Image - inside box */}
                            {currentImageUrl && (
                                <img
                                    src={currentImageUrl}
                                    alt={moduleTitle}
                                    className="w-full h-64 object-cover rounded-xl mb-6 border border-gray-200"
                                    onError={(e) => {
                                        e.target.style.display = 'none';
                                    }}
                                />
                            )}

                            {/* Cultural Note Badge */}
                            {isCulturalNote && (
                                <div className="mb-3 flex items-center justify-center gap-2">
                                    <span className="text-2xl">🌍</span>
                                    <span className="text-sm font-semibold text-yellow-800">Cultural Note</span>
                                </div>
                            )}

                            {/* Word + Translation */}
                            <p className={`text-4xl font-extrabold mb-2 ${
                                isCulturalNote ? 'text-yellow-800' : 'text-blue-800'
                            }`}>{currentExercise.correct_answer}</p>

                            <p className={`text-xl mb-4 whitespace-pre-line ${
                                isCulturalNote ? 'text-yellow-700' : 'text-blue-600'
                            }`}>{currentExercise.explanation}</p>

                            {currentExercise.sub_text && <p className="text-sm text-gray-500 italic">{currentExercise.sub_text}</p>}
                        </div>

                        {/* Audio Button */}
                        {currentExercise.audio_url && (
                            <button onClick={() => speakText(currentExercise.correct_answer, targetLang)} className="inline-flex items-center gap-2 px-6 py-3 bg-gray-100 text-gray-700 rounded-full hover:bg-gray-200 transition"><Volume2 size={24} /> Replay</button>
                        )}

                        {/* Continue Button */}
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
                    key={`mini_prompt_${currentIndex}`}
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
            case 'conversation_challenge':
                // Get round information to display both scenarios
                const round1 = currentExercise.conversation_flow?.find(r => r.round === 1);
                const round2 = currentExercise.conversation_flow?.find(r => r.round === 2);
                return (
                    <div className="space-y-6 text-center">
                        <div className="bg-gradient-to-br from-purple-50 to-blue-50 p-8 rounded-2xl border-2 border-purple-200">
                            <h3 className="text-2xl font-bold text-gray-800 mb-4">🎭 Conversation Challenge</h3>
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
                            Start Conversation Challenge 🎭
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
                    moduleTitle={lesson.moduleTitle}
                    onComplete={(score, total) => {
                        onCompleteExercises(score, total);
                    }}
                />
            )}
        </div>
    );
};

// CurriculumView is now imported from './components/curriculum/CurriculumView'

const BossFightHints = ({ activeLesson, chatHistory, currentTurn, currentRound }) => {
    if (!activeLesson || activeLesson.type !== "conversation_challenge") return null;
    
    // Extract conversation flow from boss fight exercise
    const bossExercise = activeLesson.exercises?.find(ex => ex.type === "conversation_challenge");
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
    const isBossFight = activeLesson && (activeLesson.type === "conversation_challenge" || activeLesson.lesson_id === "A1.1.BOSS" || activeLesson.lesson_id === "A1.2.BOSS" || activeLesson.lesson_id === "A1.3.BOSS" || activeLesson.lesson_id === "A1.4.BOSS" || activeLesson.lesson_id === "A1.5.BOSS" || activeLesson.lesson_id === "A1.6.BOSS");
    
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
                const bossExercise = activeLesson.exercises?.find(ex => ex.type === "conversation_challenge");
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
        const bossExercise = activeLesson.exercises?.find(ex => ex.type === "conversation_challenge");
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
            const messagePayload = {
                user_message: userMsg.text,
                chat_history: chatHistory, // This is the OLD chatHistory (before userMsg was added)
                target_language: userProfile.target_language,
                native_language: userProfile.native_language,
                level: userProfile.level,
                lesson_id: activeLesson ? (activeLesson.lesson_id || activeLesson._id) : null
            };

            const responseData = isBossFight
                ? await sendBossFightMessage(messagePayload)
                : await sendTutorMessage(messagePayload);

            // Track mistakes for end-of-round feedback
            // Only track mistakes for the current round to prevent mixing Round 1 and Round 2 mistakes
            if (isBossFight && responseData.had_mistake && responseData.mistake_info) {
                const mistakeInfo = responseData.mistake_info;
                // Only add mistake if it's from the current round (or if round is not specified, assume current round)
                if (!mistakeInfo.round || mistakeInfo.round === currentRound) {
                    setRoundMistakes(prev => [...prev, mistakeInfo]);
                }
            }

            // Update turn and round if boss fight
            if (isBossFight && responseData.turn_number) {
                // If we're already in round 2, calculate the correct turn number
                // Backend might calculate wrong turn because chat history was cleared
                let actualTurn = responseData.turn_number;
                if (currentRound === 2 && actualTurn <= 4) {
                    // We're in round 2, but backend thinks we're in round 1
                    // Adjust turn: if backend says turn 1, we're actually on turn 5, etc.
                    actualTurn = actualTurn + 4;
                }
                setCurrentTurn(actualTurn);

                if (responseData.round_number) {
                    const newRound = responseData.round_number;
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
            if (isBossFight && responseData.round_complete && responseData.next_round && !responseData.all_rounds_complete) {
                setWaitingForRound2(true);
            }
            
            // Check if round is complete
            if (isBossFight && responseData.round_complete) {
                // Show feedback immediately - no AI grammar check for boss fights (static mode)
                const bossExercise = activeLesson.exercises?.find(ex => ex.type === "conversation_challenge");
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
                    allComplete: responseData.all_rounds_complete || false,
                    mistakes: roundMistakes,
                    loadingGrammar: false // No grammar check, so not loading
                });

                // If all rounds complete, set goal achieved to show mission complete screen
                if (responseData.all_rounds_complete) {
                    setGoalAchieved(true);
                }

                // Clear pronunciation scores and mistakes for next round
                if (!responseData.all_rounds_complete) {
                    setPronunciationScores([]);
                    setRoundMistakes([]);
                }
            }

            const correctionObj = parseCorrectionData(responseData.correction_data);
            if (responseData.status === "GOAL_ACHIEVED") {
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
                    const botMessage = { role: 'polybot', text: responseData.text, explanation: "Mission Complete!" };
                    newHistory.push(botMessage);

                    // Play TTS for boss fight responses
                    if (isBossFight && responseData.text) {
                        setTimeout(() => {
                            unlockAudio();
                            speakText(responseData.text, targetLang).catch(err => {
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
                    const botMessage = { role: 'polybot', text: responseData.text };
                    newHistory.push(botMessage);

                    // Play TTS for boss fight responses
                    if (isBossFight && responseData.text) {
                        setTimeout(() => {
                            unlockAudio();
                            speakText(responseData.text, targetLang).catch(err => {
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
                        <div><p className="font-semibold text-gray-800 text-lg">{activeLesson ? "Conversation Challenge" : "Free Tutor Mode"}</p></div>
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
                                            const bossExercise = activeLesson.exercises?.find(ex => ex.type === "conversation_challenge");
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
    const [selectedScenario, setSelectedScenario] = useState(null);
    const t = getT(userProfile.native_language); 

    const handleLessonSelect = (lesson) => { setActiveLesson(lesson); setMainContentView('lesson_detail'); };
    
    // Handle Language Switch with Redirect
    const handleLanguageSwitch = async (newLangCode) => {
        setUserProfile(prev => ({ ...prev, target_language: newLangCode }));
        // Redirect to lessons
        setMainContentView('curriculum');
        try {
            await updateUserProfile(userProfile.user_id, {
                target_language: newLangCode
            });
        } catch (e) {
            console.error("Failed to switch language", e);
        }
    };

    const handleExercisesComplete = async (score, total) => {
        setTempScore({ score, total });
        
        // Check if this is a boss fight lesson - only boss fights go to tutor mode
        const isBossFight = activeLesson && (activeLesson.type === "conversation_challenge" || activeLesson.lesson_id === "A1.1.BOSS" || activeLesson.lesson_id === "A1.2.BOSS" || activeLesson.lesson_id === "A1.3.BOSS" || activeLesson.lesson_id === "A1.4.BOSS" || activeLesson.lesson_id === "A1.5.BOSS" || activeLesson.lesson_id === "A1.6.BOSS");
        
        if (isBossFight) {
            // Boss fight: go to tutor/chat mode
            setMainContentView('tutor');
            setChatHistory([]);
            setGoalAchieved(false);
            setLessonGoal("Loading..."); 
            
            if (activeLesson) {
                try {
                    const responseData = await initiateTutor({
                        target_language: userProfile.target_language,
                        native_language: userProfile.native_language,
                        level: userProfile.level,
                        lesson_id: activeLesson.lesson_id || activeLesson._id || (activeLesson.lesson_id?.includes("A1.6") ? "A1.6.BOSS" : activeLesson.lesson_id?.includes("A1.5") ? "A1.5.BOSS" : activeLesson.lesson_id?.includes("A1.4") ? "A1.4.BOSS" : activeLesson.lesson_id?.includes("A1.3") ? "A1.3.BOSS" : activeLesson.lesson_id?.includes("A1.2") ? "A1.2.BOSS" : "A1.1.BOSS")
                    });

                    const initialMessage = responseData.text;
                    setChatHistory([{ role: 'polybot', text: initialMessage, explanation: responseData.explanation }]);
                    setLessonGoal(responseData.communicative_goal);

                } catch (error) {
                    console.error("Init failed", error);
                    setChatHistory([{ role: 'polybot', text: "Hello! (Connection Error)", explanation: "Start talking." }]);
                }
            }
        } else {
            // Regular lesson: save progress and return to curriculum
            if (activeLesson) {
                try {
                    const responseData = await completeLessonProgress(
                        userProfile.user_id,
                        activeLesson.lesson_id || activeLesson._id,
                        score,
                        total
                    );

                    // Update local state with the returned PROGRESS list
                    setUserProfile(prev => ({
                        ...prev,
                        xp: responseData.new_xp,
                        words_learned: responseData.words_learned,
                        vocabulary_list: responseData.vocabulary_list || prev.vocabulary_list,
                        progress: responseData.progress || prev.progress
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
            const responseData = await completeLessonProgress(
                userProfile.user_id,
                activeLesson.lesson_id || activeLesson._id,
                tempScore.score,
                tempScore.total
            );

            // FIX: Update local state with the returned PROGRESS list
            setUserProfile(prev => ({
                ...prev,
                xp: responseData.new_xp,
                words_learned: responseData.words_learned,
                vocabulary_list: responseData.vocabulary_list || prev.vocabulary_list,
                progress: responseData.progress || prev.progress
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
            case 'settings': return <SettingsView userProfile={userProfile} t={t} />;
            case 'curriculum': return <CurriculumView onSelectLesson={handleLessonSelect} userProfile={userProfile} t={t} />;
            case 'lesson_detail': return activeLesson ? <LessonDetailView lesson={activeLesson} onStartChat={() => {}} onCompleteExercises={handleExercisesComplete} onBack={() => setMainContentView('curriculum')} targetLang={userProfile.target_language} t={t} userProfile={userProfile} /> : <CurriculumView onSelectLesson={handleLessonSelect} userProfile={userProfile} t={t} />;
            case 'scenario_selection':
                return <ScenarioSelectionView
                    onSelectScenario={(scenarioId) => {
                        setSelectedScenario(scenarioId);
                        setMainContentView('scenario_practice');
                    }}
                    onBack={() => setMainContentView('curriculum')}
                    targetLang={userProfile.target_language}
                />;
            case 'scenario_practice':
                return selectedScenario ? <ScenarioPracticeView
                    scenarioId={selectedScenario}
                    targetLang={userProfile.target_language}
                    nativeLang={userProfile.native_language}
                    userProfile={userProfile}
                    onBack={() => setMainContentView('scenario_selection')}
                    onComplete={() => {
                        setSelectedScenario(null);
                        setMainContentView('scenario_selection');
                    }}
                /> : <ScenarioSelectionView
                    onSelectScenario={(scenarioId) => {
                        setSelectedScenario(scenarioId);
                        setMainContentView('scenario_practice');
                    }}
                    onBack={() => setMainContentView('curriculum')}
                    targetLang={userProfile.target_language}
                />;
            case 'tutor': default: 
                // Keep tutor mode for Boss Fight compatibility
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
    }, [mainContentView, userProfile, chatHistory, inputMessage, setInputMessage, handleSendMessage, isLoading, setIsLoading, activeLesson, lessonGoal, goalAchieved, setChatHistory, setGoalAchieved, selectedScenario]);

    return (
        <div className="polybot-background min-h-screen flex flex-col">
            <style jsx="true">{` .polybot-background { background: #f9fafb; } `}</style>
            <header className="bg-white shadow-md p-4 flex justify-between items-center z-10">
                <div className="flex items-center space-x-4"><button onClick={() => setIsSidebarOpen(true)} className="p-2 rounded-full hover:bg-gray-100 md:hidden"><Menu size={24} /></button><h1 className="text-xl font-extrabold text-[#388E3C]">Polybot</h1></div>
                
                <div className="flex items-center space-x-6">
                     <div className="hidden md:flex space-x-2 text-sm font-medium">
                        <button onClick={() => setMainContentView('curriculum')} className="px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-600">{t('lessons')}</button>
                        <button onClick={() => setMainContentView('scenario_selection')} className="px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-600">{t('practice')}</button>
                    </div>

                    {/* Profile Info - Desktop Only */}
                    {userProfile && (
                        <div className="hidden lg:flex items-center gap-3 border-l border-gray-200 pl-6">
                            {/* Avatar */}
                            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-brand-lime-400 to-brand-lime-600 flex items-center justify-center text-white font-bold text-sm shadow-elevation-2">
                                {userProfile.name ? userProfile.name[0].toUpperCase() : 'U'}
                            </div>

                            {/* Name and Level Badge */}
                            <div>
                                <p className="text-sm font-semibold text-gray-800">
                                    {userProfile.name?.split(' ')[0] || 'Learner'}
                                </p>
                                <div className="px-2 py-0.5 bg-teal-50 border border-teal-200 rounded text-xs font-semibold text-teal-700 whitespace-nowrap">
                                    A1 Beginner
                                </div>
                            </div>

                            {/* Streak */}
                            <div className="flex items-center gap-1 ml-2">
                                <span className="text-lg">🔥</span>
                                <span className="text-sm font-semibold text-orange-600">
                                    {userProfile.streak || 0}
                                </span>
                            </div>
                        </div>
                    )}

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

    // Track whether OAuth effect has been processed
    const oauthProcessedRef = useRef(false);

    // Load profile from email (used by OAuth callback and manual registration)
    const handleLoadProfile = useCallback(async (email) => {
        try {
            console.log('[LoadProfile] Loading profile for email:', email);
            const responseData = await getUserProfile(email);
            console.log('[LoadProfile] Profile loaded successfully:', responseData);

            // Validate that response has required fields
            if (!responseData) {
                console.error('[LoadProfile] Response is empty');
                return false;
            }

            // Ensure required fields are present, use defaults if not
            const profileToSet = {
                ...responseData,
                // Ensure these fields have defaults if missing
                target_language: responseData.target_language || 'es',
                native_language: responseData.native_language || 'en',
                progress: responseData.progress || [],
                xp: responseData.xp || 0,
                streak: responseData.streak || 0
            };

            console.log('[LoadProfile] Setting profile:', profileToSet);
            setUserProfile(prev => ({ ...prev, ...profileToSet }));
            console.log('[LoadProfile] Setting view to main');
            setView('main');
            return true;
        } catch (error) {
            console.error('[LoadProfile] Failed to load profile:', error);
            console.error('[LoadProfile] Error details:', error.message, error.response?.data);
            return false;
        }
    }, []);

    // --- CHECK FOR OAUTH RETURN ---
    useEffect(() => {
        // Only run once per page load
        if (oauthProcessedRef.current) {
            console.log('[OAuth] Already processed, skipping');
            return;
        }

        const query = new URLSearchParams(window.location.search);
        const userId = query.get('user_id');

        // Only process if we have a userId (OAuth callback)
        if (!userId) {
            console.log('[OAuth] No userId in URL, skipping');
            return;
        }

        console.log('[OAuth] Processing OAuth callback with userId:', userId);

        // Mark as processed to prevent running again
        oauthProcessedRef.current = true;

        const isNewUser = query.get('new_user') === 'true';
        const error = query.get('error');

        console.log('[OAuth] isNewUser:', isNewUser, 'hasError:', !!error);

        if (error) {
            console.error('[OAuth] Error from backend:', error);
            setErrorMessage(`Login Failed: ${error.replace(/_/g, ' ')}`);
            return;
        }

        const email = query.get('email');
        const name = query.get('name');

        console.log('[OAuth] Email:', email, 'Name:', name);

        // Clear URL param
        window.history.replaceState({}, document.title, "/");

        if (isNewUser) {
            console.log('[OAuth] New user - setting language_setup view');
            setUserProfile(prev => ({ ...prev, user_id: userId, email, name }));
            setView('language_setup');
        } else {
            // Load full profile for returning user
            console.log('[OAuth] Returning user - loading profile');
            handleLoadProfile(email);
        }
    }, [handleLoadProfile]); // Keep handleLoadProfile in deps for safety

    const handleRegister = useCallback(async (isManual = false) => {
        if (!userProfile.name || !userProfile.email) {
            setErrorMessage("Fill all fields.");
            return;
        }
        setErrorMessage('');
        const userId = userProfile.user_id || uuidv4();

        try {
            await registerUser({ ...userProfile, user_id: userId });
            setUserProfile(prev => ({ ...prev, user_id: userId }));

            if (isManual) setView('language_setup');
            else setView('main');
        } catch (error) {
            if (error.response?.status === 409) {
                const loaded = await handleLoadProfile(userProfile.email);
                if (!loaded) setErrorMessage("User exists but couldn't load.");
            } else {
                setErrorMessage("Error registering.");
            }
        }
    }, [userProfile, handleLoadProfile]);
    
    const handleSendMessage = useCallback(async () => { 
        if (!inputMessage.trim() || isLoading) return; 
        const userMsg = { role: 'user', text: inputMessage.trim() }; 
        setChatHistory(prev => [...prev, userMsg]); 
        setInputMessage(''); 
        setIsLoading(true); 
        
        const isBossFight = activeLesson && (activeLesson.type === "conversation_challenge" || activeLesson.lesson_id === "A1.1.BOSS" || activeLesson.lesson_id === "A1.2.BOSS" || activeLesson.lesson_id === "A1.3.BOSS" || activeLesson.lesson_id === "A1.4.BOSS" || activeLesson.lesson_id === "A1.5.BOSS" || activeLesson.lesson_id === "A1.6.BOSS");
        
        try {
            // Use boss fight endpoint if in boss fight mode
            const messagePayload = {
                user_message: userMsg.text,
                chat_history: chatHistory,
                target_language: userProfile.target_language,
                native_language: userProfile.native_language,
                level: userProfile.level,
                lesson_id: activeLesson ? (activeLesson.lesson_id || activeLesson._id) : null
            };

            const responseData = isBossFight
                ? await sendBossFightMessage(messagePayload)
                : await sendTutorMessage(messagePayload);

            // Note: Turn state is managed in ChatTutorView component, not here
            // If turn_number needs to be handled, it should be done in ChatTutorView's handleSendMessage

            const correctionObj = parseCorrectionData(responseData.correction_data);
            if (responseData.status === "GOAL_ACHIEVED") {
                setChatHistory(prev => {
                    const newHistory = [...prev];
                    const lastUserIndex = newHistory.length - 1;
                    if (newHistory[lastUserIndex].role === 'user') {
                        // Don't add corrections in boss fight mode
                        if (!isBossFight) {
                            newHistory[lastUserIndex].correction = correctionObj;
                        }
                    }
                    newHistory.push({ role: 'polybot', text: responseData.text, explanation: "Mission Complete!" }); 
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
                    newHistory.push({ role: 'polybot', text: responseData.text });
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