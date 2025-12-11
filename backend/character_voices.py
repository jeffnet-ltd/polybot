"""
Character Voice Mapping for PolyBot

Defines character genders and maps them to appropriate Azure Speech voices.
This system enables gender-specific voice selection for dialogue immersion.
"""

# Character gender mapping
# Key: Character name (as it appears in dialogue)
# Value: "male" or "female"
CHARACTER_GENDERS = {
    # Male characters
    "Marco": "male",
    "Luca": "male",
    "John": "male",

    # Female characters
    "Sofia": "female",
    "Maria": "female",
    "Luisa": "female",
    "Anna": "female",
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
    Extract character name from dialogue text.

    Expects format: "CharacterName: dialogue text"

    Args:
        text: Dialogue text that may contain a character name prefix

    Returns:
        Character name if found, or empty string

    Example:
        extract_character_name("Marco: Ciao!") -> "Marco"
        extract_character_name("Hello") -> ""
    """
    if not text or ":" not in text:
        return ""

    # Get the part before the first colon
    potential_name = text.split(":", 1)[0].strip()

    # Verify it's a known character (to avoid false positives)
    if potential_name in CHARACTER_GENDERS:
        return potential_name

    # Try case-insensitive match
    for name in CHARACTER_GENDERS.keys():
        if name.lower() == potential_name.lower():
            return name

    return ""
