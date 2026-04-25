"""
Module A1.1 data structure — Spanish (es)
"""

MODULE_A1_1_ES_LESSONS = {
    "module_id": "A1.1",
    "title": "Greetings & Introductions",
    "goal": "Navigate informal and formal social situations in Spanish and introduce yourself with correct pronunciation.",
    "lessons": [
        {
            "lesson_id": "A1.1.0",
            "title": "Self-Assessment: Greetings & Introductions",
            "focus": "Assess your confidence with basic greetings in Spanish",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel with greetings and introductions in Spanish?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can greet someone informally (friends)",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can greet someone formally (authority figures)",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can introduce myself",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask where someone is from",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "Self-assessment helps you track your progress. No wrong answers!"
                }
            ]
        },
        {
            "lesson_id": "A1.1.1",
            "title": "The Informal Zone (Friends & Peers)",
            "focus": "Casual greetings, 'Tú' (You informal)",
            "vocabulary": [
                {"term": "Hola",         "translation": "Hi/Hello"},
                {"term": "¿Cómo estás?", "translation": "How are you? (Informal)"},
                {"term": "Bien",         "translation": "Well/Good"},
                {"term": "¿Y tú?",       "translation": "And you?"},
                {"term": "Gracias",      "translation": "Thank you"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Hola",
                    "explanation": "Hi/Hello — the universal informal Spanish greeting",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_hola_0.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "¿Cómo estás?",
                    "explanation": "How are you? (Informal — use with friends)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_como_estas_1.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Audio to Text",
                    "pairs": [["Hola", "Hi/Hello"], ["¿Cómo estás?", "How are you?"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect sound to meaning"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen to the audio. What greeting did you hear?",
                    "audio_text": "¡Hola! ¿Cómo estás?",
                    "options": ["Hola", "Buenos días", "Buenas tardes", "Adiós"],
                    "correct_answer": "Hola",
                    "explanation": "You heard '¡Hola!', the informal greeting used with friends.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How are you? (Informal)",
                    "blocks": ["¿Cómo", "estás?"],
                    "correct_answer": "¿Cómo estás?",
                    "explanation": "Use '¿Cómo estás?' for informal greetings — 'tú' is implied, not stated."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat after me",
                    "target_phrase": "¿Cómo estás?",
                    "target_lang": "es",
                    "explanation": "Practice the question intonation — Spanish questions start with ¿"
                },
                {
                    "type": "reading_comprehension",
                    "step": 6,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Carlos: ¡Hola! ¿Cómo estás?\nSofía: ¡Bien, gracias! ¿Y tú?",
                    "question": "How does Carlos greet Sofía?",
                    "options": ["Hola", "Buenos días", "Adiós"],
                    "correct_answer": "Hola",
                    "explanation": "Carlos uses '¡Hola!', the informal greeting for friends.",
                    "highlight_vocab": ["Hola", "¿Cómo estás?", "Bien", "gracias"]
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Your friend Carlos arrives.",
                    "context": "Your friend Carlos arrives.",
                    "task": "Greet him.",
                    "target_lang": "es",
                    "explanation": "This is a friend, so use a casual greeting. What informal greeting did you learn?"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match the informal greetings",
                    "pairs": [["Hola", "Hi/Hello"], ["¿Cómo estás?", "How are you?"], ["Bien", "Well"], ["Gracias", "Thank you"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the informal greetings.",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Hola vs. Buenas — When to Use Each",
                    "explanation": "While '¡Hola!' is the most common greeting among friends, '¡Buenas!' (short for buenos días / buenas tardes / buenas noches) is a handy all-purpose option:\n\n• Hola — Very informal, use with friends, family, and peers\n• Buenas — Relaxed and friendly, works at any time of day\n• Buenos días / Buenas tardes — More formal, safer with strangers\n\nTip: When in doubt, '¡Buenas!' is almost always safe and sounds natural.",
                    "sub_text": "Understanding these nuances helps you make a great first impression.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.2",
            "title": "Formal Greetings & Time-Based Expressions",
            "focus": "Time-based greetings, formal register",
            "vocabulary": [
                {"term": "Buenos días",  "translation": "Good morning (Formal)"},
                {"term": "Buenas tardes","translation": "Good afternoon (Formal)"},
                {"term": "Buenas noches","translation": "Good evening (Formal)"},
                {"term": "Adiós",        "translation": "Goodbye"},
                {"term": "¿Cómo está?",  "translation": "How are you? (Formal)"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buenos días",
                    "explanation": "Good morning (Formal) — use until around midday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_buenos_dias_5.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buenas tardes",
                    "explanation": "Good afternoon (Formal) — use from midday until evening",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_buenas_tardes_6.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buenas noches",
                    "explanation": "Good evening / Good night (Formal) — use after dark",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_buenas_noches_7.mp3"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "You meet a professor at 10 AM. Select the correct greeting.",
                    "options": ["Hola", "Buenos días", "¿Y tú?"],
                    "correct_answer": "Buenos días",
                    "explanation": "Formal situation in the morning requires 'Buenos días'"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What formal greeting did you hear?",
                    "audio_text": "Buenas tardes, ¿cómo está?",
                    "options": ["Buenos días", "Buenas tardes", "Hola", "Buenas noches"],
                    "correct_answer": "Buenas tardes",
                    "explanation": "You heard 'Buenas tardes' (Good afternoon), used in formal situations after midday.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How are you? (Formal)",
                    "blocks": ["¿Cómo", "está?"],
                    "correct_answer": "¿Cómo está?",
                    "explanation": "The formal 'you' (usted) is implied — native speakers almost always drop it and say '¿Cómo está?' rather than '¿Cómo está usted?'"
                },
                {
                    "type": "info_card",
                    "step": 5,
                    "prompt": "Cultural Note",
                    "correct_answer": "Formal vs. Informal in Spanish",
                    "explanation": "In Spanish, choosing between 'tú' (informal) and 'usted' (formal) depends on:\n• Age difference\n• Social hierarchy\n• Setting (work vs. social)\n\nUse 'tú' with friends, peers, and family.\nUse 'usted' with elders, authority figures, and in professional settings.\n\nYou may see or hear usted in texts and formal speech — it means formal 'you' — but it is usually implied and omitted in conversation. You don't need to produce it at this stage.",
                    "sub_text": "Understanding this cultural context helps you choose the right greeting.",
                    "cultural_note": True
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat after me",
                    "target_phrase": "Adiós",
                    "target_lang": "es",
                    "explanation": "Practice the accent on the final syllable: a-DIÓS"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "It is 7 PM. You see your professor.",
                    "context": "It is 7 PM. You see your professor.",
                    "task": "Greet them formally.",
                    "target_lang": "es",
                    "explanation": "It's evening. What time-based greeting is appropriate?"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match the formal greetings",
                    "pairs": [["Buenos días", "Good morning"], ["Buenas tardes", "Good afternoon"], ["Buenas noches", "Good evening"], ["¿Cómo está?", "How are you? (Formal)"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the formal greetings.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.3",
            "title": "Introducing Yourself",
            "focus": "Me llamo, Soy, Mucho gusto — and Ser vs. Estar",
            "vocabulary": [
                {"term": "Me llamo",   "translation": "My name is"},
                {"term": "Soy",        "translation": "I am"},
                {"term": "Mucho gusto","translation": "Nice to meet you"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Me llamo",
                    "explanation": "My name is (literally: I call myself)",
                    "sub_text": "The most natural way to introduce your name in Spanish",
                    "audio_url": "/static/audio/es_me_llamo_11.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Soy",
                    "explanation": "I am — alternative way to introduce yourself",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_soy_12.mp3"
                },
                {
                    "type": "unscramble",
                    "step": 2,
                    "prompt": "My name is Ana.",
                    "blocks": ["Me", "llamo", "Ana"],
                    "correct_answer": "Me llamo Ana",
                    "explanation": "The verb goes in the middle: 'Me llamo [name]'",
                    "common_mistakes": [
                        {
                            "pattern": "llamo me",
                            "explanation": "In Spanish, the reflexive pronoun 'Me' comes before the verb 'llamo'. The correct order is 'Me llamo'."
                        },
                        {
                            "pattern": "yo me llamo",
                            "explanation": "Good! 'Yo me llamo' is also correct, though 'Me llamo' is more natural. Both are acceptable!"
                        }
                    ]
                },
                {
                    "type": "info_card",
                    "step": 2,
                    "prompt": "Grammar: Ser (To Be)",
                    "correct_answer": "Ser (To Be)",
                    "table": {
                        "headers": ["Spanish", "English"],
                        "rows": [
                            ["Yo soy",     "I am"],
                            ["Tú eres",    "You are"],
                            ["Él/Ella es", "He/She is"]
                        ]
                    },
                    "sub_text": "Learn the verb 'ser' (to be) — used for identity and permanent characteristics"
                },
                {
                    "type": "match",
                    "step": 3,
                    "prompt": "Match the pronoun to the verb form",
                    "pairs": [["Yo", "soy"], ["Tú", "eres"], ["Él/Ella", "es"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect pronouns with their 'ser' forms"
                },
                {
                    "type": "reading_comprehension",
                    "step": 4,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Carlos: ¡Hola! ¿Cómo estás?\nSofía: ¡Bien, gracias! ¿Y tú?\nCarlos: ¡Bien también! ¡Mucho gusto! Me llamo Carlos.",
                    "question": "How does Carlos introduce himself?",
                    "options": ["Me llamo Carlos", "Soy Carlos", "Yo soy Carlos", "Mi nombre es Carlos"],
                    "correct_answer": "Me llamo Carlos",
                    "explanation": "Carlos says 'Me llamo Carlos' — the most natural way to introduce yourself in Spanish.",
                    "highlight_vocab": ["Hola", "¿Cómo estás?", "Bien", "gracias", "Me llamo"]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mucho gusto",
                    "target_phrase": "Mucho gusto",
                    "target_lang": "es",
                    "explanation": "Practice the 'gu' sound — the 'u' is silent between g and a vowel"
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat: Me llamo",
                    "target_phrase": "Me llamo",
                    "target_lang": "es",
                    "explanation": "Practice the double-L (ll) — it sounds like 'y' in most dialects"
                },
                {
                    "type": "fill_blank",
                    "step": 7,
                    "prompt": "Complete: '___ llamo María.'",
                    "options": ["Me", "Te", "Se"],
                    "correct_answer": "Me",
                    "explanation": "Testing memory of the reflexive pronoun 'Me'"
                },
                {
                    "type": "fill_blank",
                    "step": 8,
                    "prompt": "Complete: 'Yo ___ María.' (I am María)",
                    "options": ["soy", "eres", "es"],
                    "correct_answer": "soy",
                    "explanation": "Practice 'ser' conjugation: Yo soy = I am"
                },
                {
                    "type": "mini_prompt",
                    "step": 9,
                    "prompt": "Someone says '¡Mucho gusto!'",
                    "context": "Someone says '¡Mucho gusto!'",
                    "task": "Introduce yourself.",
                    "target_lang": "es",
                    "explanation": "Someone said '¡Mucho gusto!' to you. How do you introduce yourself in Spanish?"
                },
                {
                    "type": "free_writing",
                    "step": 10,
                    "prompt": "Write a simple introduction about yourself.",
                    "context": "You're meeting someone new.",
                    "task": "Write 2-3 sentences introducing yourself. Include: your name and a greeting.",
                    "target_lang": "es",
                    "required_elements": ["name", "greeting"],
                    "example_response": "¡Hola! Me llamo Ana.",
                    "validation_mode": "ai",
                    "explanation": "Great! You included your name and a greeting. Perfect introduction!"
                },
                {
                    "type": "info_card",
                    "step": 11,
                    "prompt": "Cultural Note",
                    "correct_answer": "Ser vs. Estar — Two Ways to Say 'To Be'",
                    "explanation": "Spanish has two verbs meaning 'to be': **ser** and **estar**.\n\n**Ser** (permanent):\n• Identity: Soy Ana (I am Ana)\n• Nationality: Soy española (I'm Spanish)\n• Origin: Soy de Madrid (I'm from Madrid)\n\n**Estar** (temporary):\n• State: Estoy bien (I'm well)\n• Feeling: Estoy cansada (I'm tired)\n\nFor introductions and nationalities, always use **ser**.\nFor greetings like '¿Cómo estás?', the answer uses **estar**: 'Estoy bien'.",
                    "sub_text": "This is one of the most important distinctions in Spanish — it becomes natural with practice.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.4",
            "title": "Polite Expressions & Closings",
            "focus": "Buenas (the safe word), polite closings",
            "vocabulary": [
                {"term": "Buenas",       "translation": "Hello/Hi (Safe/Neutral)"},
                {"term": "Por favor",    "translation": "Please"},
                {"term": "De nada",      "translation": "You're welcome"},
                {"term": "Hasta pronto", "translation": "See you soon"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buenas",
                    "explanation": "The safe word — short for 'buenos días / buenas tardes / buenas noches'. Works at any time of day.",
                    "sub_text": "Usable in almost any situation",
                    "audio_url": "/static/audio/es_buenas_13.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Pairs",
                    "pairs": [["Gracias", "Thank you"], ["De nada", "You're welcome"]],
                    "correct_answer": "match_all",
                    "explanation": "Teaches the polite response pair"
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "A coffee, please.",
                    "blocks": ["Un", "café", "por", "favor"],
                    "correct_answer": "Un café, por favor",
                    "explanation": "Noun + polite marker. 'Por favor' goes at the end in Spanish."
                },
                {
                    "type": "info_card",
                    "step": 4,
                    "prompt": "Cultural Note",
                    "correct_answer": "Spanish Coffee Culture",
                    "table": {
                        "headers": ["Spanish", "English", "Description", "When to Order"],
                        "rows": [
                            ["Café solo",      "Espresso",          "Small, strong shot",       "Any time"],
                            ["Café con leche", "Coffee with milk",  "Half coffee, half hot milk","Breakfast"],
                            ["Cortado",        "Cortado",           "Espresso with dash of milk","Any time"],
                            ["Café americano", "Americano",         "Diluted espresso",          "Any time"],
                        ]
                    },
                    "explanation": "In Spain, coffee is typically ordered at the bar counter. Café con leche is the most common breakfast coffee.",
                    "sub_text": "Ordering a cappuccino in Spain will mark you as a tourist!",
                    "cultural_note": True
                },
                {
                    "type": "listening_comprehension",
                    "step": 5,
                    "prompt": "Listen. What polite expression did you hear?",
                    "audio_text": "Buenas, por favor.",
                    "options": ["Buenas", "Hola", "Buenos días", "Adiós"],
                    "correct_answer": "Buenas",
                    "explanation": "You heard '¡Buenas!', the safe, neutral greeting that works any time of day.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat after me",
                    "target_phrase": "Hasta pronto",
                    "target_lang": "es",
                    "explanation": "Practice the 'h' — it is always silent in Spanish. Say 'asta pronto'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You are leaving a shop.",
                    "context": "You are leaving a shop.",
                    "task": "Say goodbye politely.",
                    "target_lang": "es",
                    "explanation": "Think about how to say goodbye politely. What phrases have you learned for polite closings?"
                },
                {
                    "type": "free_writing",
                    "step": 8,
                    "prompt": "Write a polite goodbye message.",
                    "context": "You are leaving a shop after buying something.",
                    "task": "Write 1-2 sentences saying goodbye politely. Include a thank you.",
                    "target_lang": "es",
                    "required_elements": ["goodbye", "thank you"],
                    "example_response": "¡Gracias! ¡Hasta pronto!",
                    "validation_mode": "ai",
                    "explanation": "Great! 'Gracias' (thank you) and 'Hasta pronto' (see you soon) are perfect for leaving a shop."
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Review: Match the polite expressions",
                    "pairs": [["Buenas", "Hello (Safe/Neutral)"], ["Por favor", "Please"], ["De nada", "You're welcome"], ["Hasta pronto", "See you soon"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the polite expressions.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.5",
            "title": "Subject Pronouns & The Verb 'To Be'",
            "focus": "Subject pronouns (Yo, Tú, Él, Ella) and 'Ser' conjugation",
            "vocabulary": [
                {"term": "Yo",   "translation": "I"},
                {"term": "Tú",   "translation": "You (informal)"},
                {"term": "Él",   "translation": "He"},
                {"term": "Ella", "translation": "She"},
                {"term": "Soy",  "translation": "I am"},
                {"term": "Eres", "translation": "You are"},
                {"term": "Es",   "translation": "He/She is"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Yo",
                    "explanation": "I (subject pronoun) — often dropped in Spanish since the verb ending shows who is speaking",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_yo_14.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Tú",
                    "explanation": "You (informal, singular) — note the accent: 'tú' (you) vs 'tu' (your)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_tu_15.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Él",
                    "explanation": "He (subject pronoun) — note the accent: 'él' (he) vs 'el' (the)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_el_16.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Ella",
                    "explanation": "She (subject pronoun)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_ella_17.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Pronouns to English",
                    "pairs": [["Yo", "I"], ["Tú", "You"], ["Él", "He"], ["Ella", "She"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect Spanish pronouns with their English meanings"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the dialogue and answer the question.",
                    "text": "Persona 1: ¿Quién eres?\nPersona 2: Yo soy María. ¿Y tú?\nPersona 1: Yo soy Lucas.",
                    "question": "What does 'Yo soy' mean?",
                    "options": ["I am", "You are", "He is", "We are"],
                    "correct_answer": "I am",
                    "explanation": "'Yo soy' means 'I am' in Spanish. It's used to introduce yourself or describe yourself.",
                    "highlight_vocab": ["¿Quién eres?", "Yo soy", "¿Y tú?"]
                },
                {
                    "type": "info_card",
                    "step": 4,
                    "prompt": "Grammar: The Verb 'Ser' (To Be)",
                    "correct_answer": "Ser (To Be)",
                    "table": {
                        "headers": ["Spanish", "English"],
                        "rows": [
                            ["Yo soy",     "I am"],
                            ["Tú eres",    "You are"],
                            ["Él/Ella es", "He/She is"]
                        ]
                    },
                    "sub_text": "Learn how to say 'I am', 'You are', 'He/She is'"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "I am Spanish.",
                    "blocks": ["Yo", "soy", "español"],
                    "correct_answer": "Yo soy español.",
                    "explanation": "Subject pronoun + verb + adjective. Note: 'Yo' is often dropped — 'Soy español' is more natural."
                },
                {
                    "type": "unscramble",
                    "step": 6,
                    "prompt": "You are well.",
                    "blocks": ["Tú", "estás", "bien"],
                    "correct_answer": "Tú estás bien.",
                    "explanation": "Practice 'tú estás' — note 'bien' uses 'estar' (temporary state), not 'ser'"
                },
                {
                    "type": "echo_chamber",
                    "step": 7,
                    "prompt": "Repeat: Yo soy",
                    "target_phrase": "Yo soy",
                    "target_lang": "es",
                    "explanation": "Practice 'I am' — the 'y' in 'yo' sounds like the 'y' in 'yes'"
                },
                {
                    "type": "echo_chamber",
                    "step": 8,
                    "prompt": "Repeat: Él es",
                    "target_phrase": "Él es",
                    "target_lang": "es",
                    "explanation": "Practice 'He is' — remember the accent on 'Él'"
                },
                {
                    "type": "fill_blank",
                    "step": 9,
                    "prompt": "Complete: '___ soy María.'",
                    "options": ["Yo", "Tú", "Él"],
                    "correct_answer": "Yo",
                    "explanation": "Choose the correct subject pronoun for 'I am'"
                },
                {
                    "type": "fill_blank",
                    "step": 10,
                    "prompt": "Complete: 'Él ___ español.'",
                    "options": ["soy", "eres", "es"],
                    "correct_answer": "es",
                    "explanation": "Choose the correct verb form for 'he'"
                },
                {
                    "type": "mini_prompt",
                    "step": 11,
                    "prompt": "Someone asks: '¿Quién eres?' (Who are you?)",
                    "context": "Someone asks: '¿Quién eres?' (Who are you?)",
                    "task": "Respond with your name using 'Soy' or 'Me llamo'.",
                    "target_lang": "es",
                    "explanation": "Use 'Soy [nombre]' or 'Me llamo [nombre]' to answer 'Who are you?'"
                },
                {
                    "type": "match",
                    "step": 12,
                    "prompt": "Review: Match the pronouns and verb forms",
                    "pairs": [["Yo", "I"], ["Tú", "You"], ["Él", "He"], ["Ella", "She"], ["Yo soy", "I am"], ["Tú eres", "You are"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the pronouns and their 'ser' forms.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.6",
            "title": "Introduction to Nouns",
            "focus": "Singular nouns, gender (masculine/feminine), basic article patterns",
            "vocabulary": [
                {"term": "café",  "translation": "coffee / café (masculine)"},
                {"term": "casa",  "translation": "house (feminine)"},
                {"term": "amigo", "translation": "friend (masculine)"},
                {"term": "amiga", "translation": "friend (feminine)"},
                {"term": "libro", "translation": "book (masculine)"},
                {"term": "pluma", "translation": "pen (feminine)"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Nouns Have Gender",
                    "correct_answer": "Masculino & Femenino",
                    "explanation": "Spanish nouns are either masculine (el/un) or feminine (la/una). Most nouns ending in -o are masculine, most ending in -a are feminine.",
                    "sub_text": "Learn about noun gender"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "café",
                    "explanation": "coffee / café (masculine — ends in -é, takes 'un/el')",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_cafe_18.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "casa",
                    "explanation": "house (feminine — ends in -a, takes 'una/la')",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_casa_19.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "amigo",
                    "explanation": "friend (masculine — ends in -o, takes 'un/el')",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_amigo_20.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "amiga",
                    "explanation": "friend (feminine — ends in -a, takes 'una/la')",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_amiga_21.mp3"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Drag each word to the correct gender column",
                    "words": ["café", "casa", "amigo", "amiga"],
                    "correct_answers": {
                        "café":  "masculino",
                        "casa":  "femenino",
                        "amigo": "masculino",
                        "amiga": "femenino",
                    },
                    "correct_answer": "all_correct",
                    "explanation": "Words ending in -o/-é are usually masculine, words ending in -a are usually feminine"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "What gender is 'libro' (book)?",
                    "options": ["Masculino", "Femenino"],
                    "correct_answer": "Masculino",
                    "explanation": "Words ending in -o are usually masculine"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "What gender is 'pluma' (pen)?",
                    "options": ["Masculino", "Femenino"],
                    "correct_answer": "Femenino",
                    "explanation": "Words ending in -a are usually feminine"
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "A coffee, please.",
                    "blocks": ["Un", "café", "por", "favor"],
                    "correct_answer": "Un café, por favor",
                    "explanation": "Practice noun + article. 'Un' is used with masculine nouns."
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "The house is big.",
                    "blocks": ["La", "casa", "es", "grande"],
                    "correct_answer": "La casa es grande.",
                    "explanation": "Practice noun + article. 'La' is used with feminine nouns."
                },
                {
                    "type": "echo_chamber",
                    "step": 4,
                    "prompt": "Repeat: un café",
                    "target_phrase": "un café",
                    "target_lang": "es",
                    "explanation": "Practice masculine noun with indefinite article"
                },
                {
                    "type": "echo_chamber",
                    "step": 4,
                    "prompt": "Repeat: la casa",
                    "target_phrase": "la casa",
                    "target_lang": "es",
                    "explanation": "Practice feminine noun with definite article"
                },
                {
                    "type": "fill_blank",
                    "step": 4,
                    "prompt": "Complete: '___ café' (a coffee)",
                    "options": ["Un", "Una"],
                    "correct_answer": "Un",
                    "explanation": "Choose the correct indefinite article for a masculine noun"
                },
                {
                    "type": "fill_blank",
                    "step": 4,
                    "prompt": "Complete: '___ casa' (the house)",
                    "options": ["El", "La"],
                    "correct_answer": "La",
                    "explanation": "Choose the correct definite article for a feminine noun"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "A pen, please.",
                    "blocks": ["Una", "pluma", "por", "favor"],
                    "correct_answer": "Una pluma, por favor",
                    "explanation": "Practice noun + article. 'Una' is used with feminine nouns — 'pluma' ends in -a, so it is feminine.",
                    "common_mistakes": [
                        {
                            "pattern": "un pluma",
                            "explanation": "Remember: 'pluma' is feminine, so use 'una' (not 'un'). 'Un' is for masculine nouns."
                        },
                        {
                            "pattern": "pluma por favor",
                            "explanation": "Good! But don't forget the article 'una' before 'pluma'. In Spanish, nouns usually need an article."
                        }
                    ]
                },
                {
                    "type": "mini_prompt",
                    "step": 6,
                    "prompt": "Estás en un café. Quieres pedir un café.",
                    "context": "You're in a café. You want to order a coffee.",
                    "task": "Order a coffee using the noun you learned.",
                    "target_lang": "es",
                    "explanation": "Use 'un café' to order a coffee. Remember: 'café' is masculine, so use 'un'."
                },
                {
                    "type": "match",
                    "step": 7,
                    "prompt": "Review: Match the nouns and their gender",
                    "pairs": [["café", "coffee (masculine)"], ["casa", "house (feminine)"], ["amigo", "friend (masculine)"], ["amiga", "friend (feminine)"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered the nouns and their genders.",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "Cultural Note",
                    "correct_answer": "Spanish Spelling: Ñ, Accents, and the Silent H",
                    "explanation": "Spanish has a few letters you won't find in English:\n\n**Ñ (eñe)** — makes an 'ny' sound, like in 'mañana' (tomorrow) or 'España' (Spain).\n\n**Written accents** (á, é, í, ó, ú) — mark which syllable to stress, and sometimes change meaning:\n• 'sí' (yes) vs 'si' (if)\n• 'tú' (you) vs 'tu' (your)\n• 'él' (he) vs 'el' (the)\n\n**The letter H** — always silent in Spanish. 'Hola' starts with the 'o' sound, and 'hasta' sounds like 'asta'.",
                    "sub_text": "Accents are required in written Spanish — missing them is an error.",
                    "cultural_note": True
                },
            ]
        },
        {
            "lesson_id": "A1.1.7",
            "title": "¿De dónde eres? (Countries & Nationalities)",
            "focus": "Asking about origin, countries, and nationalities",
            "vocabulary": [
                {"term": "¿De dónde eres?", "translation": "Where are you from? (Informal)"},
                {"term": "¿De dónde es?",    "translation": "Where are you from? (Formal)"},
                {"term": "Soy de",           "translation": "I'm from"},
                {"term": "España",           "translation": "Spain"},
                {"term": "español",          "translation": "Spanish (masculine)"},
                {"term": "española",         "translation": "Spanish (feminine)"},
                {"term": "Francia",          "translation": "France"},
                {"term": "francés",          "translation": "French (masculine)"},
                {"term": "francesa",         "translation": "French (feminine)"},
                {"term": "México",           "translation": "Mexico"},
                {"term": "mexicano",         "translation": "Mexican (masculine)"},
                {"term": "mexicana",         "translation": "Mexican (feminine)"},
                {"term": "Brasil",           "translation": "Brazil"},
                {"term": "brasileño",        "translation": "Brazilian (masculine)"},
                {"term": "brasileña",        "translation": "Brazilian (feminine)"},
                {"term": "Reino Unido",      "translation": "United Kingdom"},
                {"term": "inglés",           "translation": "English (masculine)"},
                {"term": "inglesa",          "translation": "English (feminine)"},
                {"term": "Estados Unidos",   "translation": "United States"},
                {"term": "estadounidense",   "translation": "American (US)"},
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "¿De dónde eres?",
                    "explanation": "Where are you from? (Informal — use with friends and peers)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_de_donde_eres_22.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Soy de",
                    "explanation": "I'm from (used with a country name)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_soy_de_23.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "España",
                    "explanation": "Spain",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_espana_24.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Francia",
                    "explanation": "France",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_francia_25.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "México",
                    "explanation": "Mexico",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_mexico_26.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Brasil",
                    "explanation": "Brazil",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_brasil_27.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Reino Unido",
                    "explanation": "United Kingdom",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_reino_unido_28.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Estados Unidos",
                    "explanation": "United States",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_estados_unidos_29.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Countries to English",
                    "pairs": [
                        ["España",         "Spain"],
                        ["Francia",        "France"],
                        ["México",         "Mexico"],
                        ["Brasil",         "Brazil"],
                        ["Reino Unido",    "United Kingdom"],
                        ["Estados Unidos", "United States"],
                    ],
                    "correct_answer": "match_all",
                    "explanation": "Match each Spanish country name with its English translation"
                },
                {
                    "type": "info_card",
                    "step": 3,
                    "prompt": "Cultural Note",
                    "correct_answer": "Alternative Names for Countries",
                    "explanation": "Some countries have multiple names or variations used in Spanish:\n\n**Reino Unido (United Kingdom):**\nThe UK contains four countries. You'll often hear people say:\n• Soy de Inglaterra (England)\n• Soy de Escocia (Scotland)\n• Soy de Gales (Wales)\n\nMany speakers say 'Soy de Inglaterra' rather than 'Soy de Reino Unido'.\n\n**Estados Unidos (United States):**\nCommonly shortened to:\n• EE.UU. (written abbreviation)\n• América (in casual speech)\n• Los Estados Unidos (with article)\n\nSo 'Soy de América', 'Soy de EE.UU.', and 'Soy de los Estados Unidos' are all correct.",
                    "sub_text": "Understanding these alternatives helps you sound more natural in Spanish.",
                    "cultural_note": True
                },
                {
                    "type": "reading_comprehension",
                    "step": 4,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Ana: ¿De dónde eres?\nPedro: Soy de México. ¿Y tú?\nAna: Soy de España.",
                    "question": "Where is Pedro from?",
                    "options": ["México", "España", "Francia", "Brasil"],
                    "correct_answer": "México",
                    "explanation": "Pedro says 'Soy de México' which means 'I'm from Mexico'.",
                    "highlight_vocab": ["¿De dónde eres?", "Soy de", "México", "España"]
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "I'm from Spain.",
                    "blocks": ["Soy", "de", "España"],
                    "correct_answer": "Soy de España.",
                    "explanation": "Practice saying where you're from: Soy + de + country"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "Where are you from? (Informal)",
                    "blocks": ["dónde", "¿De", "eres?"],
                    "correct_answer": "¿De dónde eres?",
                    "explanation": "Question word order: ¿De dónde + eres? Note the accent on 'dónde' — it is required in questions."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: ¿De dónde eres?",
                    "target_phrase": "¿De dónde eres?",
                    "target_lang": "es",
                    "explanation": "Practice asking where someone is from — note the accent on 'dónde'"
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Soy de España",
                    "target_phrase": "Soy de España",
                    "target_lang": "es",
                    "explanation": "Practice saying where you're from"
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: '___ dónde eres?' (Where are you from?)",
                    "options": ["De", "Di", "En"],
                    "correct_answer": "De",
                    "explanation": "Use 'De' when asking about origin"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Soy ___ México.' (I'm from Mexico)",
                    "options": ["de", "di", "en"],
                    "correct_answer": "de",
                    "explanation": "Use 'de' when saying where you're from"
                },
                {
                    "type": "form_fill",
                    "step": 11,
                    "prompt": "Fill out this registration form with your information.",
                    "form_fields": [
                        {
                            "label": "Nombre (Name)",
                            "type": "text",
                            "required": True,
                            "validation": "name",
                            "hint": "Use 'Me llamo [nombre]' or 'Soy [nombre]' format"
                        },
                        {
                            "label": "Nacionalidad (Nationality)",
                            "type": "select",
                            "options": ["español", "española", "francés", "francesa", "mexicano", "mexicana", "brasileño", "brasileña", "inglés", "inglesa", "estadounidense"],
                            "required": True
                        },
                        {
                            "label": "¿De dónde eres? (Where are you from?)",
                            "type": "text",
                            "required": True,
                            "validation": "origin",
                            "hint": "Use 'Soy de [país]' format"
                        }
                    ],
                    "correct_answer": "all_fields_filled",
                    "explanation": "Perfect! You filled out all the required information correctly."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks you: '¿De dónde eres?'",
                    "context": "Someone asks you: '¿De dónde eres?' (Where are you from?)",
                    "task": "Respond by saying where you're from.",
                    "target_lang": "es",
                    "explanation": "Use 'Soy de' followed by a country name. For example: 'Soy de España' or 'Soy de México'"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "Grammar: Gender Patterns in Spanish",
                    "correct_answer": "Nationality Adjectives",
                    "explanation": "In Spanish, ALL nationality adjectives change to match the speaker's gender. Look for these patterns:",
                    "tables": [
                        {
                            "title": "Masculine Forms",
                            "headers": ["Singular", "Translation"],
                            "rows": [
                                ["español",  "Spanish man"],
                                ["mexicano", "Mexican man"],
                                ["francés",  "French man"],
                                ["inglés",   "English man"],
                            ]
                        },
                        {
                            "title": "Feminine Forms",
                            "headers": ["Singular", "Translation"],
                            "rows": [
                                ["española", "Spanish woman"],
                                ["mexicana", "Mexican woman"],
                                ["francesa", "French woman"],
                                ["inglesa",  "English woman"],
                            ]
                        }
                    ],
                    "sub_text": "Unlike Italian, every Spanish nationality adjective has a distinct feminine form. Words ending in a consonant (francés, inglés) add -a for feminine and drop the written accent.",
                    "cultural_note": False
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "español",
                    "explanation": "Spanish (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_espanol_30.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "española",
                    "explanation": "Spanish (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_espanola_31.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "francés",
                    "explanation": "French (masculine) — accent on final syllable",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_frances_32.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "francesa",
                    "explanation": "French (feminine) — accent drops when -a is added",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_francesa_33.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "mexicano",
                    "explanation": "Mexican (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_mexicano_34.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "mexicana",
                    "explanation": "Mexican (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_mexicana_35.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "inglés",
                    "explanation": "English (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_ingles_36.mp3"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "inglesa",
                    "explanation": "English (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/es_inglesa_37.mp3"
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Match Nationalities to English",
                    "pairs": [
                        ["español",  "Spanish (masculine)"],
                        ["española", "Spanish (feminine)"],
                        ["francés",  "French (masculine)"],
                        ["francesa", "French (feminine)"],
                        ["mexicano", "Mexican (masculine)"],
                        ["mexicana", "Mexican (feminine)"],
                        ["inglés",   "English (masculine)"],
                        ["inglesa",  "English (feminine)"],
                    ],
                    "correct_answer": "match_all",
                    "explanation": "Match each Spanish nationality adjective with its English translation"
                },
                {
                    "type": "gender_categorize",
                    "step": 10,
                    "prompt": "Drag each word to the correct gender column: Masculino or Femenino",
                    "words": ["español", "española", "francés", "francesa", "mexicano", "mexicana", "inglés", "inglesa"],
                    "correct_answers": {
                        "español":  "masculino",
                        "española": "femenino",
                        "francés":  "masculino",
                        "francesa": "femenino",
                        "mexicano": "masculino",
                        "mexicana": "femenino",
                        "inglés":   "masculino",
                        "inglesa":  "femenino",
                    },
                    "correct_answer": "all_correct",
                    "explanation": "Perfect! You remembered the patterns:\n\n**Masculino (-o or consonant):** español, mexicano, francés, inglés\n**Femenino (-a):** española, mexicana, francesa, inglesa\n\nWords ending in a consonant like francés and inglés add -a for feminine and drop the written accent: francés → francesa, inglés → inglesa."
                },
                {
                    "type": "reading_comprehension",
                    "step": 12,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Carlos: ¿Qué nacionalidad tienes?\nMaría: Soy española. ¿Y tú?\nCarlos: Yo soy mexicano.",
                    "question": "What nationality is María?",
                    "options": ["española", "mexicana", "francesa", "inglesa"],
                    "correct_answer": "española",
                    "explanation": "María says 'Soy española' which means 'I am Spanish (feminine)'.",
                    "highlight_vocab": ["¿Qué nacionalidad tienes?", "Soy española", "mexicano"]
                },
                {
                    "type": "mini_prompt",
                    "step": 13,
                    "prompt": "Someone asks you: '¿Qué nacionalidad tienes?' (What nationality are you?)",
                    "context": "Someone asks you your nationality.",
                    "task": "Respond with your nationality.",
                    "target_lang": "es",
                    "explanation": "Use 'Soy' followed by the correct nationality adjective. Remember to choose masculine or feminine: 'Soy español' (male) or 'Soy española' (female), 'Soy francés/francesa', 'Soy inglés/inglesa', etc."
                },
                {
                    "type": "free_writing",
                    "step": 14,
                    "prompt": "Write a complete introduction about yourself.",
                    "context": "You're meeting someone new at a language exchange event.",
                    "task": "Write 2-3 sentences introducing yourself. Include: your name, where you're from, your greeting, and your nationality.",
                    "target_lang": "es",
                    "required_elements": ["name", "greeting", "origin", "nationality"],
                    "example_response": "¡Hola! Me llamo Ana. Soy de España y soy española.",
                    "validation_mode": "ai",
                    "explanation": "Excellent! You included your name, a greeting, where you're from, and your nationality. Perfect introduction!"
                },
                {
                    "type": "match",
                    "step": 15,
                    "prompt": "Review: Match all the greetings, introductions, and nationalities you've learned",
                    "pairs": [
                        ["Hola",            "Hi"],
                        ["Buenos días",     "Good morning"],
                        ["Me llamo",        "My name is"],
                        ["¿De dónde eres?", "Where are you from?"],
                        ["Soy de",          "I'm from"],
                        ["español",         "Spanish (masculine)"],
                        ["española",        "Spanish (feminine)"],
                        ["francés",         "French (masculine)"],
                        ["mexicano",        "Mexican (masculine)"],
                    ],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the key phrases and nationalities from this module.",
                    "review": True
                },
                {
                    "type": "mini_prompt",
                    "step": 16,
                    "prompt": "Challenge: Have a conversation introducing yourself and asking about the other person's nationality.",
                    "context": "You meet someone at a language exchange event.",
                    "task": "Use: greeting, introduction with name and origin, asking '¿De dónde eres?', asking about nationality, and responding with your nationality.",
                    "target_lang": "es",
                    "extension": True,
                    "optional": True,
                    "explanation": "Excellent! You used all the required elements including nationality in a natural conversation."
                }
            ]
        },
        {
            "lesson_id": "A1.1.BOSS",
            "title": "Conversation Practice: Meeting People — Informal & Formal",
            "type": "conversation_challenge",
            "focus": "Putting it all together: greetings, introductions, origin, and farewells",
            "vocabulary": [
                {"term": "Hola",          "translation": "Hi"},
                {"term": "Buenos días",   "translation": "Good morning"},
                {"term": "Buenas tardes", "translation": "Good afternoon"},
                {"term": "Adiós",         "translation": "Goodbye"},
                {"term": "¿Cómo estás?",  "translation": "How are you? (Informal)"},
                {"term": "¿Cómo está?",   "translation": "How are you? (Formal)"},
                {"term": "Gracias",       "translation": "Thank you"},
                {"term": "Hasta pronto",  "translation": "See you soon"},
                {"term": "Hasta mañana",  "translation": "See you tomorrow"},
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 0,
                    "prompt": "You meet your neighbour Señora García on the street.",
                    "scenario": "neighbor",
                    "ai_prompt": "You are Señora García, a friendly neighbour. Keep the conversation casual but polite. Use informal greetings.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Informal Conversation",
                            "round_description": "Have a casual conversation with your neighbour Señora García",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "¡Hola!",
                                    "user_requirement": "Respond with any greeting",
                                    "required_words": ["Hola", "Buenos días", "Buenas tardes", "Buenas"],
                                    "hints": ["Hola", "Buenos días"],
                                    "invalid_responses": ["¡Hola! ¿Cómo estás?", "¡Buenas! ¿Qué tal?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "¿Cómo estás?",
                                    "user_requirement": "Respond with how you are AND ask back",
                                    "required_words": ["Bien", "¿Y tú?"],
                                    "hints": ["Bien", "¿Y tú?"],
                                    "invalid_responses": ["¡Bien! ¿Y tú?", "Estoy bien. ¿Y tú?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "¡Bien, gracias! ¡Mucho gusto! ¿Cómo te llamas?",
                                    "user_requirement": "Introduce yourself",
                                    "required_words": ["Me llamo", "Soy"],
                                    "hints": ["Me llamo [nombre]", "Soy [nombre]"],
                                    "invalid_responses": ["¡Mucho gusto! Me llamo...", "Mi nombre es..."]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "¡Mucho gusto! ¡Hasta pronto!",
                                    "user_requirement": "Say goodbye politely",
                                    "required_words": ["Gracias", "Hasta pronto", "Adiós"],
                                    "hints": ["Gracias", "Hasta pronto", "Adiós"],
                                    "invalid_responses": ["¡Gracias! ¡Hasta pronto!", "¡Perfecto! ¡Adiós!"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Formal Conversation",
                            "round_description": "Have a formal conversation with Profesora Ramírez",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buenos días. ¿Cómo está?",
                                    "user_requirement": "Respond with a formal greeting and say how you are",
                                    "required_words": ["Buenos días", "bien", "gracias"],
                                    "hints": ["Buenos días, profesora", "Estoy bien, gracias", "¿Y usted?"],
                                    "invalid_responses": ["¡Hola!", "Buenos días. ¿Cómo estás?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Muy bien, gracias. ¿Cómo se llama?",
                                    "user_requirement": "Introduce yourself AND say nice to meet you",
                                    "required_words": ["Me llamo", "Mucho gusto"],
                                    "hints": ["Me llamo [nombre]", "Mucho gusto"],
                                    "invalid_responses": ["¡Bien! Me llamo... ¿Y tú?", "Mi nombre es...", "Me llamo... ¿Y tú?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Mucho gusto. ¿De dónde es?",
                                    "user_requirement": "Say where you are from",
                                    "required_words": ["Soy de"],
                                    "hints": ["Soy de [país]"],
                                    "invalid_responses": ["Soy de... ¿Y tú?", "Vengo de..."]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "¡Bienvenido a la clase! Hasta mañana.",
                                    "user_requirement": "Thank her AND say goodbye formally",
                                    "required_words": ["Gracias", "Hasta mañana"],
                                    "hints": ["Gracias", "Hasta mañana"],
                                    "invalid_responses": ["Gracias. ¡Adiós!", "Gracias. ¡Hasta luego!", "¡Ciao!"]
                                }
                            ]
                        }
                    ],
                    "explanation": "Complete both informal and formal greeting conversations using the Spanish you've learned in this module"
                }
            ]
        }
    ]
}
