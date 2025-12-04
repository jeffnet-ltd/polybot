FROM python:3.11-slim

WORKDIR /app

# System dependencies for audio processing (Whisper STT, XTTS TTS)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    portaudio19-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Default command (overridden by docker-compose)
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]