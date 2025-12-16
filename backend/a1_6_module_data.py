"""
Module A1.6 data structure - Daily Routine & Time
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_6_LESSONS = {
    "module_id": "A1.6",
    "title": "Daily Routine & Time",
    "goal": "Describe daily routines, tell time, and schedule appointments using present tense and reflexive verbs.",
    "lessons": [
        {
            "lesson_id": "A1.6.0",
            "title": "Self-Assessment: Daily Routine & Time",
            "focus": "Assess your confidence with daily routines and time",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel talking about your daily routine?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can name the days of the week",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can tell time in Italian",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe what I do during the day",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can talk about my morning routine",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.6.1",
            "title": "Days & Parts of the Day",
            "focus": "Weekdays, Morning vs Evening",
            "vocabulary": [
                {"term": "lunedì", "translation": "Monday"},
                {"term": "martedì", "translation": "Tuesday"},
                {"term": "mercoledì", "translation": "Wednesday"},
                {"term": "giovedì", "translation": "Thursday"},
                {"term": "venerdì", "translation": "Friday"},
                {"term": "sabato", "translation": "Saturday"},
                {"term": "domenica", "translation": "Sunday"},
                {"term": "mattina", "translation": "morning"},
                {"term": "pomeriggio", "translation": "afternoon"},
                {"term": "sera", "translation": "evening"},
                {"term": "notte", "translation": "night"},
                {"term": "oggi", "translation": "today"},
                {"term": "domani", "translation": "tomorrow"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "lunedì",
                    "explanation": "Monday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_lunedi_131.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "martedì",
                    "explanation": "Tuesday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_martedi_132.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "mercoledì",
                    "explanation": "Wednesday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mercoledi_133.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "giovedì",
                    "explanation": "Thursday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_giovedi_134.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "venerdì",
                    "explanation": "Friday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_venerdi_135.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sabato",
                    "explanation": "Saturday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sabato_136.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "domenica",
                    "explanation": "Sunday",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_domenica_137.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Days of the Week",
                    "pairs": [["lunedì", "Monday"], ["martedì", "Tuesday"], ["mercoledì", "Wednesday"], ["giovedì", "Thursday"], ["venerdì", "Friday"], ["sabato", "Saturday"], ["domenica", "Sunday"]],
                    "correct_answer": "match_all",
                    "explanation": "Days of the week"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What day is it?",
                    "audio_text": "Oggi è lunedì.",
                    "options": ["Monday", "Tuesday", "Wednesday", "Thursday"],
                    "correct_answer": "Monday",
                    "explanation": "You heard 'lunedì' (Monday).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Today is Friday.",
                    "blocks": ["Oggi", "è", "venerdì"],
                    "correct_answer": "Oggi è venerdì.",
                    "explanation": "Use 'Oggi è' + day of the week."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Oggi è lunedì",
                    "target_phrase": "Oggi è lunedì",
                    "target_lang": "it",
                    "explanation": "Practice saying the day"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Domani è ___.' (Saturday)",
                    "options": ["sabato", "domenica", "lunedì", "venerdì"],
                    "correct_answer": "sabato",
                    "explanation": "Use 'sabato' for Saturday."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Che giorno è oggi?'",
                    "context": "Today is Wednesday.",
                    "task": "Tell them what day it is.",
                    "target_lang": "it",
                    "explanation": "Say 'Oggi è mercoledì.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match days and time",
                    "pairs": [["lunedì", "Monday"], ["mattina", "morning"], ["sera", "evening"], ["oggi", "today"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.2",
            "title": "Telling Time (The Basics)",
            "focus": "Asking time, 'Sono le...' vs 'È l'una'",
            "vocabulary": [
                {"term": "che ore sono", "translation": "what time is it"},
                {"term": "sono le", "translation": "it is (plural hours)"},
                {"term": "è l'una", "translation": "it is one o'clock"},
                {"term": "mezzogiorno", "translation": "noon"},
                {"term": "mezzanotte", "translation": "midnight"},
                {"term": "un quarto", "translation": "quarter"},
                {"term": "mezza", "translation": "half"},
                {"term": "orologio", "translation": "clock"},
                {"term": "tempo", "translation": "time"},
                {"term": "due", "translation": "two"},
                {"term": "tre", "translation": "three"},
                {"term": "quattro", "translation": "four"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Telling Time",
                    "correct_answer": "Sono le / È l'una",
                    "explanation": "Use 'Sono le' (it is) for hours 2-12.\nUse 'È l'una' (it is one) for 1 o'clock.\n\nExamples:\n- Sono le due (It's two o'clock)\n- È l'una (It's one o'clock)\n- Sono le tre e un quarto (It's quarter past three)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "che ore sono",
                    "explanation": "what time is it",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_che_ore_sono_138.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "sono le",
                    "explanation": "it is (plural hours)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sono_le_139.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "è l'una",
                    "explanation": "it is one o'clock",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_e_luna_140.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "mezzogiorno",
                    "explanation": "noon",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mezzogiorno_141.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Time Expressions",
                    "pairs": [["che ore sono", "what time is it"], ["sono le", "it is (plural)"], ["è l'una", "it is one"], ["mezzogiorno", "noon"]],
                    "correct_answer": "match_all",
                    "explanation": "Time vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What time is it?",
                    "audio_text": "Sono le tre.",
                    "options": ["one o'clock", "two o'clock", "three o'clock", "four o'clock"],
                    "correct_answer": "three o'clock",
                    "explanation": "You heard 'Sono le tre' (It's three o'clock).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "What time is it?",
                    "blocks": ["Che", "ore", "sono"],
                    "correct_answer": "Che ore sono?",
                    "explanation": "Use 'Che ore sono?' to ask the time."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "It's two o'clock.",
                    "blocks": ["Sono", "le", "due"],
                    "correct_answer": "Sono le due.",
                    "explanation": "Use 'Sono le' + number for hours 2-12."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Che ore sono?",
                    "target_phrase": "Che ore sono?",
                    "target_lang": "it",
                    "explanation": "Practice asking the time"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ l'una.' (It is)",
                    "options": ["Sono", "È", "Sono le", "Sono"],
                    "correct_answer": "È",
                    "explanation": "Use 'È l'una' for one o'clock (singular)."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ le tre.' (It is)",
                    "options": ["Sono", "È", "Sono le", "È le"],
                    "correct_answer": "Sono",
                    "explanation": "Use 'Sono le' for hours 2-12 (plural)."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Che ore sono?'",
                    "context": "It's four o'clock.",
                    "task": "Tell them the time.",
                    "target_lang": "it",
                    "explanation": "Say 'Sono le quattro.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match time expressions",
                    "pairs": [["che ore sono", "what time is it"], ["sono le", "it is (plural)"], ["è l'una", "it is one"], ["mezzogiorno", "noon"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.3",
            "title": "Daily Actions (Regular Verbs)",
            "focus": "Working, Eating, Sleeping (Non-reflexive)",
            "vocabulary": [
                {"term": "lavoro", "translation": "I work"},
                {"term": "mangio", "translation": "I eat"},
                {"term": "dormo", "translation": "I sleep"},
                {"term": "studio", "translation": "I study"},
                {"term": "pranzo", "translation": "I have lunch / lunch"},
                {"term": "cena", "translation": "dinner"},
                {"term": "colazione", "translation": "breakfast"},
                {"term": "solito", "translation": "usual"},
                {"term": "sempre", "translation": "always"},
                {"term": "mai", "translation": "never"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Present Tense (Regular Verbs)",
                    "correct_answer": "Present Simple",
                    "explanation": "Regular verbs in Italian end in -are, -ere, or -ire.\n\n-are verbs: lavoro (I work), mangiare → mangio (I eat)\n-ere verbs: vedere → vedo (I see)\n-ire verbs: dormire → dormo (I sleep), partire → parto (I leave)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "lavoro",
                    "explanation": "I work",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_lavoro_142.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "mangio",
                    "explanation": "I eat",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mangio_143.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dormo",
                    "explanation": "I sleep",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dormo_144.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "studio",
                    "explanation": "I study",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_studio_145.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Daily Actions",
                    "pairs": [["lavoro", "I work"], ["mangio", "I eat"], ["dormo", "I sleep"], ["studio", "I study"], ["pranzo", "I have lunch"]],
                    "correct_answer": "match_all",
                    "explanation": "Daily action verbs"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person do?",
                    "audio_text": "Lavoro sempre la mattina.",
                    "options": ["I always work in the morning", "I always eat in the morning", "I always sleep in the morning", "I always study in the morning"],
                    "correct_answer": "I always work in the morning",
                    "explanation": "You heard 'Lavoro sempre la mattina' (I always work in the morning).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I eat breakfast in the morning.",
                    "blocks": ["Faccio", "colazione", "la", "mattina"],
                    "correct_answer": "Faccio colazione la mattina.",
                    "explanation": "Use 'Faccio colazione' (I have breakfast) + time expression."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I always study in the afternoon.",
                    "blocks": ["Studio", "sempre", "il", "pomeriggio"],
                    "correct_answer": "Studio sempre il pomeriggio.",
                    "explanation": "Use verb + 'sempre' (always) + time expression."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Lavoro sempre la mattina",
                    "target_phrase": "Lavoro sempre la mattina",
                    "target_lang": "it",
                    "explanation": "Practice describing daily routines"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ sempre la sera.' (I sleep)",
                    "options": ["Lavoro", "Mangio", "Dormo", "Studio"],
                    "correct_answer": "Dormo",
                    "explanation": "Use 'Dormo' (I sleep) for sleeping."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Cosa fai la mattina?'",
                    "context": "You work in the morning.",
                    "task": "Tell them what you do.",
                    "target_lang": "it",
                    "explanation": "Say 'Lavoro la mattina.' or 'Lavoro sempre la mattina.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match daily actions",
                    "pairs": [["lavoro", "I work"], ["mangio", "I eat"], ["dormo", "I sleep"], ["sempre", "always"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.4",
            "title": "The Morning Routine (Reflexive Verbs)",
            "focus": "Getting ready, 'Mi' + Verb",
            "vocabulary": [
                {"term": "svegliarsi", "translation": "to wake up"},
                {"term": "mi sveglio", "translation": "I wake up"},
                {"term": "alzarsi", "translation": "to get up"},
                {"term": "mi alzo", "translation": "I get up"},
                {"term": "lavarsi", "translation": "to wash oneself"},
                {"term": "mi lavo", "translation": "I wash myself"},
                {"term": "vestirsi", "translation": "to get dressed"},
                {"term": "mi vesto", "translation": "I get dressed"},
                {"term": "presto", "translation": "early"},
                {"term": "tardi", "translation": "late"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Reflexive Verbs",
                    "correct_answer": "Mi + Verb",
                    "explanation": "Reflexive verbs use pronouns: mi (myself), ti (yourself), si (himself/herself).\n\nExamples:\n- Mi sveglio (I wake up)\n- Ti alzi (You get up)\n- Si lava (He/She washes)\n\nThe pronoun comes before the verb.",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi sveglio",
                    "explanation": "I wake up",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_sveglio_146.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi alzo",
                    "explanation": "I get up",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_alzo_147.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi lavo",
                    "explanation": "I wash myself",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_lavo_148.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi vesto",
                    "explanation": "I get dressed",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_vesto_149.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Reflexive Verbs",
                    "pairs": [["mi sveglio", "I wake up"], ["mi alzo", "I get up"], ["mi lavo", "I wash myself"], ["mi vesto", "I get dressed"]],
                    "correct_answer": "match_all",
                    "explanation": "Reflexive verb vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person do in the morning?",
                    "audio_text": "Mi sveglio presto la mattina.",
                    "options": ["I wake up early", "I get up early", "I wash early", "I get dressed early"],
                    "correct_answer": "I wake up early",
                    "explanation": "You heard 'Mi sveglio presto' (I wake up early).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I get up early in the morning.",
                    "blocks": ["Mi", "alzo", "presto", "la", "mattina"],
                    "correct_answer": "Mi alzo presto la mattina.",
                    "explanation": "Use 'Mi' + verb + time expression.",
                    "common_mistakes": [
                        {
                            "pattern": "Alzo",
                            "explanation": "Use 'Mi alzo' (reflexive) not 'Alzo' (non-reflexive) for getting up."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi sveglio presto",
                    "target_phrase": "Mi sveglio presto",
                    "target_lang": "it",
                    "explanation": "Practice reflexive verbs"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ presto la mattina.' (I wake up)",
                    "options": ["Sveglio", "Mi sveglio", "Sveglio mi", "Sveglio me"],
                    "correct_answer": "Mi sveglio",
                    "explanation": "Use 'Mi sveglio' (reflexive) - the pronoun comes before the verb."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ tardi.' (I get dressed)",
                    "options": ["Vesto", "Mi vesto", "Vesto mi", "Vesto me"],
                    "correct_answer": "Mi vesto",
                    "explanation": "Use 'Mi vesto' (reflexive) for getting dressed."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Cosa fai la mattina?'",
                    "context": "You wake up and wash yourself in the morning.",
                    "task": "Describe your morning routine using reflexive verbs.",
                    "target_lang": "it",
                    "explanation": "Say 'Mi sveglio e mi lavo la mattina.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match reflexive verbs",
                    "pairs": [["mi sveglio", "I wake up"], ["mi alzo", "I get up"], ["mi lavo", "I wash myself"], ["mi vesto", "I get dressed"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.5",
            "title": "Scheduling & Prepositions",
            "focus": "'At' (Alle) vs 'On' (Il/Di)",
            "vocabulary": [
                {"term": "alle", "translation": "at (time)"},
                {"term": "di", "translation": "on (day) / of"},
                {"term": "il", "translation": "on (day) / the"},
                {"term": "quando", "translation": "when"},
                {"term": "aperto", "translation": "open"},
                {"term": "chiuso", "translation": "closed"},
                {"term": "inizio", "translation": "I start"},
                {"term": "finisco", "translation": "I finish"},
                {"term": "appuntamento", "translation": "appointment"},
                {"term": "orario", "translation": "schedule"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Prepositions of Time",
                    "correct_answer": "Alle / Il / Di",
                    "explanation": "Use 'alle' (at) for specific times.\nUse 'il' or 'di' (on) for days.\n\nExamples:\n- Alle otto (at eight o'clock)\n- Il lunedì (on Monday)\n- Di mattina (in the morning)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "alle",
                    "explanation": "at (time)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_alle_150.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quando",
                    "explanation": "when",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quando_151.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "appuntamento",
                    "explanation": "appointment",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_appuntamento_152.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Scheduling Terms",
                    "pairs": [["alle", "at (time)"], ["quando", "when"], ["appuntamento", "appointment"], ["aperto", "open"], ["chiuso", "closed"]],
                    "correct_answer": "match_all",
                    "explanation": "Scheduling vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. When does the person work?",
                    "audio_text": "Lavoro alle otto.",
                    "options": ["at eight o'clock", "at nine o'clock", "on Monday", "in the morning"],
                    "correct_answer": "at eight o'clock",
                    "explanation": "You heard 'alle otto' (at eight o'clock).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I start work at nine o'clock.",
                    "blocks": ["Inizio", "a", "lavorare", "alle", "nove"],
                    "correct_answer": "Inizio a lavorare alle nove.",
                    "explanation": "Use 'Inizio' + 'a' + verb + 'alle' + time."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I have an appointment on Monday.",
                    "blocks": ["Ho", "un", "appuntamento", "il", "lunedì"],
                    "correct_answer": "Ho un appuntamento il lunedì.",
                    "explanation": "Use 'il' or 'di' + day for appointments."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ho un appuntamento alle tre",
                    "target_phrase": "Ho un appuntamento alle tre",
                    "target_lang": "it",
                    "explanation": "Practice scheduling"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Lavoro ___ otto.' (at)",
                    "options": ["alle", "il", "di", "a"],
                    "correct_answer": "alle",
                    "explanation": "Use 'alle' (at) for specific times."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ho un appuntamento ___ martedì.' (on)",
                    "options": ["alle", "il", "di", "a"],
                    "correct_answer": "il",
                    "explanation": "Use 'il' (on) for days."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You need to schedule a dentist appointment.",
                    "context": "You want it on Tuesday at three o'clock.",
                    "task": "Say when you want the appointment.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei un appuntamento il martedì alle tre.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match scheduling vocabulary",
                    "pairs": [["alle", "at (time)"], ["quando", "when"], ["appuntamento", "appointment"], ["aperto", "open"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.6",
            "title": "Frequency & Habits",
            "focus": "How often? (Spesso, A volte)",
            "vocabulary": [
                {"term": "spesso", "translation": "often"},
                {"term": "a volte", "translation": "sometimes"},
                {"term": "raramente", "translation": "rarely"},
                {"term": "ogni", "translation": "every"},
                {"term": "giorno", "translation": "day"},
                {"term": "settimana", "translation": "week"},
                {"term": "faccio", "translation": "I do"},
                {"term": "vado", "translation": "I go"},
                {"term": "palestra", "translation": "gym"},
                {"term": "casa", "translation": "home"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "spesso",
                    "explanation": "often",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_spesso_153.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "a volte",
                    "explanation": "sometimes",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_a_volte_154.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "raramente",
                    "explanation": "rarely",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_raramente_155.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ogni",
                    "explanation": "every",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ogni_156.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "faccio",
                    "explanation": "I do",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_faccio_157.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Frequency Adverbs",
                    "pairs": [["spesso", "often"], ["a volte", "sometimes"], ["raramente", "rarely"], ["ogni", "every"]],
                    "correct_answer": "match_all",
                    "explanation": "Frequency vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How often does the person go to the gym?",
                    "audio_text": "Vado in palestra spesso.",
                    "options": ["often", "sometimes", "rarely", "never"],
                    "correct_answer": "often",
                    "explanation": "You heard 'spesso' (often).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I go to the gym every day.",
                    "blocks": ["Vado", "in", "palestra", "ogni", "giorno"],
                    "correct_answer": "Vado in palestra ogni giorno.",
                    "explanation": "Use 'Vado' + 'in' + place + 'ogni' + time period."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I sometimes study at home.",
                    "blocks": ["Studio", "a", "volte", "a", "casa"],
                    "correct_answer": "Studio a volte a casa.",
                    "explanation": "Use 'a volte' (sometimes) + verb + place."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vado in palestra spesso",
                    "target_phrase": "Vado in palestra spesso",
                    "target_lang": "it",
                    "explanation": "Practice talking about frequency"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado in palestra ___.' (often)",
                    "options": ["spesso", "a volte", "raramente", "ogni"],
                    "correct_answer": "spesso",
                    "explanation": "Use 'spesso' (often) to express frequency."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Quanto spesso vai in palestra?'",
                    "context": "You go to the gym sometimes.",
                    "task": "Tell them how often you go.",
                    "target_lang": "it",
                    "explanation": "Say 'Vado in palestra a volte.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match frequency vocabulary",
                    "pairs": [["spesso", "often"], ["a volte", "sometimes"], ["ogni", "every"], ["giorno", "day"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "The 24-Hour Clock System in Italy",
                    "table": {
                        "headers": ["24-Hour Time", "12-Hour Time", "Italian Pronunciation", "Context"],
                        "rows": [
                            ["13:00", "1:00 PM", "tredici", "Train/bus schedules"],
                            ["15:30", "3:30 PM", "quindici e trenta", "Museum hours"],
                            ["20:00", "8:00 PM", "venti", "TV programs"],
                            ["23:45", "11:45 PM", "ventitrè e quarantacinque", "Late evening"],
                            ["09:00", "9:00 AM", "nove", "Morning openings"],
                            ["19:00", "7:00 PM", "diciannove", "Evening closings"]
                        ]
                    },
                    "explanation": "Italians use the 24-hour clock for official times (schedules, appointments, TV programs). Tip: Subtract 12 from any number over 12 to convert to AM/PM time!\n\nIn conversation: Italians may use 12-hour format informally ('alle due' for 2 PM) but will clarify with 'del pomeriggio' (in the afternoon) or 'di sera' (in the evening).",
                    "sub_text": "Understanding the 24-hour clock prevents missed trains and appointments.",
                    "cultural_note": True
                },
                {
                    "type": "info_card",
                    "step": 10,
                    "prompt": "Cultural Note",
                    "correct_answer": "Riposo Culture - The Sacred Afternoon Break",
                    "explanation": "The 'riposo' (afternoon rest) is a cherished Italian tradition that shapes daily life:\n\n**What is Riposo?**\n• A 2-4 hour break in the afternoon (typically 1-4 PM or 2-5 PM)\n• Shops, offices, and businesses close for lunch and rest\n• People go home to eat pranzo (main meal), rest, and avoid the hottest part of the day\n• Families reunite for lunch - it's social time, not just eating\n\n**Where & When:**\n• More common in Southern Italy and small towns\n• Less common in big cities like Milan (more 'orario continuato' - continuous hours)\n• Especially strong in summer months when afternoon heat is intense\n• Banks, government offices, and many shops participate\n\n**What stays open:**\n• Restaurants (until 2:30-3 PM for lunch service)\n• Tourist areas and major chain stores\n• Bars (but may have limited service)\n\n**Evening reopening:**\n• Shops reopen around 4-5 PM and stay open until 7:30-8 PM\n• This creates the 'passeggiata' culture - evening strolls when shops are open and streets are lively\n\nTip: Plan your shopping and errands for morning or late afternoon. Use riposo time to rest, have a leisurely lunch, or visit attractions that stay open!",
                    "sub_text": "Respecting riposo helps you adapt to the Italian rhythm of life.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.6.BOSS",
            "title": "Boss Fight: The Appointment",
            "type": "conversation_challenge",
            "focus": "Managing a schedule - booking an appointment and discussing plans",
            "vocabulary": [
                {"term": "appuntamento", "translation": "appointment"},
                {"term": "martedì", "translation": "Tuesday"},
                {"term": "sabato", "translation": "Saturday"},
                {"term": "quando", "translation": "when"},
                {"term": "alle", "translation": "at (time)"},
                {"term": "faccio", "translation": "I do"},
                {"term": "vado", "translation": "I go"},
                {"term": "casa", "translation": "home"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You need to manage your schedule: book a dentist appointment and discuss weekend plans.",
                    "scenario": "appointment_booking",
                    "ai_prompt": "You are a formal secretary booking an appointment, then a friend discussing weekend plans.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Booking Appointment",
                            "round_description": "The secretary helps you book a dentist appointment.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Come posso aiutarla?",
                                    "user_requirement": "Greet formally and ask for an appointment.",
                                    "required_words": ["Buongiorno", "appuntamento", "vorrei"],
                                    "hints": ["Buongiorno", "Vorrei un appuntamento", "Vorrei prenotare un appuntamento"],
                                    "invalid_responses": ["Ciao!", "Appuntamento", "I want appointment"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Certamente! Per quando?",
                                    "user_requirement": "Request an appointment for Tuesday.",
                                    "required_words": ["martedì", "il", "per"],
                                    "hints": ["Per martedì", "Il martedì", "Martedì"],
                                    "invalid_responses": ["Tuesday", "Martedì quando", "On Tuesday"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene. A che ora?",
                                    "user_requirement": "Specify a time using 'alle'.",
                                    "required_words": ["alle", "tre", "due", "quattro"],
                                    "hints": ["Alle tre", "Alle due", "Alle quattro"],
                                    "invalid_responses": ["At three", "Three", "3"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! L'appuntamento è confermato per martedì alle tre.",
                                    "user_requirement": "Thank them politely.",
                                    "required_words": ["Grazie", "grazie"],
                                    "hints": ["Grazie", "Grazie mille"],
                                    "invalid_responses": ["Thanks", "Thank you", "OK"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Weekend Plans",
                            "round_description": "Your friend asks about your plans for Saturday.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Cosa fai sabato?",
                                    "user_requirement": "Say what you're doing on Saturday.",
                                    "required_words": ["sabato", "faccio", "vado"],
                                    "hints": ["Sabato faccio", "Sabato vado", "Il sabato"],
                                    "invalid_responses": ["Saturday", "I do", "I go"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Interessante! A che ora?",
                                    "user_requirement": "Tell them what time using 'alle'.",
                                    "required_words": ["alle", "due", "tre", "quattro"],
                                    "hints": ["Alle due", "Alle tre"],
                                    "invalid_responses": ["At two", "Two", "2"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene! E la sera?",
                                    "user_requirement": "Say what you do in the evening.",
                                    "required_words": ["sera", "faccio", "vado", "casa"],
                                    "hints": ["La sera vado", "La sera faccio", "Sto a casa"],
                                    "invalid_responses": ["Evening", "I stay", "Home"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! Allora ci sentiamo sabato!",
                                    "user_requirement": "Agree and say goodbye informally.",
                                    "required_words": ["Sì", "Ciao", "A presto"],
                                    "hints": ["Sì, ciao", "A presto", "Ciao"],
                                    "invalid_responses": ["Yes bye", "Bye", "See you"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
