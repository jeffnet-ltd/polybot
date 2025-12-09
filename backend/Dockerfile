FROM python:3.11-slim

WORKDIR /app

# Upgrade pip and install network tools for debugging
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
    dnsutils \
    curl \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade pip setuptools wheel

# Install Python dependencies
COPY requirements.txt .

# Install auto-gptq with CUDA extensions (try pre-built wheels first)
# CUDA extensions improve performance but are optional - model will work without them
# Try CUDA 12.1, then 11.8, then fallback to standard install
RUN pip install --no-cache-dir --upgrade auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu121/ || \
    (pip install --no-cache-dir --upgrade auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/ || \
     pip install --no-cache-dir --upgrade auto-gptq) && \
    echo "auto-gptq installed (CUDA extensions may or may not be available)"

# Install dependencies in stages to avoid resolution conflicts
# Use --use-deprecated=legacy-resolver for complex dependencies
# Stage 1: Core web framework
RUN pip install --no-cache-dir --default-timeout=100 \
    fastapi==0.110.1 \
    uvicorn==0.25.0 \
    python-dotenv==1.0.1 \
    python-multipart>=0.0.6

# Stage 2+: Remainder of deps from requirements.txt (single shot to avoid pip args issues)
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt || pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Default command (overridden by docker-compose)
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]