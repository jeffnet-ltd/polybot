/**
 * Parsing Utilities
 * Helper functions for parsing AI and API responses
 */

/**
 * Parse correction data from AI grammar/spell check responses
 * Extracts corrected text and explanation from formatted AI output
 * @param {string} data - Raw data from AI
 * @returns {Object|null} { corrected, explanation } or null if no correction
 */
export const parseCorrectionData = (data) => {
    if (!data || data === "NO_ERROR" || !data.includes("CORRECTED:")) return null;

    const correctedMatch = data.match(/CORRECTED:\s*([^E]+)/);
    const explanationMatch = data.match(/EXPLANATION:\s*([^\n]+)/);

    if (correctedMatch && explanationMatch) {
        return {
            corrected: correctedMatch[1].trim().replace(/\[|\]/g, ''),
            explanation: explanationMatch[1].trim().replace(/\[|\]/g, '')
        };
    }

    if (data.length > 100 || data.includes("ERROR")) {
        return {
            corrected: "Formatting Error",
            explanation: "AI output corrupted. Check backend logs."
        };
    }

    return null;
};
