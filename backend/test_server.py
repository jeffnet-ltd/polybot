import pytest
from httpx import AsyncClient, ASGITransport
from server import app, LESSON_CONCEPTS, CONTENT_DB
from unittest.mock import patch, MagicMock, AsyncMock

# --- FIXTURES ---

@pytest.fixture
def mock_mongo():
    """
    Mocks the MongoDB driver with AsyncMock for awaitable methods.
    Defaults to 'No User Found' (return_value=None) for clean registration testing.
    Tests that require a user can override this behavior.
    """
    with patch("server.db") as mock_db:
        # Default behavior: No user exists (good for registration)
        mock_db.users.find_one = AsyncMock(return_value=None)
        mock_db.users.insert_one = AsyncMock(return_value=MagicMock(inserted_id="test_id_123"))
        mock_db.users.update_one = AsyncMock(return_value=MagicMock(matched_count=1))
        yield mock_db

@pytest.fixture
def mock_ai():
    """
    Mocks the Llama 3 pipeline and tokenizer.
    Captures input prompts so we can verify logic without running the GPU.
    """
    with patch("server.text_generator") as mock_gen, \
         patch("server.tokenizer") as mock_tok: 
        
        # 1. Mock the AI output so the server doesn't crash
        mock_gen.return_value = [{"generated_text": "Ciao! Come ti chiami?"}]
        
        # 2. Mock the tokenizer to return the raw input prompt
        # (This allows us to inspect what was sent to the AI in our tests)
        mock_tok.apply_chat_template.side_effect = lambda msgs, **kwargs: str(msgs)
        mock_tok.convert_tokens_to_ids.return_value = 128001
        
        yield mock_gen

# --- BASIC SERVER TESTS ---

@pytest.mark.asyncio
async def test_health_check():
    """Verify the health endpoint returns 200."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_lessons_structure():
    """Verify the curriculum generator returns the correct structure."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/lessons?target_lang=it&native_lang=en")
    
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) > 0
    lesson_1 = next((l for l in data if l["_id"] == "A1.1"), None)
    assert lesson_1 is not None
    
    # Verify title matches CONTENT_DB
    assert lesson_1["title"] == "Greetings" 
    assert len(lesson_1["vocabulary"]) > 0
    # Check for new fields
    assert "target_lang" in lesson_1["vocabulary"][0]

@pytest.mark.asyncio
async def test_user_registration(mock_mongo):
    """Verify user registration logic (Requires find_one to return None)."""
    # Ensure mock is set to 'User Not Found'
    mock_mongo.users.find_one.return_value = None
    
    payload = {
        "user_id": "test_user_1",
        "name": "Test User",
        "email": "test@example.com",
        "native_language": "en",
        "target_language": "es",
        "level": "Beginner"
    }
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/user/register", json=payload)
    
    assert response.status_code == 201
    assert response.json()["message"] == "Success"

# --- ADVANCED LOGIC TESTS ---

@pytest.mark.asyncio
async def test_complete_lesson_logic(mock_mongo):
    """Verify that completing a lesson awards XP and saves Vocabulary."""
    
    # SETUP: Mock an existing user
    mock_user = {
        "user_id": "test_user_1",
        "xp": 0,
        "words_learned": 0,
        "vocabulary_list": [],
        "progress": []
    }
    mock_mongo.users.find_one.return_value = mock_user
    
    payload = {
        "user_id": "test_user_1",
        "lesson_id": "A1.1",
        "score": 10,
        "total_questions": 10
    }
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/user/complete_lesson", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # 1. Check XP Calculation
    assert data["new_xp"] == 100
    # 2. Check Vocabulary was generated
    assert len(data["vocabulary_list"]) > 0
    # 3. Check Integrity
    first_word = data["vocabulary_list"][0]
    assert "target_lang" in first_word

@pytest.mark.asyncio
async def test_multilingual_integrity():
    """Loop through ALL languages to ensure CONTENT_DB is valid for every target."""
    
    test_langs = ["es", "fr", "it", "pt", "de", "ru", "ja", "zh", "tw"]
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        for lang in test_langs:
            response = await ac.get(f"/lessons?target_lang={lang}&native_lang=en")
            assert response.status_code == 200, f"Failed to load lessons for {lang}"
            
            data = response.json()
            assert len(data) >= 10, f"Language {lang} is missing modules!"
            
            assert len(numbers_lesson["exercises"]) > 5, f"Exercises missing in {lang}"

@pytest.mark.asyncio
async def test_update_user_preferences(mock_mongo):
    """Verify we can switch languages."""
    mock_user = {"user_id": "test_user_1", "target_language": "es"}
    mock_mongo.users.find_one.return_value = mock_user
    
    payload = {"target_language": "fr"}
    
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.patch("/user/test_user_1", json=payload)
        
    assert response.status_code == 200
    assert response.json()["message"] == "Updated successfully"

# --- AI ROBUSTNESS TESTS (BOSS FIGHT LOGIC) ---

@pytest.mark.asyncio
@pytest.mark.parametrize("lesson_id", list(LESSON_CONCEPTS.keys()))
async def test_lesson_goal_is_applied(lesson_id, mock_mongo, mock_ai):
    """
    Verifies that the 'Boss Fight' prompt for EVERY lesson contains
    the correct communicative goal and keywords.
    """
    
    target_lang = "it"
    native_lang = "en"
    
    # Ensure user exists so tutor endpoint doesn't 404 on logic
    mock_mongo.users.find_one.return_value = {"user_id": "test", "xp": 100}

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        
        payload = {
            "user_message": "Hello",
            "chat_history": [],
            "target_language": target_lang,
            "native_language": native_lang,
            "level": "Beginner",
            "lesson_id": lesson_id 
        }
        
        # Force server state to 'ready'
        with patch("server.is_loading", False):
            response = await ac.post("/tutor", json=payload)
        
        assert response.status_code == 200
        
        # INSPECT PROMPTS
        calls = mock_ai.call_args_list
        all_prompts_sent = " ".join([str(call.args) for call in calls])
        
        # 1. VERIFY MISSION GOAL
        expected_goal_key = f"{lesson_id.lower()}_comm"
        expected_goal = CONTENT_DB.get(expected_goal_key, {}).get(native_lang)
        
        assert expected_goal, f"CRITICAL: Missing goal text in CONTENT_DB for {lesson_id}"
        assert expected_goal in all_prompts_sent, \
            f"FAILED: Lesson {lesson_id} prompt missing goal: '{expected_goal}'"
        
        # 2. VERIFY KEYWORDS (Any Match Strategy)
        # We check if *any* of the lesson's keywords appear in the prompt.
        # This is robust against string escaping issues (e.g. L'ora vs L\'ora).
        concepts = LESSON_CONCEPTS[lesson_id]
        found_keyword = False
        
        for concept in concepts:
            word = CONTENT_DB[concept][target_lang][0]
            if word in all_prompts_sent or word.replace("'", "\\'") in all_prompts_sent:
                found_keyword = True
                break
        
        assert found_keyword, \
            f"FAILED: Lesson {lesson_id} prompt missing keywords. Prompt dump: {all_prompts_sent[:100]}..."