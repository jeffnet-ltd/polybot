"""
Module A1.3 data structure - Home & Housing
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_3_LESSONS = {
    "module_id": "A1.3",
    "title": "Home & Housing",
    "goal": "Describe where you live (House/Apartment) and locate objects within it.",
    "lessons": [
        {
            "lesson_id": "A1.3.0",
            "title": "Self-Assessment: Home & Housing",
            "focus": "Assess your confidence with describing your home",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel talking about your home?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can describe where I live (house/apartment)",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can name rooms in a house",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe where objects are located",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe colors of furniture",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.3.1",
            "title": "House vs. Apartment",
            "focus": "Types of housing, 'Vivo in...' / 'Abito a...'",
            "vocabulary": [
                {"term": "casa", "translation": "house"},
                {"term": "appartamento", "translation": "apartment"},
                {"term": "grande", "translation": "big/large"},
                {"term": "piccolo", "translation": "small"},
                {"term": "abito", "translation": "I live"},
                {"term": "vivo", "translation": "I live"},
                {"term": "in", "translation": "in"},
                {"term": "città", "translation": "city"},
                {"term": "campagna", "translation": "countryside"},
                {"term": "bello", "translation": "beautiful (masculine)"},
                {"term": "bella", "translation": "beautiful (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "casa",
                    "explanation": "house",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_casa_51.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "appartamento",
                    "explanation": "apartment",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_appartamento_52.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Two Ways to Say 'I Live'",
                    "correct_answer": "Vivo vs Abito",
                    "explanation": "Both 'Vivo' and 'Abito' mean 'I live'.\n\nVivo in città (I live in the city)\nAbito in campagna (I live in the countryside)\n\nThey are interchangeable!",
                    "sub_text": "Learn two ways to express location"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "grande",
                    "explanation": "big/large",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_grande_53.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "piccolo",
                    "explanation": "small",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_piccolo_54.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Housing Types",
                    "pairs": [["casa", "house"], ["appartamento", "apartment"], ["grande", "big"], ["piccolo", "small"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic housing vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Where does Maria live?",
                    "audio_text": "Abito in un appartamento in città.",
                    "options": ["In a house in the city", "In an apartment in the city", "In a house in the countryside", "In an apartment in the countryside"],
                    "correct_answer": "In an apartment in the city",
                    "explanation": "You heard 'appartamento in città' (apartment in the city).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I live in a house.",
                    "blocks": ["Vivo", "in", "una", "casa", "."],
                    "correct_answer": "Vivo in una casa.",
                    "explanation": "Vivo + in + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vivo in città",
                    "target_phrase": "Vivo in città",
                    "target_lang": "it",
                    "explanation": "Practice 'Vivo in' with city names"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Abito ___ un appartamento.'",
                    "options": ["in", "a", "di"],
                    "correct_answer": "in",
                    "explanation": "Use 'in' with housing types (appartamento, casa)"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove vivi?'",
                    "context": "You are at a party.",
                    "task": "Say you live in an apartment in the city.",
                    "target_lang": "it",
                    "explanation": "Use 'Vivo in un appartamento in città' or 'Abito in un appartamento in città'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match housing vocabulary",
                    "pairs": [["casa", "house"], ["appartamento", "apartment"], ["città", "city"], ["campagna", "countryside"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.2",
            "title": "Rooms & 'C'è' (Singular)",
            "focus": "Identifying rooms, 'There is' (Singular)",
            "vocabulary": [
                {"term": "cucina", "translation": "kitchen"},
                {"term": "bagno", "translation": "bathroom"},
                {"term": "camera da letto", "translation": "bedroom"},
                {"term": "salotto", "translation": "living room"},
                {"term": "c'è", "translation": "there is"},
                {"term": "qui", "translation": "here"},
                {"term": "dove", "translation": "where"},
                {"term": "la", "translation": "the (feminine)"},
                {"term": "una", "translation": "a/an (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: There Is",
                    "correct_answer": "C'è (There is)",
                    "explanation": "Use 'C'è' (there is) for singular things.\n\nC'è una cucina (There is a kitchen)\nC'è un bagno (There is a bathroom)",
                    "sub_text": "Singular form"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cucina",
                    "explanation": "kitchen",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cucina_55.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "bagno",
                    "explanation": "bathroom",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_bagno_56.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "camera da letto",
                    "explanation": "bedroom",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_camera_da_letto_57.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "salotto",
                    "explanation": "living room",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_salotto_58.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Rooms",
                    "pairs": [["cucina", "kitchen"], ["bagno", "bathroom"], ["camera da letto", "bedroom"], ["salotto", "living room"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic room vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What room is mentioned?",
                    "audio_text": "C'è una cucina grande.",
                    "options": ["cucina", "bagno", "camera da letto", "salotto"],
                    "correct_answer": "cucina",
                    "explanation": "You heard 'cucina' (kitchen).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "There is a bathroom.",
                    "blocks": ["C'è", "un", "bagno", "."],
                    "correct_answer": "C'è un bagno.",
                    "explanation": "C'è + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: C'è una cucina",
                    "target_phrase": "C'è una cucina",
                    "target_lang": "it",
                    "explanation": "Practice 'C'è' with feminine nouns"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ una camera da letto.'",
                    "options": ["C'è", "Ci sono", "È"],
                    "correct_answer": "C'è",
                    "explanation": "Use 'C'è' (there is) for singular rooms"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're showing someone your apartment.",
                    "context": "They ask: 'Dove è la cucina?'",
                    "task": "Say: 'Here, there is a kitchen.'",
                    "target_lang": "it",
                    "explanation": "Use 'Qui, c'è una cucina'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match rooms",
                    "pairs": [["cucina", "kitchen"], ["bagno", "bathroom"], ["camera da letto", "bedroom"], ["salotto", "living room"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.3",
            "title": "Furniture & 'Ci sono' (Plural)",
            "focus": "Furniture items, 'There are' (Plural), Quantities",
            "vocabulary": [
                {"term": "letto", "translation": "bed"},
                {"term": "tavolo", "translation": "table"},
                {"term": "sedia", "translation": "chair"},
                {"term": "divano", "translation": "sofa"},
                {"term": "finestra", "translation": "window"},
                {"term": "porta", "translation": "door"},
                {"term": "ci sono", "translation": "there are"},
                {"term": "molti", "translation": "many"},
                {"term": "due", "translation": "two"},
                {"term": "tre", "translation": "three"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: There Are",
                    "correct_answer": "Ci sono (There are)",
                    "explanation": "Use 'Ci sono' (there are) for plural things.\n\nCi sono due sedie (There are two chairs)\nCi sono molti libri (There are many books)",
                    "sub_text": "Plural form"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "letto",
                    "explanation": "bed",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_letto_59.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "tavolo",
                    "explanation": "table",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tavolo_60.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sedia",
                    "explanation": "chair",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sedia_61.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "divano",
                    "explanation": "sofa",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_divano_62.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "finestra",
                    "explanation": "window",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_finestra_63.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "porta",
                    "explanation": "door",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_porta_64.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Furniture",
                    "pairs": [["letto", "bed"], ["tavolo", "table"], ["sedia", "chair"], ["divano", "sofa"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic furniture vocabulary"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the description and answer the question.",
                    "text": "Nel salotto ci sono due sedie e un divano. C'è anche una finestra grande.",
                    "question": "How many chairs are in the living room?",
                    "options": ["one", "two", "three", "many"],
                    "correct_answer": "two",
                    "explanation": "The text says 'ci sono due sedie' (there are two chairs).",
                    "highlight_vocab": ["salotto", "ci sono", "due", "sedie", "divano", "finestra"]
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "There are three chairs.",
                    "blocks": ["Ci", "sono", "tre", "sedie", "."],
                    "correct_answer": "Ci sono tre sedie.",
                    "explanation": "Ci sono + number + plural noun."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "There are many books.",
                    "blocks": ["Ci", "sono", "molti", "libri", "."],
                    "correct_answer": "Ci sono molti libri.",
                    "explanation": "Ci sono + molti + plural noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ci sono due sedie",
                    "target_phrase": "Ci sono due sedie",
                    "target_lang": "it",
                    "explanation": "Practice 'Ci sono' with numbers"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ due finestre.'",
                    "options": ["C'è", "Ci sono", "È"],
                    "correct_answer": "Ci sono",
                    "explanation": "Use 'Ci sono' (there are) for plural things"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Cosa c'è nella camera?'",
                    "context": "You're describing your bedroom.",
                    "task": "Say there is a bed and there are two chairs.",
                    "target_lang": "it",
                    "explanation": "Use 'C'è un letto e ci sono due sedie'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match furniture",
                    "pairs": [["letto", "bed"], ["tavolo", "table"], ["sedia", "chair"], ["divano", "sofa"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.4",
            "title": "Prepositions of Place (Simple)",
            "focus": "Locating objects (On, Under, Inside)",
            "vocabulary": [
                {"term": "sopra", "translation": "on/above"},
                {"term": "sotto", "translation": "under/below"},
                {"term": "dentro", "translation": "inside"},
                {"term": "libro", "translation": "book"},
                {"term": "gatto", "translation": "cat"},
                {"term": "il", "translation": "the (masculine)"},
                {"term": "sul", "translation": "on the"},
                {"term": "nella", "translation": "in the (feminine)"},
                {"term": "scatola", "translation": "box"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Prepositions of Place",
                    "correct_answer": "Sopra, Sotto, Dentro",
                    "explanation": "Sopra = on/above\nSotto = under/below\nDentro = inside\n\nIl libro è sul tavolo (The book is on the table)",
                    "sub_text": "Learn basic location words"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sopra",
                    "explanation": "on/above",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sopra_65.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sotto",
                    "explanation": "under/below",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sotto_66.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dentro",
                    "explanation": "inside",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dentro_67.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Prepositions",
                    "pairs": [["sopra", "on/above"], ["sotto", "under/below"], ["dentro", "inside"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic prepositions of place"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Where is the book?",
                    "audio_text": "Il libro è sul tavolo.",
                    "options": ["On the table", "Under the table", "Inside the box", "On the chair"],
                    "correct_answer": "On the table",
                    "explanation": "You heard 'sul tavolo' (on the table).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The cat is under the table.",
                    "blocks": ["Il", "gatto", "è", "sotto", "il", "tavolo", "."],
                    "correct_answer": "Il gatto è sotto il tavolo.",
                    "explanation": "Subject + è + preposition + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Il libro è sul tavolo",
                    "target_phrase": "Il libro è sul tavolo",
                    "target_lang": "it",
                    "explanation": "Practice preposition 'sul' (on the)"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il libro è ___ tavolo.'",
                    "options": ["sul", "sotto", "dentro"],
                    "correct_answer": "sul",
                    "explanation": "Use 'sul' (on the) to say something is on top"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove è il gatto?'",
                    "context": "You're looking for your cat.",
                    "task": "Say the cat is under the table.",
                    "target_lang": "it",
                    "explanation": "Use 'Il gatto è sotto il tavolo'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match prepositions",
                    "pairs": [["sopra", "on/above"], ["sotto", "under/below"], ["dentro", "inside"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.5",
            "title": "Prepositions of Place (Relative)",
            "focus": "Locating objects (Near, Far, Next to)",
            "vocabulary": [
                {"term": "vicino a", "translation": "near/next to"},
                {"term": "lontano da", "translation": "far from"},
                {"term": "davanti a", "translation": "in front of"},
                {"term": "dietro", "translation": "behind"},
                {"term": "a destra", "translation": "to the right"},
                {"term": "a sinistra", "translation": "to the left"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Relative Prepositions",
                    "correct_answer": "Vicino, Lontano, Davanti",
                    "explanation": "Vicino a = near/next to\nLontano da = far from\nDavanti a = in front of\nDietro = behind",
                    "sub_text": "Learn relative location words"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "vicino a",
                    "explanation": "near/next to",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vicino_a_68.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "lontano da",
                    "explanation": "far from",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_lontano_da_69.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "davanti a",
                    "explanation": "in front of",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_davanti_a_70.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "dietro",
                    "explanation": "behind",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dietro_71.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "a destra",
                    "explanation": "to the right",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_a_destra_72.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "a sinistra",
                    "explanation": "to the left",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_a_sinistra_73.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Relative Prepositions",
                    "pairs": [["vicino a", "near/next to"], ["lontano da", "far from"], ["davanti a", "in front of"], ["dietro", "behind"]],
                    "correct_answer": "match_all",
                    "explanation": "Relative location vocabulary"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the description and answer the question.",
                    "text": "Il tavolo è vicino alla finestra. La sedia è dietro il tavolo.",
                    "question": "Where is the chair?",
                    "options": ["Next to the table", "Behind the table", "In front of the table", "Far from the table"],
                    "correct_answer": "Behind the table",
                    "explanation": "The text says 'La sedia è dietro il tavolo' (The chair is behind the table).",
                    "highlight_vocab": ["tavolo", "vicino", "finestra", "sedia", "dietro"]
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The window is next to the door.",
                    "blocks": ["La", "finestra", "è", "vicino", "alla", "porta", "."],
                    "correct_answer": "La finestra è vicino alla porta.",
                    "explanation": "Subject + è + vicino a + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vicino alla porta",
                    "target_phrase": "Vicino alla porta",
                    "target_lang": "it",
                    "explanation": "Practice 'vicino a' with articles"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La sedia è ___ tavolo.' (The chair is behind the table)",
                    "options": ["dietro il", "vicino a", "davanti a"],
                    "correct_answer": "dietro il",
                    "explanation": "Use 'dietro il' (behind the) for position"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove è la finestra?'",
                    "context": "You're describing your room.",
                    "task": "Say the window is next to the door.",
                    "target_lang": "it",
                    "explanation": "Use 'La finestra è vicino alla porta'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match relative prepositions",
                    "pairs": [["vicino a", "near/next to"], ["lontano da", "far from"], ["davanti a", "in front of"], ["dietro", "behind"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.6",
            "title": "Colors & Description",
            "focus": "Describing furniture/rooms (Adjective agreement)",
            "vocabulary": [
                {"term": "bianco", "translation": "white (masculine)"},
                {"term": "bianca", "translation": "white (feminine)"},
                {"term": "nero", "translation": "black (masculine)"},
                {"term": "nera", "translation": "black (feminine)"},
                {"term": "rosso", "translation": "red (masculine)"},
                {"term": "rossa", "translation": "red (feminine)"},
                {"term": "blu", "translation": "blue (invariable)"},
                {"term": "verde", "translation": "green (invariable)"},
                {"term": "giallo", "translation": "yellow (masculine)"},
                {"term": "gialla", "translation": "yellow (feminine)"},
                {"term": "di che colore", "translation": "what color"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Color Agreement",
                    "correct_answer": "Masculine vs Feminine",
                    "explanation": "Colors must agree with the noun they describe.\n\nIl tavolo bianco (The white table - masc)\nLa sedia bianca (The white chair - fem)\n\nNote: Some colors are invariable (blu, verde)",
                    "sub_text": "Learn color agreement"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "bianco",
                    "explanation": "white (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_bianco_74.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "bianca",
                    "explanation": "white (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_bianca_75.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "nero",
                    "explanation": "black (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_nero_76.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "nera",
                    "explanation": "black (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_nera_77.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "rosso",
                    "explanation": "red (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_rosso_78.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "rossa",
                    "explanation": "red (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_rossa_79.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "blu",
                    "explanation": "blue (invariable)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_blu_80.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "verde",
                    "explanation": "green (invariable)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_verde_81.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "giallo",
                    "explanation": "yellow (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_giallo_82.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "gialla",
                    "explanation": "yellow (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_gialla_83.mp3"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Sort colors by gender",
                    "columns": [
                        {"id": "masc", "label": "Maschile"},
                        {"id": "fem", "label": "Femminile"},
                        {"id": "inv", "label": "Invariable"}
                    ],
                    "items": [
                        {"text": "Bianco", "column_id": "masc", "hint": "White (masculine)"},
                        {"text": "Bianca", "column_id": "fem", "hint": "White (feminine)"},
                        {"text": "Blu", "column_id": "inv", "hint": "Blue (same for both)"},
                        {"text": "Verde", "column_id": "inv", "hint": "Green (same for both)"}
                    ],
                    "correct_answer": "all_correct",
                    "explanation": "Some colors change ending, others stay the same."
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Colors",
                    "pairs": [["bianco", "white"], ["nero", "black"], ["rosso", "red"], ["blu", "blue"], ["verde", "green"], ["giallo", "yellow"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic color vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What color is the chair?",
                    "audio_text": "La sedia è rossa.",
                    "options": ["red", "white", "black", "blue"],
                    "correct_answer": "red",
                    "explanation": "You heard 'rossa' (red - feminine).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The white table is in the kitchen.",
                    "blocks": ["Il", "tavolo", "bianco", "è", "nella", "cucina", "."],
                    "correct_answer": "Il tavolo bianco è nella cucina.",
                    "explanation": "Article + noun + color (agreement) + è + preposition + room."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: La sedia rossa",
                    "target_phrase": "La sedia rossa",
                    "target_lang": "it",
                    "explanation": "Practice color agreement with feminine nouns"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La sedia è ___.' (The chair is white)",
                    "options": ["bianco", "bianca", "bianchi"],
                    "correct_answer": "bianca",
                    "explanation": "Sedia is feminine, so use 'bianca'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il tavolo è ___.' (The table is white)",
                    "options": ["bianco", "bianca", "bianchi"],
                    "correct_answer": "bianco",
                    "explanation": "Tavolo is masculine, so use 'bianco'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Di che colore è la sedia?'",
                    "context": "You're describing furniture.",
                    "task": "Say the chair is red.",
                    "target_lang": "it",
                    "explanation": "Use 'La sedia è rossa' (chair is feminine, so use 'rossa')."
                },
                {
                    "type": "free_writing",
                    "step": 8,
                    "prompt": "Describe your room.",
                    "context": "You're showing someone your room.",
                    "task": "Write 2-3 sentences describing your room. Include: what room it is, what furniture is there, and colors.",
                    "target_lang": "it",
                    "required_elements": ["room", "furniture", "color"],
                    "example_response": "Questa è la mia camera da letto. C'è un letto e ci sono due sedie. Il letto è bianco.",
                    "validation_mode": "ai",
                    "explanation": "Great! You described the room, furniture, and colors correctly."
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Review: Match colors",
                    "pairs": [["bianco", "white"], ["nero", "black"], ["rosso", "red"], ["blu", "blue"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.3.BOSS",
            "title": "Boss Fight: The Real Estate Viewing",
            "type": "boss_fight",
            "focus": "Viewing a rental apartment - describing rooms and furniture",
            "vocabulary": [
                {"term": "appartamento", "translation": "apartment"},
                {"term": "cucina", "translation": "kitchen"},
                {"term": "bagno", "translation": "bathroom"},
                {"term": "camera da letto", "translation": "bedroom"},
                {"term": "C'è", "translation": "there is"},
                {"term": "Ci sono", "translation": "there are"},
                {"term": "bello", "translation": "beautiful (masculine)"},
                {"term": "bella", "translation": "beautiful (feminine)"}
            ],
            "exercises": [
                {
                    "type": "boss_fight",
                    "step": 1,
                    "prompt": "You are viewing a rental apartment with a real estate agent.",
                    "scenario": "real_estate_agent",
                    "ai_prompt": "You are a formal real estate agent. Ask about rooms and describe the apartment formally.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Formal Viewing",
                            "round_description": "Ask the agent about the apartment's rooms and features.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Benvenuto. Questo è l'appartamento.",
                                    "user_requirement": "Greet formally and ask about rooms.",
                                    "required_words": ["Buongiorno", "C'è", "cucina"],
                                    "hints": ["Buongiorno", "C'è una cucina?", "Quante camere ci sono?"],
                                    "invalid_responses": ["Ciao!", "C'è cucina?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Sì, c'è una cucina grande e ci sono due camere da letto.",
                                    "user_requirement": "Ask about the bathroom.",
                                    "required_words": ["C'è", "bagno"],
                                    "hints": ["C'è un bagno?", "C'è il bagno?"],
                                    "invalid_responses": ["Bagno?", "Where is bathroom?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Sì, c'è un bagno. È molto bello.",
                                    "user_requirement": "Ask if the apartment is nice.",
                                    "required_words": ["È", "bello", "bella"],
                                    "hints": ["È bello?", "È bella?"],
                                    "invalid_responses": ["Nice?", "Is good?"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Sì, è molto bella! Vuole visitarla?",
                                    "user_requirement": "Say yes politely and thank them.",
                                    "required_words": ["Sì", "grazie"],
                                    "hints": ["Sì, grazie", "Sì, vorrei"],
                                    "invalid_responses": ["Yes", "OK"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Casual Chat",
                            "round_description": "Your friend asks if you like the apartment.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Hai visto l'appartamento?",
                                    "user_requirement": "Say yes and describe it briefly.",
                                    "required_words": ["Sì", "è", "bello", "bella"],
                                    "hints": ["Sì, è bella", "Sì, è bello"],
                                    "invalid_responses": ["Yes", "It's nice"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Bene! Cosa c'è dentro?",
                                    "user_requirement": "Say what rooms there are.",
                                    "required_words": ["C'è", "cucina", "camera"],
                                    "hints": ["C'è una cucina", "Ci sono due camere"],
                                    "invalid_responses": ["There is kitchen", "Has rooms"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Interessante! È grande?",
                                    "user_requirement": "Say if it's big or small.",
                                    "required_words": ["È", "grande", "piccolo"],
                                    "hints": ["È grande", "È piccola"],
                                    "invalid_responses": ["Big", "Small"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Capisco! Beh, buona fortuna!",
                                    "user_requirement": "Say goodbye casually.",
                                    "required_words": ["Ciao", "grazie"],
                                    "hints": ["Ciao!", "Grazie, ciao!"],
                                    "invalid_responses": ["Bye", "See you"]
                                }
                            ]
                        }
                    ],
                    "explanation": "You successfully viewed the apartment and discussed it with a friend!"
                }
            ]
        }
    ]
}
