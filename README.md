# PolyBot - AI-Powered Multilingual Language Learning Platform

PolyBot is an **AI-powered multilingual language learning platform** combining a structured **10-module CEFR A1 Curriculum** with AI-powered scenario-based practice for a "True Bilingual" learning experience. Users learn in their target language while receiving explanations in their native language.

## Live Production

Both the frontend and API share the same CloudFront domain, routed by path:

| | URL |
|---|---|
| **Frontend** (`/`) | https://d2r1f6dy1chiig.cloudfront.net |
| **Backend API** (`/api/*`) | https://d2r1f6dy1chiig.cloudfront.net/api |

## Key Features

- **Complete A1 Curriculum**: All 10 modules (A1.1–A1.10) fully implemented with 8–9 lessons each
- **AI-Powered Tutoring**: Scenario-based practice mode powered by Llama 3 8B via RunPod Serverless
- **Voice Integration**: Whisper STT for speech recognition + Azure Speech Services TTS with gendered character voices
- **13 Exercise Types**: Info Cards, Match Pairs, Unscramble, Arrange, Echo Chamber, Listening/Reading Comprehension, Free Writing, Form Fill, Boss Fight, and more
- **Google OAuth**: Full sign-in flow with automatic profile creation and language setup
- **Context-Aware Validation**: Intelligent client-side and server-side validation with pedagogical feedback

## Architecture & Deployment

### Production Stack

| Layer | Technology | Hosting |
|---|---|---|
| **Frontend** | React 18 + Tailwind CSS | AWS S3 + CloudFront |
| **Backend** | FastAPI (Python 3.11) | AWS ECS Fargate |
| **HTTPS / CDN** | AWS CloudFront | — |
| **Load Balancer** | AWS ALB | — |
| **LLM** | Llama 3 8B Instruct GPTQ | RunPod Serverless GPU |
| **Database** | MongoDB Atlas | — |
| **STT** | OpenAI Whisper (`small`, baked into image) | ECS Fargate |
| **TTS** | Azure Speech Services | — |
| **Auth** | Google OAuth 2.0 | — |

### CI/CD

Deployments are automated via GitHub Actions (`.github/workflows/deploy.yml`):
- **Frontend**: on push to `main` → `npm run build` → S3 sync → CloudFront invalidation
- **Backend**: manual trigger → `docker build` → ECR push → ECS service update

### External Service Dependencies

| Service | Purpose | Required |
|---|---|---|
| MongoDB Atlas | User data, progress, lessons, scenarios | Yes |
| RunPod Serverless | LLM inference (Llama 3 8B) | Yes (practice mode) |
| Azure Speech Services | Text-to-speech | Yes (voice exercises) |
| Google OAuth 2.0 | Authentication | Yes |
| AWS (S3, ECR, ECS, ALB, CloudFront) | Infrastructure | Yes (production) |

## Project Structure

```
polybot/
├── backend/
│   ├── server.py                 # FastAPI main server
│   ├── llm_client.py             # RunPod serverless LLM client (async)
│   ├── practice_mode.py          # Scenario-based practice logic
│   ├── character_voices.py       # Character-gender mapping & voice selection
│   ├── a1_1_module_data.py       # A1.1–A1.10 curriculum data (10 files)
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # python:3.11-slim; Whisper model baked in
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
5. ✅ **Production Deployment** — ECS Fargate + CloudFront HTTPS + Google OAuth live
6. ✅ **S3 + CloudFront Frontend** — Static frontend served via CloudFront from S3
7. ✅ **GitHub Actions CI/CD** — Automated frontend deploy on push to main
8. ✅ **Session Persistence** — `/auth/me` endpoint + session cookie across reloads
9. **Streaming Pipeline** — Real-time LLM/TTS streaming to reduce latency
10. **Scenario-Based Practice Mode** — Game state architecture, Stage Manager, Post-Game Report
11. **Mobile App** — Capacitor-based native apps (Android/iOS)
12. **Global Expansion** — Multi-language curriculum + multi-model support (Qwen, Aya)
13. **Custom Domain** — Replace CloudFront workaround with proper domain + ACM cert on ALB

## License

[Add your license here]
