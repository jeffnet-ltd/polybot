"""
PolyBot RunPod Serverless Handler
LLM inference worker for Meta-Llama-3-8B-Instruct-GPTQ
"""

import os
import sys
import runpod
from auto_gptq import AutoGPTQForCausalLM
from transformers import AutoTokenizer, pipeline
from huggingface_hub import snapshot_download

# ---------------------------------------------------------------------------
# Cold-start: model is loaded once when the worker container starts
# ---------------------------------------------------------------------------

MODEL_PATH = os.environ.get("MODEL_PATH", "/workspace/models/llama3-8b-gptq")

if not os.path.exists(MODEL_PATH) or not os.listdir(MODEL_PATH):
    print(f"[PolyBot] Model not found at {MODEL_PATH}, downloading...", flush=True)
    os.makedirs(MODEL_PATH, exist_ok=True)
    snapshot_download(
        repo_id="MaziyarPanahi/Meta-Llama-3-8B-Instruct-GPTQ",
        local_dir=MODEL_PATH,
        ignore_patterns=["*.bin"],
    )
    print("[PolyBot] Download complete.", flush=True)

print(f"[PolyBot] Cold start — loading tokenizer from {MODEL_PATH}...", flush=True)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
print("[PolyBot] Tokenizer loaded.", flush=True)

print(f"[PolyBot] Loading model from {MODEL_PATH}...", flush=True)
model = AutoGPTQForCausalLM.from_quantized(
    MODEL_PATH,
    use_safetensors=True,
    device="cuda:0",
    inject_fused_attention=False,
)
print("[PolyBot] Model loaded onto cuda:0.", flush=True)

text_generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map={"": "cuda:0"},
)
print("[PolyBot] Pipeline ready. Worker is warm.", flush=True)

# ---------------------------------------------------------------------------
# Handler — called for every serverless request
# ---------------------------------------------------------------------------

def handler(job):
    """
    Expected job["input"] fields:
        prompt          str   — chat-template-formatted string
        max_new_tokens  int   — tokens to generate (30–600)
        temperature     float — 0.1 (deterministic) … 0.8 (creative)
        do_sample       bool  — True for conversation, False for assessment
        top_k           int   — (optional) used only when do_sample is True
    """
    job_input = job.get("input", {})

    prompt = job_input.get("prompt")
    if not prompt:
        return {"error": "Missing required field: 'prompt'"}

    max_new_tokens = int(job_input.get("max_new_tokens", 60))
    temperature    = float(job_input.get("temperature", 0.7))
    do_sample      = bool(job_input.get("do_sample", True))
    top_k          = int(job_input.get("top_k", 50))

    generate_kwargs = {
        "max_new_tokens": max_new_tokens,
        "temperature":    temperature,
        "do_sample":      do_sample,
        "return_full_text": False,
    }
    if do_sample:
        generate_kwargs["top_k"] = top_k

    try:
        output = text_generator(prompt, **generate_kwargs)
        generated_text = output[0]["generated_text"].strip()
        return {"generated_text": generated_text}
    except Exception as e:
        print(f"[PolyBot] Inference error: {e}", flush=True)
        return {"error": str(e)}


runpod.serverless.start({"handler": handler})
