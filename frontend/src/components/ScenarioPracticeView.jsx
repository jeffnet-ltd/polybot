import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Mic, MessageSquare, Send, X, CheckCircle, AlertCircle, Volume2, Target, Languages } from 'lucide-react';
import axios from 'axios';
import PushToTalkButton from './PushToTalkButton';

const API = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

/**
 * ScenarioPracticeView Component
 * Main practice mode view with Voice/Text mode toggle and conversation display
 */
const ScenarioPracticeView = ({ 
    scenarioId, 
    targetLang, 
    nativeLang, 
    userProfile,
    onBack,
    onComplete 
}) => {
    const [mode, setMode] = useState('text'); // 'voice' or 'text'
    const [chatHistory, setChatHistory] = useState([]);
    const [inputMessage, setInputMessage] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [sceneStatus, setSceneStatus] = useState('ACTIVE');
    const [postGameReport, setPostGameReport] = useState(null);
    const [showReport, setShowReport] = useState(false);
    const [userTranscripts, setUserTranscripts] = useState([]);
    const [winningCondition, setWinningCondition] = useState('');
    const [userGoalDescription, setUserGoalDescription] = useState('');
    const [showInstructions, setShowInstructions] = useState(true); // Show instructions first
    const [initialGreeting, setInitialGreeting] = useState(''); // Store greeting until user starts
    const [translationUsed, setTranslationUsed] = useState(false); // Track if translation has been used
    const [showTranslateConfirm, setShowTranslateConfirm] = useState(false); // Show confirmation modal
    const [messageToTranslate, setMessageToTranslate] = useState(null); // Message to translate
    const [translatedMessages, setTranslatedMessages] = useState({}); // Store translations by message index
    const messagesEndRef = useRef(null);
    const audioRef = useRef(null);

    // Define speakText FIRST before it's used in initiateScenario
    const speakText = useCallback(async (text, langCode) => {
        if (!text) return;
        try {
            const response = await fetch(`${API}/api/v1/voice/synthesize`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text, language: langCode }),
            });

            if (!response.ok) throw new Error('TTS failed');

            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const audio = new Audio(url);
            
            return new Promise((resolve, reject) => {
                audio.onended = () => {
                    URL.revokeObjectURL(url);
                    resolve();
                };
                audio.onerror = reject;
                audio.play();
            });
        } catch (error) {
            console.error('TTS error:', error);
        }
    }, []); // No dependencies - API is a constant

    const initiateScenario = useCallback(async () => {
        try {
            setIsLoading(true);
            const response = await axios.post(`${API}/api/practice/initiate`, {
                scenario_id: scenarioId,
                target_language: targetLang,
                native_language: nativeLang
            });

            const greeting = response.data.text;
            // Store the greeting but don't add to chat yet - wait for user to click "Start Conversation"
            setInitialGreeting(greeting);
            setSceneStatus(response.data.scene_status);
            
            // Store the winning condition/goal so user knows what to aim for
            if (response.data.winning_condition) {
                setWinningCondition(response.data.winning_condition);
            }
            // Store the user-friendly goal description for instructions screen
            if (response.data.user_goal_description) {
                console.log('✅ Goal description received:', response.data.user_goal_description.substring(0, 50) + '...');
                setUserGoalDescription(response.data.user_goal_description);
            } else {
                console.warn('⚠️ No user_goal_description in response:', response.data);
                console.warn('Response keys:', Object.keys(response.data));
            }
        } catch (error) {
            console.error('Error initiating scenario:', error);
            alert('Failed to start scenario. Please try again.');
        } finally {
            setIsLoading(false);
        }
    }, [scenarioId, targetLang, nativeLang]);

    useEffect(() => {
        // Always fetch scenario data (goal description) on mount
        initiateScenario();
    }, [initiateScenario]);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [chatHistory]);

    // Handle case where goal description is not available - skip instructions
    // Only skip if we've confirmed there's no goal description after loading completes
    useEffect(() => {
        if (!showInstructions) return; // Already dismissed
        
        // Only skip instructions if we've finished loading AND confirmed no goal description exists
        // Give it a moment to load first - wait 2 seconds after loading completes
        if (!isLoading && !userGoalDescription && initialGreeting) {
            console.log('⚠️ No goal description after loading, waiting before skipping instructions...');
            // Wait a bit to see if goal description arrives
            const timer = setTimeout(() => {
                // Double-check we still don't have goal description
                if (!userGoalDescription && showInstructions) {
                    console.warn('⚠️ Still no goal description after wait, skipping instructions');
                    setShowInstructions(false);
                    setChatHistory([{
                        role: 'polybot',
                        text: initialGreeting,
                        scene_status: 'ACTIVE'
                    }]);
                } else if (userGoalDescription) {
                    console.log('✅ Goal description loaded after wait');
                }
            }, 2000); // Wait 2 seconds for goal description to load
            
            return () => clearTimeout(timer);
        }
    }, [userGoalDescription, isLoading, initialGreeting, showInstructions]);

    const sendTextMessage = async () => {
        if (!inputMessage.trim() || isLoading) return;

        const userMessage = inputMessage.trim();
        setInputMessage('');
        
        // Add user message to history
        const newHistory = [...chatHistory, { role: 'user', text: userMessage }];
        setChatHistory(newHistory);

        try {
            setIsLoading(true);
            const response = await axios.post(`${API}/api/practice/text-chat`, {
                scenario_id: scenarioId,
                user_message: userMessage,
                conversation_history: chatHistory,
                target_language: targetLang,
                native_language: nativeLang
            });

            const reply = response.data.reply;
            const status = response.data.scene_status;

            // Add AI response
            setChatHistory([...newHistory, {
                role: 'polybot',
                text: reply,
                scene_status: status,
                thought: response.data.thought
            }]);

            setSceneStatus(status);

            // If complete, generate post-game report
            if (status === 'COMPLETE') {
                await generatePostGameReport(newHistory);
            }
        } catch (error) {
            console.error('Error sending message:', error);
            alert('Failed to send message. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    const handleVoiceRecording = async (audioBlob) => {
        try {
            setIsLoading(true);

            // Create FormData
            const formData = new FormData();
            formData.append('file', audioBlob, 'recording.webm');
            formData.append('scenario_id', scenarioId);
            formData.append('conversation_history', JSON.stringify(chatHistory));
            formData.append('target_language', targetLang);
            formData.append('native_language', nativeLang);

            const response = await fetch(`${API}/api/practice/voice-chat`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Voice chat failed: ${response.status}`);
            }

            // Get transcript and reply from headers
            const transcript = response.headers.get('X-Polybot-Transcript') || '';
            const replyText = response.headers.get('X-Polybot-Reply-Text') || '';
            const status = response.headers.get('X-Polybot-Scene-Status') || 'ACTIVE';
            const confidence = parseFloat(response.headers.get('X-Polybot-Confidence') || '0');

            // Add user message
            const newHistory = [...chatHistory, { role: 'user', text: transcript }];
            setChatHistory(newHistory);

            // Store transcript with confidence
            setUserTranscripts([...userTranscripts, {
                text: transcript,
                confidence: confidence,
                phonetic_score: 0.0 // Would need to calculate this separately
            }]);

            // Get audio blob
            const audioBlobResponse = await response.blob();
            const audioUrl = URL.createObjectURL(audioBlobResponse);
            
            // Play audio
            const audio = new Audio(audioUrl);
            await new Promise((resolve, reject) => {
                audio.onended = () => {
                    URL.revokeObjectURL(audioUrl);
                    resolve();
                };
                audio.onerror = reject;
                audio.play();
            });

            // Add AI response
            setChatHistory([...newHistory, {
                role: 'polybot',
                text: replyText,
                scene_status: status
            }]);

            setSceneStatus(status);

            // If complete, generate post-game report
            if (status === 'COMPLETE') {
                await generatePostGameReport(newHistory);
            }
        } catch (error) {
            console.error('Error with voice chat:', error);
            alert('Failed to process voice message. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    const generatePostGameReport = async (conversationHistory) => {
        try {
            // Build conversation transcript
            const transcript = conversationHistory
                .map(msg => `${msg.role === 'user' ? 'User' : 'AI'}: ${msg.text}`)
                .join('\n');

            const response = await axios.post(`${API}/api/practice/post-game-report`, {
                scenario_id: scenarioId,
                conversation_transcript: transcript,
                user_transcripts: userTranscripts,
                target_language: targetLang,
                native_language: nativeLang
            });

            setPostGameReport(response.data);
            setShowReport(true);
        } catch (error) {
            console.error('Error generating post-game report:', error);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendTextMessage();
        }
    };

    const handleTranslateConfirm = async () => {
        if (!messageToTranslate) return;
        
        setShowTranslateConfirm(false);
        setIsLoading(true);
        
        try {
            const response = await axios.post(`${API}/api/practice/translate`, {
                text: messageToTranslate.text,
                target_language: targetLang,
                native_language: nativeLang
            });
            
            setTranslatedMessages(prev => ({
                ...prev,
                [messageToTranslate.index]: response.data.translation
            }));
            setTranslationUsed(true);
            setMessageToTranslate(null);
        } catch (error) {
            console.error('Error translating message:', error);
            alert('Failed to translate message. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    // Show instructions screen first (or loading if goal not yet loaded)
    if (showInstructions) {
        // Show loading state while fetching goal description
        if (!userGoalDescription && isLoading) {
            return (
                <div className="h-full flex flex-col bg-gray-50 items-center justify-center">
                    <div className="text-center">
                        <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
                        <p className="text-gray-600">Loading scenario...</p>
                    </div>
                </div>
            );
        }
        
        // Show instructions if we have the goal description
        if (userGoalDescription) {
            return (
            <div className="h-full flex flex-col bg-gray-50">
                <div className="flex-1 overflow-y-auto p-6">
                    <div className="max-w-3xl mx-auto">
                        <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-8">
                            <div className="flex items-center space-x-3 mb-6">
                                <Target className="w-8 h-8 text-blue-600" />
                                <h2 className="text-2xl font-bold text-gray-800">Your Mission</h2>
                            </div>
                            
                            <div className="prose prose-blue max-w-none mb-6">
                                <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mb-4">
                                    <p className="text-gray-700 whitespace-pre-line leading-relaxed">
                                        {userGoalDescription}
                                    </p>
                                </div>
                            </div>

                            <div className="bg-gray-50 rounded-xl p-4 mb-6">
                                <h3 className="text-sm font-semibold text-gray-700 mb-2">Quick Tips:</h3>
                                <ul className="text-sm text-gray-600 space-y-1 list-disc list-inside">
                                    <li>Listen carefully to the barista's questions</li>
                                    <li>Use context clues to understand unfamiliar words</li>
                                    <li>You can translate one message if you're stuck</li>
                                    <li>Complete all steps to finish the scenario</li>
                                </ul>
                            </div>

                            <button
                                onClick={() => {
                                    setShowInstructions(false);
                                    // Now start the conversation with the stored greeting
                                    if (initialGreeting) {
                                        setChatHistory([{
                                            role: 'polybot',
                                            text: initialGreeting,
                                            scene_status: 'ACTIVE'
                                        }]);
                                        // Play audio for initial greeting if in voice mode
                                        if (mode === 'voice') {
                                            speakText(initialGreeting, targetLang);
                                        }
                                    }
                                }}
                                className="w-full py-3 bg-blue-600 text-white rounded-xl font-semibold hover:bg-blue-700 transition shadow-md"
                            >
                                Start Conversation
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            );
        }
        
        // If no goal description but not loading, show loading (will be handled by useEffect)
        return (
            <div className="h-full flex flex-col bg-gray-50 items-center justify-center">
                <div className="text-center">
                    <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
                    <p className="text-gray-600">Loading scenario...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="h-full flex flex-col bg-gray-50">
            {/* Header with Mode Toggle */}
            <div className="bg-white border-b border-gray-200 p-4">
                <div className="flex items-center justify-between max-w-4xl mx-auto">
                    <button
                        onClick={onBack}
                        className="text-gray-600 hover:text-gray-800"
                    >
                        ← Back
                    </button>

                    <div className="flex items-center space-x-4">
                        <span className="text-sm text-gray-600">Mode:</span>
                        <div className="flex bg-gray-100 rounded-lg p-1">
                            <button
                                onClick={() => setMode('voice')}
                                className={`px-4 py-2 rounded-md flex items-center space-x-2 transition ${
                                    mode === 'voice'
                                        ? 'bg-blue-600 text-white'
                                        : 'text-gray-600 hover:text-gray-800'
                                }`}
                            >
                                <Mic className="w-4 h-4" />
                                <span>Voice</span>
                            </button>
                            <button
                                onClick={() => setMode('text')}
                                className={`px-4 py-2 rounded-md flex items-center space-x-2 transition ${
                                    mode === 'text'
                                        ? 'bg-blue-600 text-white'
                                        : 'text-gray-600 hover:text-gray-800'
                                }`}
                            >
                                <MessageSquare className="w-4 h-4" />
                                <span>Text</span>
                            </button>
                        </div>

                        <div className={`px-3 py-1 rounded-full text-xs font-semibold ${
                            sceneStatus === 'COMPLETE'
                                ? 'bg-green-100 text-green-700'
                                : 'bg-blue-100 text-blue-700'
                        }`}>
                            {sceneStatus === 'COMPLETE' ? 'Complete' : 'Active'}
                        </div>
                    </div>
                </div>
            </div>

            {/* Goal Display - Brief reminder above chat */}
            {winningCondition && sceneStatus === 'ACTIVE' && (
                <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border-b border-blue-200 px-4 py-2">
                    <div className="max-w-4xl mx-auto">
                        <div className="flex items-center space-x-2">
                            <Target className="w-4 h-4 text-blue-600 flex-shrink-0" />
                            <p className="text-xs text-blue-800">
                                <span className="font-semibold">Goal:</span> Place your order, choose seating (al banco/al tavolo), and complete the transaction
                            </p>
                        </div>
                    </div>
                </div>
            )}

            {/* Conversation Display */}
            <div className="flex-1 overflow-y-auto p-4">
                <div className="max-w-4xl mx-auto space-y-4">
                    {chatHistory.map((msg, idx) => (
                        <div
                            key={idx}
                            className={`flex flex-col ${msg.role === 'user' ? 'items-end' : 'items-start'}`}
                        >
                            <div
                                className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                                    msg.role === 'user'
                                        ? 'bg-blue-600 text-white'
                                        : 'bg-white text-gray-800 border border-gray-200'
                                }`}
                            >
                                <p className="whitespace-pre-wrap">{msg.text}</p>
                                {translatedMessages[idx] && (
                                    <div className="mt-2 pt-2 border-t border-gray-300">
                                        <p className="text-sm text-gray-600 italic">{translatedMessages[idx]}</p>
                                    </div>
                                )}
                            </div>
                            {msg.role === 'polybot' && !translationUsed && (
                                <button
                                    onClick={() => {
                                        setMessageToTranslate({ index: idx, text: msg.text });
                                        setShowTranslateConfirm(true);
                                    }}
                                    className="mt-1 text-xs text-blue-600 hover:text-blue-800 flex items-center space-x-1"
                                >
                                    <Languages className="w-3 h-3" />
                                    <span>Translate</span>
                                </button>
                            )}
                        </div>
                    ))}
                    {isLoading && (
                        <div className="flex justify-start">
                            <div className="bg-white rounded-2xl px-4 py-3 border border-gray-200">
                                <div className="flex items-center space-x-2">
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }} />
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }} />
                                </div>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>
            </div>

            {/* Translation Confirmation Modal */}
            {showTranslateConfirm && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
                    <div className="bg-white rounded-2xl p-6 max-w-md mx-4 shadow-xl">
                        <h3 className="text-xl font-bold text-gray-800 mb-4">Confirm Translation</h3>
                        <p className="text-gray-600 mb-4">
                            You only have <strong>one translation</strong> available for this entire conversation. Are you sure you want to use it now?
                        </p>
                        <div className="flex space-x-3">
                            <button
                                onClick={() => {
                                    setShowTranslateConfirm(false);
                                    setMessageToTranslate(null);
                                }}
                                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition"
                            >
                                Cancel
                            </button>
                            <button
                                onClick={handleTranslateConfirm}
                                className="flex-1 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                            >
                                Yes, Translate
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Input Area - Mode Dependent */}
            {sceneStatus !== 'COMPLETE' && (
                <div className="bg-white border-t border-gray-200 p-4">
                    <div className="max-w-4xl mx-auto">
                        {mode === 'text' ? (
                            <div className="flex items-center space-x-2">
                                <input
                                    type="text"
                                    value={inputMessage}
                                    onChange={(e) => setInputMessage(e.target.value)}
                                    onKeyPress={handleKeyPress}
                                    placeholder="Type your message..."
                                    className="flex-1 px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    disabled={isLoading}
                                />
                                <button
                                    onClick={sendTextMessage}
                                    disabled={!inputMessage.trim() || isLoading}
                                    className="px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition flex items-center space-x-2"
                                >
                                    <Send className="w-5 h-5" />
                                </button>
                            </div>
                        ) : (
                            <div className="flex flex-col items-center space-y-4">
                                <PushToTalkButton
                                    onRecordingComplete={handleVoiceRecording}
                                    onError={(error) => alert(error.message)}
                                    disabled={isLoading}
                                />
                                <p className="text-sm text-gray-600">
                                    Hold to record, release to send
                                </p>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Post-Game Report Modal */}
            {showReport && postGameReport && (
                <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
                    <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
                        <div className="p-6">
                            <div className="flex items-center justify-between mb-6">
                                <h2 className="text-2xl font-bold text-gray-800">Practice Report</h2>
                                <button
                                    onClick={() => {
                                        setShowReport(false);
                                        if (onComplete) onComplete();
                                    }}
                                    className="text-gray-400 hover:text-gray-600"
                                >
                                    <X className="w-6 h-6" />
                                </button>
                            </div>

                            {/* Pronunciation Feedback */}
                            <div className="mb-6 p-4 bg-blue-50 rounded-xl">
                                <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                                    <Volume2 className="w-5 h-5 mr-2" />
                                    Pronunciation
                                </h3>
                                <p className="text-gray-700">{postGameReport.pronunciation.feedback}</p>
                                <p className="text-sm text-gray-600 mt-2">
                                    Score: {(postGameReport.pronunciation.overall_score * 100).toFixed(0)}%
                                </p>
                            </div>

                            {/* Grammar Feedback */}
                            {postGameReport.grammar.errors.length > 0 && (
                                <div className="mb-6 p-4 bg-amber-50 rounded-xl">
                                    <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                                        <AlertCircle className="w-5 h-5 mr-2" />
                                        Grammar
                                    </h3>
                                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                                        {postGameReport.grammar.errors.map((error, idx) => (
                                            <li key={idx}>{error}</li>
                                        ))}
                                    </ul>
                                </div>
                            )}

                            {/* Vocabulary Suggestions */}
                            {postGameReport.vocabulary.suggestions.length > 0 && (
                                <div className="mb-6 p-4 bg-green-50 rounded-xl">
                                    <h3 className="font-semibold text-gray-800 mb-2 flex items-center">
                                        <CheckCircle className="w-5 h-5 mr-2" />
                                        Vocabulary Suggestions
                                    </h3>
                                    <ul className="list-disc list-inside space-y-1 text-gray-700">
                                        {postGameReport.vocabulary.suggestions.map((suggestion, idx) => (
                                            <li key={idx}>{suggestion}</li>
                                        ))}
                                    </ul>
                                </div>
                            )}

                            <div className="flex space-x-4">
                                <button
                                    onClick={() => {
                                        setShowReport(false);
                                        if (onComplete) onComplete();
                                    }}
                                    className="flex-1 px-4 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition"
                                >
                                    Done
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

export default ScenarioPracticeView;

