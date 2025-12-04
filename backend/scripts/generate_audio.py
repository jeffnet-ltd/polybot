#!/usr/bin/env python3
"""
Audio Generation Script for PolyBot A1.1 Module
Pre-generates Edge-TTS audio files for all Intro Card phrases and stores URLs.
"""

import os
import sys
import asyncio
import edge_tts
import json
from pathlib import Path

# Add parent directory to path to import server functions
sys.path.insert(0, str(Path(__file__).parent.parent))

# Audio output directory
AUDIO_DIR = Path(__file__).parent.parent / "static" / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Language to voice mapping (from server.py)
VOICE_MAPPING = {
    "en": "en-US-AriaNeural",
    "es": "es-ES-ElviraNeural",
    "fr": "fr-FR-DeniseNeural",
    "it": "it-IT-ElsaNeural",
    "pt": "pt-PT-RaquelNeural",
    "tw": "en-US-AriaNeural",
    "de": "de-DE-KatjaNeural",
}

def get_voice(lang_code: str) -> str:
    """Get Edge-TTS voice for language code."""
    return VOICE_MAPPING.get(lang_code.lower(), "en-US-AriaNeural")

async def generate_audio_file(text: str, lang_code: str, filename: str) -> str:
    """
    Generate audio file using Edge-TTS and save to static/audio directory.
    Returns the relative URL path.
    """
    voice = get_voice(lang_code)
    print(f"Generating audio for: '{text}' (lang: {lang_code}, voice: {voice})")
    
    communicate = edge_tts.Communicate(text=text, voice=voice)
    audio_bytes = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_bytes += chunk["data"]
    
    # Save to file
    filepath = AUDIO_DIR / filename
    with open(filepath, "wb") as f:
        f.write(audio_bytes)
    
    # Return relative URL (from frontend perspective, served from backend)
    relative_url = f"/static/audio/{filename}"
    print(f"  ✓ Saved to {filepath} ({len(audio_bytes)} bytes)")
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

