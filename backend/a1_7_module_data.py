"""
Module A1.7 data structure - Places in Town & Directions
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_7_LESSONS = {
    "module_id": "A1.7",
    "title": "Places in Town & Directions",
    "goal": "Navigate a city, ask for directions, and give simple directions using the verb 'Andare' and imperative commands.",
    "lessons": [
        {
            "lesson_id": "A1.7.0",
            "title": "Self-Assessment: Places in Town & Directions",
            "focus": "Assess your confidence with places and directions",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel navigating a city and asking for directions?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can name common places in a city",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask where something is located",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can understand simple directions",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can give simple directions to someone",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.7.1",
            "title": "Essential Places (In vs. A)",
            "focus": "Common buildings and the 'In' vs 'A' rule",
            "vocabulary": [
                {"term": "banca", "translation": "bank"},
                {"term": "farmacia", "translation": "pharmacy"},
                {"term": "centro", "translation": "center"},
                {"term": "piazza", "translation": "square"},
                {"term": "ufficio", "translation": "office"},
                {"term": "vado", "translation": "I go"},
                {"term": "in", "translation": "in/to (with places)"},
                {"term": "a", "translation": "to/at"},
                {"term": "posta", "translation": "post office"},
                {"term": "ospedale", "translation": "hospital"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Prepositions 'In' vs 'A'",
                    "correct_answer": "In vs A",
                    "explanation": "Use 'in' for enclosed places (banca, farmacia, posta).\nUse 'a' for open places or cities (piazza, centro, Roma).\n\nExamples:\n- Vado in banca (I go to the bank)\n- Vado a Roma (I go to Rome)\n- Vado in farmacia (I go to the pharmacy)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "banca",
                    "explanation": "bank",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_banca_158.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "farmacia",
                    "explanation": "pharmacy",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_farmacia_159.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "posta",
                    "explanation": "post office",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_posta_160.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ospedale",
                    "explanation": "hospital",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ospedale_161.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Places",
                    "pairs": [["banca", "bank"], ["farmacia", "pharmacy"], ["posta", "post office"], ["ospedale", "hospital"], ["piazza", "square"]],
                    "correct_answer": "match_all",
                    "explanation": "Essential places vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Where is the person going?",
                    "audio_text": "Vado in banca.",
                    "options": ["bank", "pharmacy", "post office", "hospital"],
                    "correct_answer": "bank",
                    "explanation": "You heard 'in banca' (to the bank).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I go to the pharmacy.",
                    "blocks": ["Vado", "in", "farmacia"],
                    "correct_answer": "Vado in farmacia.",
                    "explanation": "Use 'Vado in' + place (for enclosed places like farmacia)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vado in banca",
                    "target_phrase": "Vado in banca",
                    "target_lang": "it",
                    "explanation": "Practice saying where you go"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ banca.' (to the)",
                    "options": ["in", "a", "al", "alla"],
                    "correct_answer": "in",
                    "explanation": "Use 'in' for enclosed places like 'banca'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ centro.' (to the)",
                    "options": ["in", "a", "al", "alla"],
                    "correct_answer": "a",
                    "explanation": "Use 'a' for open places like 'centro'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove vai?'",
                    "context": "You're going to the post office.",
                    "task": "Tell them where you're going.",
                    "target_lang": "it",
                    "explanation": "Say 'Vado in posta.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match places and prepositions",
                    "pairs": [["banca", "bank"], ["farmacia", "pharmacy"], ["in", "in/to"], ["vado", "I go"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.2",
            "title": "Leisure Places (Articulated Prepositions)",
            "focus": "Places taking 'Al/Alla' (To the)",
            "vocabulary": [
                {"term": "cinema", "translation": "cinema"},
                {"term": "ristorante", "translation": "restaurant"},
                {"term": "supermercato", "translation": "supermarket"},
                {"term": "stazione", "translation": "station"},
                {"term": "bar", "translation": "bar/café"},
                {"term": "al", "translation": "to the (masculine)"},
                {"term": "alla", "translation": "to the (feminine)"},
                {"term": "andiamo", "translation": "we go"},
                {"term": "parco", "translation": "park"},
                {"term": "museo", "translation": "museum"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Articulated Prepositions",
                    "correct_answer": "Al / Alla",
                    "explanation": "'Al' = 'a' + 'il' (to the - masculine)\n'Alla' = 'a' + 'la' (to the - feminine)\n\nExamples:\n- Vado al cinema (I go to the cinema)\n- Vado alla stazione (I go to the station)\n- Andiamo al ristorante (We go to the restaurant)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cinema",
                    "explanation": "cinema",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cinema_162.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ristorante",
                    "explanation": "restaurant",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ristorante_97.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "supermercato",
                    "explanation": "supermarket",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_supermercato_163.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "stazione",
                    "explanation": "station",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_stazione_164.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Leisure Places",
                    "pairs": [["cinema", "cinema"], ["ristorante", "restaurant"], ["supermercato", "supermarket"], ["stazione", "station"], ["parco", "park"]],
                    "correct_answer": "match_all",
                    "explanation": "Leisure places vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Where are they going?",
                    "audio_text": "Andiamo al cinema.",
                    "options": ["cinema", "restaurant", "supermarket", "station"],
                    "correct_answer": "cinema",
                    "explanation": "You heard 'al cinema' (to the cinema).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "We go to the restaurant.",
                    "blocks": ["Andiamo", "al", "ristorante"],
                    "correct_answer": "Andiamo al ristorante.",
                    "explanation": "Use 'Andiamo' (we go) + 'al' (to the - masculine) + place."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Andiamo al cinema",
                    "target_phrase": "Andiamo al cinema",
                    "target_lang": "it",
                    "explanation": "Practice saying where you go together"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ cinema.' (to the - masculine)",
                    "options": ["in", "a", "al", "alla"],
                    "correct_answer": "al",
                    "explanation": "Use 'al' (to the - masculine) with masculine places like 'cinema'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ stazione.' (to the - feminine)",
                    "options": ["in", "a", "al", "alla"],
                    "correct_answer": "alla",
                    "explanation": "Use 'alla' (to the - feminine) with feminine places like 'stazione'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Dove andiamo?'",
                    "context": "You want to go to the cinema.",
                    "task": "Suggest going to the cinema.",
                    "target_lang": "it",
                    "explanation": "Say 'Andiamo al cinema.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match leisure places",
                    "pairs": [["cinema", "cinema"], ["ristorante", "restaurant"], ["al", "to the (masc)"], ["alla", "to the (fem)"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.3",
            "title": "The Verb 'Andare' (Irregular)",
            "focus": "Conjugating To Go (Vado, Vai, Va)",
            "vocabulary": [
                {"term": "andare", "translation": "to go"},
                {"term": "vado", "translation": "I go"},
                {"term": "vai", "translation": "you go"},
                {"term": "va", "translation": "he/she goes"},
                {"term": "andiamo", "translation": "we go"},
                {"term": "vanno", "translation": "they go"},
                {"term": "dove", "translation": "where"},
                {"term": "piedi", "translation": "on foot"},
                {"term": "macchina", "translation": "car"},
                {"term": "autobus", "translation": "bus"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: The Verb 'Andare' (To Go)",
                    "correct_answer": "Irregular Verb",
                    "explanation": "'Andare' is irregular. Here are the present tense forms:\n\nIo vado (I go)\nTu vai (You go)\nLui/Lei va (He/She goes)\nNoi andiamo (We go)\nVoi andate (You all go)\nLoro vanno (They go)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "vado",
                    "explanation": "I go",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vado_165.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "vai",
                    "explanation": "you go",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vai_166.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "va",
                    "explanation": "he/she goes",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_va_167.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "andiamo",
                    "explanation": "we go",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_andiamo_168.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Verb Forms",
                    "pairs": [["vado", "I go"], ["vai", "you go"], ["va", "he/she goes"], ["andiamo", "we go"], ["vanno", "they go"]],
                    "correct_answer": "match_all",
                    "explanation": "Verb 'Andare' conjugation"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person say?",
                    "audio_text": "Dove vai?",
                    "options": ["Where are you going?", "Where am I going?", "Where is he going?", "Where are we going?"],
                    "correct_answer": "Where are you going?",
                    "explanation": "You heard 'Dove vai?' (Where are you going? - informal).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Where are you going?",
                    "blocks": ["Dove", "vai"],
                    "correct_answer": "Dove vai?",
                    "explanation": "Use 'Dove' (where) + 'vai' (you go)."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I go by car.",
                    "blocks": ["Vado", "in", "macchina"],
                    "correct_answer": "Vado in macchina.",
                    "explanation": "Use 'Vado' + 'in' + means of transport."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Dove vai?",
                    "target_phrase": "Dove vai?",
                    "target_lang": "it",
                    "explanation": "Practice asking where someone is going"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ in macchina.' (I go)",
                    "options": ["Vado", "Vai", "Va", "Andiamo"],
                    "correct_answer": "Vado",
                    "explanation": "Use 'Vado' (I go) for first person singular."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Dove ___?' (you go)",
                    "options": ["vado", "vai", "va", "andiamo"],
                    "correct_answer": "vai",
                    "explanation": "Use 'vai' (you go) for second person singular."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Come vai al cinema?'",
                    "context": "You're going by bus.",
                    "task": "Tell them how you're going.",
                    "target_lang": "it",
                    "explanation": "Say 'Vado in autobus.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match verb forms",
                    "pairs": [["vado", "I go"], ["vai", "you go"], ["va", "he/she goes"], ["dove", "where"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.4",
            "title": "Asking 'Where is...?'",
            "focus": "Polite interruption (Scusi) and finding things",
            "vocabulary": [
                {"term": "scusi", "translation": "excuse me (formal)"},
                {"term": "scusa", "translation": "excuse me (informal)"},
                {"term": "dov'è", "translation": "where is"},
                {"term": "cerco", "translation": "I'm looking for"},
                {"term": "vicino", "translation": "near"},
                {"term": "lontano", "translation": "far"},
                {"term": "qui", "translation": "here"},
                {"term": "lì", "translation": "there"},
                {"term": "per", "translation": "for/to"},
                {"term": "arrivare", "translation": "to arrive"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "scusi",
                    "explanation": "excuse me (formal)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_scusi_169.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "scusa",
                    "explanation": "excuse me (informal)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_scusa_170.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "dov'è",
                    "explanation": "where is",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dove_171.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "cerco",
                    "explanation": "I'm looking for",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cerco_172.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "vicino",
                    "explanation": "near",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vicino_173.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Direction Questions",
                    "pairs": [["scusi", "excuse me (formal)"], ["scusa", "excuse me (informal)"], ["dov'è", "where is"], ["cerco", "I'm looking for"], ["vicino", "near"]],
                    "correct_answer": "match_all",
                    "explanation": "Asking for directions vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What is the person asking?",
                    "audio_text": "Scusi, dov'è la stazione?",
                    "options": ["Where is the station?", "Where is the bank?", "Where is the pharmacy?", "Where is the post office?"],
                    "correct_answer": "Where is the station?",
                    "explanation": "You heard 'dov'è la stazione' (where is the station).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Excuse me, where is the bank?",
                    "blocks": ["Scusi", "dov'è", "la", "banca"],
                    "correct_answer": "Scusi, dov'è la banca?",
                    "explanation": "Use 'Scusi' (excuse me - formal) + 'dov'è' (where is) + article + place."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Scusi, dov'è la stazione?",
                    "target_phrase": "Scusi, dov'è la stazione?",
                    "target_lang": "it",
                    "explanation": "Practice asking for directions politely"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___, dov'è la farmacia?' (Excuse me - formal)",
                    "options": ["Scusi", "Scusa", "Scuse", "Scusate"],
                    "correct_answer": "Scusi",
                    "explanation": "Use 'Scusi' (excuse me - formal) when asking strangers."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Cerco la banca. È ___?' (near)",
                    "options": ["vicino", "lontano", "qui", "lì"],
                    "correct_answer": "vicino",
                    "explanation": "Use 'vicino' (near) to ask if something is close."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're lost. You need to find the station.",
                    "context": "You see a stranger on the street.",
                    "task": "Ask them politely where the station is.",
                    "target_lang": "it",
                    "explanation": "Say 'Scusi, dov'è la stazione?'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match direction questions",
                    "pairs": [["scusi", "excuse me (formal)"], ["dov'è", "where is"], ["cerco", "I'm looking for"], ["vicino", "near"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.5",
            "title": "Simple Directions (Imperative)",
            "focus": "Commands (Go, Turn, Stop)",
            "vocabulary": [
                {"term": "gira", "translation": "turn"},
                {"term": "destra", "translation": "right"},
                {"term": "sinistra", "translation": "left"},
                {"term": "vai", "translation": "go"},
                {"term": "dritto", "translation": "straight"},
                {"term": "sempre", "translation": "always"},
                {"term": "fermata", "translation": "stop"},
                {"term": "incrocio", "translation": "intersection"},
                {"term": "semaforo", "translation": "traffic light"},
                {"term": "poi", "translation": "then"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: The Imperative (Commands)",
                    "correct_answer": "Imperative Form",
                    "explanation": "Use the imperative to give directions:\n\nVai (Go - informal)\nGira (Turn - informal)\n\nExamples:\n- Vai dritto (Go straight)\n- Gira a destra (Turn right)\n- Gira a sinistra (Turn left)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "gira",
                    "explanation": "turn",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_gira_174.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "destra",
                    "explanation": "right",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_destra_175.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sinistra",
                    "explanation": "left",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sinistra_176.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dritto",
                    "explanation": "straight",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dritto_177.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Directions",
                    "pairs": [["gira", "turn"], ["destra", "right"], ["sinistra", "left"], ["vai", "go"], ["dritto", "straight"]],
                    "correct_answer": "match_all",
                    "explanation": "Direction vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What direction is given?",
                    "audio_text": "Vai dritto, poi gira a destra.",
                    "options": ["Go straight, then turn right", "Go straight, then turn left", "Turn right, then go straight", "Turn left, then go straight"],
                    "correct_answer": "Go straight, then turn right",
                    "explanation": "You heard 'Vai dritto, poi gira a destra' (Go straight, then turn right).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Go straight, then turn left.",
                    "blocks": ["Vai", "dritto", "poi", "gira", "a", "sinistra"],
                    "correct_answer": "Vai dritto, poi gira a sinistra.",
                    "explanation": "Use 'Vai' (go) + direction + 'poi' (then) + 'gira' (turn) + 'a' + direction.",
                    "common_mistakes": [
                        {
                            "pattern": "Vai a destra",
                            "explanation": "Use 'Vai dritto' (go straight) not 'Vai a destra' (go to the right)."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vai dritto, poi gira a destra",
                    "target_phrase": "Vai dritto, poi gira a destra",
                    "target_lang": "it",
                    "explanation": "Practice giving directions"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ a destra.' (Turn)",
                    "options": ["Vai", "Gira", "Va", "Andiamo"],
                    "correct_answer": "Gira",
                    "explanation": "Use 'Gira' (turn) for changing direction."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ dritto.' (Go)",
                    "options": ["Vai", "Gira", "Va", "Andiamo"],
                    "correct_answer": "Vai",
                    "explanation": "Use 'Vai' (go) for moving forward."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Come arrivo alla stazione?'",
                    "context": "You know the way: go straight, then turn right.",
                    "task": "Give them simple directions.",
                    "target_lang": "it",
                    "explanation": "Say 'Vai dritto, poi gira a destra.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match directions",
                    "pairs": [["gira", "turn"], ["destra", "right"], ["sinistra", "left"], ["dritto", "straight"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.6",
            "title": "Spatial Locators (Street Level)",
            "focus": "'Next to', 'Opposite', 'Between' applied to buildings",
            "vocabulary": [
                {"term": "accanto a", "translation": "next to"},
                {"term": "di fronte a", "translation": "opposite"},
                {"term": "tra", "translation": "between"},
                {"term": "angolo", "translation": "corner"},
                {"term": "pizzeria", "translation": "pizzeria"},
                {"term": "chiesa", "translation": "church"},
                {"term": "scuola", "translation": "school"},
                {"term": "dietro", "translation": "behind"},
                {"term": "davanti", "translation": "in front of"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "accanto a",
                    "explanation": "next to",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_accanto_a_178.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "di fronte a",
                    "explanation": "opposite",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_di_fronte_a_179.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "tra",
                    "explanation": "between",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tra_180.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "angolo",
                    "explanation": "corner",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_angolo_181.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pizzeria",
                    "explanation": "pizzeria",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pizzeria_182.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Spatial Prepositions",
                    "pairs": [["accanto a", "next to"], ["di fronte a", "opposite"], ["tra", "between"], ["angolo", "corner"], ["dietro", "behind"]],
                    "correct_answer": "match_all",
                    "explanation": "Spatial locators vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Where is the pizzeria?",
                    "audio_text": "La pizzeria è accanto alla chiesa.",
                    "options": ["next to the church", "opposite the church", "behind the church", "in front of the church"],
                    "correct_answer": "next to the church",
                    "explanation": "You heard 'accanto alla chiesa' (next to the church).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The school is opposite the church.",
                    "blocks": ["La", "scuola", "è", "di", "fronte", "alla", "chiesa"],
                    "correct_answer": "La scuola è di fronte alla chiesa.",
                    "explanation": "Use 'è di fronte a' (is opposite) + article + place."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: La pizzeria è accanto alla chiesa",
                    "target_phrase": "La pizzeria è accanto alla chiesa",
                    "target_lang": "it",
                    "explanation": "Practice describing locations"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La banca è ___ alla farmacia.' (next to)",
                    "options": ["accanto", "di fronte", "tra", "dietro"],
                    "correct_answer": "accanto",
                    "explanation": "Use 'accanto a' (next to) to describe proximity."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La scuola è ___ alla chiesa.' (opposite)",
                    "options": ["accanto", "di fronte", "tra", "dietro"],
                    "correct_answer": "di fronte",
                    "explanation": "Use 'di fronte a' (opposite) to describe facing position."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dov'è la pizzeria?'",
                    "context": "The pizzeria is next to the church.",
                    "task": "Tell them where it is.",
                    "target_lang": "it",
                    "explanation": "Say 'La pizzeria è accanto alla chiesa.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match spatial locators",
                    "pairs": [["accanto a", "next to"], ["di fronte a", "opposite"], ["tra", "between"], ["angolo", "corner"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Il Centro - More Than Just 'Downtown'",
                    "explanation": "'Il centro' in Italian means more than just the city center - it's the heart of Italian urban life:\n\n**What 'Centro' means:**\n• The historic old town (centro storico) with medieval/Renaissance architecture\n• Usually pedestrian-friendly with narrow streets\n• Where locals go to socialize, shop, and stroll\n• The cultural and social hub, not just a tourist area\n\n**Why it's important:**\n• 'Vado al centro' (I'm going to the center) = going out to socialize, meet friends, window shop\n• Different from American 'downtown' which might be just business district\n• Centro is where the passeggiata (evening stroll) happens\n• Contains the main piazza, duomo (cathedral), shops, and cafés\n\n**ZTL (Zona Traffico Limitato):**\n• Most historic centers are restricted to local traffic only\n• Heavy fines for driving in without permit (€100+)\n• Park outside and walk in, or use public transport\n\n**Finding directions:**\n• 'Dov'è il centro?' (Where's the center?) is a common first question in any Italian city\n• Locals measure distance from the centro: 'È vicino al centro' (It's near the center)\n\nTip: When visiting a new Italian city, go 'al centro' first to orient yourself and experience authentic local life!",
                    "sub_text": "Understanding il centro helps you navigate Italian cities like a local.",
                    "cultural_note": True
                },
                {
                    "type": "info_card",
                    "step": 10,
                    "prompt": "Cultural Note",
                    "correct_answer": "La Piazza - Italy's Living Room",
                    "explanation": "The piazza (town square) is the social center of every Italian community:\n\n**What happens in the piazza:**\n• Children play while parents watch from café tables\n• Elderly gather on benches to chat\n• Evening passeggiata (stroll) - people walk in circles socializing\n• Markets, festivals, and community events\n• Political rallies and public celebrations\n\n**Famous piazzas:**\n• Piazza Navona (Rome) - Baroque fountains, artists, cafés\n• Piazza del Campo (Siena) - Shell-shaped, hosts Palio horse race\n• Piazza San Marco (Venice) - Grand with Basilica\n• Piazza del Duomo - Almost every city has one (cathedral square)\n\n**Piazza culture:**\n• No single purpose - it's a flexible community space\n• Free and open to all - the opposite of private malls\n• Car-free zones where people > vehicles\n• Usually has a fountain, church, and cafés around the edges\n• Changes character throughout the day: quiet morning, lively evening\n\n**Social norms:**\n• Sitting on steps/fountains is common (except famous monuments)\n• Kids playing is welcomed, not frowned upon\n• Lingering is encouraged - 'la dolce far niente' (the sweetness of doing nothing)\n\n**Useful phrases:**\n• 'Ci vediamo in piazza' (Let's meet in the piazza) - a common meeting point\n• Every neighborhood has its own piazza for local life\n\nThe piazza represents Italian values: community over privacy, leisure over rushing, face-to-face connection over digital!",
                    "sub_text": "Spend time in piazzas to truly understand Italian social culture.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.7.BOSS",
            "title": "Boss Fight: The Lost Tourist",
            "type": "conversation_challenge",
            "focus": "Navigating a new city - asking for directions and giving directions",
            "vocabulary": [
                {"term": "stazione", "translation": "station"},
                {"term": "scusi", "translation": "excuse me (formal)"},
                {"term": "per", "translation": "for/to"},
                {"term": "vai", "translation": "go"},
                {"term": "gira", "translation": "turn"},
                {"term": "dritto", "translation": "straight"},
                {"term": "poi", "translation": "then"},
                {"term": "bar", "translation": "bar/café"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You are a lost tourist in a new city. First, ask a stranger for directions, then help a friend find you.",
                    "scenario": "lost_tourist",
                    "ai_prompt": "You are a helpful local giving directions formally, then a friend asking where to meet you.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Asking a Stranger",
                            "round_description": "You are lost. Ask a stranger for directions to the station.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Posso aiutarla?",
                                    "user_requirement": "Greet formally and ask for directions to the station.",
                                    "required_words": ["Scusi", "stazione", "per"],
                                    "hints": ["Scusi, per la stazione?", "Scusi, dov'è la stazione?"],
                                    "invalid_responses": ["Ciao!", "Stazione", "Where is station?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "La stazione? Vai dritto, poi gira a destra.",
                                    "user_requirement": "Ask for clarification or confirm the directions.",
                                    "required_words": ["Grazie", "dritto", "destra"],
                                    "hints": ["Grazie", "Dritto e poi destra?", "Capito"],
                                    "invalid_responses": ["Thanks", "OK", "Right"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Sì, esatto. È vicino.",
                                    "user_requirement": "Thank them and ask how far it is.",
                                    "required_words": ["Grazie", "vicino", "lontano"],
                                    "hints": ["Grazie, è vicino?", "Quanto è lontano?"],
                                    "invalid_responses": ["Thanks", "Far?", "Close?"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Prego! Buona giornata!",
                                    "user_requirement": "Say goodbye politely.",
                                    "required_words": ["Grazie", "Arrivederci", "Buona giornata"],
                                    "hints": ["Grazie, arrivederci", "Buona giornata"],
                                    "invalid_responses": ["Bye", "See you", "Thanks bye"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Giving Directions to a Friend",
                            "round_description": "Your friend asks where to meet you. Give them directions to the bar.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Dove sei?",
                                    "user_requirement": "Say you're at a bar and invite them to come.",
                                    "required_words": ["bar", "vieni", "qui"],
                                    "hints": ["Sono al bar", "Vieni qui", "Sono qui al bar"],
                                    "invalid_responses": ["Bar", "I'm here", "Come here"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Ok! Come arrivo?",
                                    "user_requirement": "Give simple directions using imperative.",
                                    "required_words": ["vai", "gira", "dritto", "destra", "sinistra"],
                                    "hints": ["Vai dritto", "Gira a destra", "Vai dritto, poi gira"],
                                    "invalid_responses": ["Go straight", "Turn right", "Straight then right"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Perfetto! E poi?",
                                    "user_requirement": "Continue giving directions using 'poi'.",
                                    "required_words": ["poi", "gira", "vai"],
                                    "hints": ["Poi gira", "Poi vai", "Poi gira a sinistra"],
                                    "invalid_responses": ["Then turn", "Then go", "After that"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Ok, capito! Arrivo tra poco!",
                                    "user_requirement": "Confirm and say you'll wait.",
                                    "required_words": ["Ok", "Aspetto", "Ciao"],
                                    "hints": ["Ok, ti aspetto", "Aspetto qui", "Ciao"],
                                    "invalid_responses": ["OK wait", "I wait", "See you"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
