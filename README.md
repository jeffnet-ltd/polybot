# PolyBot - AI-Powered Multilingual Language Learning Platform

PolyBot is an **AI-powered multilingual language learning platform** that combines a structured **10-module CEFR A1 Curriculum** with AI-powered scenario-based practice for "True Bilingual" learning (target language + native language explanations).

## Key Features

- **Complete A1 Curriculum**: All 10 modules (A1.1-A1.10) fully implemented with 8-9 lessons each
- **AI-Powered Tutoring**: Scenario-based practice mode with game state architecture powered by Llama 3 8B
- **Voice Integration**: Whisper STT for speech recognition + Azure Speech Services TTS with gendered character voices
- **Multiple Exercise Types**: Info Cards, Match Pairs, Unscramble, Echo Chamber, Listening/Reading Comprehension, and Dialogue exercises
- **Boss Fight System**: Immersive conversation practice with grammar and pronunciation feedback
- **Context-Aware Validation**: Intelligent client-side and server-side validation with pedagogical feedback

## Tech Stack

- **Frontend**: React 18.2.0 + Tailwind CSS + Lucide React
- **Backend**: FastAPI (Python 3.11) — lightweight API server, no local model loading
- **LLM Inference**: Llama 3 8B Instruct GPTQ via RunPod Serverless GPU
- **Database**: MongoDB Atlas
- **Voice**: Whisper (STT) + Azure Speech Services (TTS with gendered character voices)
- **Auth**: Google OAuth 2.0 + Local Session Management
- **Deployment**: Docker + Docker Compose (local dev) / RunPod + Atlas (cloud)

## Current Status

**Version**: 2.2.1 (Stable, Cloud-Ready)

Complete A1 curriculum. LLM inference via RunPod Serverless GPU. Database on MongoDB Atlas. Backend starts in seconds with no local GPU required.

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose (for containerized deployment)
- MongoDB Atlas account (free tier) — or local MongoDB for development
- RunPod account with a configured Serverless endpoint (for LLM inference)

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
Copy `.env.example` to `.env` and fill in your credentials (MongoDB Atlas URI, RunPod API key, Azure Speech key, Google OAuth).

5. Run with Docker Compose:
```bash
docker-compose up
```

## Project Structure

```
polybot/
├── backend/
│   ├── server.py                 # FastAPI main server (no local model loading)
│   ├── llm_client.py             # RunPod serverless LLM client
│   ├── character_voices.py        # Character-gender mapping & voice selection
│   ├── practice_mode.py           # Scenario-based practice logic
│   ├── a1_1_module_data.py        # A1.1 Curriculum (Greetings & Introductions)
│   ├── a1_2_module_data.py        # A1.2 Curriculum (Personal Information & Family)
│   ├── a1_3_module_data.py        # A1.3 Curriculum (Home & Housing)
│   ├── a1_4_module_data.py        # A1.4 Curriculum (Food & Drinks)
│   ├── a1_5_module_data.py        # A1.5 Curriculum (Shopping & Prices)
│   ├── a1_6_module_data.py        # A1.6 Curriculum (Directions & Transportation)
│   ├── a1_7_module_data.py        # A1.7 Curriculum (Time & Daily Routines)
│   ├── a1_8_module_data.py        # A1.8 Curriculum (Weather & Seasons)
│   ├── a1_9_module_data.py        # A1.9 Curriculum (Hobbies & Interests)
│   ├── a1_10_module_data.py       # A1.10 Curriculum (Health & Body Parts)
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                 # Backend containerization
│   └── scripts/                   # Utility scripts (data seeding, testing)
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # Main React application
│   │   ├── components/           # React components (exercises, dialogs, etc.)
│   │   └── utils/                # Helper functions (audio, API calls, etc.)
│   └── package.json              # Node.js dependencies
├── runpod-handler/
│   ├── handler.py                # RunPod serverless worker
│   ├── requirements.txt          # Worker dependencies
│   └── Dockerfile                # Worker container (CUDA 11.8 + PyTorch 2.1)
├── context-docs/
│   ├── project-docs/             # Project documentation
│   └── course-docs/              # Curriculum documentation
├── docker-compose.yml            # Docker Compose orchestration (local dev)
├── .env.example                  # Environment variable template
└── README.md                      # This file
```

## Development Roadmap

1. ✅ **Complete A1 Curriculum** - All 10 modules fully implemented
2. ✅ **Azure TTS Integration** - High-availability voice with gendered character voices
3. ✅ **RunPod Serverless LLM** - Llama 3 8B GPTQ inference via cloud GPU
4. ✅ **MongoDB Atlas** - Cloud database, no local MongoDB required
5. **Streaming Pipeline** - Real-time sentence-by-sentence LLM/TTS streaming
6. **Frontend Deployment** - Vercel/Netlify pointing to cloud backend
7. **Mobile App** - Capacitor-based native apps (Android/iOS)
8. **Global Expansion** - Multi-language curriculum and multi-model support

## License

[Add your license here]

## Contributing

[Add contributing guidelines here]

