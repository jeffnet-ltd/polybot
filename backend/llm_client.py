"""
PolyBot LLM Client
Calls the RunPod serverless endpoint instead of loading Llama 3 8B locally.
"""

import os
import httpx
from uvicorn.config import logger

RUNPOD_API_KEY     = os.environ.get("RUNPOD_API_KEY", "")
RUNPOD_ENDPOINT_ID = os.environ.get("RUNPOD_ENDPOINT_ID", "")
_TIMEOUT = 120.0  # seconds


def _base_url() -> str:
    return f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/runsync"


async def generate(
    prompt: str,
    max_new_tokens: int = 60,
    temperature: float = 0.7,
    do_sample: bool = True,
    top_k: int = 50,
) -> str:
    """
    Send a formatted prompt to the RunPod serverless endpoint and return the
    generated text string.

    Raises:
        RuntimeError — on missing credentials, HTTP error, or unexpected response
    """
    if not RUNPOD_API_KEY or not RUNPOD_ENDPOINT_ID:
        raise RuntimeError(
            "RUNPOD_API_KEY and RUNPOD_ENDPOINT_ID environment variables must be set"
        )

    payload = {
        "input": {
            "prompt":         prompt,
            "max_new_tokens": max_new_tokens,
            "temperature":    temperature,
            "do_sample":      do_sample,
            "top_k":          top_k,
        }
    }

    headers = {
        "Authorization": f"Bearer {RUNPOD_API_KEY}",
        "Content-Type":  "application/json",
    }

    logger.debug(f"[LLM] → RunPod ({RUNPOD_ENDPOINT_ID}) max_new_tokens={max_new_tokens} temp={temperature}")

    async with httpx.AsyncClient(timeout=_TIMEOUT) as client:
        response = await client.post(_base_url(), json=payload, headers=headers)

    if response.status_code != 200:
        raise RuntimeError(
            f"RunPod returned HTTP {response.status_code}: {response.text[:300]}"
        )

    body = response.json()

    # runsync wraps the handler's return value in {"output": {...}}
    output = body.get("output", {})

    if "error" in output:
        raise RuntimeError(f"RunPod inference error: {output['error']}")

    generated_text = output.get("generated_text")
    if generated_text is None:
        raise RuntimeError(f"Unexpected RunPod response shape: {body}")

    logger.debug(f"[LLM] ← {len(generated_text)} chars")
    return generated_text
