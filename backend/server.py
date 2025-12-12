import os
import time
import asyncio
import logging
import random
import re
import traceback
import io
import gc
import tempfile
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, status, Depends, Request, UploadFile, File, Form, Body
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Optional, Union
from uvicorn.config import logger

# NEW IMPORTS FOR GOOGLE OAUTH
from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.middleware.sessions import SessionMiddleware 
from urllib.parse import urlencode

# HuggingFace Transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import whisper

try:
    import azure.cognitiveservices.speech as speechsdk
    AZURE_SPEECH_AVAILABLE = True
except ImportError:
    AZURE_SPEECH_AVAILABLE = False
    logger.warning("Azure Speech SDK not available. Install with: pip install azure-cognitiveservices-speech")

# Practice Mode imports
from scenario_templates import get_scenario_template, get_all_scenarios, build_stage_manager_prompt
from practice_mode import GameState, check_goal_achievement, generate_pronunciation_feedback, generate_grammar_vocabulary_review
from practice_cache import get_cached_system_prompt, get_template_response

# Character voice mapping for gendered TTS
from character_voices import get_voice_for_character, extract_character_name

# --- Configuration ---
# Allow OAuth over HTTP for local development
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

model = None
tokenizer = None
text_generator = None 
db_client: Optional[AsyncIOMotorClient] = None
db = None
is_loading = True
whisper_model = None

# Default to pre-quantized GPTQ model (4-bit, ~5.5GB VRAM)
# Override with MODEL_NAME env var if needed (e.g., for non-GPTQ models)
MODEL_NAME = os.getenv("MODEL_NAME", "TheBloke/Llama-3-8B-Instruct-GPTQ") 
TRANSFORMERS_CACHE = os.getenv("TRANSFORMERS_CACHE", "/app/model_cache")
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017")
DB_NAME = os.getenv("DB_NAME", "polybot_database")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
WHISPER_MODEL_NAME = os.getenv("WHISPER_MODEL_NAME", "turbo")
UNLOAD_VOICE_MODELS = os.getenv("UNLOAD_VOICE_MODELS", "false").lower() == "true"
# Azure Speech Service configuration
AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

# OAUTH CREDENTIALS
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY", "A_SECURE_RANDOM_STRING_FOR_SESSION") 

origins = ["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:3000"]
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# --- CONSTANTS ---
GOOGLE_REDIRECT_URI = "http://localhost:8000/api/google/auth"
LLAMA_STOP_TOKENS = []

class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("GET /health") == -1

# --- Schemas ---

class DialogueLine(BaseModel):
    speaker: str
    text: str
    translation: str
    missing_word: Optional[str] = None 

class Exercise(BaseModel):
    type: str 
    prompt: str 
    options: Optional[List[str]] = None 
    correct_answer: Union[str, List[str]]
    pairs: Optional[List[List[str]]] = None
    dialogue: Optional[List[DialogueLine]] = None
    explanation: Optional[str] = None
    context_text: Optional[str] = None 
    sub_text: Optional[str] = None

class VocabularyItem(BaseModel):
    term: str
    translation: str
    context_sentence: Optional[str] = None
    target_lang: Optional[str] = None
    proficiency: float = 0.0
    is_header: bool = False

class Lesson(BaseModel):
    id: str = Field(..., alias="_id")
    title: str
    goal: str
    communicative_goal: str
    topics: List[str]
    ai_prompt_context: str
    vocabulary: List[VocabularyItem] = [] 
    exercises: List[Exercise] = []        

class LessonProgress(BaseModel):
    module_id: str
    target_lang: str = "en" 
    mastery_score: float = 0.0
    last_practiced: float = Field(default_factory=time.time)
    xp_earned: int = 0

class UserProfile(BaseModel):
    user_id: str
    name: str
    email: str
    native_language: str
    target_language: str
    level: str
    xp: int = 0
    words_learned: int = 0
    streak: int = 0
    progress: List[LessonProgress] = []
    vocabulary_list: List[VocabularyItem] = []
    
    class Config:
        populate_by_name = True

class UserUpdate(BaseModel):
    native_language: Optional[str] = None
    target_language: Optional[str] = None
    level: Optional[str] = None

class TutorRequest(BaseModel):
    user_message: str
    chat_history: List[dict]
    target_language: str
    native_language: str
    level: str
    lesson_id: Optional[str] = None

class LessonCompletionRequest(BaseModel):
    user_id: str
    lesson_id: str
    score: int
    total_questions: int

class InitiateChatRequest(BaseModel):
    target_language: str
    native_language: str
    level: str
    lesson_id: str


class TTSRequest(BaseModel):
    text: str
    language: str

class VoiceAnalyzeResponse(BaseModel):
    text: str
    confidence: float
    phonetic_score: float

class BossCheckRequest(BaseModel):
    user_message: str
    turn_number: int
    conversation_history: List[dict]
    lesson_id: str
    target_language: str
    native_language: str

class BossCheckResponse(BaseModel):
    valid: bool
    feedback: str
    next_turn: int
    completed: bool
    used_words: Optional[List[str]] = []

class GrammarCheckRequest(BaseModel):
    text: str
    target_language: str
    native_language: str
    expected_words: List[str] = []
    round_number: int = 1
    turn_number: int = 1

class GrammarCheckResponse(BaseModel):
    has_errors: bool
    errors: List[str] = []
    suggestions: List[str] = []
    feedback: str
    spelling_score: float = 1.0
    grammar_score: float = 1.0

# Practice Mode Request/Response Models
class PracticeTextChatRequest(BaseModel):
    scenario_id: str
    user_message: str
    conversation_history: List[dict]
    target_language: str
    native_language: str

class PracticeVoiceChatRequest(BaseModel):
    scenario_id: str
    conversation_history: List[dict]
    target_language: str
    native_language: str

class PracticeInitiateRequest(BaseModel):
    scenario_id: str
    target_language: str
    native_language: str

class PostGameReportRequest(BaseModel):
    scenario_id: str
    conversation_transcript: str
    user_transcripts: List[dict]
    target_language: str
    native_language: str

# --- FastAPI Initialization ---

app = FastAPI(title="Polybot Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET_KEY)

# Mount static files for audio
static_dir = Path(__file__).parent / "static"
static_dir.mkdir(exist_ok=True)
audio_dir = static_dir / "audio"
audio_dir.mkdir(exist_ok=True)
try:
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")
except Exception as e:
    logger.warning(f"Could not mount static files: {e}")

oauth = OAuth()
if GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET:
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={'scope': 'openid email profile'}
    )
else:
    logger.warning("Google OAuth credentials not found.")

# --- HELPER FUNCTIONS ---
def normalize_lang(lang_input: str) -> str:
    if not lang_input: return "en"
    lang = lang_input.lower().strip()
    name_map = { "english": "en", "french": "fr", "spanish": "es", "italian": "it", "portuguese": "pt", "twi": "tw", "german": "de" }
    if lang in name_map: return name_map[lang]
    return lang if len(lang) == 2 else "en"

def get_full_lang_name(lang_code: str) -> str:
    lang_map = { 'en': 'English', 'fr': 'French', 'es': 'Spanish', 'it': 'Italian', 'pt': 'Portuguese', 'tw': 'Twi' }
    return lang_map.get(lang_code.lower(), 'the target language')

# --- EXPANDED A1 CURRICULUM CONTENT ---
CONTENT_DB = {
    # --- A1.1: Greetings ---
    "a1.1_title": { "en": "Greetings", "fr": "Salutations", "es": "Saludos", "it": "Saluti", "pt": "Saudações", "tw": "Nkyia" },
    "a1.1_goal": { "en": "Introduce yourself.", "fr": "Présentez-vous.", "es": "Preséntate.", "it": "Presentati.", "pt": "Apresente-se.", "tw": "Kyerɛ wo ho." },
    "a1.1_comm": { "en": "Introduce yourself", "fr": "Présentez-vous", "es": "Preséntate", "it": "Presentati", "pt": "Apresente-se", "tw": "Kyerɛ wo ho" },
    
    "concept_hello": { 
        "en": ["Hello", "Ciao", "Hello!", "Ciao!", ["Bye"]],
        "it": ["Ciao", "Hello", "Ciao, amico!", "Hello friend!", ["Addio"]], 
        "es": ["Hola", "Hello", "¡Hola amigo!", "Hello friend!", ["Adios"]], 
        "fr": ["Bonjour", "Hello", "Bonjour!", "Hello!", ["Au revoir"]],
        "pt": ["Olá", "Hello", "Olá!", "Hello!", ["Adeus"]],
        "tw": ["Akwaaba", "Hello", "Akwaaba!", "Hello!", ["Nante yie"]] 
    },
    "concept_whatname": { 
        "en": ["What is your name?", "Come ti chiami?", "What is your name?", "Come ti chiami?", ["Who?"]],
        "it": ["Come ti chiami?", "What is your name?", "Come ti chiami tu?", "What is your name?", ["Chi sei?"]], 
        "es": ["¿Cómo te llamas?", "What is your name?", "¿Cómo te llamas?", "What is your name?", ["¿Qué?"]], 
        "fr": ["Comment tu t'appelles?", "What is your name?", "Comment tu t'appelles?", "What is your name?", ["Qui?"]],
        "pt": ["Como te chamas?", "What is your name?", "Como te chamas?", "What is your name?", ["Quem?"]],
        "tw": ["Wo din de sɛn?", "What is your name?", "Wo din de sɛn?", "What is your name?", ["Hwan?"]] 
    },
    "concept_name": { 
        "en": ["My name is", "Mi chiamo", "My name is Polybot.", "Mi chiamo Polybot.", ["I name"]],
        "it": ["Mi chiamo", "My name is", "Mi chiamo Polybot.", "My name is Polybot.", ["Io chiamo"]], 
        "es": ["Me llamo", "My name is", "Me llamo Polybot.", "My name is Polybot.", ["Yo llamo"]], 
        "fr": ["Je m'appelle", "My name is", "Je m'appelle Polybot.", "My name is Polybot.", ["Je suis"]],
        "pt": ["Chamo-me", "My name is", "Chamo-me Polybot.", "My name is Polybot.", ["Eu sou"]],
        "tw": ["Me din de", "My name is", "Me din de Polybot.", "My name is Polybot.", ["Me din"]] 
    },
    "concept_andyou": { 
        "en": ["And you?", "E tu?", "I am fine, and you?", "Sto bene, e tu?", ["And u?"]],
        "it": ["E tu?", "And you?", "Bene, e tu?", "I am fine, and you?", ["O tu?"]], 
        "es": ["¿Y tú?", "And you?", "Bien, ¿y tú?", "I am fine, and you?", ["¿O tu?"]], 
        "fr": ["Et toi?", "And you?", "Ça va, et toi?", "I am fine, and you?", ["Et vous?"]],
        "pt": ["E tu?", "And you?", "Estou bem, e tu?", "I am fine, and you?", ["E você?"]],
        "tw": ["Na wo nso ɛ?", "And you?", "Me ho yɛ, na wo nso ɛ?", "I am fine, and you?", ["Na wo?"]] 
    },
    "concept_pleased": { 
        "en": ["Nice to meet you", "Piacere", "Nice to meet you!", "Piacere!", ["Sad"]],
        "it": ["Piacere", "Nice to meet you", "Piacere!", "Nice to meet you!", ["Dispiacere"]], 
        "es": ["Mucho gusto", "Nice to meet you", "¡Mucho gusto!", "Nice to meet you!", ["Mal"]], 
        "fr": ["Enchanté", "Nice to meet you", "Enchanté!", "Nice to meet you!", ["Désolé"]],
        "pt": ["Prazer", "Nice to meet you", "Prazer!", "Nice to meet you!", ["Desculpa"]],
        "tw": ["Me pa wo kyɛw", "Nice to meet you", "Me pa wo kyɛw.", "Nice to meet you.", ["Daabi"]] 
    },
    "concept_goodbye": { 
        "en": ["Goodbye", "Arrivederci", "Goodbye friend.", "Arrivederci amico.", ["Hello"]],
        "it": ["Arrivederci", "Goodbye", "Arrivederci amico.", "Goodbye friend.", ["Ciao"]], 
        "es": ["Adiós", "Goodbye", "Adiós amigo.", "Goodbye friend.", ["Hola"]], 
        "fr": ["Au revoir", "Goodbye", "Au revoir mon ami.", "Goodbye friend.", ["Bonjour"]],
        "pt": ["Adeus", "Goodbye", "Adeus amigo.", "Goodbye friend.", ["Olá"]],
        "tw": ["Nante yie", "Goodbye", "Nante yie adamfo.", "Goodbye friend.", ["Akwaaba"]] 
    },

    
    "concept_howmuch": { "en": ["How much?", "Quanto?", "How much is it?", "Quanto costa?", ["When?"]], "fr": ["C'est combien?", "How much?", "C'est combien?", "How much?", ["Quand?"]], "es": ["¿Cuánto cuesta?", "How much?", "¿Cuánto cuesta?", "How much?", ["¿Cuándo?"]], "it": ["Quanto costa?", "How much?", "Quanto costa?", "How much?", ["Quando?"]], "pt": ["Quanto custa?", "How much?", "Quanto custa?", "How much?", ["Quando?"]], "tw": ["Eyɛ sɛn?", "How much?", "Eyɛ sɛn?", "How much?", ["Sɛn?"]] },
    "concept_cash": { 
        "en": ["Cash", "Contanti", "I pay cash.", "Pago con i soldi.", ["Card"]],
        "fr": ["Liquide", "Cash", "Je paie en liquide.", "I pay cash.", ["Carte"]],
        "es": ["Efectivo", "Cash", "Pago en efectivo.", "I pay cash.", ["Tarjeta"]], 
        "it": ["Soldi", "Cash", "Pago con i soldi.", "I pay with money.", ["Carta"]], 
        "pt": ["Dinheiro", "Cash", "Pago em dinheiro.", "I pay cash.", ["Cartão"]],
        "tw": ["Sika", "Cash", "Metua sika.", "I pay cash.", ["Kaade"]] 
    },
    "concept_card": { "en": ["Card", "Carta", "Credit card.", "Carta di credito.", ["Cash"]], "fr": ["Carte", "Card", "Carte de crédit.", "Credit card.", ["Liquide"]], "es": ["Tarjeta", "Card", "Tarjeta de crédito.", "Credit card.", ["Efectivo"]], "it": ["Carta", "Card", "Carta di credito.", "Credit card.", ["Soldi"]], "pt": ["Cartão", "Card", "Cartão de crédito.", "Credit card.", ["Dinheiro"]], "tw": ["Kaade", "Card", "Sika kaade.", "Credit card.", ["Sika"]] },
    
    # Numbers 1-5 (Contexts Standardized to Noun Phrases: One Coffee, Two Tickets, etc.)
    "concept_one": { "en": ["One", "Uno", "One coffee.", "Un caffè.", ["Two"]], "fr": ["Un", "One", "Un café.", "One coffee.", ["Deux"]], "es": ["Uno", "One", "Un café.", "One coffee.", ["Dos"]], "it": ["Uno", "One", "Un caffè.", "One coffee.", ["Due"]], "pt": ["Um", "One", "Um café.", "One coffee.", ["Dois"]], "tw": ["Baako", "One", "Kofi baako.", "One coffee.", ["Mmienu"]] },
    "concept_two": { "en": ["Two", "Due", "Two tickets.", "Due biglietti.", ["Three"]], "fr": ["Deux", "Two", "Deux billets.", "Two tickets.", ["Trois"]], "es": ["Dos", "Two", "Dos billetes.", "Two tickets.", ["Tres"]], "it": ["Due", "Two", "Due biglietti.", "Two tickets.", ["Tre"]], "pt": ["Dois", "Two", "Dois bilhetes.", "Two tickets.", ["Três"]], "tw": ["Mmienu", "Two", "Tiket mmienu.", "Two tickets.", ["Mmiɛnsa"]] },
    "concept_three": { "en": ["Three", "Tre", "Three days.", "Tre giorni.", ["Four"]], "fr": ["Trois", "Three", "Trois jours.", "Three days.", ["Quatre"]], "es": ["Tres", "Three", "Tres días.", "Three days.", ["Cuatro"]], "it": ["Tre", "Three", "Tre giorni.", "Three days.", ["Quattro"]], "pt": ["Três", "Three", "Três dias.", "Three days.", ["Quatro"]], "tw": ["Mmiɛnsa", "Three", "Nna mmiɛnsa.", "Three days.", ["Enan"]] },
    "concept_four": { "en": ["Four", "Quattro", "Four people.", "Quattro persone.", ["Five"]], "fr": ["Quatre", "Four", "Quatre personnes.", "Four people.", ["Cinq"]], "es": ["Cuatro", "Four", "Cuatro personas.", "Four people.", ["Cinco"]], "it": ["Quattro", "Four", "Quattro persone.", "Four people.", ["Cinque"]], "pt": ["Quatro", "Four", "Quatro pessoas.", "Four people.", ["Cinco"]], "tw": ["Ɛnan", "Four", "Nnipa ɛnan.", "Four people.", ["Enum"]] },
    "concept_five": { "en": ["Five", "Cinque", "Five euros.", "Cinque euro.", ["Six"]], "fr": ["Cinq", "Five", "Cinq euros.", "Five euros.", ["Six"]], "es": ["Cinco", "Five", "Cinco euros.", "Five euros.", ["Seis"]], "it": ["Cinque", "Five", "Cinque euro.", "Five euros.", ["Sei"]], "pt": ["Cinco", "Five", "Cinco euros.", "Five euros.", ["Seis"]], "tw": ["Enum", "Five", "Sedi enum.", "Five cedis.", ["Nsia"]] },

    # --- A1.3: Food ---
    "a1.3_title": { "en": "Food", "fr": "Nourriture", "es": "Comida", "it": "Cibo", "pt": "Comida", "tw": "Aduane" },
    "a1.3_goal": { "en": "Order food.", "fr": "Commandez.", "es": "Pedir comida.", "it": "Ordina cibo.", "pt": "Pedir comida.", "tw": "Tɔ aduane." },
    "a1.3_comm": { "en": "Order a drink", "fr": "Commander", "es": "Pedir bebida", "it": "Ordina bevanda", "pt": "Pedir bebida", "tw": "Tɔ nsa" },
    "concept_coffee": { "en": ["Coffee", "Caffè", "Coffee please.", "Caffè per favore.", ["Water"]], "fr": ["Café", "Coffee", "Un café.", "A coffee.", ["Eau"]], "es": ["El café", "Coffee", "Un café.", "A coffee.", ["Agua"]], "it": ["Il caffè", "Coffee", "Un caffè.", "A coffee.", ["Acqua"]], "pt": ["O café", "Coffee", "Um café.", "A coffee.", ["Água"]], "tw": ["Kofi", "Coffee", "Kofi.", "Coffee.", ["Nsuo"]] },
    "concept_water": { "en": ["Water", "Acqua", "Water please.", "Acqua per favore.", ["Wine"]], "fr": ["L'eau", "Water", "De l'eau.", "Some water.", ["Vin"]], "es": ["El agua", "Water", "Un agua.", "Water.", ["Vino"]], "it": ["L'acqua", "Water", "Un'acqua.", "Water.", ["Vino"]], "pt": ["A água", "Water", "Uma água.", "Water.", ["Vinho"]], "tw": ["Nsuo", "Water", "Nsuo.", "Water.", ["Nsa"]] },
    "concept_bread": { "en": ["Bread", "Pane", "Fresh bread.", "Pane fresco.", ["Milk"]], "fr": ["Le pain", "Bread", "Pain frais.", "Fresh bread.", ["Lait"]], "es": ["El pan", "Bread", "Pan fresco.", "Fresh bread.", ["Leche"]], "it": ["Il pane", "Bread", "Pane fresco.", "Fresh bread.", ["Latte"]], "pt": ["O pão", "Bread", "Pão fresco.", "Fresh bread.", ["Leite"]], "tw": ["Paano", "Bread", "Paano.", "Bread.", ["Nkosua"]] },
    "concept_please": { "en": ["Please", "Per favore", "Yes please.", "Sì per favore.", ["No"]], "fr": ["S'il vous plaît", "Please", "Oui s'il vous plaît.", "Yes please.", ["Non"]], "es": ["Por favor", "Please", "Por favor.", "Please.", ["Gracias"]], "it": ["Per favore", "Please", "Per favore.", "Please.", ["Grazie"]], "pt": ["Por favor", "Please", "Por favor.", "Please.", ["Obrigado"]], "tw": ["Mepa wo kyɛw", "Please", "Mepa wo kyɛw.", "Please.", ["Medaase"]] },
    "concept_bill": { "en": ["The bill", "Il conto", "The bill please.", "Il conto.", ["Menu"]], "fr": ["L'addition", "The bill", "L'addition.", "The bill.", ["Menu"]], "es": ["La cuenta", "The bill", "La cuenta.", "The bill.", ["Menú"]], "it": ["Il conto", "The bill", "Il conto.", "The bill.", ["Menu"]], "pt": ["A conta", "The bill", "A conta.", "The bill.", ["Menu"]], "tw": ["Ka no", "The bill", "Ka no.", "The bill.", ["Aduane"]] },

    # --- A1.4: Family ---
    "a1.4_title": { "en": "Family", "fr": "Famille", "es": "Familia", "it": "Famiglia", "pt": "Família", "tw": "Abusua" },
    "a1.4_goal": { "en": "Describe family.", "fr": "Décrivez la famille.", "es": "Describir familia.", "it": "Descrivi famiglia.", "pt": "Descrever família.", "tw": "Kyerɛ abusua." },
    "a1.4_comm": { "en": "Talk about family", "fr": "Parler de la famille", "es": "Hablar de familia", "it": "Parla di famiglia", "pt": "Falar da família", "tw": "Kasa fa abusua" },
    "concept_mother": { "en": ["Mother", "Madre", "My mother.", "Mia madre.", ["Father"]], "fr": ["Mère", "Mother", "Ma mère.", "My mother.", ["Père"]], "es": ["La madre", "Mother", "Mi madre.", "My mother.", ["Padre"]], "it": ["La madre", "Mother", "Mia madre.", "My mother.", ["Padre"]], "pt": ["A mãe", "Mother", "Minha mãe.", "My mother.", ["Pai"]], "tw": ["Maame", "Mother", "Me maame.", "My mother.", ["Papa"]] },
    "concept_father": { "en": ["Father", "Padre", "My father.", "Mio padre.", ["Mother"]], "fr": ["Père", "Father", "Mon père.", "My father.", ["Mère"]], "es": ["El padre", "Father", "Mi padre.", "My father.", ["Madre"]], "it": ["Il padre", "Father", "Mio padre.", "My father.", ["Madre"]], "pt": ["O pai", "Father", "Meu pai.", "My father.", ["Mãe"]], "tw": ["Papa", "Father", "Me papa.", "My father.", ["Maame"]] },
    "concept_brother": { "en": ["Brother", "Fratello", "My brother.", "Mio fratello.", ["Sister"]], "fr": ["Frère", "Brother", "Mon frère.", "My brother.", ["Soeur"]], "es": ["El hermano", "Brother", "Mi hermano.", "My brother.", ["Hermana"]], "it": ["Il fratello", "Brother", "Mio fratello.", "My brother.", ["Sorella"]], "pt": ["O irmão", "Brother", "Meu irmão.", "My brother.", ["Irmã"]], "tw": ["Nuabarima", "Brother", "Me nuabarima.", "My brother.", ["Nuabaa"]] },
    "concept_sister": { "en": ["Sister", "Sorella", "My sister.", "Mia sorella.", ["Brother"]], "fr": ["Soeur", "Sister", "Ma soeur.", "My sister.", ["Frère"]], "es": ["La hermana", "Sister", "Mi hermana.", "My sister.", ["Hermano"]], "it": ["La sorella", "Sister", "Mia sorella.", "My sister.", ["Fratello"]], "pt": ["A irmã", "Sister", "Minha irmã.", "My sister.", ["Irmão"]], "tw": ["Nuabaa", "Sister", "Me nuabaa.", "My sister.", ["Nuabarima"]] },
    "concept_family": { "en": ["Family", "Famiglia", "Big family.", "Grande famiglia.", ["Friend"]], "fr": ["Famille", "Family", "Grande famille.", "Big family.", ["Ami"]], "es": ["La familia", "Family", "La familia.", "The family.", ["Amigo"]], "it": ["La famiglia", "Family", "La famiglia.", "The family.", ["Amico"]], "pt": ["A família", "Family", "A família.", "The family.", ["Amigo"]], "tw": ["Abusua", "Family", "Abusua.", "Family.", ["Adamfo"]] },

    # --- A1.5: Daily Routine ---
    "a1.5_title": { "en": "Daily Routine", "fr": "Routine", "es": "Rutina", "it": "Routine", "pt": "Rotina" },
    "a1.5_goal": { "en": "Talk about your day.", "fr": "Parlez de votre journée.", "es": "Habla de tu día.", "it": "Parla della tua giornata.", "pt": "Fale do seu dia." },
    "a1.5_comm": { "en": "Describe routine", "fr": "Décrire la routine", "es": "Describir rutina", "it": "Descrivi routine", "pt": "Descrever rotina" },
    "concept_morning": { "en": ["Morning", "Mattina", "In the morning.", "Di mattina.", ["Night"]], "fr": ["Matin", "Morning", "Le matin.", "The morning.", ["Nuit"]], "es": ["La mañana", "Morning", "Por la mañana.", "In the morning.", ["La noche"]], "it": ["La mattina", "Morning", "Di mattina.", "In the morning.", ["La notte"]], "pt": ["Manhã", "Morning", "De manhã.", "In the morning.", ["Noite"]] },
    "concept_evening": { "en": ["Evening", "Sera", "Good evening.", "Buona sera.", ["Day"]], "fr": ["Soir", "Evening", "Bonsoir.", "Good evening.", ["Jour"]], "es": ["La tarde", "Evening", "Buenas tardes.", "Good evening.", ["Día"]], "it": ["La sera", "Evening", "Buona sera.", "Good evening.", ["Giorno"]], "pt": ["Tarde", "Evening", "Boa tarde.", "Good afternoon.", ["Dia"]] },
    "concept_work": { "en": ["To work", "Lavorare", "I work today.", "Lavoro oggi.", ["Sleep"]], "fr": ["Travailler", "To work", "Je travaille.", "I work.", ["Dormir"]], "es": ["Trabajar", "To work", "Trabajo hoy.", "I work today.", ["Dormir"]], "it": ["Lavorare", "To work", "Lavoro oggi.", "I work today.", ["Dormire"]], "pt": ["Trabalhar", "To work", "Eu trabalho.", "I work.", ["Dormir"]] },
    "concept_sleep": { "en": ["To sleep", "Dormire", "I sleep now.", "Dormo ora.", ["Run"]], "fr": ["Dormir", "To sleep", "Je dors.", "I sleep.", ["Courir"]], "es": ["Dormir", "To sleep", "Duermo ahora.", "I sleep now.", ["Correr"]], "it": ["Dormire", "To sleep", "Dormo ora.", "I sleep now.", ["Correre"]], "pt": ["Dormir", "To sleep", "Eu durmo.", "I sleep.", ["Correr"]] },
    "concept_today": { "en": ["Today", "Oggi", "Today is Monday.", "Oggi è lunedì.", ["Yesterday"]], "fr": ["Aujourd'hui", "Today", "Aujourd'hui.", "Today.", ["Hier"]], "es": ["Hoy", "Today", "Hoy es lunes.", "Today is Monday.", ["Ayer"]], "it": ["Oggi", "Today", "Oggi è lunedì.", "Today is Monday.", ["Ieri"]], "pt": ["Hoje", "Today", "Hoje.", "Today.", ["Ontem"]] },

    # --- A1.6: Time & Numbers 6-10 (NEW) ---
    "a1.6_title": { "en": "Time & Numbers 6-10", "fr": "Heure et Nombres 6-10", "es": "Hora y Números 6-10", "it": "Orario e Numeri 6-10", "pt": "Hora e Números 6-10", "tw": "Mmere ne Nontabuo 6-10" },
    "a1.6_goal": { "en": "Tell time and count.", "fr": "Dire l'heure et compter.", "es": "Decir la hora.", "it": "Dì l'ora e conta.", "pt": "Dizer as horas.", "tw": "Kyerɛ mmere." },
    "a1.6_comm": { "en": "Ask the time", "fr": "Demander l'heure", "es": "Preguntar la hora", "it": "Chiedi l'ora", "pt": "Perguntar as horas", "tw": "Bisa mmere" },
    
    "concept_time": { "en": ["Time", "Tempo/Ora", "What time is it?", "Che ore sono?", ["Date"]], "fr": ["Heure", "Time", "Quelle heure est-il?", "What time is it?", ["Date"]], "es": ["La hora", "Time", "¿Qué hora es?", "What time is it?", ["Fecha"]], "it": ["L'ora", "Time", "Che ore sono?", "What time is it?", ["Data"]], "pt": ["A hora", "Time", "Que horas são?", "What time is it?", ["Data"]], "tw": ["Mmere", "Time", "Ɛyɛ mmere bɛn?", "What time is it?", ["Da"]] },
    "concept_now": { "en": ["Now", "Adesso", "Do it now.", "Fallo adesso.", ["Later"]], "fr": ["Maintenant", "Now", "Maintenant.", "Now.", ["Plus tard"]], "es": ["Ahora", "Now", "Ahora.", "Now.", ["Luego"]], "it": ["Adesso", "Now", "Adesso.", "Now.", ["Dopo"]], "pt": ["Agora", "Now", "Agora.", "Now.", ["Depois"]], "tw": ["Seesei", "Now", "Seesei ara.", "Now.", ["Akyire"]] },
    
    # Group 2: 6-10 (Contexts Standardized)
    "concept_six": { "en": ["Six", "Sei", "Six months.", "Sei mesi.", ["Seven"]], "fr": ["Six", "Six", "Six mois.", "Six months.", ["Sept"]], "es": ["Seis", "Six", "Seis meses.", "Six months.", ["Siete"]], "it": ["Sei", "Six", "Sei mesi.", "Six months.", ["Sette"]], "pt": ["Seis", "Six", "Seis meses.", "Six months.", ["Sete"]], "tw": ["Nsia", "Six", "Abosome nsia.", "Six months.", ["Nson"]] },
    "concept_seven": { "en": ["Seven", "Sette", "Seven days.", "Sette giorni.", ["Eight"]], "fr": ["Sept", "Seven", "Sept jours.", "Seven days.", ["Huit"]], "es": ["Siete", "Seven", "Siete días.", "Seven days.", ["Ocho"]], "it": ["Sette", "Seven", "Sette giorni.", "Seven days.", ["Otto"]], "pt": ["Sete", "Seven", "Sete dias.", "Seven days.", ["Oito"]], "tw": ["Nson", "Seven", "Nna nson.", "Seven days.", ["Nwɔtwe"]] },
    "concept_eight": { "en": ["Eight", "Otto", "Eight o'clock.", "Alle otto.", ["Nine"]], "fr": ["Huit", "Eight", "Huit heures.", "Eight o'clock.", ["Neuf"]], "es": ["Ocho", "Eight", "A las ocho.", "Eight o'clock.", ["Nueve"]], "it": ["Otto", "Eight", "Alle otto.", "Eight o'clock.", ["Nove"]], "pt": ["Oito", "Eight", "Às oito.", "Eight o'clock.", ["Nove"]], "tw": ["Nwɔtwe", "Eight", "Nnɔn nwɔtwe.", "Eight o'clock.", ["Nkron"]] },
    "concept_nine": { "en": ["Nine", "Nove", "Nine students.", "Nove studenti.", ["Ten"]], "fr": ["Neuf", "Nine", "Neuf étudiants.", "Nine students.", ["Dix"]], "es": ["Nueve", "Nine", "Nueve estudiantes.", "Nine students.", ["Diez"]], "it": ["Nove", "Nine", "Nove studenti.", "Nine students.", ["Dieci"]], "pt": ["Nove", "Nine", "Nove estudantes.", "Nine students.", ["Dez"]], "tw": ["Nkron", "Nine", "Asukuufoɔ nkron.", "Nine students.", ["Edu"]] },
    "concept_ten": { "en": ["Ten", "Dieci", "Ten minutes.", "Dieci minuti.", ["Eleven"]], "fr": ["Dix", "Ten", "Dix euros.", "Ten euros.", ["Neuf"]], "es": ["Diez", "Ten", "Diez euros.", "Ten euros.", ["Nueve"]], "it": ["Dieci", "Ten", "Dieci minuti.", "Ten minutes.", ["Nove"]], "pt": ["Dez", "Ten", "Dez euros.", "Ten euros.", ["Nove"]], "tw": ["Edu", "Ten", "Sedi edu.", "Ten cedis.", ["Nkron"]] },

    # --- A1.7: At Home ---
    "a1.7_title": { "en": "At Home", "fr": "À la maison", "es": "En Casa", "it": "A Casa", "pt": "Em Casa" },
    "a1.7_goal": { "en": "Describe your home.", "fr": "Décrivez votre maison.", "es": "Describe tu casa.", "it": "Descrivi la tua casa.", "pt": "Descreva sua casa." },
    "a1.7_comm": { "en": "Describe where items are", "fr": "Décrire la maison", "es": "Describir casa", "it": "Descrivi casa", "pt": "Descrever casa" },
    "concept_house": { "en": ["House", "Casa", "My house.", "Home.", ["Car"]], "fr": ["Maison", "House", "Ma maison.", "My house.", ["Voiture"]], "es": ["La casa", "House", "Mi casa.", "My house.", ["Coche"]], "it": ["La casa", "House", "La mia casa.", "My house.", ["Auto"]], "pt": ["A casa", "House", "A minha casa.", "My house.", ["Carro"]] },
    "concept_kitchen": { "en": ["Kitchen", "Cucina", "In the kitchen.", "Cook.", ["Bed"]], "fr": ["Cuisine", "Kitchen", "Dans la cuisine.", "In the kitchen.", ["Lit"]], "es": ["La cocina", "Kitchen", "En la cocina.", "Cocinar.", ["Cama"]], "it": ["La cucina", "Kitchen", "In cucina.", "Cucinare.", ["Letto"]], "pt": ["Cozinha", "Kitchen", "Na cozinha.", "In the kitchen.", ["Cama"]] },
    "concept_room": { "en": ["Room", "Stanza", "My room.", "Small.", ["Street"]], "fr": ["Chambre", "Room", "Ma chambre.", "My room.", ["Rue"]], "es": ["La habitación", "Room", "Mi habitación.", "Pequeña.", ["Calle"]], "it": ["La stanza", "Room", "La mia stanza.", "Piccola.", ["Strada"]], "pt": ["Quarto", "Room", "Meu quarto.", "My room.", ["Rua"]] },
    "concept_bed": { "en": ["Bed", "Letto", "Big bed.", "Sleep.", ["Chair"]], "fr": ["Lit", "Bed", "Grand lit.", "Big bed.", ["Chaise"]], "es": ["La cama", "Bed", "Cama grande.", "Dormir.", ["Silla"]], "it": ["Il letto", "Bed", "Letto grande.", "Dormire.", ["Sedia"]], "pt": ["Cama", "Bed", "Cama grande.", "Big bed.", ["Cadeira"]] },

    # --- A1.8: Weather ---
    "a1.8_title": { "en": "Weather", "fr": "Météo", "es": "El Tiempo", "it": "Meteo", "pt": "Tempo" },
    "a1.8_goal": { "en": "Talk about weather.", "fr": "Parlez du temps.", "es": "Habla del tiempo.", "it": "Parla del tempo.", "pt": "Fale do tempo." },
    "a1.8_comm": { "en": "Discuss weather", "fr": "Parler météo", "es": "Hablar del tiempo", "it": "Discuti meteo", "pt": "Falar do tempo" },
    "concept_sun": { "en": ["Sun", "Sole", "Sunny.", "Hot.", ["Rain"]], "fr": ["Soleil", "Sun", "Du soleil.", "Sunny.", ["Pluie"]], "es": ["El sol", "Sun", "Hace sol.", "Sunny.", ["Lluvia"]], "it": ["Il sole", "Sun", "C'è il sole.", "Sunny.", ["Pioggia"]], "pt": ["Sol", "Sun", "Faz sol.", "Sunny.", ["Chuva"]] },
    "concept_rain": { "en": ["Rain", "Pioggia", "It rains.", "Wet.", ["Sun"]], "fr": ["Pluie", "Rain", "Il pleut.", "It rains.", ["Soleil"]], "es": ["La lluvia", "Rain", "Llueve.", "It rains.", ["Sol"]], "it": ["La pioggia", "Rain", "Piove.", "It rains.", ["Sole"]], "pt": ["Chuva", "Rain", "Chove.", "It rains.", ["Sol"]] },
    "concept_cold": { "en": ["Cold", "Freddo", "It is cold.", "Ice.", ["Hot"]], "fr": ["Froid", "Cold", "Il fait froid.", "It is cold.", ["Chaud"]], "es": ["Frío", "Cold", "Hace frío.", "Hielo.", ["Caliente"]], "it": ["Freddo", "Cold", "Fa freddo.", "Ghiaccio.", ["Caldo"]], "pt": ["Frio", "Cold", "Está frio.", "It is cold.", ["Quente"]] },
    "concept_hot": { "en": ["Hot", "Caldo", "It is hot.", "Summer.", ["Cold"]], "fr": ["Chaud", "Hot", "Il fait chaud.", "It is hot.", ["Froid"]], "es": ["Caliente", "Hot", "Hace calor.", "Verano.", ["Frío"]], "it": ["Caldo", "Hot", "Fa caldo.", "Estate.", ["Freddo"]], "pt": ["Quente", "Hot", "Está quente.", "It is hot.", ["Frio"]] },

    # --- A1.9: Travel ---
    "a1.9_title": { "en": "Travel", "fr": "Voyage", "es": "Viajes", "it": "Viaggi", "pt": "Viagem" },
    "a1.9_goal": { "en": "Ask for directions.", "fr": "Demandez directions.", "es": "Pedir direcciones.", "it": "Chiedi direzioni.", "pt": "Pedir direções." },
    "a1.9_comm": { "en": "Buy a ticket", "fr": "Acheter un billet", "es": "Comprar billete", "it": "Compra biglietto", "pt": "Comprar bilhete" },
    "concept_ticket": { "en": ["Ticket", "Biglietto", "One ticket.", "Buy.", ["Passport"]], "fr": ["Billet", "Ticket", "Un billet.", "One ticket.", ["Passeport"]], "es": ["El billete", "Ticket", "Un billete.", "Comprar.", ["Pasaporte"]], "it": ["Il biglietto", "Ticket", "Un biglietto.", "Comprare.", ["Passaporto"]], "pt": ["Bilhete", "Ticket", "Um bilhete.", "One ticket.", ["Passaporte"]] },
    "concept_train": { "en": ["Train", "Treno", "Train to Rome.", "Fast.", ["Car"]], "fr": ["Train", "Train", "Le train.", "The train.", ["Voiture"]], "es": ["El tren", "Train", "El tren.", "The train.", ["Coche"]], "it": ["Il treno", "Train", "Il treno.", "The train.", ["Auto"]], "pt": ["Comboio", "Train", "O comboio.", "The train.", ["Carro"]] },
    "concept_bus": { "en": ["Bus", "Autobus", "Take the bus.", "Stop.", ["Plane"]], "fr": ["Bus", "Bus", "Le bus.", "The bus.", ["Avion"]], "es": ["El autobús", "Bus", "El autobús.", "The bus.", ["Avión"]], "it": ["L'autobus", "Bus", "L'autobus.", "The bus.", ["Aereo"]], "pt": ["Autocarro", "Bus", "O autocarro.", "The bus.", ["Avião"]] },
    "concept_station": { "en": ["Station", "Stazione", "Train station.", "Wait.", ["House"]], "fr": ["Gare", "Station", "La gare.", "The station.", ["Maison"]], "es": ["La estación", "Station", "La estación.", "The station.", ["Casa"]], "it": ["La stazione", "Station", "La stazione.", "The station.", ["Casa"]], "pt": ["Estação", "Station", "A estação.", "The station.", ["Casa"]] },

    # --- A1.10: Hobbies ---
    "a1.10_title": { "en": "Hobbies", "fr": "Loisirs", "es": "Aficiones", "it": "Hobby", "pt": "Hobbies" },
    "a1.10_goal": { "en": "Talk about hobbies.", "fr": "Parlez de loisirs.", "es": "Habla de aficiones.", "it": "Parla di hobby.", "pt": "Fale de hobbies." },
    "a1.10_comm": { "en": "Discuss interests", "fr": "Discuter intérêts", "es": "Discutir intereses", "it": "Discuti interessi", "pt": "Discutir interesses" },
    "concept_like": { "en": ["To like", "Piacere", "I like it.", "Good.", ["Hate"]], "fr": ["Aimer", "To like", "J'aime.", "I like.", ["Détester"]], "es": ["Gustar", "To like", "Me gusta.", "I like.", ["Odiar"]], "it": ["Mi piace", "To like", "Mi piace.", "I like.", ["Odio"]], "pt": ["Gostar", "To like", "Eu gosto.", "I like.", ["Odiar"]] },
    "concept_sport": { "en": ["Sport", "Sport", "Play sport.", "Run.", ["Sleep"]], "fr": ["Sport", "Sport", "Le sport.", "The sport.", ["Dormir"]], "es": ["El deporte", "Sport", "El deporte.", "The sport.", ["Dormir"]], "it": ["Lo sport", "Sport", "Lo sport.", "The sport.", ["Dormire"]], "pt": ["Desporto", "Sport", "O desporto.", "The sport.", ["Dormir"]] },
    "concept_music": { "en": ["Music", "Musica", "Listen to music.", "Song.", ["Silence"]], "fr": ["Musique", "Music", "La musique.", "The music.", ["Silence"]], "es": ["La música", "Music", "La música.", "The music.", ["Silencio"]], "it": ["La musica", "Music", "La musica.", "The music.", ["Silenzio"]], "pt": ["Música", "Music", "A música.", "The music.", ["Silêncio"]] },
    "concept_read": { "en": ["To read", "Leggere", "Read a book.", "Book.", ["Write"]], "fr": ["Lire", "To read", "Je lis.", "I read.", ["Écrire"]], "es": ["Leer", "To read", "Leo un libro.", "I read.", ["Escribir"]], "it": ["Leggere", "To read", "Leggo.", "I read.", ["Scrivere"]], "pt": ["Ler", "To read", "Eu leio.", "I read.", ["Escrever"]] },

    # --- A1.11: Health ---
    "a1.11_title": { "en": "Health", "fr": "Santé", "es": "Salud", "it": "Salute", "pt": "Saúde" },
    "a1.11_goal": { "en": "Describe health.", "fr": "Décrivez la santé.", "es": "Describir salud.", "it": "Descrivi salute.", "pt": "Descrever saúde." },
    "a1.11_comm": { "en": "Describe feelings", "fr": "Décrire sentiments", "es": "Describir salud", "it": "Descrivi sentimenti", "pt": "Descrever sentimentos" },
    "concept_doctor": { "en": ["Doctor", "Dottore", "The doctor.", "Help.", ["Teacher"]], "fr": ["Médecin", "Doctor", "Le médecin.", "The doctor.", ["Professeur"]], "es": ["El médico", "Doctor", "El médico.", "The doctor.", ["Profesor"]], "it": ["Il dottore", "Doctor", "Il dottore.", "The doctor.", ["Insegnante"]], "pt": ["Médico", "Doctor", "O médico.", "The doctor.", ["Professor"]] },
    "concept_sick": { "en": ["Sick", "Malato", "I am sick.", "Pain.", ["Happy"]], "fr": ["Malade", "Sick", "Je suis malade.", "I am sick.", ["Heureux"]], "es": ["Enfermo", "Sick", "Estoy enfermo.", "I am sick.", ["Feliz"]], "it": ["Malato", "Sick", "Sono malato.", "I am sick.", ["Felice"]], "pt": ["Doente", "Sick", "Estou doente.", "I am sick.", ["Feliz"]] },
    "concept_pain": { "en": ["Pain", "Dolore", "It hurts.", "Ouch.", ["Joy"]], "fr": ["Douleur", "Pain", "J'ai mal.", "I have pain.", ["Joie"]], "es": ["El dolor", "Pain", "Tengo dolor.", "I have pain.", ["Alegría"]], "it": ["Il dolore", "Pain", "Ho dolore.", "I have pain.", ["Gioia"]], "pt": ["Dor", "Pain", "Tenho dor.", "I have pain.", ["Alegria"]] },
    "concept_medicine": { "en": ["Medicine", "Medicina", "Take medicine.", "Pill.", ["Candy"]], "fr": ["Médicament", "Medicine", "Le médicament.", "Medicine.", ["Bonbon"]], "es": ["La medicina", "Medicine", "La medicina.", "Medicine.", ["Dulce"]], "it": ["La medicina", "Medicine", "La medicina.", "Medicine.", ["Caramella"]], "pt": ["Remédio", "Medicine", "O remédio.", "Medicine.", ["Doce"]] },
}

# --- CONVERSATION TEMPLATES (NEW) ---
LESSON_DIALOGUES = {
    "A1.1": {
        "en": [
            {"speaker": "A", "text": "Hello! What is your {name}?", "translation": "Ciao! Come ti chiami?"},
            {"speaker": "B", "text": "My name is John. And {you}?", "translation": "Mi chiamo John. E tu?"},
            {"speaker": "A", "text": "My name is Anna. {Nice} to meet you.", "translation": "Mi chiamo Anna. Piacere."}
        ],
        "it": [
            {"speaker": "A", "text": "Ciao! Come ti {chiami}?", "translation": "Hello! What is your name?"},
            {"speaker": "B", "text": "Mi chiamo Marco. E {tu}?", "translation": "My name is Marco. And you?"},
            {"speaker": "A", "text": "Mi chiamo Sofia. {Piacere}!", "translation": "My name is Sofia. Nice to meet you!"}
        ]
    },
}

# Map of Lesson ID to Concept Keys
LESSON_CONCEPTS = {
    "A1.1": ["concept_hello", "concept_whatname", "concept_name", "concept_andyou", "concept_pleased", "concept_goodbye"],
    "A1.3": ["concept_coffee", "concept_water", "concept_bread", "concept_please", "concept_bill"],
    "A1.4": ["concept_mother", "concept_father", "concept_brother", "concept_sister", "concept_family"],
    "A1.5": ["concept_morning", "concept_evening", "concept_work", "concept_sleep", "concept_today"],
    "A1.6": ["concept_time", "concept_now", "concept_six", "concept_seven", "concept_eight", "concept_nine", "concept_ten"], 
    "A1.7": ["concept_house", "concept_kitchen", "concept_room", "concept_bed"],
    "A1.8": ["concept_sun", "concept_rain", "concept_cold", "concept_hot"],
    "A1.9": ["concept_ticket", "concept_train", "concept_bus", "concept_station"],
    "A1.10": ["concept_like", "concept_sport", "concept_music", "concept_read"],
    "A1.11": ["concept_doctor", "concept_sick", "concept_pain", "concept_medicine"]
}

def get_text(key, lang):
    code = normalize_lang(lang)
    return CONTENT_DB.get(key, {}).get(code, CONTENT_DB.get(key, {}).get("en", "Missing"))

def get_concept(key, target, native):
    t_code = normalize_lang(target)
    n_code = normalize_lang(native)
    t_data = CONTENT_DB.get(key, {}).get(t_code)
    if not t_data: t_data = CONTENT_DB.get(key, {}).get("en", ["?", "?", "?", "?", ["?"]])
    n_data = CONTENT_DB.get(key, {}).get(n_code)
    if not n_data: n_data = CONTENT_DB.get(key, {}).get("en", ["?", "?", "?", "?", ["?"]])
    # Structure: [term, translation, context_in_this_lang, context_translation, distractors]
    # t_data[2] = target context, t_data[3] = native translation of target context
    # So n_context should be t_data[3] (the translation of the target context), not n_data[2]
    return t_data[0], n_data[0], t_data[2], t_data[3], t_data[3], t_data[4]

def generate_concept_flow(concept_key, target, native):
    term, trans, t_context, n_context, response, distractors = get_concept(concept_key, target, native)
    exercises = []
    exercises.append({ "type": "info_card", "prompt": "New Phrase", "correct_answer": term, "explanation": trans, "sub_text": "Listen and repeat." })
    exercises.append({ "type": "info_card", "prompt": "In Context", "correct_answer": t_context, "explanation": f"Usage: {term}", "sub_text": "See how it is used." })
    clean_term = term.rstrip("?.!…")
    escaped_term = re.escape(clean_term)
    pattern = re.compile(escaped_term, re.IGNORECASE)
    blank_sentence = pattern.sub("_____", t_context)
    if blank_sentence == t_context: blank_sentence = "_____ " + " ".join(t_context.split(" ")[2:]) if len(t_context.split(" ")) > 2 else "_____"
    options = [term] + random.sample(distractors, min(2, len(distractors)))
    random.shuffle(options)
    exercises.append({ "type": "fill_blank", "prompt": f"Complete: \"{blank_sentence}\"", "options": options, "correct_answer": term, "explanation": f"\"{t_context}\"" })
    spelling_opts = [term] + random.sample(distractors, min(2, len(distractors)))
    random.shuffle(spelling_opts)
    exercises.append({ "type": "multiple_choice", "prompt": f"Select the correct phrase for '{trans}'", "options": spelling_opts, "correct_answer": term, "explanation": f"{term} is correct." })
    # For arrange exercise: translate n_context (native language context) to t_context (target language context)
    # These should now match as n_context is the translation of t_context
    words = t_context.split(" ")
    extra_words = random.sample(distractors, min(2, len(distractors)))
    words.extend(extra_words)
    random.shuffle(words)
    exercises.append({ "type": "arrange", "prompt": f"Translate: '{n_context}'", "options": words, "correct_answer": t_context, "explanation": "Correct sentence structure." })
    return exercises

# NEW FUNCTION: Generate Conversation Exercise
def generate_conversation_exercise(lesson_id, target_lang, native_lang):
    """Creates a gap-fill conversation exercise."""
    t_code = normalize_lang(target_lang)
    
    # Fallback to English if specific lang dialogue missing
    dialogue_data = LESSON_DIALOGUES.get(lesson_id, {}).get(t_code, LESSON_DIALOGUES.get(lesson_id, {}).get("en", []))
    
    if not dialogue_data: return None

    processed_lines = []
    word_bank = []
    
    for line in dialogue_data:
        # Extract word in {brackets}
        match = re.search(r'\{(.*?)\}', line["text"])
        missing = None
        clean_text = line["text"]
        
        if match:
            missing = match.group(1)
            word_bank.append(missing)
            # Replace {word} with specific placeholder marker for frontend
            clean_text = line["text"].replace(f"{{{missing}}}", "___")
            
        processed_lines.append({
            "speaker": line["speaker"],
            "text": clean_text,
            "translation": line.get("translation", ""),
            "missing_word": missing
        })
    
    # Add some distractors to the word bank?
    # Simple shuffle for now
    random.shuffle(word_bank)
    
    return {
        "type": "conversation",
        "prompt": "Complete the Conversation",
        "dialogue": processed_lines,
        "options": word_bank, # The chips
        "correct_answer": "conversation_complete", # Placeholder
        "explanation": "Great conversation!"
    }

def generate_chat_input(system_content: str, conversation_history: List[dict] = None) -> str:
    global tokenizer
    messages = [{"role": "system", "content": system_content}]
    if conversation_history:
        for msg in conversation_history:
            role = 'user' if msg.get('role') == 'user' else 'assistant'
            messages.append({"role": role, "content": msg['content']}) 
    formatted_input = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    return formatted_input


# --- VOICE MODELS (WHISPER + Edge-TTS) ---

async def get_whisper_model():
    global whisper_model
    if whisper_model is not None:
        return whisper_model

    loop = asyncio.get_event_loop()

    def _load():
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = whisper.load_model(WHISPER_MODEL_NAME, device=device)
        return model

    whisper_model = await loop.run_in_executor(None, _load)
    return whisper_model


def release_whisper_model():
    global whisper_model
    if UNLOAD_VOICE_MODELS:
        whisper_model = None
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()


async def transcribe_audio_file(upload_file: UploadFile, language: Optional[str] = None):
    """Run Whisper on an uploaded audio file and return transcription."""
    model = await get_whisper_model()
    contents = await upload_file.read()

    suffix = os.path.splitext(upload_file.filename or "")[-1] or ".wav"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    loop = asyncio.get_event_loop()

    def _run():
        result = model.transcribe(tmp_path, language=language if language else None)
        return result

    try:
        result = await loop.run_in_executor(None, _run)
    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass
        release_whisper_model()

    return result


def get_azure_speech_voice(lang_code: str) -> str:
    """
    Get Azure Speech voice name for language code.
    Maps our language codes to Azure Speech voice names.
    Returns the best quality voice for each language.
    """
    code = normalize_lang(lang_code)
    # Azure Speech voice mapping - using high-quality neural voices
    voice_mapping = {
        "en": "en-US-JennyNeural",      # English (US, Female, Natural)
        "fr": "fr-FR-DeniseNeural",     # French (Female, Natural)
        "it": "it-IT-ElsaNeural",       # Italian (Female, Natural)
        "es": "es-ES-ElviraNeural",     # Spanish (Female, Natural)
        "pt": "pt-BR-FranciscaNeural",  # Portuguese (Brazilian, Female)
        "de": "de-DE-KatjaNeural",      # German (Female, Natural)
        "tw": "en-US-JennyNeural",      # Twi not supported, fallback to English
        "ja": "ja-JP-NanamiNeural",     # Japanese (Female, Natural)
        "zh": "zh-CN-XiaoxiaoNeural",   # Chinese (Mandarin, Female, Natural)
    }
    return voice_mapping.get(code, "en-US-JennyNeural")

async def synthesize_azure_speech(text: str, lang_code: str, character_name: str = None) -> bytes:
    """
    Synthesize speech from text using Azure Speech Service.
    Returns audio bytes (MP3 format).

    Args:
        text: Text to synthesize
        lang_code: Language code (en, it, fr, etc.)
        character_name: Optional character name for gendered voice selection

    Raises:
        RuntimeError: If Azure Speech is unavailable or synthesis fails
    """
    if not AZURE_SPEECH_AVAILABLE:
        raise RuntimeError("Azure Speech SDK is not available")

    if not AZURE_SPEECH_KEY or not AZURE_SPEECH_REGION:
        raise RuntimeError("Azure Speech credentials not configured. Set AZURE_SPEECH_KEY and AZURE_SPEECH_REGION")

    try:
        # Use character-aware voice selection
        voice_name = get_voice_for_character(lang_code, character_name)
        logger.info(f"[TTS] Synthesizing with Azure Speech: '{text[:50]}...' (lang: {lang_code}, char: {character_name or 'unknown'}, voice: {voice_name})")
        
        # Configure Azure Speech
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_SPEECH_KEY,
            region=AZURE_SPEECH_REGION
        )
        speech_config.speech_synthesis_voice_name = voice_name
        
        # Use WAV format (Azure returns WAV by default)
        speech_config.set_speech_synthesis_output_format(
            speechsdk.SpeechSynthesisOutputFormat.Audio16Khz128KBitRateMonoMp3
        )
        
        # Create synthesizer
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
        
        # Synthesize speech (this is synchronous, so we run it in executor)
        def synthesize_sync():
            result = synthesizer.speak_text_async(text).get()
            
            if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                return result.audio_data
            elif result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speechsdk.CancellationDetails(result)
                error_msg = f"Azure Speech synthesis canceled: {cancellation_details.reason}"
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    error_msg += f" Error details: {cancellation_details.error_details}"
                raise RuntimeError(error_msg)
            else:
                raise RuntimeError(f"Azure Speech synthesis failed: {result.reason}")
        
        # Run in executor to avoid blocking
        loop = asyncio.get_event_loop()
        audio_bytes = await loop.run_in_executor(None, synthesize_sync)
        
        if not audio_bytes or len(audio_bytes) == 0:
            raise RuntimeError("No audio was received from Azure Speech Service")
        
        logger.info(f"[TTS] Generated {len(audio_bytes)} bytes of audio via Azure Speech")
        return audio_bytes
        
    except Exception as e:
        logger.error(f"[TTS] Azure Speech synthesis error: {e}")
        raise

async def synthesize_tts(text: str, lang_code: str = "en", character_name: str = None) -> bytes:
    """
    Synthesize speech using Azure Speech Services.

    Args:
        text: Text to synthesize
        lang_code: Language code (en, it, fr, etc.)
        character_name: Optional character name for gendered voice selection

    Returns:
        Audio bytes in MP3 format

    Raises:
        RuntimeError: If Azure Speech is unavailable or synthesis fails
    """
    if not AZURE_SPEECH_AVAILABLE:
        raise RuntimeError("Azure Speech Services not available")

    if not AZURE_SPEECH_KEY or not AZURE_SPEECH_REGION:
        raise RuntimeError("Azure Speech credentials not configured")

    try:
        audio_bytes = await synthesize_azure_speech(text, lang_code, character_name)
        logger.info(f"[TTS] Azure synthesis successful ({len(audio_bytes)} bytes)")
        return audio_bytes
    except Exception as e:
        logger.error(f"[TTS] Azure synthesis failed: {str(e)}")
        raise RuntimeError(f"TTS synthesis failed: {str(e)}")

async def load_resources_bg():
    global model, tokenizer, text_generator, db_client, db, is_loading, LLAMA_STOP_TOKENS
    logger.info("🚀 Background Task: Starting resource loading...")
    try:
        db_client = AsyncIOMotorClient(MONGO_URL, serverSelectionTimeoutMS=30000)
        db = db_client[DB_NAME]
        await db_client.admin.command('ping')
        logger.info("✅ MongoDB connection successful.")
    except Exception as e: logger.error(f"❌ FATAL ERROR connecting to MongoDB: {e}")

    logger.info(f"⏳ Loading AI model ({MODEL_NAME})...")
    os.environ['TRANSFORMERS_CACHE'] = TRANSFORMERS_CACHE
    
    # Optimization flags
    USE_GPTQ = os.getenv("USE_GPTQ", "true").lower() == "true"  # Default to GPTQ for pre-quantized models
    USE_TORCH_COMPILE = os.getenv("USE_TORCH_COMPILE", "false").lower() == "true"
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32 
    
    # Check if accelerate is available for device_map
    try:
        import accelerate
        HAS_ACCELERATE = True
        logger.info("✅ accelerate library available")
    except ImportError:
        HAS_ACCELERATE = False
        logger.error("❌ accelerate library not found! It's required for model loading. Please install it: pip install accelerate")

    try:
        loop = asyncio.get_event_loop() 
        def load_hf():
            auth_kwargs = {"token": HUGGINGFACE_TOKEN} if HUGGINGFACE_TOKEN else {} 
            
            # Try GPTQ first (pre-quantized models)
            # When auto-gptq is installed, transformers' AutoModelForCausalLM can auto-detect GPTQ models
            if USE_GPTQ and torch.cuda.is_available():
                try:
                    # Check if auto-gptq is available
                    import auto_gptq
                    logger.info("📦 Loading pre-quantized GPTQ model (auto-detected)...")
                    
                    # Load tokenizer first
                    tok = AutoTokenizer.from_pretrained(MODEL_NAME, **auth_kwargs)
                    
                    # Use standard transformers API - it will auto-detect GPTQ when auto-gptq is installed
                    # This is the recommended way for pre-quantized models from TheBloke
                    model_kwargs = {
                        "trust_remote_code": False,
                        "low_cpu_mem_usage": True,
                        **auth_kwargs
                    }
                    
                    if HAS_ACCELERATE:
                        model_kwargs["device_map"] = "auto"
                    
                    # AutoModelForCausalLM will automatically use AutoGPTQForCausalLM 
                    # when it detects GPTQ format and auto-gptq is installed
                    mod = AutoModelForCausalLM.from_pretrained(
                        MODEL_NAME,
                        **model_kwargs
                    )
                    
                    # If device_map wasn't used, manually move to device
                    if not HAS_ACCELERATE:
                        mod = mod.to(device)
                    
                    logger.info("✅ Successfully loaded GPTQ quantized model (~5.5GB VRAM)")
                    
                    # Create pipeline
                    pipe = pipeline("text-generation", model=mod, tokenizer=tok)
                    return tok, mod, pipe
                    
                except ImportError as import_err:
                    logger.warning(f"⚠️ AutoGPTQ not available: {import_err}. Install auto-gptq for GPTQ support. Falling back to standard model.")
                except Exception as gptq_error:
                    logger.warning(f"⚠️ GPTQ loading failed: {gptq_error}")
                    logger.info("🔄 Falling back to standard model loading...")
            
            # Fallback: Standard model loading (for non-GPTQ models or if GPTQ fails)
            logger.info("📦 Loading standard model (non-quantized)...")
            tok = AutoTokenizer.from_pretrained(MODEL_NAME, **auth_kwargs)
            
            # Prepare model loading kwargs
            model_kwargs = {
                "dtype": dtype,  # Use dtype instead of deprecated torch_dtype
                **auth_kwargs
            }
            
            if HAS_ACCELERATE:
                model_kwargs["device_map"] = "auto"
            else:
                # Without accelerate, we need to load on CPU first, then move to device
                # This avoids the accelerate requirement that newer transformers enforces
                logger.warning("⚠️ Loading model without device_map (accelerate not available)")
                # Don't pass device parameter - load on CPU, then move manually
                mod = AutoModelForCausalLM.from_pretrained(
                    MODEL_NAME, 
                    torch_dtype=dtype,  # Use torch_dtype for older compatibility
                    **auth_kwargs
                )
                # Move to device after loading
                mod = mod.to(device)
                mod.eval()
                pipe = pipeline("text-generation", model=mod, tokenizer=tok)
                return tok, mod, pipe
            
            # With accelerate, use device_map
            mod = AutoModelForCausalLM.from_pretrained(
                MODEL_NAME, 
                **model_kwargs
            )
            
            mod.eval()
            
            # Apply torch.compile() for faster inference (PyTorch 2.0+)
            if USE_TORCH_COMPILE and hasattr(torch, 'compile'):
                try:
                    logger.info("⚡ Compiling model with torch.compile() for faster inference...")
                    mod = torch.compile(mod, mode="reduce-overhead", fullgraph=False)
                    logger.info("✅ Model compiled successfully")
                except Exception as e:
                    logger.warning(f"⚠️ torch.compile() failed: {e}. Continuing without compilation.")
            
            pipe = pipeline("text-generation", model=mod, tokenizer=tok) 
            return tok, mod, pipe
        tokenizer, model, text_generator = await loop.run_in_executor(None, load_hf)
        if "<|eot_id|>" in tokenizer.vocab:
             LLAMA_STOP_TOKENS.append(tokenizer.convert_tokens_to_ids("<|eot_id|>"))
             text_generator.tokenizer.eos_token_id = tokenizer.convert_tokens_to_ids("<|eot_id|>")
        logger.info(f"✅ Successfully loaded model '{MODEL_NAME}'.")
    except Exception as e: logger.error(f"❌ FATAL ERROR loading AI model: {e}")
    is_loading = False
    logger.info("🎉 Resource loading complete.")

@app.on_event("startup")
async def startup_event():
    logging.getLogger("uvicorn.access").addFilter(EndpointFilter())
    asyncio.create_task(load_resources_bg())

@app.get("/health")
def health_check(): return {"status": "loading" if is_loading else "healthy"}


# --- VOICE: SPEECH-TO-TEXT (WHISPER) ---

@app.post("/api/v1/voice/transcribe")
async def voice_transcribe(
    file: UploadFile = File(...),
    language: Optional[str] = None,
):
    """
    Transcribe an uploaded audio file using Whisper.
    Accepts WAV/MP3/OGG/etc via multipart/form-data.
    """
    try:
        result = await transcribe_audio_file(file, language=language)
    except Exception as e:
        logger.error(f"Whisper transcription error: {e}")
        raise HTTPException(status_code=500, detail="Transcription failed")

    text = result.get("text", "").strip()
    lang = result.get("language", language or "unknown")
    duration = result.get("duration", 0)

    return {
        "text": text,
        "language": lang,
        "duration_ms": int(duration * 1000),
        "model": WHISPER_MODEL_NAME,
    }

def levenshtein_distance(s1, s2):
    """Calculate Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def calculate_similarity(str1, str2):
    """Calculate similarity ratio between two strings using Levenshtein distance."""
    if not str1 or not str2:
        return 0.0
    
    # Normalize strings
    s1 = str1.lower().strip()
    s2 = str2.lower().strip()
    
    if s1 == s2:
        return 1.0
    
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 0.0
    
    distance = levenshtein_distance(s1, s2)
    similarity = 1.0 - (distance / max_len)
    return max(0.0, similarity)

@app.post("/voice/analyze", response_model=VoiceAnalyzeResponse)
async def voice_analyze(
    file: UploadFile = File(...),
    language: Optional[str] = Form(None),
    target_phrase: Optional[str] = Form(None),
):
    """
    Analyze audio for Echo Chamber exercise.
    Transcribes audio using Whisper and calculates confidence/phonetic scores.
    """
    # Log received parameters for debugging
    logger.info(f"[Voice Analyze] Received - language: {language}, target_phrase: {target_phrase}")
    
    # Map language codes to Whisper language codes
    whisper_lang_map = {
        "it": "it",  # Italian
        "en": "en",  # English
        "es": "es",  # Spanish
        "fr": "fr",  # French
        "pt": "pt",  # Portuguese
        "de": "de",  # German
    }
    
    # Convert language code to Whisper format
    whisper_lang = None
    if language:
        whisper_lang = whisper_lang_map.get(language.lower(), language.lower())
        logger.info(f"[Voice Analyze] Using Whisper language: {whisper_lang}")
    
    try:
        # Pass language explicitly to Whisper for better accuracy
        result = await transcribe_audio_file(file, language=whisper_lang)
    except Exception as e:
        logger.error(f"Whisper transcription error in analyze: {e}")
        raise HTTPException(status_code=500, detail="Transcription failed")

    text = result.get("text", "").strip()
    detected_lang = result.get("language", language or "unknown")
    
    # Log transcription for debugging
    logger.info(f"[Voice Analyze] Language: {whisper_lang}, Detected: {detected_lang}, Text: '{text}', Target: '{target_phrase}'")
    
    # Calculate confidence based on segments (if available)
    segments = result.get("segments", [])
    confidence = 0.0
    if segments:
        # Use average logprob if available (better confidence metric)
        logprobs = [seg.get("avg_logprob", -1.0) for seg in segments if seg.get("avg_logprob") is not None]
        if logprobs:
            # Convert logprob to confidence (higher logprob = higher confidence)
            # Logprobs are typically negative, so normalize to 0-1 range
            avg_logprob = sum(logprobs) / len(logprobs)
            # Normalize: logprob range is roughly -1 to 0, map to 0-1
            confidence = max(0.0, min(1.0, (avg_logprob + 1.0)))
        else:
            # Fallback: use no_speech_prob
            confidences = [seg.get("no_speech_prob", 0.0) for seg in segments]
            if confidences:
                confidence = 1.0 - (sum(confidences) / len(confidences))
    else:
        # Fallback: if we got text, assume some confidence
        confidence = 0.7 if text else 0.0
    
    # Calculate phonetic score if target phrase provided
    phonetic_score = 0.0
    if target_phrase and text:
        # Normalize both strings for comparison (remove punctuation, normalize spaces)
        import re
        target_clean = re.sub(r'[?.!,:;]', '', target_phrase.lower().strip())
        target_clean = re.sub(r'\s+', ' ', target_clean)
        text_clean = re.sub(r'[?.!,:;]', '', text.lower().strip())
        text_clean = re.sub(r'\s+', ' ', text_clean)
        
        # Use Levenshtein distance for better phonetic similarity
        phonetic_score = calculate_similarity(target_clean, text_clean)
        
        # Bonus: if transcription is very close (high similarity), boost score slightly
        if phonetic_score >= 0.8:
            phonetic_score = min(1.0, phonetic_score * 1.1)  # Small boost for very close matches
        
        # If detected language doesn't match expected language, penalize score less harshly
        if language and detected_lang != language.lower():
            logger.warning(f"Language mismatch: expected {language}, detected {detected_lang}")
            # Only penalize if the mismatch is significant (not just en vs it detection issue)
            if detected_lang not in ["it", "en", language.lower()]:
                phonetic_score *= 0.7  # Less harsh penalty (30% instead of 50%)
    elif text and not target_phrase:
        # If no target phrase provided but we have transcription, 
        # check if transcription matches expected pattern (for Italian phrases)
        # This is a fallback for when target_phrase isn't passed
        logger.warning("No target_phrase provided, cannot calculate phonetic score accurately")
        # Set a default low score since we can't compare
        phonetic_score = 0.0
    
    return VoiceAnalyzeResponse(
        text=text,
        confidence=round(confidence, 2),
        phonetic_score=round(phonetic_score, 2)
    )

# --- VOICE: TEXT-TO-SPEECH (Edge-TTS) ---

@app.post("/api/v1/voice/synthesize")
async def voice_synthesize(body: TTSRequest):
    """
    Synthesize speech from text using Azure Speech Services.
    Returns audio/mpeg (MP3) as a streamed response.
    """
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    if not AZURE_SPEECH_AVAILABLE:
        raise HTTPException(status_code=503, detail="Azure Speech Services not available")

    try:
        # Extract character name from dialogue text (e.g., "Marco: Ciao!" -> "Marco")
        character_name = extract_character_name(body.text)
        audio_data = await synthesize_tts(body.text, body.language, character_name)

    except Exception as e:
        logger.error(f"TTS synthesis error: {e}")
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {str(e)}")

    return StreamingResponse(
        io.BytesIO(audio_data),
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": "inline; filename=audio.mp3",
            "Content-Length": str(len(audio_data)),
        }
    )


# --- VOICE: COMBINED VOICE CHAT (STT → LLM → TTS) ---

@app.post("/api/v1/voice/chat")
async def voice_chat(
    file: UploadFile = File(...),
    target_language: str = Form(...),
    native_language: str = Form(...),
    level: str = Form("Beginner"),
    lesson_id: Optional[str] = Form(None),
    chat_history: Optional[str] = Form(None),
):
    """
    End-to-end voice chat:
    - STT via Whisper
    - Llama 3 tutor-style reply
    - TTS via Edge-TTS
    Returns audio/mpeg (MP3), with transcript and reply text in headers.
    """
    if is_loading or text_generator is None:
        raise HTTPException(status_code=503, detail="Model is still loading")

    # 1) STT
    try:
        stt_result = await transcribe_audio_file(file, language=target_language)
    except Exception as e:
        logger.error(f"Voice chat STT error: {e}")
        raise HTTPException(status_code=500, detail="Transcription failed")

    user_text = stt_result.get("text", "").strip()
    if not user_text:
        raise HTTPException(status_code=400, detail="Could not transcribe any speech")

    # 2) Parse chat history if provided
    history = []
    if chat_history:
        try:
            history = json.loads(chat_history)
        except Exception as e:
            logger.warning(f"Failed to parse chat_history: {e}")

    # 3) LLM reply (tutor-style with conversation history)
    t_lang = normalize_lang(target_language)
    n_lang = normalize_lang(native_language)
    target_lang_name = get_full_lang_name(t_lang)

    if lesson_id:
        lesson_key = lesson_id.lower() + "_comm"
    else:
        lesson_key = "a1.1_comm"
    comm_goal = get_text(lesson_key, n_lang)

    # Extract keywords for guidance (similar to /tutor endpoint)
    t_hello, _, _, _, _, _ = get_concept("concept_hello", t_lang, n_lang)
    keywords = f"{t_hello}"

    # Build conversation history for LLM
    llama_history = []
    for msg in history:
        if 'text' in msg:
            llama_history.append({"role": msg['role'], "content": msg['text']})
    llama_history.append({"role": "user", "content": user_text})
    full_history = llama_history

    loop = asyncio.get_event_loop()

    # Grammar correction system (similar to /tutor endpoint)
    correction_system_prompt = f"""
You are a highly analytical grammar checker.
Student Input: "{user_text}"
Target Language: {target_lang_name}
Native Language: {n_lang}
Task: Check the Student Input for grammar or vocabulary errors in {target_lang_name}.
If the Student Input is error-free, output: NO_ERROR.
If there are errors, output the correct sentence followed by the explanation in {n_lang}.
---
FORMAT:
CORRECTED: [Corrected Sentence in Target Lang]
EXPLANATION: [Explanation in Native Lang]
---
"""
    correction_prompt_input = generate_chat_input(correction_system_prompt, [{"role": "user", "content": user_text}])
    try:
        correction_output = await loop.run_in_executor(None, lambda: text_generator(correction_prompt_input, max_new_tokens=100, temperature=0.1, stop_sequences=["CORRECTED:", "EXPLANATION:"], return_full_text=False))
        correction_result = correction_output[0]['generated_text'].strip()
    except Exception as e:
        logger.error(f"Voice chat correction inference error: {e}")
        correction_result = "ERROR_INFERENCE"

    # Strengthened system prompt with keyword guidance and strict goal constraints
    conversation_system_prompt = f"""
You are Polybot, a friendly language tutor. The target language is {target_lang_name}.
Your role is to guide the student to achieve the communicative goal: "{comm_goal}".
Target Keywords: {keywords}
Constraint 1: You must speak ONLY in {target_lang_name}.
Constraint 2: Keep the conversation focused strictly on achieving "{comm_goal}". Do not deviate to other topics.
Constraint 3: If the student hasn't used keywords related to the goal, ask questions to guide them toward it.
Respond naturally to the student's last message while staying within these constraints.
"""
    conversation_prompt_input = generate_chat_input(conversation_system_prompt, llama_history)

    def _run_llm():
        output = text_generator(
            conversation_prompt_input,
            max_new_tokens=60,
            do_sample=True,
            top_k=50,
            temperature=0.7,
            return_full_text=False,
        )
        raw = output[0]["generated_text"].strip()
        return raw

    try:
        reply_text = await loop.run_in_executor(None, _run_llm)
    except Exception as e:
        logger.error(f"Voice chat LLM error: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate reply")

    if not reply_text:
        reply_text = "..."

    # 4) Check for goal achievement (similar to /tutor endpoint)
    status = "CONTINUE"
    assessment_system_prompt = f"""
You are an analysis bot. Your only job is to determine if the student has met the goal.
Goal: {comm_goal}
Output ONLY 'YES' or 'NO'.
"""
    assessment_prompt_input = generate_chat_input(assessment_system_prompt, full_history)
    try:
        check_output = await loop.run_in_executor(None, lambda: text_generator(assessment_prompt_input, max_new_tokens=5, temperature=0.1, return_full_text=False))
        result = check_output[0]['generated_text'].strip().upper()
        if "YES" in result:
            status = "GOAL_ACHIEVED"
    except Exception as e:
        logger.error(f"Voice chat goal assessment error: {e}")

    # 5) TTS using Azure Speech Services
    # For conversation challenges, extract character name for gendered voices
    character_name = extract_character_name(reply_text)
    try:
        audio_bytes = await synthesize_tts(reply_text, t_lang, character_name=character_name)
    except Exception as e:
        logger.error(f"Voice chat TTS error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to synthesize audio: {str(e)}")

    # Parse correction data for header
    correction_data = correction_result if "CORRECTED:" in correction_result or correction_result == "NO_ERROR" else "ERROR_FORMAT"
    
    headers = {
        "X-Polybot-Transcript": user_text.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Reply-Text": reply_text.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Status": status,
        "X-Polybot-Correction": correction_data.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Target-Lang": t_lang,
        "X-Polybot-Native-Lang": n_lang,
        "X-Polybot-Goal": comm_goal.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
    }

    return StreamingResponse(
        io.BytesIO(audio_bytes),
        media_type="audio/mpeg",
        headers=headers,
    )

# --- AUTH ENDPOINTS ---
@app.get('/api/google/login')
async def google_login(request: Request):
    google = oauth.create_client('google')
    if not google: raise HTTPException(status_code=400, detail="Google OAuth is not configured on the backend.")
    return await google.authorize_redirect(request, GOOGLE_REDIRECT_URI)

@app.get('/api/google/auth')
async def google_auth(request: Request):
    try:
        google = oauth.create_client('google')
        if not google: raise HTTPException(status_code=400, detail="Google OAuth not configured.")
        token = await google.authorize_access_token(request)
        user_info = token.get('userinfo')
        if not user_info: user_info = await google.userinfo(token=token)
        if not user_info or not user_info.get('email'): raise HTTPException(status_code=400, detail="Could not retrieve user email.")

        user_email = user_info['email']
        user_name = user_info.get('name', user_email.split('@')[0])

        logger.info(f"[OAuth] Google auth for email: {user_email}, name: {user_name}")

        if db is None: return RedirectResponse(url=f"{FRONTEND_URL}/register?error=DB_NOT_READY")

        user = await db.users.find_one({"email": user_email})
        logger.info(f"[OAuth] Database lookup result: {user is not None}")

        is_new_user = False
        if not user:
            is_new_user = True
            user_id = str(os.urandom(16).hex())
            new_profile = { "user_id": user_id, "name": user_name, "email": user_email, "native_language": "en", "target_language": "es", "level": "Beginner", "xp": 0, "words_learned": 0, "streak": 0 }
            logger.info(f"[OAuth] Creating new user with profile: {new_profile}")
            result = await db.users.insert_one(new_profile)
            logger.info(f"[OAuth] Insert result: {result.inserted_id}")
            user = new_profile
        else:
            logger.info(f"[OAuth] User exists: {user.get('user_id')}")
            if user.get('xp', 0) == 0: is_new_user = True

        logger.info(f"[OAuth] Final user data: user_id={user['user_id']}, email={user['email']}, name={user['name']}, is_new={is_new_user}")
        params = urlencode({ 'user_id': user['user_id'], 'email': user['email'], 'name': user['name'], 'new_user': 'true' if is_new_user else 'false' })
        logger.info(f"[OAuth] Redirecting to: /?{params}")
        return RedirectResponse(url=f"{FRONTEND_URL}/?{params}")

    except OAuthError as e:
        logger.error(f"Google OAuth Failed: {e}")
        return RedirectResponse(url=f"{FRONTEND_URL}/register?error=OAUTH_STATE_FAILED")
    except Exception as e:
        logger.error(f"Google OAuth UNHANDLED CRASH: {traceback.format_exc()}")
        return RedirectResponse(url=f"{FRONTEND_URL}/register?error=OAUTH_UNHANDLED_CRASH")

@app.patch("/user/{user_id}")
async def update_user(user_id: str, update: UserUpdate):
    if db is None: raise HTTPException(status_code=503, detail="DB not ready")
    update_data = {k: v for k, v in update.dict().items() if v is not None}
    if "native_language" in update_data: update_data["native_language"] = normalize_lang(update_data["native_language"])
    if "target_language" in update_data: update_data["target_language"] = normalize_lang(update_data["target_language"])
    if not update_data: return {"message": "No changes"}
    result = await db.users.update_one({"user_id": user_id}, {"$set": update_data})
    if result.matched_count == 0: raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Updated successfully", "user_id": user_id}

@app.post("/user/register", status_code=status.HTTP_201_CREATED)
async def register_user(profile: UserProfile):
    if db is None: raise HTTPException(status_code=503, detail="Database not ready")
    profile.native_language = normalize_lang(profile.native_language)
    profile.target_language = normalize_lang(profile.target_language)
    if await db.users.find_one({"$or": [{"user_id": profile.user_id}, {"email": profile.email}]}): raise HTTPException(status_code=409, detail="User exists")
    result = await db.users.insert_one(profile.dict(by_alias=True))
    return {"message": "Success", "id": str(result.inserted_id)}

@app.get("/user/profile")
async def get_profile(email: str):
    if db is None: raise HTTPException(status_code=503, detail="Database not ready")

    logger.info(f"[GetProfile] Looking up user with email: {email}")
    user = await db.users.find_one({"email": email})

    if not user:
        # Debug: log all emails in database
        all_users = await db.users.find().to_list(None)
        existing_emails = [u.get('email', 'NO_EMAIL') for u in all_users]
        logger.warning(f"[GetProfile] User not found! Email searched: '{email}'. Emails in DB: {existing_emails}")
        raise HTTPException(status_code=404, detail=f"User not found for email: {email}")

    logger.info(f"[GetProfile] Found user: {user.get('user_id')}")
    user["_id"] = str(user["_id"])
    return user

@app.post("/tutor/initiate")
async def initiate_chat(request: InitiateChatRequest):
    n_lang = normalize_lang(request.native_language)
    t_lang = normalize_lang(request.target_language)
    
    # Check if this is a boss fight FIRST - boss fights don't need AI, so bypass loading check
    # Handle both string lesson_id and potential ObjectId
    lesson_id = str(request.lesson_id) if request.lesson_id else ""
    lesson_id_lower = lesson_id.lower()
    # Check multiple patterns to catch boss fights
    is_conversation_challenge = (
        "boss" in lesson_id_lower or 
        lesson_id == "A1.1.BOSS" or 
        lesson_id == "A1.2.BOSS" or
        lesson_id == "A1.3.BOSS" or
        lesson_id == "A1.4.BOSS" or
        lesson_id == "A1.5.BOSS" or
        lesson_id == "A1.6.BOSS" or
        lesson_id == "A1.7.BOSS" or
        lesson_id == "A1.8.BOSS" or
        lesson_id == "A1.9.BOSS" or
        lesson_id == "A1.10.BOSS" or
        "A1.1.BOSS" in lesson_id or
        "A1.2.BOSS" in lesson_id or
        "A1.3.BOSS" in lesson_id or
        "A1.4.BOSS" in lesson_id or
        "A1.5.BOSS" in lesson_id or
        "A1.6.BOSS" in lesson_id or
        "A1.7.BOSS" in lesson_id or
        "A1.8.BOSS" in lesson_id or
        "A1.9.BOSS" in lesson_id or
        "A1.10.BOSS" in lesson_id or
        lesson_id.endswith(".BOSS") or
        lesson_id.endswith(".boss")
    )
    
    logger.info(f"Initiate request - lesson_id: {lesson_id} (type: {type(request.lesson_id)}), is_conversation_challenge: {is_conversation_challenge}")
    
    if is_conversation_challenge:
        # Try to get boss fight data from MongoDB or embedded data
        boss_exercise = None
        # Determine which module based on lesson_id
        lesson_id_str = str(request.lesson_id) if request.lesson_id else ""
        if "A1.10" in lesson_id_str or lesson_id_str.endswith("A1.10.BOSS") or lesson_id_str == "A1.10.BOSS":
            module_id = "A1.10"
            boss_lesson_id = "A1.10.BOSS"
        elif "A1.9" in lesson_id_str or lesson_id_str.endswith("A1.9.BOSS") or lesson_id_str == "A1.9.BOSS":
            module_id = "A1.9"
            boss_lesson_id = "A1.9.BOSS"
        elif "A1.8" in lesson_id_str or lesson_id_str.endswith("A1.8.BOSS") or lesson_id_str == "A1.8.BOSS":
            module_id = "A1.8"
            boss_lesson_id = "A1.8.BOSS"
        elif "A1.7" in lesson_id_str or lesson_id_str.endswith("A1.7.BOSS") or lesson_id_str == "A1.7.BOSS":
            module_id = "A1.7"
            boss_lesson_id = "A1.7.BOSS"
        elif "A1.6" in lesson_id_str or lesson_id_str.endswith("A1.6.BOSS") or lesson_id_str == "A1.6.BOSS":
            module_id = "A1.6"
            boss_lesson_id = "A1.6.BOSS"
        elif "A1.5" in lesson_id_str or lesson_id_str.endswith("A1.5.BOSS") or lesson_id_str == "A1.5.BOSS":
            module_id = "A1.5"
            boss_lesson_id = "A1.5.BOSS"
        elif "A1.4" in lesson_id_str or lesson_id_str.endswith("A1.4.BOSS") or lesson_id_str == "A1.4.BOSS":
            module_id = "A1.4"
            boss_lesson_id = "A1.4.BOSS"
        elif "A1.3" in lesson_id_str or lesson_id_str.endswith("A1.3.BOSS") or lesson_id_str == "A1.3.BOSS":
            module_id = "A1.3"
            boss_lesson_id = "A1.3.BOSS"
        elif "A1.2" in lesson_id_str or lesson_id_str.endswith("A1.2.BOSS") or lesson_id_str == "A1.2.BOSS":
            module_id = "A1.2"
            boss_lesson_id = "A1.2.BOSS"
        else:
            module_id = "A1.1"  # default
            boss_lesson_id = "A1.1.BOSS"  # default
        
        try:
            if db is not None:
                module = await db.modules.find_one({"module_id": module_id})
                if module:
                    boss_lesson = next((l for l in module.get("lessons", []) if l.get("lesson_id") == boss_lesson_id), None)
                    if boss_lesson:
                        boss_exercise = next((e for e in boss_lesson.get("exercises", []) if e.get("type") == "conversation_challenge"), None)
        except Exception as e:
            logger.error(f"Error getting boss fight data from MongoDB: {e}")
        
        # Fallback to embedded data
        if not boss_exercise:
            try:
                if module_id == "A1.10":
                    from a1_10_module_data import MODULE_A1_10_LESSONS
                    lessons_list = MODULE_A1_10_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.10.BOSS"), None)
                elif module_id == "A1.9":
                    from a1_9_module_data import MODULE_A1_9_LESSONS
                    lessons_list = MODULE_A1_9_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.9.BOSS"), None)
                elif module_id == "A1.8":
                    from a1_8_module_data import MODULE_A1_8_LESSONS
                    lessons_list = MODULE_A1_8_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.8.BOSS"), None)
                elif module_id == "A1.7":
                    from a1_7_module_data import MODULE_A1_7_LESSONS
                    lessons_list = MODULE_A1_7_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.7.BOSS"), None)
                elif module_id == "A1.6":
                    from a1_6_module_data import MODULE_A1_6_LESSONS
                    lessons_list = MODULE_A1_6_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.6.BOSS"), None)
                elif module_id == "A1.5":
                    from a1_5_module_data import MODULE_A1_5_LESSONS
                    lessons_list = MODULE_A1_5_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.5.BOSS"), None)
                elif module_id == "A1.4":
                    from a1_4_module_data import MODULE_A1_4_LESSONS
                    lessons_list = MODULE_A1_4_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.4.BOSS"), None)
                elif module_id == "A1.3":
                    from a1_3_module_data import MODULE_A1_3_LESSONS
                    lessons_list = MODULE_A1_3_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.3.BOSS"), None)
                elif module_id == "A1.2":
                    from a1_2_module_data import MODULE_A1_2_LESSONS
                    lessons_list = MODULE_A1_2_LESSONS.get("lessons", [])
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.2.BOSS"), None)
                else:
                    from a1_1_module_data import MODULE_A1_1_LESSONS
                    logger.info(f"Trying embedded data. MODULE_A1_1_LESSONS keys: {MODULE_A1_1_LESSONS.keys() if MODULE_A1_1_LESSONS else 'None'}")
                    lessons_list = MODULE_A1_1_LESSONS.get("lessons", [])
                    logger.info(f"Found {len(lessons_list)} lessons in embedded data")
                    for lesson in lessons_list:
                        logger.info(f"Checking lesson: lesson_id={lesson.get('lesson_id')}, type={lesson.get('type')}")
                    boss_lesson = next((l for l in lessons_list if l.get("lesson_id") == "A1.1.BOSS"), None)
                
                if boss_lesson:
                    logger.info(f"Found boss lesson: {boss_lesson.get('title')}")
                    exercises = boss_lesson.get("exercises", [])
                    logger.info(f"Found {len(exercises)} exercises in boss lesson")
                    boss_exercise = next((e for e in exercises if e.get("type") == "conversation_challenge"), None)
                    if boss_exercise:
                        logger.info(f"Found boss exercise with conversation_flow: {bool(boss_exercise.get('conversation_flow'))}")
                else:
                    logger.warning(f"Boss lesson '{boss_lesson_id}' not found in embedded data. Available lesson_ids: {[l.get('lesson_id') for l in lessons_list]}")
            except Exception as e:
                logger.error(f"Error getting embedded boss fight data: {e}", exc_info=True)
        
        # If boss fight data found, return static message
        if boss_exercise and boss_exercise.get("conversation_flow"):
            round_1 = next((r for r in boss_exercise["conversation_flow"] if r.get("round") == 1), None)
            if round_1:
                first_turn = next((t for t in round_1.get("turns", []) if t.get("turn") == 1), None)
                if first_turn and first_turn.get("ai_message"):
                    static_message = first_turn["ai_message"]
                    logger.info(f"Boss fight: Returning static message '{static_message}' from conversation_flow")
                    return {
                        "text": static_message,
                        "explanation": "Conversation started.",
                        "sender": "polybot",
                        "communicative_goal": "Complete the conversation"
                    }
                else:
                    logger.warning(f"Boss fight: First turn not found or missing ai_message. round_1: {round_1}, first_turn: {first_turn}")
            else:
                logger.warning(f"Boss fight: Round 1 not found in conversation_flow. conversation_flow: {boss_exercise.get('conversation_flow')}")
        else:
            logger.warning(f"Boss fight: boss_exercise not found or missing conversation_flow. boss_exercise: {boss_exercise}")
        
        # If we're here, boss fight data wasn't found - return default static message instead of falling through to AI
        logger.warning(f"Boss fight data not found for lesson_id: {lesson_id}, returning default static message 'Ciao!'")
        return {
            "text": "Ciao!",
            "explanation": "Conversation started.",
            "sender": "polybot",
            "communicative_goal": "Complete the conversation"
        }
    
    # Only check AI loading for non-boss-fight lessons
    if is_loading or text_generator is None: 
        return {"text": "System is warming up...", "communicative_goal": "Wait for AI"}
    
    # Fallback to regular initiation
    lesson_key = request.lesson_id.lower() + "_comm" if request.lesson_id else "a1.1_comm"
    comm_goal = get_text(lesson_key, n_lang)
    
    target_lang_name = get_full_lang_name(t_lang)
    
    system_prompt = f"""
You are Polybot, a friendly, encouraging, and highly strict language tutor speaking only {target_lang_name} (ISO Code: {t_lang}).
Your task is to start a conversation to help the student achieve the following communicative goal: "{comm_goal}".
Constraint 1: You must speak ONLY in {target_lang_name}.
Constraint 2: Your first response MUST be a friendly blended greeting and question, like 'Ciao! Come ti chiami?' or similar, translated into {target_lang_name}.
"""
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": f"Start the conversation now. Ask your first question in {target_lang_name}."}]
    final_prompt = generate_chat_input(system_prompt, messages[1:])
    loop = asyncio.get_event_loop()
    try:
        output = await loop.run_in_executor(None, lambda: text_generator(final_prompt, max_new_tokens=40, do_sample=True, top_k=50, temperature=0.8, return_full_text=False))
        raw = output[0]['generated_text'].strip()
        if not raw or len(raw) < 2: raw = f"Ciao! Come ti chiami?"
        return {"text": raw, "explanation": "Conversation started.", "sender": "polybot", "communicative_goal": comm_goal}
    except Exception as e:
        logger.error(f"Initiation error: {e}")
        return {"text": "Ciao!", "communicative_goal": comm_goal}

@app.post("/tutor")
async def tutor_mode(request: TutorRequest):
    if is_loading or text_generator is None: return {"text": "Warming up..."}
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    target_lang_name = get_full_lang_name(t_lang)
    
    t_hello, _, _, _, _, _ = get_concept("concept_hello", t_lang, n_lang)
    keywords = f"{t_hello}"
    
    llama_history = []
    for msg in request.chat_history:
        if 'text' not in msg: continue 
        llama_history.append({"role": msg['role'], "content": msg['text']})
    full_history = llama_history + [{"role": "user", "content": request.user_message}]
    loop = asyncio.get_event_loop()
    
    assessment_system_prompt = f"""
You are an analysis bot. Your only job is to determine if the student has met the goal.
Goal: The student must successfully state their name in {target_lang_name} (e.g., "Mi chiamo Jeff").
Output ONLY 'YES' or 'NO'.
"""
    assessment_prompt_input = generate_chat_input(assessment_system_prompt, full_history)
    try:
        check_output = await loop.run_in_executor(None, lambda: text_generator(assessment_prompt_input, max_new_tokens=5, temperature=0.1, return_full_text=False))
        result = check_output[0]['generated_text'].strip().upper()
        if "YES" in result: return {"text": "Fantastico! You have introduced yourself perfectly.", "status": "GOAL_ACHIEVED", "xp_reward": 50}
    except Exception as e: logger.error(f"Assessment error: {e}")

    correction_system_prompt = f"""
You are a highly analytical grammar checker.
Student Input: "{request.user_message}"
Target Language: {target_lang_name}
Native Language: {n_lang}
Task: Check the Student Input for grammar or vocabulary errors in {target_lang_name}.
If the Student Input is error-free, output: NO_ERROR.
If there are errors, output the correct sentence followed by the explanation in {n_lang}.
---
FORMAT:
CORRECTED: [Corrected Sentence in Target Lang]
EXPLANATION: [Explanation in Native Lang]
---
"""
    correction_prompt_input = generate_chat_input(correction_system_prompt, [{"role": "user", "content": request.user_message}])
    try:
        correction_output = await loop.run_in_executor(None, lambda: text_generator(correction_prompt_input, max_new_tokens=100, temperature=0.1, stop_sequences=["CORRECTED:", "EXPLANATION:"], return_full_text=False))
        correction_result = correction_output[0]['generated_text'].strip()
    except Exception as e:
        logger.error(f"Correction inference error: {e}")
        correction_result = "ERROR_INFERENCE"

    conversation_system_prompt = f"""
You are Polybot, a friendly language tutor. The target language is {target_lang_name}.
Your role is to guide the student to use the following Target Keywords: {keywords} in {target_lang_name}.
Constraint: You must speak ONLY in {target_lang_name}. If the student hasn't used a keyword, ask a question to trigger it.
"""
    conversation_prompt_input = generate_chat_input(conversation_system_prompt, full_history)
    try:
        output = await loop.run_in_executor(None, lambda: text_generator(conversation_prompt_input, max_new_tokens=60, do_sample=True, top_k=50, temperature=0.7, return_full_text=False))
        raw = output[0]['generated_text'].strip()
        return {"text": raw, "status": "CONTINUE", "correction_data": correction_result if "CORRECTED:" in correction_result or correction_result == "NO_ERROR" else "ERROR_FORMAT"}
    except Exception as e:
        logger.error(f"Conversation inference error: {e}")
        return {"text": "Error generating reply.", "status": "ERROR"}

@app.post("/boss/grammar-check", response_model=GrammarCheckResponse)
async def grammar_check(request: GrammarCheckRequest):
    """
    Check spelling, grammar, and sentence construction for boss fight responses.
    Uses AI for intelligent grammar and spelling checking.
    """
    if is_loading or text_generator is None:
        return GrammarCheckResponse(
            has_errors=False,
            feedback="Grammar check unavailable - system warming up",
            spelling_score=1.0,
            grammar_score=1.0
        )
    
    text = request.text.strip()
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    target_lang_name = get_full_lang_name(t_lang)
    
    if not text:
        return GrammarCheckResponse(
            has_errors=True,
            errors=["Empty response"],
            feedback="Please provide a response.",
            spelling_score=0.0,
            grammar_score=0.0
        )
    
    # Note: We don't check for required words here - that's handled by boss/check
    # This endpoint only checks grammar and spelling, not word requirements
    text_lower = text.lower()
    missing_words = []  # Not used for boss fight grammar check
    
    # Use AI to check grammar and spelling
    grammar_system_prompt = f"""
You are an expert language tutor checking a student's response in {target_lang_name}.
Student's response: "{text}"
Expected words/phrases that should be present: {', '.join(request.expected_words) if request.expected_words else 'None specified'}

Check for:
1. Spelling errors
2. Grammar mistakes
3. Sentence construction issues
4. Missing required words/phrases
5. Naturalness and appropriateness

Respond in {n_lang} with:
- List any errors found (or "NO_ERRORS" if perfect)
- Provide specific suggestions for improvement
- Rate spelling (0.0-1.0) and grammar (0.0-1.0)

Format:
ERRORS: [list of errors, or NO_ERRORS]
SUGGESTIONS: [list of suggestions]
SPELLING_SCORE: [0.0-1.0]
GRAMMAR_SCORE: [0.0-1.0]
"""
    
    loop = asyncio.get_event_loop()
    try:
        grammar_prompt_input = generate_chat_input(grammar_system_prompt, [])
        grammar_output = await loop.run_in_executor(
            None,
            lambda: text_generator(grammar_prompt_input, max_new_tokens=150, temperature=0.3, return_full_text=False)
        )
        ai_response = grammar_output[0]['generated_text'].strip()
        
        # Parse AI response
        errors = []
        suggestions = []
        spelling_score = 1.0
        grammar_score = 1.0
        
        # Extract errors
        if "ERRORS:" in ai_response:
            errors_section = ai_response.split("ERRORS:")[1].split("SUGGESTIONS:")[0].strip()
            if "NO_ERRORS" not in errors_section.upper():
                errors_list = [e.strip() for e in errors_section.split("\n") if e.strip()]
                errors.extend(errors_list)
        
        # Add missing words as errors
        if missing_words:
            errors.append(f"Missing required words: {', '.join(missing_words)}")
        
        # Extract suggestions
        if "SUGGESTIONS:" in ai_response:
            suggestions_section = ai_response.split("SUGGESTIONS:")[1].split("SPELLING_SCORE:")[0].strip()
            suggestions_list = [s.strip() for s in suggestions_section.split("\n") if s.strip()]
            suggestions.extend(suggestions_list)
        
        # Extract scores
        if "SPELLING_SCORE:" in ai_response:
            try:
                score_text = ai_response.split("SPELLING_SCORE:")[1].split("GRAMMAR_SCORE:")[0].strip()
                spelling_score = float(score_text.split()[0])
            except:
                pass
        
        if "GRAMMAR_SCORE:" in ai_response:
            try:
                score_text = ai_response.split("GRAMMAR_SCORE:")[1].strip()
                grammar_score = float(score_text.split()[0])
            except:
                pass
        
        # Adjust scores based on missing words
        if missing_words:
            spelling_score = max(0.0, spelling_score - (0.2 * len(missing_words)))
        
        # Generate friendly feedback
        if errors:
            feedback = f"I found {len(errors)} area(s) to improve. " + " ".join(errors[:3])  # Limit to first 3 errors
            if suggestions:
                feedback += " " + suggestions[0]  # Include first suggestion
        else:
            feedback = "Excellent! Your spelling and grammar look great. Keep up the good work!"
        
        return GrammarCheckResponse(
            has_errors=len(errors) > 0,
            errors=errors,
            suggestions=suggestions,
            feedback=feedback,
            spelling_score=max(0.0, min(1.0, spelling_score)),
            grammar_score=max(0.0, min(1.0, grammar_score))
        )
    except Exception as e:
        logger.error(f"Grammar check AI error: {e}")
        # Fallback to basic checking
        has_errors = len(missing_words) > 0
        feedback = f"Missing required words: {', '.join(missing_words)}" if missing_words else "Response looks good!"
        return GrammarCheckResponse(
            has_errors=has_errors,
            errors=[f"Missing: {w}" for w in missing_words] if missing_words else [],
            feedback=feedback,
            spelling_score=0.8 if not missing_words else 0.5,
            grammar_score=0.8 if not missing_words else 0.5
        )

@app.post("/tutor/boss")
async def tutor_boss_mode(request: TutorRequest):
    """
    Static boss fight mode - NO AI generation, just pattern matching and predefined responses.
    All AI infrastructure remains intact for future chat mode.
    """
    # Count user messages to determine current turn
    # The chat_history in the request should NOT include the current user message
    # because the frontend adds it to local state before sending
    user_message_count = len([msg for msg in request.chat_history if msg.get('role') == 'user'])
    current_turn = user_message_count + 1
    
    # Calculate round and turn within round
    # Turn 1-4 = Round 1, Turn 5-8 = Round 2
    # IMPORTANT: If chat history was cleared (e.g., transitioning to Round 2), 
    # user_message_count will be 0, making current_turn = 1, which incorrectly calculates Round 1.
    # We need to detect Round 2 by checking the first AI message in chat history.
    # Round 1 starts with "Ciao!" (informal), Round 2 starts with "Buongiorno! Come posso aiutarla?" (formal)
    current_round = ((current_turn - 1) // 4) + 1
    turn_in_round = ((current_turn - 1) % 4) + 1
    
    # Detect Round 2 by checking the first AI message
    # If chat history is short (suggesting Round 2 start) and first message is formal, we're in Round 2
    if len(request.chat_history) > 0:
        first_ai_message = None
        for msg in request.chat_history:
            if msg.get('role') in ['polybot', 'assistant']:
                first_ai_message = msg.get('text', '').lower()
                break
        
        # Round 2 starts with formal greetings
        if first_ai_message and ('buongiorno' in first_ai_message or 'come posso aiutarla' in first_ai_message):
            # We're in Round 2 - adjust the calculation
            # If we calculated Round 1 but the first message is formal, we're actually in Round 2
            if current_round == 1 and current_turn <= 4:
                current_round = 2
                # Adjust turn_in_round: if we thought we were on turn 1-4, we're actually on turn 1-4 of round 2
                # But the turn number should still be 1-4 within the round
                logger.info(f"Detected Round 2 based on formal greeting. Adjusting from Round 1 to Round 2.")
    
    logger.info(f"Boss fight turn calculation: user_message_count={user_message_count}, current_turn={current_turn}, current_round={current_round}, turn_in_round={turn_in_round}")
    
    # Validate the user's message using boss/check
    boss_check_response = None
    try:
        boss_check_request = BossCheckRequest(
            user_message=request.user_message,
            turn_number=current_turn,
            conversation_history=request.chat_history,
            lesson_id=request.lesson_id or "A1.1.BOSS",
            target_language=request.target_language,
            native_language=request.native_language
        )
        boss_check_response = await boss_check(boss_check_request)
    except Exception as e:
        logger.error(f"Boss check error: {e}")
        return {
            "text": "Scusa, puoi ripetere?",
            "status": "CONTINUE",
            "correction_data": "NO_ERROR",
            "turn_number": current_turn,
            "round_number": current_round
        }
    
    # Get boss fight conversation flow data
    boss_exercise = None
    # Determine which module based on lesson_id
    lesson_id_str = str(request.lesson_id) if request.lesson_id else ""
    if "A1.10" in lesson_id_str or lesson_id_str.endswith("A1.10.BOSS") or lesson_id_str == "A1.10.BOSS":
        module_id = "A1.10"
        boss_lesson_id = "A1.10.BOSS"
    elif "A1.9" in lesson_id_str or lesson_id_str.endswith("A1.9.BOSS") or lesson_id_str == "A1.9.BOSS":
        module_id = "A1.9"
        boss_lesson_id = "A1.9.BOSS"
    elif "A1.8" in lesson_id_str or lesson_id_str.endswith("A1.8.BOSS") or lesson_id_str == "A1.8.BOSS":
        module_id = "A1.8"
        boss_lesson_id = "A1.8.BOSS"
    elif "A1.7" in lesson_id_str or lesson_id_str.endswith("A1.7.BOSS") or lesson_id_str == "A1.7.BOSS":
        module_id = "A1.7"
        boss_lesson_id = "A1.7.BOSS"
    elif "A1.6" in lesson_id_str or lesson_id_str.endswith("A1.6.BOSS") or lesson_id_str == "A1.6.BOSS":
        module_id = "A1.6"
        boss_lesson_id = "A1.6.BOSS"
    elif "A1.5" in lesson_id_str or lesson_id_str.endswith("A1.5.BOSS") or lesson_id_str == "A1.5.BOSS":
        module_id = "A1.5"
        boss_lesson_id = "A1.5.BOSS"
    elif "A1.4" in lesson_id_str or lesson_id_str.endswith("A1.4.BOSS") or lesson_id_str == "A1.4.BOSS":
        module_id = "A1.4"
        boss_lesson_id = "A1.4.BOSS"
    elif "A1.3" in lesson_id_str or lesson_id_str.endswith("A1.3.BOSS") or lesson_id_str == "A1.3.BOSS":
        module_id = "A1.3"
        boss_lesson_id = "A1.3.BOSS"
    elif "A1.2" in lesson_id_str or lesson_id_str.endswith("A1.2.BOSS") or lesson_id_str == "A1.2.BOSS":
        module_id = "A1.2"
        boss_lesson_id = "A1.2.BOSS"
    else:
        module_id = "A1.1"  # default
        boss_lesson_id = "A1.1.BOSS"  # default
    
    try:
        if db is not None:
            module = await db.modules.find_one({"module_id": module_id})
            if module:
                boss_lesson = next((l for l in module.get("lessons", []) if l.get("lesson_id") == boss_lesson_id), None)
                if boss_lesson:
                    boss_exercise = next((e for e in boss_lesson.get("exercises", []) if e.get("type") == "conversation_challenge"), None)
    except Exception as e:
        logger.error(f"Error getting boss fight data from MongoDB: {e}")
    
    # Fallback to embedded data
    if not boss_exercise:
        try:
            if module_id == "A1.10":
                from a1_10_module_data import MODULE_A1_10_LESSONS
                boss_lesson = next((l for l in MODULE_A1_10_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.10.BOSS"), None)
            elif module_id == "A1.9":
                from a1_9_module_data import MODULE_A1_9_LESSONS
                boss_lesson = next((l for l in MODULE_A1_9_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.9.BOSS"), None)
            elif module_id == "A1.8":
                from a1_8_module_data import MODULE_A1_8_LESSONS
                boss_lesson = next((l for l in MODULE_A1_8_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.8.BOSS"), None)
            elif module_id == "A1.7":
                from a1_7_module_data import MODULE_A1_7_LESSONS
                boss_lesson = next((l for l in MODULE_A1_7_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.7.BOSS"), None)
            elif module_id == "A1.6":
                from a1_6_module_data import MODULE_A1_6_LESSONS
                boss_lesson = next((l for l in MODULE_A1_6_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.6.BOSS"), None)
            elif module_id == "A1.5":
                from a1_5_module_data import MODULE_A1_5_LESSONS
                boss_lesson = next((l for l in MODULE_A1_5_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.5.BOSS"), None)
            elif module_id == "A1.4":
                from a1_4_module_data import MODULE_A1_4_LESSONS
                boss_lesson = next((l for l in MODULE_A1_4_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.4.BOSS"), None)
            elif module_id == "A1.3":
                from a1_3_module_data import MODULE_A1_3_LESSONS
                boss_lesson = next((l for l in MODULE_A1_3_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.3.BOSS"), None)
            elif module_id == "A1.2":
                from a1_2_module_data import MODULE_A1_2_LESSONS
                boss_lesson = next((l for l in MODULE_A1_2_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.2.BOSS"), None)
            else:
                from a1_1_module_data import MODULE_A1_1_LESSONS
                boss_lesson = next((l for l in MODULE_A1_1_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.1.BOSS"), None)
            if boss_lesson:
                boss_exercise = next((e for e in boss_lesson.get("exercises", []) if e.get("type") == "conversation_challenge"), None)
        except Exception as e:
            logger.error(f"Error getting embedded boss fight data: {e}")
    
    if not boss_exercise or not boss_exercise.get("conversation_flow"):
        return {
            "text": "Scusa, c'è un problema. Riprova.",
            "status": "CONTINUE",
            "correction_data": "NO_ERROR",
            "turn_number": current_turn,
            "round_number": current_round
        }
    
    conversation_flow = boss_exercise["conversation_flow"]
    current_round_data = next((r for r in conversation_flow if r.get("round") == current_round), None)
    
    if not current_round_data:
        return {
            "text": "Scusa, c'è un problema. Riprova.",
            "status": "CONTINUE",
            "correction_data": "NO_ERROR",
            "turn_number": current_turn,
            "round_number": current_round
        }
    
    # Track if this response was valid (for end-of-round feedback)
    was_valid = boss_check_response.valid
    mistake_info = None
    if not was_valid:
        # Track the mistake for end-of-round feedback
        current_turn_data = next((t for t in current_round_data.get("turns", []) if t.get("turn") == turn_in_round), None)
        if current_turn_data:
            required_words = current_turn_data.get("required_words", [])
            used_words = boss_check_response.used_words or []
            user_requirement = current_turn_data.get("user_requirement", "")
            requires_all = " and " in user_requirement.lower() or user_requirement.lower().startswith("and ")
            
            # Calculate missing words based on whether we need all or any
            if requires_all:
                # Need all words - missing are those not used
                missing_words = [w for w in required_words if w not in used_words]
            else:
                # Need any one - missing if none were used
                missing_words = required_words if len(used_words) == 0 else []
            
            if missing_words:  # Only track if there are actually missing words
                mistake_info = {
                    "turn": turn_in_round,
                    "round": current_round,  # Include round number to distinguish Round 1 vs Round 2
                    "user_message": request.user_message,
                    "required_words": required_words,
                    "missing_words": missing_words,
                    "user_requirement": user_requirement
                }
    
    # Continue conversation regardless of validity - always advance to next turn
    # Check if round is complete
    is_last_turn_in_round = turn_in_round == 4
    is_last_round = current_round == 2
    
    if is_last_turn_in_round:
        # Round complete - return round completion flag
        next_turn = current_turn + 1
        if is_last_round:
            # Round 2 complete - show completion message, wait for user to click button to finish
            return {
                "text": "Ottimo! Hai completato la conversazione formale.",
                "status": "ROUND_COMPLETE",
                "correction_data": "NO_ERROR",
                "turn_number": next_turn,
                "round_number": 2,  # Round 2 is complete
                "round_complete": True,
                "all_rounds_complete": True,  # All rounds are done, but wait for user to complete lesson
                "had_mistake": not was_valid,
                "mistake_info": mistake_info
            }
        else:
            # Round 1 complete - don't auto-start round 2, wait for user to click button
            return {
                "text": "Ottimo! Hai completato la conversazione informale.",
                "status": "ROUND_COMPLETE",
                "correction_data": "NO_ERROR",
                "turn_number": next_turn,
                "round_number": 1,  # Still on round 1, but it's complete
                "round_complete": True,
                "all_rounds_complete": False,
                "had_mistake": not was_valid,
                "mistake_info": mistake_info,
                "next_round": 2  # Indicate next round is available
            }
    else:
        # Get next turn's AI message (same regardless of validity)
        next_turn_in_round = turn_in_round + 1
        next_turn_data = next((t for t in current_round_data.get("turns", []) if t.get("turn") == next_turn_in_round), None)
        
        if next_turn_data and next_turn_data.get("ai_message"):
            response_text = next_turn_data["ai_message"]
        else:
            response_text = "Bene! Continuiamo."
        
        return {
            "text": response_text,
            "status": "CONTINUE",
            "correction_data": "NO_ERROR",
            "turn_number": current_turn + 1,
            "round_number": current_round,
            "round_complete": False,
            "had_mistake": not was_valid,
            "mistake_info": mistake_info
        }

# --- SCENARIO-BASED PRACTICE MODE ENDPOINTS ---

@app.get("/api/practice/scenarios")
async def get_available_scenarios():
    """
    Get list of all available practice scenarios
    """
    scenarios = get_all_scenarios()
    return [
        {
            "scenario_id": s.scenario_id,
            "title": s.title,
            "description": s.description,
            "estimated_duration": s.estimated_duration,
            "difficulty": s.difficulty
        }
        for s in scenarios
    ]


@app.post("/api/practice/initiate")
async def practice_initiate(request: PracticeInitiateRequest):
    """
    Initialize a practice scenario with initial character greeting
    """
    if is_loading or text_generator is None:
        return {"text": "System is warming up...", "scene_status": "ACTIVE"}
    
    scenario = get_scenario_template(request.scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario '{request.scenario_id}' not found")
    
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    target_lang_name = get_full_lang_name(t_lang)
    
    # Try template-based greeting first (fastest)
    greeting = get_template_response(request.scenario_id, "greetings", t_lang)
    
    # If no template, use cached system prompt and generate
    if not greeting:
        # Use cached system prompt
        system_prompt = get_cached_system_prompt(request.scenario_id, t_lang, n_lang)
        if not system_prompt:
            system_prompt = build_stage_manager_prompt(scenario, t_lang, n_lang)
        
        # Generate initial greeting based on scenario
        init_message = f"Start the conversation as the character. Greet the customer in {target_lang_name} and ask what they would like to order."
        messages = [{"role": "user", "content": init_message}]
        prompt_input = generate_chat_input(system_prompt, messages)
        
        loop = asyncio.get_event_loop()
        try:
            output = await loop.run_in_executor(
                None,
                lambda: text_generator(prompt_input, max_new_tokens=30, do_sample=True, top_k=25, temperature=0.5, return_full_text=False)
            )
            greeting = output[0]['generated_text'].strip()
            if not greeting or len(greeting) < 2:
                # Fallback greeting based on scenario
                if request.scenario_id == "coffee_order":
                    greeting = "Buongiorno! Cosa desidera?" if t_lang == "it" else "Good morning! What would you like?"
        except Exception as e:
            logger.error(f"Practice initiation error: {e}")
            greeting = "Ciao!" if t_lang == "it" else "Hello!"
    
    return {
        "text": greeting,
        "scene_status": "ACTIVE",
        "scenario_id": request.scenario_id,
        "winning_condition": scenario.winning_condition,
        "user_goal_description": scenario.user_goal_description
    }


@app.post("/api/practice/text-chat")
async def practice_text_chat(request: PracticeTextChatRequest):
    """
    Text-based practice mode conversation
    Uses GameState to track conversation and Goal Check Classifier
    """
    if is_loading or text_generator is None:
        return {"reply": "System is warming up...", "scene_status": "ACTIVE", "thought": ""}
    
    scenario = get_scenario_template(request.scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario '{request.scenario_id}' not found")
    
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    target_lang_name = get_full_lang_name(t_lang)
    
    # Build conversation history for LLM
    llama_history = []
    for msg in request.conversation_history:
        if 'text' in msg or 'content' in msg:
            content = msg.get('text') or msg.get('content', '')
            role = 'user' if msg.get('role') == 'user' else 'assistant'
            llama_history.append({"role": role, "content": content})
    
    # Add current user message
    llama_history.append({"role": "user", "content": request.user_message})
    
    # Check for template-based response first (for common interactions)
    # Simple heuristics: check if user message contains order-related keywords
    user_lower = request.user_message.lower()
    # Use cached system prompt
    system_prompt = get_cached_system_prompt(request.scenario_id, t_lang, n_lang)
    if not system_prompt:
        system_prompt = build_stage_manager_prompt(scenario, t_lang, n_lang)
    
    # Generate character response using LLM
    prompt_input = generate_chat_input(system_prompt, llama_history)
    loop = asyncio.get_event_loop()
    
    try:
        output = await loop.run_in_executor(
            None,
            lambda: text_generator(prompt_input, max_new_tokens=35, do_sample=True, top_k=25, temperature=0.5, return_full_text=False)
        )
        reply_text = output[0]['generated_text'].strip()
        if not reply_text:
            reply_text = "..."
    except Exception as e:
        logger.error(f"Practice text chat LLM error: {e}")
        reply_text = "Scusa, puoi ripetere?"
    
    # Check goal achievement using Goal Check Classifier
    # Check after at least 2 messages (user + AI response) to have enough context
    # Check every message after the initial exchange to catch completion accurately
    should_check_goal = len(llama_history) >= 2
    if should_check_goal:
        goal_check_result = await check_goal_achievement(
            llama_history,
            scenario.winning_condition,
            t_lang,
            text_generator,
            generate_chat_input
        )
    else:
        # Default to ACTIVE if not checking (first message)
        goal_check_result = {"scene_status": "ACTIVE", "thought": "", "reply": ""}
    
    # If goal is complete, use the reply from goal check; otherwise use character response
    if goal_check_result["scene_status"] == "COMPLETE":
        final_reply = goal_check_result.get("reply", reply_text)
    else:
        final_reply = reply_text
    
    return {
        "reply": final_reply,
        "scene_status": goal_check_result["scene_status"],
        "thought": goal_check_result.get("thought", "")
    }


@app.post("/api/practice/voice-chat")
async def practice_voice_chat(
    file: UploadFile = File(...),
    scenario_id: str = Form(...),
    conversation_history: Optional[str] = Form(None),
    target_language: str = Form(...),
    native_language: str = Form(...),
):
    """
    Voice-based practice mode conversation
    Process: Whisper STT → GameState update → Llama 3 → Goal Check → Edge-TTS
    """
    if is_loading or text_generator is None:
        raise HTTPException(status_code=503, detail="Model is still loading")
    
    scenario = get_scenario_template(scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario '{scenario_id}' not found")
    
    # 1) STT via Whisper
    try:
        stt_result = await transcribe_audio_file(file, language=target_language)
    except Exception as e:
        logger.error(f"Practice voice chat STT error: {e}")
        raise HTTPException(status_code=500, detail="Transcription failed")
    
    user_text = stt_result.get("text", "").strip()
    user_confidence = stt_result.get("confidence", 0.0)
    
    if not user_text:
        raise HTTPException(status_code=400, detail="Could not transcribe any speech")
    
    # 2) Parse conversation history
    history = []
    if conversation_history:
        try:
            history = json.loads(conversation_history)
        except Exception as e:
            logger.warning(f"Failed to parse conversation_history: {e}")
    
    # 3) Build conversation history for LLM
    t_lang = normalize_lang(target_language)
    n_lang = normalize_lang(native_language)
    
    llama_history = []
    for msg in history:
        if 'text' in msg or 'content' in msg:
            content = msg.get('text') or msg.get('content', '')
            role = 'user' if msg.get('role') == 'user' else 'assistant'
            llama_history.append({"role": role, "content": content})
    
    llama_history.append({"role": "user", "content": user_text})
    
    # 4) Generate character response using cached Stage Manager prompt
    # Use cached system prompt
    system_prompt = get_cached_system_prompt(scenario_id, t_lang, n_lang)
    if not system_prompt:
        system_prompt = build_stage_manager_prompt(scenario, t_lang, n_lang)
    
    # Generate character response using LLM
    prompt_input = generate_chat_input(system_prompt, llama_history)
    loop = asyncio.get_event_loop()
    
    try:
        output = await loop.run_in_executor(
            None,
            lambda: text_generator(prompt_input, max_new_tokens=35, do_sample=True, top_k=25, temperature=0.5, return_full_text=False)
        )
        reply_text = output[0]['generated_text'].strip()
        if not reply_text:
            reply_text = "..."
    except Exception as e:
        logger.error(f"Practice voice chat LLM error: {e}")
        reply_text = "Scusa, puoi ripetere?"
    
    # 5) Check goal achievement
    # Check after at least 2 messages (user + AI response) to have enough context
    # Check every message after the initial exchange to catch completion accurately
    should_check_goal = len(llama_history) >= 2
    if should_check_goal:
        goal_check_result = await check_goal_achievement(
            llama_history,
            scenario.winning_condition,
            t_lang,
            text_generator,
            generate_chat_input
        )
    else:
        goal_check_result = {"scene_status": "ACTIVE", "thought": "", "reply": ""}
    
    # Use goal check reply if complete, otherwise use character response
    if goal_check_result["scene_status"] == "COMPLETE":
        final_reply = goal_check_result.get("reply", reply_text)
    else:
        final_reply = reply_text
    
    # 6) TTS using Azure Speech Services
    # Note: final_reply is from Polybot (AI system), not a curriculum character
    # Use default voice (female) for system responses
    try:
        audio_bytes = await synthesize_tts(final_reply, t_lang)
    except Exception as e:
        logger.error(f"Practice voice chat TTS error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to synthesize audio: {str(e)}")
    
    # Return audio with headers
    headers = {
        "X-Polybot-Transcript": user_text.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Reply-Text": final_reply.encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Scene-Status": goal_check_result["scene_status"],
        "X-Polybot-Thought": goal_check_result.get("thought", "").encode("utf-8", "ignore")[:4096].decode("utf-8", "ignore"),
        "X-Polybot-Confidence": str(user_confidence)
    }
    
    return StreamingResponse(
        io.BytesIO(audio_bytes),
        media_type="audio/mpeg",
        headers=headers,
    )


@app.post("/api/practice/translate")
async def practice_translate(request: dict = Body(...)):
    """
    Translate a message from target language to native language
    """
    if is_loading or text_generator is None:
        raise HTTPException(status_code=503, detail="Model is still loading")
    
    text = request.get("text", "")
    target_language = request.get("target_language", "")
    native_language = request.get("native_language", "")
    
    if not text or not target_language or not native_language:
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    t_lang = normalize_lang(target_language)
    n_lang = normalize_lang(native_language)
    target_lang_name = get_full_lang_name(t_lang)
    native_lang_name = get_full_lang_name(n_lang)
    
    # Build translation prompt
    translation_prompt = f"""Translate the following text from {target_lang_name} to {native_lang_name}. 
Provide only the translation, no additional text or explanations.

Text to translate: "{text}"

Translation:"""
    
    try:
        prompt_input = generate_chat_input(translation_prompt, [])
        loop = asyncio.get_event_loop()
        output = await loop.run_in_executor(
            None,
            lambda: text_generator(prompt_input, max_new_tokens=100, temperature=0.3, return_full_text=False)
        )
        
        translation = output[0]['generated_text'].strip()
        # Clean up any extra text that might have been generated
        translation = translation.split('\n')[0].strip()
        # Remove quotes if present
        translation = translation.strip('"').strip("'")
        
        return {"translation": translation}
    except Exception as e:
        logger.error(f"Translation error: {e}")
        raise HTTPException(status_code=500, detail="Translation failed")


@app.post("/api/practice/post-game-report")
async def practice_post_game_report(request: PostGameReportRequest):
    """
    Generate Post-Game Report with pronunciation, grammar, and vocabulary feedback
    """
    if is_loading or text_generator is None:
        raise HTTPException(status_code=503, detail="Model is still loading")
    
    scenario = get_scenario_template(request.scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario '{request.scenario_id}' not found")
    
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    
    # Generate pronunciation feedback
    pronunciation_feedback = generate_pronunciation_feedback(request.user_transcripts)
    
    # Generate grammar and vocabulary review
    grammar_vocab_review = await generate_grammar_vocabulary_review(
        request.conversation_transcript,
        t_lang,
        n_lang,
        text_generator,
        generate_chat_input
    )
    
    return {
        "pronunciation": pronunciation_feedback,
        "grammar": {
            "errors": grammar_vocab_review.get("grammar_errors", []),
            "overall_feedback": grammar_vocab_review.get("overall_feedback", "")
        },
        "vocabulary": {
            "suggestions": grammar_vocab_review.get("vocabulary_suggestions", []),
            "overall_feedback": grammar_vocab_review.get("overall_feedback", "")
        }
    }

# --- DYNAMIC CURRICULUM GENERATOR (Updated with Grouping & Conversations) ---
@app.get("/lessons", response_model=List[Lesson])
async def get_lessons(target_lang: str = "en", native_lang: str = "es"):
    t_lang = normalize_lang(target_lang)
    n_lang = normalize_lang(native_lang)
    
    lesson_list = []
    
    # Check MongoDB first for A1.1 module structure
    if db is not None:
        try:
            a1_1_module = await db.modules.find_one({"module_id": "A1.1"})
            if a1_1_module:
                # Return A1.1 as a special module structure (will be handled by frontend)
                # For now, skip A1.1 in the dynamic generation
                pass  # We'll handle A1.1 separately below
        except Exception as e:
            logger.error(f"Error checking MongoDB for A1.1: {e}")
    
    for lesson_id, concepts in LESSON_CONCEPTS.items():
        # Skip A1.1 if it exists in MongoDB (will be returned via /modules endpoint)
        if lesson_id == "A1.1" and db is not None:
            try:
                a1_1_module = await db.modules.find_one({"module_id": "A1.1"})
                if a1_1_module:
                    continue  # Skip dynamic generation, use MongoDB version
            except Exception:
                pass  # Continue with dynamic generation if check fails
        module_exercises = []
        module_vocab = []

        # Special handling for A1.6 (Numbers 6-10 & Time)
        if lesson_id == "A1.6":
            # Group: Time
            module_exercises.append({ "type": "info_card", "prompt": "Topic", "correct_answer": "Time", "explanation": "Asking the time", "sub_text": "" })
            module_vocab.append({"term": "--- Time ---", "translation": "", "target_lang": t_lang, "is_header": True})
            
            for c in ["concept_time", "concept_now"]:
                module_exercises.extend(generate_concept_flow(c, t_lang, n_lang))
                t, n, _, _, _, _ = get_concept(c, t_lang, n_lang)
                module_vocab.append({"term": t, "translation": n, "target_lang": t_lang})

            # Group: Numbers 6-10
            module_exercises.append({ "type": "info_card", "prompt": "Topic", "correct_answer": "Numbers 6-10", "explanation": "Counting higher", "sub_text": "" })
            module_vocab.append({"term": "--- Numbers 6-10 ---", "translation": "", "target_lang": t_lang, "is_header": True})
            
            for c in ["concept_six", "concept_seven", "concept_eight", "concept_nine", "concept_ten"]:
                module_exercises.extend(generate_concept_flow(c, t_lang, n_lang))
                t, n, _, _, _, _ = get_concept(c, t_lang, n_lang)
                module_vocab.append({"term": t, "translation": n, "target_lang": t_lang})

        else:
            # Standard flow
            for c in concepts:
                module_exercises.extend(generate_concept_flow(c, t_lang, n_lang))
                t, n, _, _, _, _ = get_concept(c, t_lang, n_lang)
                module_vocab.append({"term": t, "translation": n, "target_lang": t_lang})
        
        # NEW: Add Conversation Exercise (if available)
        convo_ex = generate_conversation_exercise(lesson_id, t_lang, n_lang)
        if convo_ex:
            module_exercises.append(convo_ex)

        if module_vocab:
            # Only include real words in matching game, not headers
            real_vocab = [v for v in module_vocab if not v.get("is_header")]
            pairs = [[v["term"], v["translation"]] for v in real_vocab]
            final_review = { 
                "type": "match", 
                "prompt": "Review", 
                "pairs": pairs, 
                "correct_answer": "match_all", 
                "explanation": "Module Complete!" 
            }
            module_exercises.append(final_review)

        title_key = f"{lesson_id.lower()}_title"
        goal_key = f"{lesson_id.lower()}_goal"
        comm_key = f"{lesson_id.lower()}_comm"
        
        lesson_obj = {
            "_id": lesson_id,
            "title": get_text(title_key, n_lang),
            "goal": get_text(goal_key, n_lang),
            "communicative_goal": get_text(comm_key, n_lang),
            "topics": [get_text(title_key, n_lang)], 
            "ai_prompt_context": f"Focus on {get_text(title_key, n_lang)}",
            "vocabulary": module_vocab,
            "exercises": module_exercises
        }
        lesson_list.append(lesson_obj)
        
    return lesson_list

@app.get("/modules")
async def get_modules(target_lang: str = "en", native_lang: str = "es"):
    """
    Fetch structured modules from MongoDB (e.g., Module A1.1 with nested lessons).
    Falls back to generating A1.1 from embedded data if MongoDB doesn't have it.
    Currently, A1.1 is only available for Italian (target_lang='it').
    """
    modules = []
    
    # Only return A1.1 module if target language is Italian
    if target_lang.lower() != 'it':
        return modules  # Return empty list for non-Italian languages
    
    # Try to fetch from MongoDB first
    if db is not None:
        try:
            async for module_doc in db.modules.find({}):
                # Convert MongoDB document to dict
                module_dict = {
                    "_id": module_doc.get("module_id"),
                    "title": module_doc.get("title"),
                    "goal": module_doc.get("goal"),
                    "lessons": module_doc.get("lessons", []),
                    "type": "module"
                }
                modules.append(module_dict)
        except Exception as e:
            logger.error(f"Error fetching modules from MongoDB: {e}")
    
    # If no modules in MongoDB, generate A1.1 and A1.2 from embedded data
    if not modules:
        try:
            from a1_1_module_data import MODULE_A1_1_LESSONS
            module_dict = {
                "_id": MODULE_A1_1_LESSONS.get("module_id"),
                "title": MODULE_A1_1_LESSONS.get("title"),
                "goal": MODULE_A1_1_LESSONS.get("goal"),
                "lessons": MODULE_A1_1_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.1 module data")
        
        try:
            from a1_2_module_data import MODULE_A1_2_LESSONS
            module_dict = {
                "_id": MODULE_A1_2_LESSONS.get("module_id"),
                "title": MODULE_A1_2_LESSONS.get("title"),
                "goal": MODULE_A1_2_LESSONS.get("goal"),
                "lessons": MODULE_A1_2_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.2 module data")
        
        try:
            from a1_3_module_data import MODULE_A1_3_LESSONS
            module_dict = {
                "_id": MODULE_A1_3_LESSONS.get("module_id"),
                "title": MODULE_A1_3_LESSONS.get("title"),
                "goal": MODULE_A1_3_LESSONS.get("goal"),
                "lessons": MODULE_A1_3_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.3 module data")
        
        try:
            from a1_4_module_data import MODULE_A1_4_LESSONS
            module_dict = {
                "_id": MODULE_A1_4_LESSONS.get("module_id"),
                "title": MODULE_A1_4_LESSONS.get("title"),
                "goal": MODULE_A1_4_LESSONS.get("goal"),
                "lessons": MODULE_A1_4_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.4 module data")
        
        try:
            from a1_5_module_data import MODULE_A1_5_LESSONS
            module_dict = {
                "_id": MODULE_A1_5_LESSONS.get("module_id"),
                "title": MODULE_A1_5_LESSONS.get("title"),
                "goal": MODULE_A1_5_LESSONS.get("goal"),
                "lessons": MODULE_A1_5_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.5 module data")
        
        try:
            from a1_6_module_data import MODULE_A1_6_LESSONS
            module_dict = {
                "_id": MODULE_A1_6_LESSONS.get("module_id"),
                "title": MODULE_A1_6_LESSONS.get("title"),
                "goal": MODULE_A1_6_LESSONS.get("goal"),
                "lessons": MODULE_A1_6_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.6 module data")
        
        try:
            from a1_7_module_data import MODULE_A1_7_LESSONS
            module_dict = {
                "_id": MODULE_A1_7_LESSONS.get("module_id"),
                "title": MODULE_A1_7_LESSONS.get("title"),
                "goal": MODULE_A1_7_LESSONS.get("goal"),
                "lessons": MODULE_A1_7_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.7 module data")
        
        try:
            from a1_8_module_data import MODULE_A1_8_LESSONS
            module_dict = {
                "_id": MODULE_A1_8_LESSONS.get("module_id"),
                "title": MODULE_A1_8_LESSONS.get("title"),
                "goal": MODULE_A1_8_LESSONS.get("goal"),
                "lessons": MODULE_A1_8_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.8 module data")
        
        try:
            from a1_9_module_data import MODULE_A1_9_LESSONS
            module_dict = {
                "_id": MODULE_A1_9_LESSONS.get("module_id"),
                "title": MODULE_A1_9_LESSONS.get("title"),
                "goal": MODULE_A1_9_LESSONS.get("goal"),
                "lessons": MODULE_A1_9_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.9 module data")
        
        try:
            from a1_10_module_data import MODULE_A1_10_LESSONS
            module_dict = {
                "_id": MODULE_A1_10_LESSONS.get("module_id"),
                "title": MODULE_A1_10_LESSONS.get("title"),
                "goal": MODULE_A1_10_LESSONS.get("goal"),
                "lessons": MODULE_A1_10_LESSONS.get("lessons", []),
                "type": "module"
            }
            modules.append(module_dict)
        except ImportError:
            logger.warning("Could not import A1.10 module data")
        
    
    # If still no modules, fallback to dynamic lessons
    if not modules:
        dynamic_lessons = await get_lessons(target_lang, native_lang)
        return dynamic_lessons
    
    return modules

@app.post("/admin/seed-a1-1")
async def seed_a1_1_module():
    """
    Admin endpoint to seed Module A1.1 into MongoDB.
    This populates the new structured format for A1.1 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_1_module_data import MODULE_A1_1_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.1"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.1"},
                {"$set": {**MODULE_A1_1_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_1_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.1: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/admin/seed-a1-2")
async def seed_a1_2_module():
    """
    Admin endpoint to seed Module A1.2 into MongoDB.
    This populates the new structured format for A1.2 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_2_module_data import MODULE_A1_2_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.2"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.2"},
                {"$set": {**MODULE_A1_2_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_2_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.2: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/admin/seed-a1-3")
async def seed_a1_3_module():
    """
    Admin endpoint to seed Module A1.3 into MongoDB.
    This populates the new structured format for A1.3 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_3_module_data import MODULE_A1_3_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.3"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.3"},
                {"$set": {**MODULE_A1_3_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_3_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.3: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/admin/seed-a1-4")
async def seed_a1_4_module():
    """
    Admin endpoint to seed Module A1.4 into MongoDB.
    This populates the new structured format for A1.4 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_4_module_data import MODULE_A1_4_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.4"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.4"},
                {"$set": {**MODULE_A1_4_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_4_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.4: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/admin/seed-a1-5")
async def seed_a1_5_module():
    """
    Admin endpoint to seed Module A1.5 into MongoDB.
    This populates the new structured format for A1.5 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_5_module_data import MODULE_A1_5_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.5"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.5"},
                {"$set": {**MODULE_A1_5_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_5_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.5: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/admin/seed-a1-6")
async def seed_a1_6_module():
    """
    Admin endpoint to seed Module A1.6 into MongoDB.
    This populates the new structured format for A1.6 with nested lessons.
    """
    if db is None:
        raise HTTPException(status_code=503, detail="Database not connected")
    
    try:
        from a1_6_module_data import MODULE_A1_6_LESSONS
        from datetime import datetime
        
        # Insert or update module
        collection = db.modules
        existing = await collection.find_one({"module_id": "A1.6"})
        
        if existing:
            result = await collection.update_one(
                {"module_id": "A1.6"},
                {"$set": {**MODULE_A1_6_LESSONS, "updated_at": datetime.utcnow()}}
            )
            return {"status": "updated", "matched": result.matched_count, "modified": result.modified_count}
        else:
            result = await collection.insert_one({
                **MODULE_A1_6_LESSONS,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            })
            return {"status": "inserted", "id": str(result.inserted_id)}
    except Exception as e:
        logger.error(f"Error seeding A1.6: {e}")
        raise HTTPException(status_code=500, detail=f"Seeding failed: {str(e)}")

@app.post("/user/complete_lesson")
async def complete_lesson(req: LessonCompletionRequest):
    if db is None: raise HTTPException(status_code=503, detail="DB not ready")
    user = await db.users.find_one({"user_id": req.user_id})
    if not user: raise HTTPException(status_code=404, detail="User not found")
    
    proficiency = (req.score / req.total_questions) * 100 if req.total_questions > 0 else 0
    t_lang = user.get("target_language", "en")
    n_lang = user.get("native_language", "es")
    
    # Check if this is a nested lesson (e.g., A1.1.1) or a module-level lesson (e.g., A1.1)
    lesson_id = req.lesson_id
    module_id = None
    
    # Extract module_id from lesson_id (e.g., A1.1.1 -> A1.1, A1.1.BOSS -> A1.1)
    if "." in lesson_id:
        parts = lesson_id.split(".")
        if len(parts) >= 2:
            module_id = ".".join(parts[:2])  # A1.1
    else:
        module_id = lesson_id
    
    # Get vocabulary from lesson concepts if it's a module-level lesson
    concepts = LESSON_CONCEPTS.get(module_id, [])
    
    # For nested lessons, try to get vocabulary from MongoDB
    if db is not None and "." in lesson_id:
        try:
            # Check if this is a nested lesson in a module
            module_doc = await db.modules.find_one({"module_id": module_id})
            if module_doc:
                lesson_doc = next((l for l in module_doc.get("lessons", []) if l.get("lesson_id") == lesson_id), None)
                if lesson_doc and lesson_doc.get("vocabulary"):
                    # Use vocabulary from the lesson document
                    concepts = lesson_doc.get("vocabulary", [])
        except Exception as e:
            logger.error(f"Error fetching lesson vocabulary: {e}")
    
    new_vocab = []
    for c in concepts:
        if isinstance(c, str):
            # It's a concept key, get the concept
            t_term, n_term, _, _, _, _ = get_concept(c, t_lang, n_lang)
            new_vocab.append({"term": t_term, "translation": n_term, "target_lang": t_lang, "proficiency": proficiency})
        elif isinstance(c, dict) and "term" in c:
            # It's already a vocabulary item
            new_vocab.append({**c, "target_lang": t_lang, "proficiency": proficiency})

    current_vocab = user.get("vocabulary_list", [])
    vocab_map = {(v['term'], v.get('target_lang', 'unknown')): v for v in current_vocab}
    
    for word in new_vocab:
        key = (word['term'], word['target_lang'])
        if key in vocab_map:
             vocab_map[key]['proficiency'] = max(vocab_map[key].get('proficiency', 0), word['proficiency'])
        else:
             vocab_map[key] = word
             
    updated_vocab_list = list(vocab_map.values())
    
    current_progress = user.get("progress", [])
    found_progress = False
    for p in current_progress:
        # Match by lesson_id OR module_id for nested lessons
        if (p.get("lesson_id") == lesson_id or p.get("module_id") == lesson_id or 
            (p.get("module_id") == module_id and p.get("lesson_id") == lesson_id)):
            if p.get("target_lang") == t_lang:
                p["mastery_score"] = max(p["mastery_score"], proficiency)
                p["last_practiced"] = time.time()
                found_progress = True
                break
    
    if not found_progress:
        new_p = {
            "lesson_id": lesson_id,  # Store the specific lesson_id
            "module_id": module_id,   # Also store the module_id
            "target_lang": t_lang,
            "mastery_score": proficiency,
            "last_practiced": time.time(),
            "xp_earned": req.score * 10
        }
        current_progress.append(new_p)

    new_xp = user.get("xp", 0) + (req.score * 10)
    
    await db.users.update_one(
        {"user_id": req.user_id},
        {
            "$set": {
                "vocabulary_list": updated_vocab_list, 
                "xp": new_xp, 
                "words_learned": len(updated_vocab_list),
                "progress": current_progress
            }
        }
    )
    return {"status": "success", "new_xp": new_xp, "words_learned": len(updated_vocab_list), "vocabulary_list": updated_vocab_list, "progress": current_progress}

# --- BOSS FIGHT VALIDATION ---

@app.post("/boss/check", response_model=BossCheckResponse)
async def boss_check(request: BossCheckRequest):
    """
    Validates boss fight conversation turns for both rounds.
    NO AI - uses pattern matching only.
    """
    user_msg = request.user_message.strip()
    turn = request.turn_number
    t_lang = normalize_lang(request.target_language)
    n_lang = normalize_lang(request.native_language)
    used_words = []
    
    # Calculate round and turn within round
    current_round = ((turn - 1) // 4) + 1
    turn_in_round = ((turn - 1) % 4) + 1
    
    # IMPORTANT: Detect Round 2 by checking conversation history
    # If chat history was cleared (e.g., transitioning to Round 2), 
    # turn will be 1-4, which incorrectly calculates Round 1.
    # We need to detect Round 2 by checking the first AI message in conversation history.
    if len(request.conversation_history) > 0:
        first_ai_message = None
        for msg in request.conversation_history:
            if msg.get('role') in ['polybot', 'assistant']:
                first_ai_message = msg.get('text', '').lower()
                break
        
        # Round 2 starts with formal greetings
        if first_ai_message and ('buongiorno' in first_ai_message or 'come posso aiutarla' in first_ai_message):
            # We're in Round 2 - adjust the calculation
            # If we calculated Round 1 but the first message is formal, we're actually in Round 2
            if current_round == 1 and turn <= 4:
                current_round = 2
                logger.info(f"[boss/check] Detected Round 2 based on formal greeting. Adjusting from Round 1 to Round 2. turn={turn}, turn_in_round={turn_in_round}")
    
    logger.info(f"[boss/check] Round calculation: turn={turn}, current_round={current_round}, turn_in_round={turn_in_round}")
    
    # Get boss fight data
    boss_exercise = None
    # Determine which module based on lesson_id
    lesson_id_str = str(request.lesson_id) if request.lesson_id else ""
    if "A1.6" in lesson_id_str or lesson_id_str.endswith("A1.6.BOSS") or lesson_id_str == "A1.6.BOSS":
        module_id = "A1.6"
        boss_lesson_id = "A1.6.BOSS"
    elif "A1.5" in lesson_id_str or lesson_id_str.endswith("A1.5.BOSS") or lesson_id_str == "A1.5.BOSS":
        module_id = "A1.5"
        boss_lesson_id = "A1.5.BOSS"
    elif "A1.4" in lesson_id_str or lesson_id_str.endswith("A1.4.BOSS") or lesson_id_str == "A1.4.BOSS":
        module_id = "A1.4"
        boss_lesson_id = "A1.4.BOSS"
    elif "A1.3" in lesson_id_str or lesson_id_str.endswith("A1.3.BOSS") or lesson_id_str == "A1.3.BOSS":
        module_id = "A1.3"
        boss_lesson_id = "A1.3.BOSS"
    elif "A1.2" in lesson_id_str or lesson_id_str.endswith("A1.2.BOSS") or lesson_id_str == "A1.2.BOSS":
        module_id = "A1.2"
        boss_lesson_id = "A1.2.BOSS"
    else:
        module_id = "A1.1"  # default
        boss_lesson_id = "A1.1.BOSS"  # default
    
    try:
        if db is not None:
            module = await db.modules.find_one({"module_id": module_id})
            if module:
                boss_lesson = next((l for l in module.get("lessons", []) if l.get("lesson_id") == boss_lesson_id), None)
                if boss_lesson:
                    boss_exercise = next((e for e in boss_lesson.get("exercises", []) if e.get("type") == "conversation_challenge"), None)
    except Exception as e:
        logger.error(f"Error getting boss fight data: {e}")
    
    # Fallback to embedded data
    if not boss_exercise:
        try:
            if module_id == "A1.5":
                from a1_5_module_data import MODULE_A1_5_LESSONS
                boss_lesson = next((l for l in MODULE_A1_5_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.5.BOSS"), None)
            elif module_id == "A1.4":
                from a1_4_module_data import MODULE_A1_4_LESSONS
                boss_lesson = next((l for l in MODULE_A1_4_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.4.BOSS"), None)
            elif module_id == "A1.3":
                from a1_3_module_data import MODULE_A1_3_LESSONS
                boss_lesson = next((l for l in MODULE_A1_3_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.3.BOSS"), None)
            elif module_id == "A1.2":
                from a1_2_module_data import MODULE_A1_2_LESSONS
                boss_lesson = next((l for l in MODULE_A1_2_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.2.BOSS"), None)
            else:
                from a1_1_module_data import MODULE_A1_1_LESSONS
                boss_lesson = next((l for l in MODULE_A1_1_LESSONS.get("lessons", []) if l.get("lesson_id") == "A1.1.BOSS"), None)
            if boss_lesson:
                boss_exercise = next((e for e in boss_lesson.get("exercises", []) if e.get("type") == "conversation_challenge"), None)
        except Exception as e:
            logger.error(f"Error getting embedded boss fight data: {e}")
    
    if not boss_exercise or not boss_exercise.get("conversation_flow"):
        return BossCheckResponse(
            valid=False,
            feedback="Boss fight data not found",
            next_turn=turn,
            completed=False,
            used_words=[]
        )
    
    conversation_flow = boss_exercise["conversation_flow"]
    current_round_data = next((r for r in conversation_flow if r.get("round") == current_round), None)
    
    if not current_round_data:
        return BossCheckResponse(
            valid=False,
            feedback="Round data not found",
            next_turn=turn,
            completed=False,
            used_words=[]
        )
    
    current_turn_data = next((t for t in current_round_data.get("turns", []) if t.get("turn") == turn_in_round), None)
    
    if not current_turn_data:
        return BossCheckResponse(
            valid=False,
            feedback="Turn data not found",
            next_turn=turn,
            completed=False,
            used_words=[]
        )
    
    # Validate based on required words
    user_lower = user_msg.lower().strip()
    required_words = current_turn_data.get("required_words", [])
    user_requirement = current_turn_data.get("user_requirement", "").lower()
    
    import re
    # Determine if we need ALL words (AND) or ANY word (OR)
    # If user_requirement contains "AND", require all words
    # Otherwise, accept any one word
    requires_all = " and " in user_requirement or user_requirement.startswith("and ")
    
    logger.info(f"Validating: user_msg='{user_msg}', user_lower='{user_lower}', required_words={required_words}, requires_all={requires_all}")
    
    for word in required_words:
        word_lower = word.lower()
        matched = False
        
        # Handle multi-word phrases
        if " " in word_lower:
            # For phrases like "Sto bene" or "E Lei?", check case-insensitively
            # The user might type "e Lei?" (lowercase e, capital L) which should match "E Lei?"
            # Convert both to lowercase for comparison
            # First try simple substring match (handles "Sto bene" in "Sto bene, e Lei?")
            if word_lower in user_lower:
                used_words.append(word)
                matched = True
            else:
                # For phrases with punctuation like "E Lei?", try removing punctuation
                # Remove punctuation from both for flexible matching
                word_clean = re.sub(r'[^\w\s]', '', word_lower)
                user_clean = re.sub(r'[^\w\s]', '', user_lower)
                # Check if the clean phrase appears in the clean user message
                if word_clean in user_clean:
                    used_words.append(word)
                    matched = True
                else:
                    # Also try matching word by word - for "e lei?" check if both "e" and "lei" appear
                    word_parts = word_clean.split()
                    if len(word_parts) >= 2:
                        # Check if all parts appear in order (allowing for other words in between)
                        all_parts_found = all(part in user_clean for part in word_parts)
                        if all_parts_found:
                            # Verify they appear in the correct order
                            last_index = -1
                            in_order = True
                            for part in word_parts:
                                index = user_clean.find(part, last_index + 1)
                                if index == -1:
                                    in_order = False
                                    break
                                last_index = index
                            if in_order:
                                used_words.append(word)
                                matched = True
        
        if not matched:
            # Single word - check with word boundaries (case-insensitive)
            # Escape special regex characters in the word
            word_pattern = re.escape(word_lower)
            if re.search(rf'\b{word_pattern}\b', user_lower, re.IGNORECASE):
                used_words.append(word)
                matched = True
        
        # Log for debugging
        if matched:
            logger.info(f"✓ Matched word '{word}' (lowercase: '{word_lower}') in user message")
        else:
            logger.warning(f"✗ Word '{word}' (lowercase: '{word_lower}') NOT matched in user message '{user_msg}' (lowercase: '{user_lower}')")
            logger.warning(f"  Simple substring check: '{word_lower}' in '{user_lower}' = {word_lower in user_lower}")
    
    # Check if requirement is met
    if requires_all:
        # Need ALL words
        all_required_found = len(used_words) == len(required_words)
        logger.info(f"Requires ALL: found {len(used_words)}/{len(required_words)} words. Used: {used_words}")
    else:
        # Need AT LEAST ONE word
        all_required_found = len(used_words) > 0
        logger.info(f"Requires ANY: found {len(used_words)} words. Used: {used_words}")
    
    if all_required_found:
        # Check if this is the last turn of the last round
        is_last_turn_in_round = turn_in_round == 4
        is_last_round = current_round == 2
        
        if is_last_turn_in_round and is_last_round:
            completed = True
            next_turn = turn + 1
        elif is_last_turn_in_round:
            # End of round 1, move to round 2
            completed = False
            next_turn = turn + 1
        else:
            completed = False
            next_turn = turn + 1
        
        return BossCheckResponse(
            valid=True,
            feedback="Perfect!",
            next_turn=next_turn,
            completed=completed,
            used_words=used_words
        )
    else:
        missing = [w for w in required_words if w not in used_words]
        return BossCheckResponse(
            valid=False,
            feedback=f"Please use: {', '.join(missing)}",
            next_turn=turn,
            completed=False,
            used_words=used_words
        )