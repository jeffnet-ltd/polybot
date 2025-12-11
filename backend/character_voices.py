"""
Character Voice Mapping for PolyBot

Defines character genders and maps them to appropriate Azure Speech voices.
This system enables gender-specific voice selection for dialogue immersion.
"""

import re

# Character gender mapping
# Key: Character name (as it appears in dialogue)
# Value: "male" or "female"
CHARACTER_GENDERS = {
    # Male characters
    "Marco": "male",
    "Luca": "male",
    "John": "male",
    "Bianchi": "male",
    "Professor": "male",

    # Female characters
    "Sofia": "female",
    "Maria": "female",
    "Luisa": "female",
    "Anna": "female",
    "Rossi": "female",
}

# Voice mapping by language and gender
# Structure: {language_code: {gender: azure_voice_name}}
GENDER_VOICE_MAPPING = {
    "en": {
        "male": "en-US-GuyNeural",
        "female": "en-US-JennyNeural",
    },
    "it": {
        "male": "it-IT-DiegoNeural",
        "female": "it-IT-ElsaNeural",
    },
    "fr": {
        "male": "fr-FR-HenriNeural",
        "female": "fr-FR-DeniseNeural",
    },
    "es": {
        "male": "es-ES-AlvaroNeural",
        "female": "es-ES-ElviraNeural",
    },
    "pt": {
        "male": "pt-BR-AntonioNeural",
        "female": "pt-BR-FranciscaNeural",
    },
    "de": {
        "male": "de-DE-ConradNeural",
        "female": "de-DE-KatjaNeural",
    },
    "ja": {
        "male": "ja-JP-KeitaNeural",
        "female": "ja-JP-NanamiNeural",
    },
    "zh": {
        "male": "zh-CN-YunxiNeural",
        "female": "zh-CN-XiaoxiaoNeural",
    },
    # Fallback for unsupported languages
    "tw": {
        "male": "en-US-GuyNeural",
        "female": "en-US-JennyNeural",
    },
}


def normalize_lang(lang_code: str) -> str:
    """
    Normalize language code to lowercase.

    Args:
        lang_code: Language code (e.g., "en", "IT", "Fr")

    Returns:
        Normalized language code (e.g., "en")
    """
    return lang_code.lower() if lang_code else "en"


def get_character_gender(character_name: str) -> str:
    """
    Get the gender of a character based on their name.

    Args:
        character_name: Name of the character (e.g., "Marco", "Sofia")

    Returns:
        "male", "female", or "female" (default if unknown)
    """
    if not character_name:
        return "female"

    # Try exact match first
    gender = CHARACTER_GENDERS.get(character_name)
    if gender:
        return gender

    # Try case-insensitive match
    for name, gen in CHARACTER_GENDERS.items():
        if name.lower() == character_name.lower():
            return gen

    # Default to female if character not found
    return "female"


def get_voice_for_character(lang_code: str, character_name: str = None) -> str:
    """
    Get the appropriate Azure Speech voice for a character.

    Combines language and character gender to select the right voice.
    If no character is provided, defaults to female voice for the language.

    Args:
        lang_code: Language code (e.g., "en", "it", "fr")
        character_name: Optional character name (e.g., "Marco", "Sofia")

    Returns:
        Azure Speech voice name (e.g., "it-IT-DiegoNeural")
    """
    code = normalize_lang(lang_code)

    # Get language-specific voice mapping
    lang_voices = GENDER_VOICE_MAPPING.get(code, GENDER_VOICE_MAPPING.get("en"))

    if not lang_voices:
        # Fallback to English if language not found
        return "en-US-JennyNeural"

    # Determine character gender
    if character_name:
        gender = get_character_gender(character_name)
    else:
        gender = "female"  # Default to female

    # Get voice for this gender
    voice = lang_voices.get(gender, lang_voices.get("female"))

    return voice if voice else "en-US-JennyNeural"


def extract_character_name(text: str) -> str:
    """
    Extract character name from dialogue or self-introduction text.

    Supports multiple formats:
    - Dialogue format: "CharacterName: dialogue text"
    - Italian self-intro: "mi chiamo Marco" or "sono Marco"
    - French self-intro: "je m'appelle Marco" or "je suis Marco"
    - Spanish self-intro: "me llamo Marco" or "soy Marco"
    - English self-intro: "my name is Marco" or "I'm Marco"
    - Portuguese self-intro: "meu nome é Marco" or "chamo-me Marco"
    - German self-intro: "ich heiße Marco" or "mein Name ist Marco"
    - Titles: "Professor Marco Bianchi" -> extracts "Bianchi" (surname preferred)

    Args:
        text: Text that may contain a character name

    Returns:
        Character name if found, or empty string

    Examples:
        extract_character_name("Marco: Ciao!") -> "Marco"
        extract_character_name("Ciao, mi chiamo Marco") -> "Marco"
        extract_character_name("Mi chiamo Professor Bianchi") -> "Bianchi"
        extract_character_name("Je m'appelle Sofia") -> "Sofia"
        extract_character_name("Hello") -> ""
    """
    if not text:
        return ""

    # 1. Try dialogue format "Marco: text"
    if ":" in text:
        potential_name = text.split(":", 1)[0].strip()
        if _is_known_character(potential_name):
            return potential_name

    # 2. Try self-introduction patterns across multiple languages
    # Order matters: more specific patterns first
    patterns = [
        # Italian: "mi chiamo Marco" or "sono Marco"
        r'\b(?:mi chiamo|sono)\s+(.+?)(?:\.|,|$)',
        # French: "je m'appelle Marco" or "je suis Marco"
        r'\b(?:je m\'appelle|je suis)\s+(.+?)(?:\.|,|$)',
        # Spanish: "me llamo Marco" or "soy Marco"
        r'\b(?:me llamo|soy)\s+(.+?)(?:\.|,|$)',
        # English: "my name is Marco" or "I'm Marco" or "I am Marco"
        r'\b(?:my name is|i\'m|i am)\s+(.+?)(?:\.|,|$)',
        # Portuguese: "meu nome é Marco" or "chamo-me Marco"
        r'\b(?:meu nome é|chamo-me)\s+(.+?)(?:\.|,|$)',
        # German: "ich heiße Marco" or "mein Name ist Marco"
        r'\b(?:ich heiße|mein Name ist)\s+(.+?)(?:\.|,|$)',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Extract all words from the match
            full_name = match.group(1).strip()
            words = full_name.split()

            # Try words in reverse order (surname last is most common)
            for word in reversed(words):
                # Remove punctuation from word
                word_clean = word.rstrip('.,!?;:')
                if _is_known_character(word_clean):
                    return word_clean

            # If no match found in multi-word name, try the first word as fallback
            if words and _is_known_character(words[0]):
                return words[0]

    return ""


def _is_known_character(name: str) -> bool:
    """
    Check if a name is a known character in the curriculum.

    Performs exact and case-insensitive matching.

    Args:
        name: Character name to verify

    Returns:
        True if character is in CHARACTER_GENDERS, False otherwise
    """
    if not name:
        return False

    # Try exact match first
    if name in CHARACTER_GENDERS:
        return True

    # Try case-insensitive match
    for known_name in CHARACTER_GENDERS.keys():
        if known_name.lower() == name.lower():
            return True

    return False
