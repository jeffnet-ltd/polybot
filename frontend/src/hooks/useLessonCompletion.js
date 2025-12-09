import { initiateTutor } from '../services/tutorService';
import { completeLessonProgress } from '../services/userService';

/**
 * Custom hook for handling lesson completion logic
 *
 * This hook manages the completion flow for both regular lessons and boss fight lessons.
 * For boss fights, it initiates the tutor mode. For regular lessons, it saves progress
 * and returns to the curriculum view.
 *
 * @param {Object} params - Hook parameters
 * @param {Object} params.activeLesson - The currently active lesson object
 * @param {Object} params.userProfile - The user profile object containing user data
 * @param {Function} params.setMainContentView - State setter for main content view
 * @param {Function} params.setActiveLesson - State setter for active lesson
 * @param {Function} params.setChatHistory - State setter for chat history
 * @param {Function} params.setGoalAchieved - State setter for goal achievement status
 * @param {Function} params.setLessonGoal - State setter for lesson goal
 * @param {Function} params.setUserProfile - State setter for user profile
 *
 * @returns {Object} - Object containing handleExercisesComplete function
 */
const useLessonCompletion = ({
    activeLesson,
    userProfile,
    setMainContentView,
    setActiveLesson,
    setChatHistory,
    setGoalAchieved,
    setLessonGoal,
    setUserProfile
}) => {
    /**
     * Handles the completion of exercises
     *
     * @param {number} score - The score achieved in the exercises
     * @param {number} total - The total possible score
     */
    const handleExercisesComplete = async (score, total) => {
        // Check if this is a boss fight lesson - only boss fights go to tutor mode
        const isBossFight = activeLesson && (
            activeLesson.type === "boss_fight" ||
            activeLesson.lesson_id === "A1.1.BOSS" ||
            activeLesson.lesson_id === "A1.2.BOSS" ||
            activeLesson.lesson_id === "A1.3.BOSS" ||
            activeLesson.lesson_id === "A1.4.BOSS" ||
            activeLesson.lesson_id === "A1.5.BOSS" ||
            activeLesson.lesson_id === "A1.6.BOSS"
        );

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
                        lesson_id: activeLesson.lesson_id || activeLesson._id || (
                            activeLesson.lesson_id?.includes("A1.6") ? "A1.6.BOSS" :
                            activeLesson.lesson_id?.includes("A1.5") ? "A1.5.BOSS" :
                            activeLesson.lesson_id?.includes("A1.4") ? "A1.4.BOSS" :
                            activeLesson.lesson_id?.includes("A1.3") ? "A1.3.BOSS" :
                            activeLesson.lesson_id?.includes("A1.2") ? "A1.2.BOSS" :
                            "A1.1.BOSS"
                        )
                    });

                    const initialMessage = responseData.text;
                    setChatHistory([{
                        role: 'polybot',
                        text: initialMessage,
                        explanation: responseData.explanation
                    }]);
                    setLessonGoal(responseData.communicative_goal);

                } catch (error) {
                    console.error("Init failed", error);
                    setChatHistory([{
                        role: 'polybot',
                        text: "Hello! (Connection Error)",
                        explanation: "Start talking."
                    }]);
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

    return {
        handleExercisesComplete
    };
};

export default useLessonCompletion;
