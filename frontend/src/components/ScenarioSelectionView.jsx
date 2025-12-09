import React, { useState, useEffect, useCallback } from 'react';
import { Coffee, Clock, TrendingUp, ArrowRight } from 'lucide-react';
import axios from 'axios';

const API = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';

/**
 * ScenarioSelectionView Component
 * Displays available practice scenarios and allows user to select one
 */
const ScenarioSelectionView = ({ onSelectScenario, onBack, targetLang }) => {
    const [scenarios, setScenarios] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchScenarios = useCallback(async () => {
        try {
            setLoading(true);
            const response = await axios.get(`${API}/api/practice/scenarios`, {
                params: { target_language: targetLang }
            });
            setScenarios(response.data.scenarios || response.data);
            setError(null);
        } catch (err) {
            console.error('Error fetching scenarios:', err);
            setError('Failed to load scenarios. Please try again.');
        } finally {
            setLoading(false);
        }
    }, [targetLang]);

    useEffect(() => {
        fetchScenarios();
    }, [fetchScenarios]);

    const handleSelectScenario = (scenarioId) => {
        onSelectScenario(scenarioId);
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center h-full">
                <div className="text-center">
                    <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-4" />
                    <p className="text-gray-600">Loading scenarios...</p>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex items-center justify-center h-full">
                <div className="text-center p-6 bg-red-50 rounded-xl border border-red-200">
                    <p className="text-red-800 mb-4">{error}</p>
                    <button
                        onClick={fetchScenarios}
                        className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition"
                    >
                        Retry
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="p-6 max-w-4xl mx-auto h-full flex flex-col">
            <div className="mb-6">
                <button
                    onClick={onBack}
                    className="text-gray-600 hover:text-gray-800 mb-4 flex items-center"
                >
                    ← Back
                </button>
                <h1 className="text-3xl font-bold text-gray-800 mb-2">Practice Scenarios</h1>
                <p className="text-gray-600">
                    Choose a scenario to practice real-world conversations in {targetLang || 'your target language'}
                </p>
            </div>

            {scenarios.length === 0 ? (
                <div className="flex-1 flex items-center justify-center">
                    <div className="text-center p-8 bg-gray-50 rounded-xl">
                        <p className="text-gray-600 mb-2">No scenarios available</p>
                        <p className="text-sm text-gray-500">Check back soon for new practice scenarios!</p>
                    </div>
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 flex-1 overflow-y-auto">
                    {scenarios.map((scenario) => (
                        <div
                            key={scenario.scenario_id}
                            className="bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-md transition-all duration-200 overflow-hidden flex flex-col"
                        >
                            <div className="p-6 flex-1">
                                <div className="flex items-start justify-between mb-4">
                                    <div className="flex items-center space-x-3">
                                        <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                                            <Coffee className="w-6 h-6 text-blue-600" />
                                        </div>
                                        <div>
                                            <h3 className="text-xl font-bold text-gray-800">
                                                {scenario.title}
                                            </h3>
                                            <span className={`inline-block px-2 py-1 text-xs font-semibold rounded mt-1 ${
                                                scenario.difficulty === 'Beginner' 
                                                    ? 'bg-green-100 text-green-700'
                                                    : scenario.difficulty === 'Intermediate'
                                                    ? 'bg-yellow-100 text-yellow-700'
                                                    : 'bg-red-100 text-red-700'
                                            }`}>
                                                {scenario.difficulty}
                                            </span>
                                        </div>
                                    </div>
                                </div>

                                <p className="text-gray-600 mb-4 line-clamp-3">
                                    {scenario.description}
                                </p>

                                <div className="flex items-center space-x-4 text-sm text-gray-500 mb-4">
                                    <div className="flex items-center space-x-1">
                                        <Clock className="w-4 h-4" />
                                        <span>{scenario.estimated_duration}</span>
                                    </div>
                                </div>
                            </div>

                            <div className="px-6 py-4 bg-gray-50 border-t border-gray-100">
                                <button
                                    onClick={() => handleSelectScenario(scenario.scenario_id)}
                                    className="w-full flex items-center justify-center space-x-2 px-4 py-3 bg-blue-600 text-white rounded-xl font-semibold hover:bg-blue-700 transition transform hover:scale-[1.02] active:scale-[0.98]"
                                >
                                    <span>Start Scenario</span>
                                    <ArrowRight className="w-5 h-5" />
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default ScenarioSelectionView;

