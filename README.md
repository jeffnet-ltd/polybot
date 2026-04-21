# PolyBot - AI-Powered Multilingual Language Learning Platform

PolyBot is an **AI-powered multilingual language learning platform** combining a structured **10-module CEFR A1 Curriculum** with AI-powered scenario-based practice for a "True Bilingual" learning experience. Users learn in their target language while receiving explanations in their native language.

## Live Production

| Service | URL |
|---|---|
| **Frontend** | https://polybot-sand.vercel.app |
| **Backend API** | https://d2r1f6dy1chiig.cloudfront.net |

## Key Features

- **Complete A1 Curriculum**: All 10 modules (A1.1-A1.10) fully implemented with 8-9 lessons each
- **AI-Powered Tutoring**: Scenario-based practice mode with game state architecture powered by Llama 3 8B via RunPod Serverless
- **Voice Integration**: Whisper STT for speech recognition + Azure Speech Services TTS with gendered character voices
- **13 Exercise Types**: Info Cards, Match Pairs, Unscramble, Echo Chamber, Listening/Reading Comprehension, Free Writing, Form Fill, Boss Fight, and more
- **Google OAuth**: Full sign-in flow with automatic profile creation and language setup
- **Context-Aware Validation**: Intelligent client-side and server-side validation with pedagogical feedback

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 18.2.0 + Tailwind CSS + Lucide React — deployed on Vercel |
| **Backend** | FastAPI (Python 3.11) — deployed on AWS ECS Fargate |
| **HTTPS** | AWS CloudFront in front of HTTP ALB (fixes mixed content) |
| **LLM** | Llama 3 8B Instruct GPTQ via RunPod Serverless GPU |
| **Database** | MongoDB Atlas |
| **Voice** | OpenAI Whisper (STT) + Azure Speech Services (TTS) |
| **Auth** | Google OAuth 2.0 via authlib + Starlette sessions |

## Current Version

**v2.2.2** — Full production deployment operational. Frontend on Vercel, backend on ECS Fargate behind CloudFront HTTPS, LLM on RunPod Serverless, database on MongoDB Atlas. Google OAuth end-to-end working.

## Getting Started (Local Development)

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose
- MongoDB Atlas account (free tier)
- RunPod account with a configured Serverless endpoint
- Azure Speech Services key
- Google OAuth 2.0 credentials

### Setup

1. Clone the repository:
```bash
git clone https://github.com/jeffnet-ltd/polybot.git
cd polybot
```

2. Copy and fill in environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Install and run:
```bash
# Backend
cd backend && pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8000

# Frontend (separate terminal)
cd frontend && npm install && npm start
```

4. Or run with Docker Compose:
```bash
docker-compose up
```

## Project Structure

```
polybot/
├── backend/
│   ├── server.py                 # FastAPI main server
│   ├── llm_client.py             # RunPod serverless LLM client (async)
│   ├── practice_mode.py          # Scenario-based practice logic
│   ├── character_voices.py       # Character-gender mapping & voice selection
│   ├── a1_1_module_data.py       # A1.1–A1.10 curriculum data (10 files)
│   ├── requirements.txt          # Python dependencies (includes certifi)
│   ├── Dockerfile                # python:3.11-slim + ca-certificates
│   └── scripts/                  # MongoDB seeding scripts (10 modules)
├── frontend/
│   ├── src/
│   │   ├── App.jsx               # Main React application
│   │   ├── components/           # Exercise components, views, curriculum
│   │   ├── services/             # API, user, lesson, TTS service layers
│   │   └── config/               # Constants (API URL, languages, levels)
│   ├── .env                      # Local dev (REACT_APP_BACKEND_URL=localhost)
│   ├── .env.production           # Production (REACT_APP_BACKEND_URL=CloudFront)
│   └── package.json
├── runpod-handler/
│   ├── handler.py                # RunPod serverless worker (GPTQ inference)
│   ├── requirements.txt
│   └── Dockerfile                # CUDA 11.8 + PyTorch 2.1
├── context-docs/
│   ├── project-docs/             # Versioned project context documents
│   └── course-docs/              # A1 curriculum master reference
├── docker-compose.yml            # Local dev orchestration
├── .env.example                  # Environment variable template
└── README.md
```

## Development Roadmap

1. ✅ **Complete A1 Curriculum** — All 10 modules fully implemented
2. ✅ **Azure TTS Integration** — High-availability voice with gendered character voices
3. ✅ **RunPod Serverless LLM** — Llama 3 8B GPTQ inference via cloud GPU
4. ✅ **MongoDB Atlas** — Cloud database migration complete
5. ✅ **Production Deployment** — Vercel + ECS Fargate + CloudFront HTTPS + Google OAuth live
6. **Streaming Pipeline** — Real-time LLM/TTS streaming to reduce latency
7. **Scenario-Based Practice Mode** — Game state architecture, Stage Manager, Post-Game Report
8. **Mobile App** — Capacitor-based native apps (Android/iOS)
9. **Global Expansion** — Multi-language curriculum + multi-model support (Qwen, Aya)
10. **Custom Domain** — Replace CloudFront workaround with proper domain + ACM cert on ALB

## License

[Add your license here]
