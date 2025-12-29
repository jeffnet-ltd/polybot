/**
 * MiniPromptExercise Component
 *
 * A context-based language exercise where users respond to specific scenarios. It
 * features intelligent, client-side validation for various contexts like greetings,
 * introductions, and ordering, providing instant and pedagogically-focused feedback.
 */
import React, { useState, useRef, useCallback } from 'react';
import { Loader2 } from 'lucide-react';
import AccentedLetterChips from '../common/AccentedLetterChips';
import { sendTutorMessage } from '../../services/tutorService';

const MiniPromptExercise = ({ prompt, context, task, targetLang, nativeLang, onAnswer, explanation }) => {
    const [userInput, setUserInput] = useState("");
    const [isProcessing, setIsProcessing] = useState(false);
    const [isComplete, setIsComplete] = useState(false);
    const textareaRef = useRef(null);

    // Italian number word to digit mapping (ages 0-99)
    const italianNumberMap = {
        'zero': 0, 'uno': 1, 'un': 1, 'due': 2, 'tre': 3, 'quattro': 4,
        'cinque': 5, 'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10,
        'undici': 11, 'dodici': 12, 'tredici': 13, 'quattordici': 14,
        'quindici': 15, 'sedici': 16, 'diciassette': 17, 'diciotto': 18,
        'diciannove': 19, 'venti': 20, 'ventuno': 21, 'ventidue': 22,
        'ventitre': 23, 'ventiquattro': 24, 'venticinque': 25, 'ventisei': 26,
        'ventisette': 27, 'ventotto': 28, 'ventinove': 29, 'trenta': 30,
        'trentuno': 31, 'trentadue': 32, 'trentatre': 33, 'trentaquattro': 34,
        'trentacinque': 35, 'trentasei': 36, 'trentasette': 37, 'trentotto': 38,
        'trentanove': 39, 'quaranta': 40, 'cinquanta': 50, 'sessanta': 60,
        'settanta': 70, 'ottanta': 80, 'novanta': 90
    };

    /**
     * Normalizes Italian number words to digits for comparison
     * Accepts both "nove" and "9" as valid
     */
    const normalizeItalianNumbers = (text) => {
        let normalized = text.toLowerCase().trim();

        // Replace Italian number words with digits
        Object.entries(italianNumberMap).forEach(([word, digit]) => {
            const regex = new RegExp(`\\b${word}\\b`, 'gi');
            normalized = normalized.replace(regex, digit.toString());
        });

        return normalized;
    };

    /**
     * Normalizes apostrophes for reliable regex matching
     * Converts both straight (U+0027) and curly (U+2019) apostrophes to straight
     * This ensures regex patterns work regardless of input apostrophe type
     */
    const normalizeApostrophes = (text) => {
        // Replace all curly apostrophes (U+2019) and other variants with straight apostrophe (U+0027)
        return text.replace(/[''´`]/g, "'");
    };

    const validateResponse = useCallback((input, validationContext, validationTask) => {
        // Normalize apostrophes first to handle both straight (') and curly (') characters
        const normalizedInput = normalizeApostrophes(input);
        const userLower = normalizedInput.toLowerCase().trim();
        const contextLower = (validationContext || '').toLowerCase();
        const taskLower = (validationTask || '').toLowerCase();

        // --- Context-Specific Validation Rules ---

        if (contextLower.includes("piacere")) { // Introduction
            const hasMiChiamo = userLower.includes("mi chiamo");
            const hasSonoIntro = userLower.startsWith("sono ") || (userLower.includes("sono ") && userLower.indexOf("sono ") < 5);
            const hasPiacere = userLower.includes("piacere");

            let hasMiChiamoWithName = false;
            if (hasMiChiamo) {
                const afterMiChiamo = userLower.split("mi chiamo")[1]?.trim();
                hasMiChiamoWithName = afterMiChiamo && afterMiChiamo.length > 0 && !afterMiChiamo.match(/^[.,!?;:]+$/);
            }

            const hasValidIntroduction = hasMiChiamoWithName || hasSonoIntro || (hasPiacere && userLower.length > 7);
            if (hasValidIntroduction) {
                return { status: 'correct', explanation: `Great! You included your name and greeting. Perfect introduction.` };
            }
            return { status: 'incorrect', explanation: `When someone says "Piacere", you should introduce yourself. Try "Mi chiamo [your name]" or "Sono [your name]".` };
        }

        if (contextLower.includes("friend") && taskLower.includes("greet")) { // Informal Greeting
            const hasInformal = userLower.includes("ciao") || userLower.includes("come stai") || userLower.includes("come va");
            const hasFormal = userLower.includes("buongiorno") || userLower.includes("buonasera");

            if (hasInformal && !hasFormal) {
                return { status: 'correct', explanation: `Perfect! "${userInput}" is a great informal greeting for a friend.` };
            }
            if (hasInformal && hasFormal) {
                return { status: 'almost', explanation: `You're close! You used both formal and informal greetings. With friends, just stick to informal ones like "Ciao".` };
            }
            return { status: 'incorrect', explanation: `For a friend, use an informal greeting like "Ciao" or "Come stai?".` };
        }

        if (contextLower.includes("professor") || contextLower.includes("dr.") || contextLower.includes("7 pm")) { // Formal Greeting
            const hasFormal = userLower.includes("buongiorno") || userLower.includes("buonasera") || userLower.includes("salve");
            const hasInformal = userLower.includes("ciao") && !userLower.includes("buongiorno");

            if (hasFormal && !hasInformal) {
                return { status: 'correct', explanation: `Excellent! Using a formal greeting like "${userInput}" is perfect for this situation.` };
            }
            if (hasFormal && hasInformal) {
                return { status: 'almost', explanation: `Good effort, but you mixed formal and informal greetings. Stick to just the formal one in this context.` };
            }
            return { status: 'incorrect', explanation: `This situation requires a formal greeting like "Buongiorno" or "Buonasera".` };
        }

        if (contextLower.includes("café") && taskLower.includes("order")) { // Ordering Coffee
            const hasCaffe = userLower.includes("caffè");
            const hasWrongAccent = userLower.includes("caffé");
            const hasPerFavore = userLower.includes("per favore");

            if (hasCaffe && hasPerFavore) {
                return { status: 'correct', explanation: `Perfect! "Un caffè per favore" is exactly how you order a coffee politely.` };
            }
            if (hasCaffe && !hasPerFavore) {
                return { status: 'almost', explanation: `You're so close! You ordered the coffee, but remember to add "per favore" to be polite.` };
            }
            if (hasWrongAccent) {
                return { status: 'almost', explanation: `Great try! Just a small correction: the accent on "caffè" goes the other way (è, not é).` };
            }
            return { status: 'incorrect', explanation: `To order a coffee, you can say "Un caffè per favore".` };
        }

        // Residence questions (where you LIVE)
        if (contextLower.includes("dove vivi") || contextLower.includes("dove abiti") ||
            contextLower.includes("where do you live") || contextLower.includes("where you live") ||
            taskLower.includes("live in")) {

            const hasVivo = /\bvivo\b/.test(userLower);
            const hasAbito = /\babito\b/.test(userLower);

            // Check for BOTH preposition patterns
            const hasPrepositionA = / a /.test(userLower);  // City names: "a Roma"
            const hasPrepositionIn = / in /.test(userLower);  // Dwelling types/locations: "in un appartamento", "in città"
            const hasPreposition = hasPrepositionA || hasPrepositionIn;

            // Check for dwelling type keywords (when "in" is used)
            const dwellingKeywords = ['appartamento', 'casa'];
            const hasDwellingType = dwellingKeywords.some(dwelling => userLower.includes(dwelling));

            // Check for location keywords (città, campagna, etc.)
            const locationKeywords = ['città', 'campagna'];
            const hasLocationKeyword = locationKeywords.some(loc => userLower.includes(loc));

            const hasLocation = userLower.length > 10; // Rough check for location name

            // Valid patterns:
            // 1. "Vivo a Roma" (preposition "a" + city name)
            // 2. "Vivo in un appartamento" (preposition "in" + dwelling type)
            // 3. "Vivo in città" (preposition "in" + general location)
            // 4. "Vivo in un appartamento in città" (combination)

            if ((hasVivo || hasAbito) && hasPreposition && hasLocation) {
                // Check if the preposition matches the pattern
                if (hasPrepositionIn && (hasDwellingType || hasLocationKeyword)) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly used "in" with a dwelling type or location: "${userInput}".`
                    };
                }
                if (hasPrepositionA) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly stated where you live: "${userInput}".`
                    };
                }
                // Has preposition but doesn't match expected pattern - still accept it
                return {
                    status: 'correct',
                    explanation: `Perfect! You correctly stated where you live: "${userInput}".`
                };
            }

            if (hasVivo || hasAbito) {
                return {
                    status: 'almost',
                    explanation: `Good start! Use "Vivo in un appartamento" or "Vivo a [city]". Examples: "Vivo in un appartamento in città" or "Vivo a Roma".`
                };
            }

            return {
                status: 'incorrect',
                explanation: `To say where you live, use "Vivo in [dwelling]" or "Vivo a [city]". Examples: "Vivo in un appartamento" or "Vivo a Roma".`
            };
        }

        if (contextLower.includes("di dove") || contextLower.includes("where are you from") ||
            contextLower.includes("where you're from") || taskLower.includes("where you're from") ||
            (contextLower.includes("from") && !contextLower.includes("live"))) { // Origin/Location Question
            const hasSonoDi = userLower.includes("sono di");
            const hasVengoDa = userLower.includes("vengo da");
            const hasCountryMention = userLower.length > 10; // Rough check for country name

            if ((hasSonoDi || hasVengoDa) && hasCountryMention) {
                return { status: 'correct', explanation: `Perfect! You correctly answered where you're from using "${userInput}".` };
            }
            if (hasSonoDi || hasVengoDa) {
                return { status: 'almost', explanation: `Good! You used the right structure. Make sure to include the country name.` };
            }
            return { status: 'incorrect', explanation: `To answer where you're from, use "Sono di [country]" or "Vengo da [country]".` };
        }

        // Age-related exercises (e.g., "You are roleplaying as a 9-year-old")
        if (contextLower.includes("year") || contextLower.includes("old") ||
            contextLower.includes("roleplaying as a") || contextLower.includes("anni") ||
            taskLower.includes("years old") || taskLower.includes("age")) {

            // Normalize numbers in user input (converts "nove" → "9")
            const normalizedInput = normalizeItalianNumbers(userLower);

            // Check for age statement pattern: "ho [number] anni"
            const hasHo = normalizedInput.includes("ho ");
            const hasAnni = userLower.includes("anni");

            // Extract any number (word or digit) from input
            const numberMatch = normalizedInput.match(/\b(\d+)\b/);
            const hasNumber = numberMatch !== null;

            if (targetLang === 'it') {
                // Italian validation
                if (hasHo && hasAnni && hasNumber) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly stated your age: "Ho ${numberMatch[1]} anni."`
                    };
                }

                // Provide helpful feedback for common mistakes
                if (!hasHo) {
                    return {
                        status: 'incorrect',
                        explanation: `Remember to start with "Ho" (I have). Try: "Ho [number] anni."`
                    };
                }
                if (!hasAnni) {
                    return {
                        status: 'incorrect',
                        explanation: `Don't forget "anni" (years). Try: "Ho [number] anni."`
                    };
                }
                if (!hasNumber) {
                    return {
                        status: 'incorrect',
                        explanation: `Include your age as a number. Try: "Ho [number] anni."`
                    };
                }
            }

            // For other languages, check for basic age pattern
            if (hasNumber) {
                return {
                    status: 'correct',
                    explanation: `Great! You stated your age.`
                };
            }

            return {
                status: 'incorrect',
                explanation: `Try stating your age with a number.`
            };
        }

        // Family member introduction exercises (questo/questa è mio/mia + family member)
        if (contextLower.includes("photo") || contextLower.includes("introduce") ||
            contextLower.includes("father") || contextLower.includes("mother") ||
            contextLower.includes("brother") || contextLower.includes("sister") ||
            contextLower.includes("showing") ||
            taskLower.includes("this is my")) {

            // Family member keywords (all 13 family members from A1.2)
            const familyMembers = [
                'padre', 'madre', 'fratello', 'sorella', 'famiglia',
                'nonno', 'nonna', 'zio', 'zia',
                'cugino', 'cugina', 'figlio', 'figlia'
            ];

            // Check for introduction pattern
            const hasQuesto = userLower.includes('questo') || userLower.includes('questa');
            const hasE = /\bè\b|\be\b/.test(userLower);
            const hasPossessive = /\b(mio|mia|tuo|tua|suo|sua)\b/.test(userLower);
            const hasFamilyMember = familyMembers.some(member =>
                new RegExp(`\\b${member}\\b`).test(userLower)
            );

            if (hasQuesto && hasE && hasPossessive && hasFamilyMember) {
                // Validate gender agreement: questo/questa with family member
                const masculineMembers = ['padre', 'fratello', 'nonno', 'zio', 'cugino', 'figlio'];
                const feminineMembers = ['madre', 'sorella', 'nonna', 'zia', 'cugina', 'figlia'];

                const hasMasculineMember = masculineMembers.some(m =>
                    new RegExp(`\\b${m}\\b`).test(userLower)
                );
                const hasFeminineMember = feminineMembers.some(m =>
                    new RegExp(`\\b${m}\\b`).test(userLower)
                );

                const hasQuesto_check = userLower.includes('questo');
                const hasQuesta_check = userLower.includes('questa');

                // Check gender agreement
                if ((hasMasculineMember && hasQuesto_check) || (hasFeminineMember && hasQuesta_check)) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly introduced your family member: "${userInput}".`
                    };
                }

                // Wrong gender agreement
                if ((hasMasculineMember && hasQuesta_check) || (hasFeminineMember && hasQuesto_check)) {
                    return {
                        status: 'almost',
                        explanation: `Good structure! But check the gender: use "questo" for masculine family members (padre, fratello, nonno) and "questa" for feminine (madre, sorella, nonna).`
                    };
                }
            }

            // Has possessive + family member but missing introduction structure
            if (hasPossessive && hasFamilyMember) {
                return {
                    status: 'almost',
                    explanation: `Good! You mentioned the family member. Try the full introduction: "Questo/Questa è mio/mia [family member]".`
                };
            }

            // Has family member but missing possessive
            if (hasFamilyMember) {
                return {
                    status: 'almost',
                    explanation: `You mentioned a family member. Don't forget the possessive: "Questo è mio padre" or "Questa è mia madre".`
                };
            }
        }

        // Family description/composition exercises (Ho + family member pattern)
        if ((contextLower.includes("family") && contextLower.includes("describe")) ||
            taskLower.includes("say you have")) {

            const hasHo = /\bho\b/.test(userLower);
            const familyMembers = ['padre', 'madre', 'fratello', 'sorella', 'famiglia',
                                  'nonno', 'nonna', 'zio', 'zia',
                                  'cugino', 'cugina', 'figlio', 'figlia'];

            const hasFamilyMember = familyMembers.some(member =>
                new RegExp(`\\b${member}\\b`).test(userLower)
            );

            if (hasHo && hasFamilyMember) {
                // Basic validation - structure is correct
                return {
                    status: 'correct',
                    explanation: `Good! You described your family using "Ho" with family members: "${userInput}".`
                };
            }

            if (hasFamilyMember) {
                return {
                    status: 'almost',
                    explanation: `Good! You mentioned family members. Use "Ho" (I have) to describe your family: "Ho una nonna e una cugina".`
                };
            }

            if (hasHo) {
                return {
                    status: 'almost',
                    explanation: `Good start with "Ho"! Now add the family members you have.`
                };
            }
        }

        // Profession/Occupation exercises (job responses)
        if (contextLower.includes("student") || contextLower.includes("job") || contextLower.includes("do") ||
            contextLower.includes("lavoro") || contextLower.includes("fai") ||
            taskLower.includes("reply") && (taskLower.includes("student") || taskLower.includes("job")) ||
            userLower.includes("faccio") || userLower.includes("sono")) {

            // Profession keywords in Italian (all genders)
            const professions = [
                'studente', 'studentessa', 'insegnante', 'professore', 'professoressa',
                'dottore', 'dottoressa', 'infermiere', 'infermiera', 'impiegato', 'impiegata',
                'ingegnere', 'avvocato', 'avvocata', 'architetto', 'architetta'
            ];

            // Check if user mentioned a profession
            const hasProfession = professions.some(prof => userLower.includes(prof));

            // Check if response includes occupation structure (Faccio/Sono + article + profession)
            const hasFaccio = userLower.includes('faccio');
            const hasSono = userLower.includes('sono');
            const hasArticle = /\b(un|una|il|lo|la|l')\b/.test(userLower);

            if ((hasFaccio || hasSono) && hasProfession) {
                // Check gender context if provided
                const isFemaleContext = contextLower.includes('female') || contextLower.includes('woman') || contextLower.includes('donna');
                const isMaleContext = (contextLower.includes('male') || contextLower.includes('man') || contextLower.includes('uomo')) && !contextLower.includes('female');

                // Check if the profession gender matches context
                const feminineProfs = ['studentessa', 'professoressa', 'dottoressa', 'infermiera', 'impiegata'];
                const masculineProfs = ['studente', 'professore', 'dottore', 'infermiere', 'impiegato'];
                const unisexProfs = ['insegnante', 'ingegnere', 'avvocato', 'architetto'];

                const hasFeminineProfession = feminineProfs.some(prof => new RegExp(`\\b${prof}\\b`).test(userLower));
                const hasMasculineProfession = masculineProfs.some(prof => new RegExp(`\\b${prof}\\b`).test(userLower));

                let mismatch = false;
                if (isFemaleContext && hasMasculineProfession && !unisexProfs.some(prof => new RegExp(`\\b${prof}\\b`).test(userLower))) {
                    mismatch = true;
                }
                if (isMaleContext && hasFeminineProfession && !unisexProfs.some(prof => new RegExp(`\\b${prof}\\b`).test(userLower))) {
                    mismatch = true;
                }

                if (mismatch) {
                    return {
                        status: 'almost',
                        explanation: isFemaleContext ?
                            `Good effort! You mentioned a job, but for a female, use the feminine form (e.g., insegnante, dottoressa, impiegata, studentessa).` :
                            `Good effort! You mentioned a job, but for a male, use the masculine form (e.g., professore, dottore, infermiere, studente).`
                    };
                }

                return {
                    status: 'correct',
                    explanation: `Perfect! You correctly stated your profession: "${userInput}". Both "Faccio" and "Sono" can be used with professions!`
                };
            }

            // Has profession but missing proper structure
            if (hasProfession) {
                return {
                    status: 'almost',
                    explanation: `Good! You mentioned a profession. Try using "Faccio" or "Sono" with the profession: "Faccio una studentessa" or "Sono insegnante".`
                };
            }
        }

        // Number-only exercises (phone numbers, room numbers, registration numbers, etc.)
        if (contextLower.includes("numero") || contextLower.includes("registration") ||
            contextLower.includes("room number") || taskLower.includes("number between") ||
            taskLower.includes("respond with a number")) {

            // Normalize numbers in user input (converts "quindici" → "15")
            const normalizedInput = normalizeItalianNumbers(userLower);

            // Extract any number (word or digit) from input
            const numberMatch = normalizedInput.match(/\b(\d+)\b/);
            const hasNumber = numberMatch !== null;

            // Check if task specifies a range (e.g., "number between 11 and 20")
            const rangeMatch = taskLower.match(/between\s+(\d+)\s+and\s+(\d+)/);

            if (hasNumber) {
                const userNumber = parseInt(numberMatch[1]);

                // If range specified, validate number is in range
                if (rangeMatch) {
                    const minNum = parseInt(rangeMatch[1]);
                    const maxNum = parseInt(rangeMatch[2]);

                    if (userNumber >= minNum && userNumber <= maxNum) {
                        return {
                            status: 'correct',
                            explanation: `Perfect! You correctly provided a number in Italian: "${userInput}".`
                        };
                    } else {
                        return {
                            status: 'incorrect',
                            explanation: `Good use of Italian numbers! But please provide a number between ${minNum} and ${maxNum}.`
                        };
                    }
                }

                // No range specified, any number is correct
                return {
                    status: 'correct',
                    explanation: `Perfect! You correctly provided a number in Italian: "${userInput}".`
                };
            }

            // User didn't provide a number
            return {
                status: 'incorrect',
                explanation: `Please respond with a number in Italian. Example: undici, dodici, tredici, etc.`
            };
        }

        // "C'è" (there is) and "Ci sono" (there are) constructions - showing rooms/objects
        if (contextLower.includes("cucina") || contextLower.includes("camera") ||
            contextLower.includes("bagno") || contextLower.includes("salotto") ||
            contextLower.includes("apartment") || contextLower.includes("showing") ||
            taskLower.includes("there is") || taskLower.includes("there are")) {

            const hasCe = /\bc'è/i.test(userLower) || /\bc è/.test(userLower);
            const hasCiSono = /\bci sono\b/.test(userLower);
            const hasQui = /\bqui\b/.test(userLower);
            const hasLi = /\blì\b/.test(userLower) || /\bli\b/.test(userLower);

            // Check if task mentions singular (there is) or plural (there are)
            const taskIsSingular = taskLower.includes("there is") ||
                                   contextLower.includes("è") ||
                                   taskLower.includes("c'è");
            const taskIsPlural = taskLower.includes("there are") ||
                                 contextLower.includes("sono") ||
                                 taskLower.includes("ci sono");

            // Room/object keywords to check for
            const roomKeywords = ['cucina', 'camera', 'bagno', 'salotto', 'divano',
                                  'letto', 'tavolo', 'sedia', 'finestra', 'porta'];
            const hasRoomMention = roomKeywords.some(room => userLower.includes(room));

            // Validation logic - accept both with and without location words
            if (taskIsSingular && hasCe && hasRoomMention) {
                if (hasQui || hasLi) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly used "C'è" with a location word. "${userInput}" is exactly right.`
                    };
                } else {
                    // "Qui" is optional - accept answer without it
                    return {
                        status: 'correct',
                        explanation: `Good! You correctly used "C'è" and named the room. Perfect!`
                    };
                }
            }

            if (taskIsPlural && hasCiSono && hasRoomMention) {
                if (hasQui || hasLi) {
                    return {
                        status: 'correct',
                        explanation: `Excellent! You correctly used "Ci sono" with a location word. "${userInput}" is perfect.`
                    };
                } else {
                    // "Qui" is optional - accept answer without it
                    return {
                        status: 'correct',
                        explanation: `Good! You correctly used "Ci sono" and named the items. Perfect!`
                    };
                }
            }

            // Wrong construction (singular vs plural mismatch)
            if (taskIsSingular && hasCiSono) {
                return {
                    status: 'almost',
                    explanation: `Close! Use "C'è" (there is) for singular items, not "Ci sono" (there are). Try: "Qui, c'è una cucina".`
                };
            }

            if (taskIsPlural && hasCe) {
                return {
                    status: 'almost',
                    explanation: `Close! Use "Ci sono" (there are) for plural items, not "C'è" (there is).`
                };
            }

            // Missing "C'è" or "Ci sono" entirely
            if (!hasCe && !hasCiSono) {
                return {
                    status: 'incorrect',
                    explanation: taskIsSingular
                        ? `To say "there is", use "C'è". For example: "Qui, c'è una cucina".`
                        : `To say "there are", use "Ci sono". For example: "Qui, ci sono due camere".`
                };
            }

            // Has construction but no room mention
            if ((hasCe || hasCiSono) && !hasRoomMention) {
                return {
                    status: 'almost',
                    explanation: `You're using the right construction! Make sure to include the room or object name.`
                };
            }
        }

        // Preposition location descriptions (sopra, sotto, dentro)
        if (contextLower.includes("gatto") || contextLower.includes("cat") ||
            contextLower.includes("libro") || contextLower.includes("book") ||
            contextLower.includes("looking for") || contextLower.includes("dove è") ||
            taskLower.includes("under") || taskLower.includes("on the") || taskLower.includes("inside")) {

            // Check for essere (è) + preposition pattern
            const hasE = / è /.test(userLower) || /\bè/.test(userLower);
            const hasSotto = /\bsotto\b/.test(userLower);
            const hasSopra = /\bsopra\b/.test(userLower);
            const hasDentro = /\bdentro\b/.test(userLower);
            const hasPreposition = hasSotto || hasSopra || hasDentro;

            // Check for location/object keywords
            const locationKeywords = ['tavolo', 'sedia', 'scatola', 'borsa', 'casa'];
            const hasLocation = locationKeywords.some(loc => userLower.includes(loc));

            // Check which preposition the task expects
            const taskExpectsSotto = taskLower.includes("under");
            const taskExpectsSopra = taskLower.includes("on the");
            const taskExpectsDentro = taskLower.includes("inside");

            // Valid pattern: [Subject] è [preposition] [location]
            // Example: "Il gatto è sotto il tavolo"

            if (hasE && hasPreposition && hasLocation) {
                // Check if correct preposition is used
                if (taskExpectsSotto && hasSotto) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly used "sotto" (under): "${userInput}".`
                    };
                }
                if (taskExpectsSopra && hasSopra) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly used "sopra" (on/above): "${userInput}".`
                    };
                }
                if (taskExpectsDentro && hasDentro) {
                    return {
                        status: 'correct',
                        explanation: `Perfect! You correctly used "dentro" (inside): "${userInput}".`
                    };
                }

                // Wrong preposition used
                if (taskExpectsSotto && (hasSopra || hasDentro)) {
                    return {
                        status: 'almost',
                        explanation: `Close! The task asks for "under". Use "sotto": "Il gatto è sotto il tavolo".`
                    };
                }
                if (taskExpectsSopra && (hasSotto || hasDentro)) {
                    return {
                        status: 'almost',
                        explanation: `Close! The task asks for "on the table". Use "sopra": "Il libro è sopra il tavolo".`
                    };
                }
                if (taskExpectsDentro && (hasSotto || hasSopra)) {
                    return {
                        status: 'almost',
                        explanation: `Close! The task asks for "inside". Use "dentro": "Il telefono è dentro la borsa".`
                    };
                }
            }

            // Has preposition but missing "è"
            if (hasPreposition && !hasE) {
                return {
                    status: 'almost',
                    explanation: `You're using the right preposition! Add "è" before it. Example: "Il gatto è sotto il tavolo".`
                };
            }

            // Has "è" but missing preposition
            if (hasE && !hasPreposition) {
                return {
                    status: 'almost',
                    explanation: `Add a preposition (sotto/sopra/dentro) to describe the location. Example: "Il gatto è sotto il tavolo".`
                };
            }

            // Has "è" and preposition but no location
            if (hasE && hasPreposition && !hasLocation) {
                return {
                    status: 'almost',
                    explanation: `Good! You're using "è" and a preposition. Add the location (tavolo, sedia, scatola, etc.).`
                };
            }
        }

        // Window next to door (A1.3.5 vicino a)
        if ((taskLower.includes("window") && taskLower.includes("next to") && taskLower.includes("door")) ||
            (contextLower.includes("describing your room") && taskLower.includes("window"))) {

            const hasFinestra = /\bfinestra\b/.test(userLower);
            const hasE = / è /.test(userLower) || /\bè/.test(userLower);
            const hasVicino = /\bvicino\b/.test(userLower);
            const hasPorta = /\bporta\b/.test(userLower);

            // Correct pattern: La finestra è vicino alla porta
            if (hasFinestra && hasE && hasVicino && hasPorta) {
                return {
                    status: 'correct',
                    explanation: `Perfect! You correctly said "La finestra è vicino alla porta" (The window is next to the door).`
                };
            }

            // Partial validations for helpful feedback
            if (hasFinestra && hasVicino && !hasE) {
                return {
                    status: 'almost',
                    explanation: `Add "è" between finestra and vicino. Example: "La finestra è vicino alla porta".`
                };
            }

            if (hasFinestra && hasE && !hasVicino) {
                return {
                    status: 'almost',
                    explanation: `Use "vicino" (next to) to describe the position. Example: "La finestra è vicino alla porta".`
                };
            }
        }

        // Chair is red (A1.3.6 color description)
        if ((promptLower.includes("di che colore") && promptLower.includes("sedia")) ||
            (taskLower.includes("chair") && taskLower.includes("red"))) {

            const hasSedia = /\bsedia\b/.test(userLower);
            const hasE = / è /.test(userLower) || /\bè/.test(userLower);
            const hasRossa = /\brossa\b/.test(userLower);
            const hasTavolo = /\btavolo\b/.test(userLower);
            const hasRosso = /\brosso\b/.test(userLower) && !/\brossa\b/.test(userLower);

            // Correct: La sedia è rossa
            if (hasSedia && hasE && hasRossa) {
                return {
                    status: 'correct',
                    explanation: `Perfect! You correctly said "La sedia è rossa" (The chair is red - feminine).`
                };
            }

            // Wrong furniture (tavolo instead of sedia)
            if (hasTavolo) {
                return {
                    status: 'incorrect',
                    explanation: `The question asks about "la sedia" (chair), not "il tavolo" (table). Try: "La sedia è rossa".`
                };
            }

            // Wrong gender agreement (rosso instead of rossa)
            if (hasSedia && hasE && hasRosso) {
                return {
                    status: 'almost',
                    explanation: `Close! "Sedia" is feminine, so use "rossa" not "rosso": "La sedia è rossa".`
                };
            }

            // Missing verb "è"
            if (hasSedia && hasRossa && !hasE) {
                return {
                    status: 'almost',
                    explanation: `Add "è" between sedia and rossa. Example: "La sedia è rossa".`
                };
            }
        }

        // Fallback if no specific context matches
        return { status: 'ai_required', explanation: null };
    }, []);

    const handleSubmit = async () => {
        if (!userInput.trim() || isProcessing || isComplete) {
            return;
        }

        setIsProcessing(true);

        try {
            let validationResult = validateResponse(userInput, context, task);

            // If client-side validation is inconclusive, call the AI
            if (validationResult.status === 'ai_required') {
                const responseData = await sendTutorMessage({
                    user_message: userInput.trim(),
                    chat_history: [],
                    target_language: targetLang,
                    native_language: nativeLang,
                    level: "Beginner",
                    lesson_id: null
                });

                const aiResponse = responseData.text || "";
                const aiStatus = responseData.status;
                const aiLower = aiResponse.toLowerCase();
                const isCorrect = aiStatus === "GOAL_ACHIEVED" || ["correct", "good", "perfect", "bravo", "ottimo"].some(word => aiLower.includes(word));

                validationResult = {
                    status: isCorrect ? 'correct' : 'incorrect',
                    explanation: aiResponse || (isCorrect ? "Well done!" : "That's not quite right. Please try again.")
                };
            }

            setIsProcessing(false);
            setIsComplete(true);
            // Pass the result up to the parent ExerciseView
            onAnswer(validationResult.status, userInput, validationResult.explanation);
        } catch (error) {
            console.error("Error in mini prompt:", error);
            setIsProcessing(false);
            setIsComplete(true);
            onAnswer('incorrect', userInput, "Error validating response. Please try again.");
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

            {/* Feedback handled by parent ExerciseView after submission */}
        </div>
    );
};

MiniPromptExercise.displayName = 'MiniPromptExercise';

export default MiniPromptExercise;
