#!/usr/bin/env python3
"""Test script to diagnose edge-tts functionality"""
import asyncio
import edge_tts
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

TEXT = "Hello, this is a test."
VOICE = "en-US-JennyNeural"
OUTPUT_FILE = "/tmp/test.mp3"

async def main():
    try:
        logger.info(f"Python version: {sys.version}")
        logger.info(f"Testing edge-tts with text: '{TEXT}'")
        logger.info(f"Voice: {VOICE}")

        logger.info("Initializing edge_tts.Communicate...")
        communicate = edge_tts.Communicate(TEXT, VOICE)
        logger.info("✓ Communicate object created successfully")

        logger.info(f"Saving audio to {OUTPUT_FILE}...")
        await communicate.save(OUTPUT_FILE)
        logger.info(f"✓ Audio saved successfully")

        # Check file size
        import os
        if os.path.exists(OUTPUT_FILE):
            file_size = os.path.getsize(OUTPUT_FILE)
            logger.info(f"✓ SUCCESS: TTS audio saved to {OUTPUT_FILE} ({file_size} bytes)")
            os.remove(OUTPUT_FILE)
        else:
            logger.error(f"✗ FAILURE: File was not created at {OUTPUT_FILE}")

    except asyncio.TimeoutError as e:
        logger.error(f"✗ TIMEOUT: {e}")
    except Exception as e:
        logger.error(f"✗ FAILURE: {e}", exc_info=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
