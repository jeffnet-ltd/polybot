#!/usr/bin/env python3
"""
Audio Generation Script for PolyBot A1.1 Module
Pre-generates Edge-TTS audio files for all Intro Card phrases and stores URLs.
"""

import os
import sys
import json
import asyncio
import tempfile
from pathlib import Path

try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    EDGE_TTS_AVAILABLE = False
    print("ERROR: Edge-TTS not available. Install with: pip install edge-tts")
    sys.exit(1)

# Add parent directory to path to import server functions
sys.path.insert(0, str(Path(__file__).parent.parent))

# Audio output directory
AUDIO_DIR = Path(__file__).parent.parent / "static" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Language to Edge-TTS voice mapping (using high-quality neural voices)
EDGE_TTS_VOICES = {
    "en": "en-US-JennyNeural",      # English (US, Female, Natural)
    "fr": "fr-FR-DeniseNeural",     # French (Female, Natural)
    "it": "it-IT-ElsaNeural",       # Italian (Female, Natural)
    "es": "es-ES-ElviraNeural",     # Spanish (Female, Natural)
    "pt": "pt-BR-FranciscaNeural",  # Portuguese (Brazilian, Female)
    "de": "de-DE-KatjaNeural",      # German (Female, Natural)
    "tw": "en-US-JennyNeural",      # Twi not supported, fallback to English
    "ja": "ja-JP-NanamiNeural",     # Japanese (Female, Natural)
    "zh": "zh-CN-XiaoxiaoNeural",   # Chinese (Mandarin, Female, Natural)
}

def get_voice_name(lang_code: str) -> str:
    """Get Edge-TTS voice name for language code."""
    return EDGE_TTS_VOICES.get(lang_code.lower(), "en-US-JennyNeural")

async def generate_audio_file(text: str, lang_code: str, filename: str) -> str:
    """
    Generate audio file using Edge-TTS and save to static/audio directory.
    Returns the relative URL path.
    """
    if not EDGE_TTS_AVAILABLE:
        raise RuntimeError("Edge-TTS is not installed")
    
    voice_name = get_voice_name(lang_code)
    print(f"Generating audio for: '{text}' (lang: {lang_code}, voice: {voice_name})")
    
    filepath = AUDIO_DIR / filename
    
    # Generate audio using Edge-TTS
    try:
        communicate = edge_tts.Communicate(text, voice_name)
        await communicate.save(str(filepath))
    except Exception as e:
        print(f"  ✗ Error synthesizing audio: {e}")
        raise
    
    if not filepath.exists():
        raise RuntimeError("Audio file was not created")
    
    # Get file size for logging
    file_size = filepath.stat().st_size
    
    # Return relative URL (from frontend perspective, served from backend)
    relative_url = f"/static/audio/{filename}"
    print(f"  ✓ Saved to {filepath} ({file_size} bytes)")
    return relative_url

def generate_filename(text: str, lang_code: str, index: int = 0) -> str:
    """Generate a safe filename from text."""
    # Clean text for filename
    safe_text = "".join(c if c.isalnum() or c in (" ", "-", "_") else "" for c in text[:30])
    safe_text = safe_text.replace(" ", "_").lower()
    return f"{lang_code}_{safe_text}_{index}.mp3"

async def generate_module_a1_1_audio():
    """
    Generate audio files for Module A1.1: Greetings & Introductions.
    Focus on Italian (it) language.
    """
    # Module A1.1 vocabulary for Italian
    italian_phrases = [
        # Lesson 1: Informal Zone
        "Ciao",
        "Come stai?",
        "Bene",
        "E tu?",
        "Grazie",
        
        # Lesson 2: Formal Zone
        "Buongiorno",
        "Buonasera",
        "Arrivederci",
        "Come sta?",
        "Lei",
        
        # Lesson 3: The Name Game
        "Mi chiamo",
        "Sono",
        "Piacere",
        
        # Lesson 4: Politeness
        "Salve",
        "Per favore",
        "Prego",
        "A presto",
    ]
    
    lang_code = "it"
    audio_urls = {}
    
    print(f"\n🎵 Generating audio files for Module A1.1 (Italian)...\n")
    
    for i, phrase in enumerate(italian_phrases):
        filename = generate_filename(phrase, lang_code, i)
        try:
            url = await generate_audio_file(phrase, lang_code, filename)
            audio_urls[phrase] = url
        except Exception as e:
            print(f"  ✗ Error generating audio for '{phrase}': {e}")
            audio_urls[phrase] = None
    
    # Save mapping to JSON file
    mapping_file = AUDIO_DIR / "a1_1_audio_mapping.json"
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(audio_urls, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Audio generation complete!")
    print(f"   Generated {len([v for v in audio_urls.values() if v])} audio files")
    print(f"   Mapping saved to: {mapping_file}")
    
    return audio_urls

if __name__ == "__main__":
    print("=" * 60)
    print("PolyBot Audio Generation Script")
    print("=" * 60)
    asyncio.run(generate_module_a1_1_audio())

