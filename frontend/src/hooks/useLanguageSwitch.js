import { updateUserProfile } from '../services/userService';

/**
 * Custom hook for handling language switching
 *
 * This hook manages the language switching logic, updating both the local state
 * and persisting the change to the backend.
 *
 * @param {Object} params - Hook parameters
 * @param {Object} params.userProfile - The user profile object containing user data
 * @param {Function} params.setUserProfile - State setter for user profile
 * @param {Function} params.setMainContentView - State setter for main content view
 *
 * @returns {Object} - Object containing handleLanguageSwitch function
 */
const useLanguageSwitch = ({
    userProfile,
    setUserProfile,
    setMainContentView
}) => {
    /**
     * Handles switching to a new target language
     *
     * @param {string} newLangCode - The language code to switch to (e.g., 'es', 'fr', 'de')
     */
    const handleLanguageSwitch = async (newLangCode) => {
        // Update local state immediately for responsive UI
        setUserProfile(prev => ({
            ...prev,
            target_language: newLangCode
        }));

        // Redirect to lessons
        setMainContentView('curriculum');

        // Persist the change to backend
        try {
            await updateUserProfile(userProfile.user_id, {
                target_language: newLangCode
            });
        } catch (e) {
            console.error("Failed to switch language", e);
        }
    };

    return {
        handleLanguageSwitch
    };
};

export default useLanguageSwitch;
