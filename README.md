# PolyBot - AI-Powered Multilingual Language Learning Platform

PolyBot is an **AI-powered multilingual language learning platform** that combines a structured **10-module CEFR A1 Curriculum** with free-flowing AI roleplay to provide a "True Bilingual" learning experience.

## Key Features

- **Structured Curriculum**: 10-module CEFR A1 course with comprehensive exercises
- **AI-Powered Tutoring**: Scenario-based practice mode with game state architecture
- **Voice Integration**: Whisper STT for speech recognition and TTS for audio playback
- **Multiple Exercise Types**: Info Cards, Match Pairs, Unscramble, Echo Chamber, Listening/Reading Comprehension, and more
- **Boss Fight System**: Conversation practice with grammar and pronunciation feedback

## Tech Stack

- **Frontend**: React 18.2.0 + Tailwind CSS + Lucide React
- **Backend**: FastAPI (Python 3.11) + Llama 3 8B Instruct
- **Database**: MongoDB 7.0
- **Voice**: Whisper (STT), Edge-TTS (TTS) - migrating to Piper TTS + StyleTTS 2
- **Auth**: Google OAuth 2.0

## Current Status

**Version**: 1.0.18 (Stable, Verified, & Tested)

Module A1.1 (Greetings & Introductions) is fully implemented with 9 lessons, comprehensive exercise types, and enhanced feedback mechanisms. Scenario-Based Practice Mode architecture is designed and ready for implementation.

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- MongoDB 7.0+
- Docker & Docker Compose (for containerized deployment)
- NVIDIA GPU (for local LLM inference) or RunPod Serverless GPU access

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/polybot.git
cd polybot
```

2. Backend Setup:
```bash
cd backend
pip install -r requirements.txt
```

3. Frontend Setup:
```bash
cd frontend
npm install
```

4. Environment Variables:
Create `.env` files in `backend/` and `frontend/` with required configuration (see project documentation).

5. Run with Docker Compose:
```bash
docker-compose up
```

## Project Structure

```
polybot/
├── backend/           # FastAPI backend
│   ├── server.py     # Main API server
│   ├── a1_1_module_data.py  # Module A1.1 structured data
│   └── scripts/      # Utility scripts
├── frontend/         # React frontend
│   └── src/          # React components
├── context-docs/     # Project and curriculum documentation
└── docker-compose.yml
```

## Development Roadmap

1. **Scenario-Based Practice Mode** (Priority)
   - Game State Architecture
   - Voice/Text Mode separation
   - Post-Game Report feedback system

2. **Voice Stack Migration**
   - Migrate to Piper TTS (static content)
   - Migrate to StyleTTS 2 (Tutor persona)
   - ModelManager implementation

3. **Module A1.2**: Personal Information & Family

## License

[Add your license here]

## Contributing

[Add contributing guidelines here]

