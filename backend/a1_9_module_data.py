"""
Module A1.9 data structure - Travel & Transport
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_9_LESSONS = {
    "module_id": "A1.9",
    "title": "Travel & Transport",
    "goal": "Navigate travel situations, buy tickets, understand schedules, and discuss travel plans using present tense for future.",
    "lessons": [
        {
            "lesson_id": "A1.9.0",
            "title": "Self-Assessment: Travel & Transport",
            "focus": "Assess your confidence with travel and transport",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel traveling and using transport?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can name different modes of transport",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can buy tickets at a station",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can understand departure and arrival times",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can talk about my travel plans",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.9.1",
            "title": "Modes of Transport (In vs. A)",
            "focus": "Vehicles and the 'In' rule (In treno) vs 'A' rule (A piedi)",
            "vocabulary": [
                {"term": "treno", "translation": "train"},
                {"term": "autobus", "translation": "bus"},
                {"term": "macchina", "translation": "car"},
                {"term": "aereo", "translation": "plane"},
                {"term": "bicicletta", "translation": "bicycle"},
                {"term": "piedi", "translation": "on foot"},
                {"term": "in", "translation": "in/by"},
                {"term": "a", "translation": "to/at/by"},
                {"term": "vado", "translation": "I go"},
                {"term": "viaggiare", "translation": "to travel"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Prepositions with Transport",
                    "correct_answer": "In vs A",
                    "explanation": "Use 'in' for vehicles (in treno, in autobus, in macchina, in aereo).\nUse 'a' for walking (a piedi).\n\nExamples:\n- Vado in treno (I go by train)\n- Vado in macchina (I go by car)\n- Vado a piedi (I go on foot)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "treno",
                    "explanation": "train",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_treno_204.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "autobus",
                    "explanation": "bus",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_autobus_205.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "aereo",
                    "explanation": "plane",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_aereo_206.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "bicicletta",
                    "explanation": "bicycle",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_bicicletta_207.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Modes of Transport",
                    "pairs": [["treno", "train"], ["autobus", "bus"], ["aereo", "plane"], ["bicicletta", "bicycle"], ["a piedi", "on foot"]],
                    "correct_answer": "match_all",
                    "explanation": "Transport vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How is the person traveling?",
                    "audio_text": "Vado in treno.",
                    "options": ["by train", "by bus", "by car", "by plane"],
                    "correct_answer": "by train",
                    "explanation": "You heard 'in treno' (by train).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I go by bus.",
                    "blocks": ["Vado", "in", "autobus", "."],
                    "correct_answer": "Vado in autobus.",
                    "explanation": "Use 'Vado in' + vehicle (for most vehicles)."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I go on foot.",
                    "blocks": ["Vado", "a", "piedi", "."],
                    "correct_answer": "Vado a piedi.",
                    "explanation": "Use 'Vado a piedi' (I go on foot) - special case."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vado in treno",
                    "target_phrase": "Vado in treno",
                    "target_lang": "it",
                    "explanation": "Practice saying how you travel"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ treno.' (by)",
                    "options": ["in", "a", "al", "con"],
                    "correct_answer": "in",
                    "explanation": "Use 'in' for vehicles like 'treno'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vado ___ piedi.' (on)",
                    "options": ["in", "a", "al", "con"],
                    "correct_answer": "a",
                    "explanation": "Use 'a piedi' (on foot) - special case."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Come vai a Roma?'",
                    "context": "You're going by train.",
                    "task": "Tell them how you're traveling.",
                    "target_lang": "it",
                    "explanation": "Say 'Vado in treno.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match transport modes",
                    "pairs": [["treno", "train"], ["autobus", "bus"], ["aereo", "plane"], ["a piedi", "on foot"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.2",
            "title": "At the Station (Buying Tickets)",
            "focus": "Ticket types, Platforms",
            "vocabulary": [
                {"term": "biglietto", "translation": "ticket"},
                {"term": "andata", "translation": "one-way"},
                {"term": "ritorno", "translation": "return"},
                {"term": "solo andata", "translation": "one-way only"},
                {"term": "binario", "translation": "platform"},
                {"term": "stazione", "translation": "station"},
                {"term": "treno", "translation": "train"},
                {"term": "per", "translation": "for/to"},
                {"term": "Roma", "translation": "Rome"},
                {"term": "Milano", "translation": "Milan"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "biglietto",
                    "explanation": "ticket",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_biglietto_208.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "solo andata",
                    "explanation": "one-way only",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_solo_andata_209.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ritorno",
                    "explanation": "return",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ritorno_210.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "binario",
                    "explanation": "platform",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_binario_211.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Ticket Terms",
                    "pairs": [["biglietto", "ticket"], ["solo andata", "one-way only"], ["ritorno", "return"], ["binario", "platform"], ["stazione", "station"]],
                    "correct_answer": "match_all",
                    "explanation": "Ticket vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What type of ticket does the customer want?",
                    "audio_text": "Vorrei un biglietto per Roma, solo andata.",
                    "options": ["one-way to Rome", "return to Rome", "one-way to Milan", "return to Milan"],
                    "correct_answer": "one-way to Rome",
                    "explanation": "You heard 'solo andata' (one-way) and 'per Roma' (to Rome).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I would like a ticket to Milan, return.",
                    "blocks": ["Vorrei", "un", "biglietto", "per", "Milano", "e", "ritorno", "."],
                    "correct_answer": "Vorrei un biglietto per Milano e ritorno.",
                    "explanation": "Use 'Vorrei' + article + 'biglietto' + 'per' + destination + 'e ritorno'."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vorrei un biglietto per Roma",
                    "target_phrase": "Vorrei un biglietto per Roma",
                    "target_lang": "it",
                    "explanation": "Practice buying tickets"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei un biglietto ___ Roma.' (to/for)",
                    "options": ["per", "a", "in", "al"],
                    "correct_answer": "per",
                    "explanation": "Use 'per' (for/to) when specifying destination."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at a train station. You want a one-way ticket to Rome.",
                    "context": "You're speaking to the ticket clerk.",
                    "task": "Ask for the ticket politely.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei un biglietto per Roma, solo andata, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match ticket vocabulary",
                    "pairs": [["biglietto", "ticket"], ["solo andata", "one-way"], ["ritorno", "return"], ["binario", "platform"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.3",
            "title": "Departure & Arrival (Verbs)",
            "focus": "Partire (To leave) vs Arrivare (To arrive)",
            "vocabulary": [
                {"term": "partire", "translation": "to leave"},
                {"term": "arrivare", "translation": "to arrive"},
                {"term": "parte", "translation": "he/she leaves"},
                {"term": "arriva", "translation": "he/she arrives"},
                {"term": "quando", "translation": "when"},
                {"term": "a che ora", "translation": "at what time"},
                {"term": "adesso", "translation": "now"},
                {"term": "presto", "translation": "early"},
                {"term": "tardi", "translation": "late"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Verbs of Movement",
                    "correct_answer": "Partire vs Arrivare",
                    "explanation": "'Partire' (to leave) and 'Arrivare' (to arrive) are regular -ire verbs.\n\nPartire:\n- Io parto (I leave)\n- Il treno parte (The train leaves)\n\nArrivare:\n- Io arrivo (I arrive)\n- Il treno arriva (The train arrives)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "partire",
                    "explanation": "to leave",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_partire_212.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "arrivare",
                    "explanation": "to arrive",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_arrivare_213.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "a che ora",
                    "explanation": "at what time",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_a_che_ora_214.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Movement Verbs",
                    "pairs": [["partire", "to leave"], ["arrivare", "to arrive"], ["parte", "he/she leaves"], ["arriva", "he/she arrives"], ["quando", "when"]],
                    "correct_answer": "match_all",
                    "explanation": "Movement verbs vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. When does the train leave?",
                    "audio_text": "Il treno parte alle tre.",
                    "options": ["at three o'clock", "at four o'clock", "at five o'clock", "at six o'clock"],
                    "correct_answer": "at three o'clock",
                    "explanation": "You heard 'parte alle tre' (leaves at three).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "When does the train arrive?",
                    "blocks": ["Quando", "arriva", "il", "treno", "?"],
                    "correct_answer": "Quando arriva il treno?",
                    "explanation": "Use 'Quando' (when) + verb + article + noun."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The train leaves at five o'clock.",
                    "blocks": ["Il", "treno", "parte", "alle", "cinque", "."],
                    "correct_answer": "Il treno parte alle cinque.",
                    "explanation": "Use article + noun + verb + 'alle' + time."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Il treno parte alle tre",
                    "target_phrase": "Il treno parte alle tre",
                    "target_lang": "it",
                    "explanation": "Practice talking about departures"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il treno ___ alle tre.' (leaves)",
                    "options": ["parte", "parto", "parti", "partiamo"],
                    "correct_answer": "parte",
                    "explanation": "Use 'parte' (third person singular) with 'il treno'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il treno ___ alle cinque.' (arrives)",
                    "options": ["arriva", "arrivo", "arrivi", "arriviamo"],
                    "correct_answer": "arriva",
                    "explanation": "Use 'arriva' (third person singular) with 'il treno'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'A che ora parte il treno?'",
                    "context": "The train leaves at four o'clock.",
                    "task": "Tell them the departure time.",
                    "target_lang": "it",
                    "explanation": "Say 'Parte alle quattro.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match movement verbs",
                    "pairs": [["partire", "to leave"], ["arrivare", "to arrive"], ["quando", "when"], ["a che ora", "at what time"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.4",
            "title": "The Airport & Luggage",
            "focus": "Air travel specifics, Checking in",
            "vocabulary": [
                {"term": "aeroporto", "translation": "airport"},
                {"term": "volo", "translation": "flight"},
                {"term": "valigia", "translation": "suitcase"},
                {"term": "bagaglio", "translation": "luggage"},
                {"term": "passaporto", "translation": "passport"},
                {"term": "carta d'imbarco", "translation": "boarding pass"},
                {"term": "gate", "translation": "gate"},
                {"term": "controllo", "translation": "check/control"},
                {"term": "partenze", "translation": "departures"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "aeroporto",
                    "explanation": "airport",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_aeroporto_215.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "volo",
                    "explanation": "flight",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_volo_216.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "valigia",
                    "explanation": "suitcase",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_valigia_217.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "passaporto",
                    "explanation": "passport",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_passaporto_218.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "carta d'imbarco",
                    "explanation": "boarding pass",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_carta_dimbarco_219.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Airport Terms",
                    "pairs": [["aeroporto", "airport"], ["volo", "flight"], ["valigia", "suitcase"], ["passaporto", "passport"], ["carta d'imbarco", "boarding pass"]],
                    "correct_answer": "match_all",
                    "explanation": "Airport vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person need?",
                    "audio_text": "Ho bisogno del passaporto e della carta d'imbarco.",
                    "options": ["passport and boarding pass", "suitcase and passport", "flight and gate", "luggage and ticket"],
                    "correct_answer": "passport and boarding pass",
                    "explanation": "You heard 'passaporto e carta d'imbarco' (passport and boarding pass).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I need my passport and boarding pass.",
                    "blocks": ["Ho", "bisogno", "del", "passaporto", "e", "della", "carta", "d'imbarco", "."],
                    "correct_answer": "Ho bisogno del passaporto e della carta d'imbarco.",
                    "explanation": "Use 'Ho bisogno di' (I need) + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ho bisogno del passaporto",
                    "target_phrase": "Ho bisogno del passaporto",
                    "target_lang": "it",
                    "explanation": "Practice airport vocabulary"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ho bisogno della ___.' (suitcase)",
                    "options": ["valigia", "volo", "gate", "controllo"],
                    "correct_answer": "valigia",
                    "explanation": "Use 'valigia' (suitcase) for luggage."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at the airport. You need to check in.",
                    "context": "You need your passport and boarding pass.",
                    "task": "Say what you need.",
                    "target_lang": "it",
                    "explanation": "Say 'Ho bisogno del passaporto e della carta d'imbarco.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match airport vocabulary",
                    "pairs": [["aeroporto", "airport"], ["volo", "flight"], ["valigia", "suitcase"], ["passaporto", "passport"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.5",
            "title": "Schedules & Delays",
            "focus": "Understanding status announcements",
            "vocabulary": [
                {"term": "orario", "translation": "schedule"},
                {"term": "in orario", "translation": "on time"},
                {"term": "ritardo", "translation": "delay"},
                {"term": "minuti", "translation": "minutes"},
                {"term": "cancellato", "translation": "cancelled"},
                {"term": "cambio", "translation": "change"},
                {"term": "prossimo", "translation": "next"},
                {"term": "ultimo", "translation": "last"},
                {"term": "attenzione", "translation": "attention"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "orario",
                    "explanation": "schedule",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_orario_220.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "in orario",
                    "explanation": "on time",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_in_orario_221.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ritardo",
                    "explanation": "delay",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ritardo_222.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cancellato",
                    "explanation": "cancelled",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cancellato_223.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Schedule Terms",
                    "pairs": [["orario", "schedule"], ["in orario", "on time"], ["ritardo", "delay"], ["cancellato", "cancelled"], ["prossimo", "next"]],
                    "correct_answer": "match_all",
                    "explanation": "Schedule vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What is the status of the train?",
                    "audio_text": "Il treno è in ritardo di dieci minuti.",
                    "options": ["delayed by ten minutes", "on time", "cancelled", "early"],
                    "correct_answer": "delayed by ten minutes",
                    "explanation": "You heard 'in ritardo di dieci minuti' (delayed by ten minutes).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The train is on time.",
                    "blocks": ["Il", "treno", "è", "in", "orario", "."],
                    "correct_answer": "Il treno è in orario.",
                    "explanation": "Use 'è in orario' (is on time) for punctual trains."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The flight is cancelled.",
                    "blocks": ["Il", "volo", "è", "cancellato", "."],
                    "correct_answer": "Il volo è cancellato.",
                    "explanation": "Use 'è cancellato' (is cancelled) for cancelled flights."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Il treno è in ritardo",
                    "target_phrase": "Il treno è in ritardo",
                    "target_lang": "it",
                    "explanation": "Practice understanding delays"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il treno è ___.' (on time)",
                    "options": ["in orario", "ritardo", "cancellato", "prossimo"],
                    "correct_answer": "in orario",
                    "explanation": "Use 'in orario' (on time) for punctual trains."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Il treno è in ___.' (delay)",
                    "options": ["orario", "ritardo", "cancellato", "cambio"],
                    "correct_answer": "ritardo",
                    "explanation": "Use 'in ritardo' (delayed) for late trains."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Il treno è in orario?'",
                    "context": "No, it's delayed by five minutes.",
                    "task": "Tell them about the delay.",
                    "target_lang": "it",
                    "explanation": "Say 'No, è in ritardo di cinque minuti.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match schedule terms",
                    "pairs": [["orario", "schedule"], ["in orario", "on time"], ["ritardo", "delay"], ["cancellato", "cancelled"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.6",
            "title": "Future Plans (Using Present Tense)",
            "focus": "Talking about tomorrow/vacation",
            "vocabulary": [
                {"term": "domani", "translation": "tomorrow"},
                {"term": "dopo", "translation": "after/later"},
                {"term": "settimana prossima", "translation": "next week"},
                {"term": "vacanza", "translation": "vacation"},
                {"term": "mare", "translation": "sea"},
                {"term": "montagna", "translation": "mountain"},
                {"term": "visitare", "translation": "to visit"},
                {"term": "vado a", "translation": "I go to"},
                {"term": "parto per", "translation": "I leave for"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Present Tense for Future",
                    "correct_answer": "Present + Time Marker",
                    "explanation": "In Italian, you can use Present Tense + time marker to talk about future plans.\n\nExamples:\n- Domani vado a Roma (Tomorrow I go to Rome)\n- Settimana prossima parto per Milano (Next week I leave for Milan)\n\nNo need for Future Simple tense at A1 level!",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "domani",
                    "explanation": "tomorrow",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_domani_224.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "settimana prossima",
                    "explanation": "next week",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_settimana_prossima_225.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "vacanza",
                    "explanation": "vacation",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vacanza_226.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "mare",
                    "explanation": "sea",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mare_227.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Time Expressions",
                    "pairs": [["domani", "tomorrow"], ["dopo", "after/later"], ["settimana prossima", "next week"], ["vacanza", "vacation"], ["mare", "sea"]],
                    "correct_answer": "match_all",
                    "explanation": "Future time vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. When is the person going?",
                    "audio_text": "Domani vado a Roma.",
                    "options": ["tomorrow", "next week", "today", "yesterday"],
                    "correct_answer": "tomorrow",
                    "explanation": "You heard 'Domani' (tomorrow).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Tomorrow I go to the sea.",
                    "blocks": ["Domani", "vado", "al", "mare", "."],
                    "correct_answer": "Domani vado al mare.",
                    "explanation": "Use time marker + present tense verb + preposition + destination.",
                    "common_mistakes": [
                        {
                            "pattern": "andrò",
                            "explanation": "Use present tense 'vado' with time markers, not future tense 'andrò'."
                        }
                    ]
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Next week I leave for vacation.",
                    "blocks": ["Settimana", "prossima", "parto", "per", "vacanza", "."],
                    "correct_answer": "Settimana prossima parto per vacanza.",
                    "explanation": "Use 'parto per' (I leave for) + destination."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Domani vado a Roma",
                    "target_phrase": "Domani vado a Roma",
                    "target_lang": "it",
                    "explanation": "Practice talking about future plans"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ vado al mare.' (Tomorrow)",
                    "options": ["Domani", "Dopo", "Oggi", "Ieri"],
                    "correct_answer": "Domani",
                    "explanation": "Use 'Domani' (tomorrow) for future plans."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Settimana prossima ___ per Milano.' (I leave)",
                    "options": ["vado", "parto", "arrivo", "prendo"],
                    "correct_answer": "parto",
                    "explanation": "Use 'parto per' (I leave for) when starting a journey."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Dove vai in vacanza?'",
                    "context": "Tomorrow you're going to the sea.",
                    "task": "Tell them your vacation plans.",
                    "target_lang": "it",
                    "explanation": "Say 'Domani vado al mare.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match future time expressions",
                    "pairs": [["domani", "tomorrow"], ["settimana prossima", "next week"], ["vacanza", "vacation"], ["vado a", "I go to"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.9.BOSS",
            "title": "Boss Fight: The Ticket Office",
            "type": "boss_fight",
            "focus": "Booking a trip and discussing plans - buying tickets and talking about vacation",
            "vocabulary": [
                {"term": "biglietto", "translation": "ticket"},
                {"term": "Firenze", "translation": "Florence"},
                {"term": "per", "translation": "for/to"},
                {"term": "vacanza", "translation": "vacation"},
                {"term": "dove vai", "translation": "where are you going"},
                {"term": "vado", "translation": "I go"},
                {"term": "parto", "translation": "I leave"},
                {"term": "mare", "translation": "sea"}
            ],
            "exercises": [
                {
                    "type": "boss_fight",
                    "step": 1,
                    "prompt": "You need to book a trip: buy a train ticket and discuss your vacation plans with a friend.",
                    "scenario": "ticket_office",
                    "ai_prompt": "You are a formal ticket clerk selling tickets, then a friend asking about vacation plans.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Buying a Ticket",
                            "round_description": "The ticket clerk helps you buy a train ticket.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Posso aiutarla?",
                                    "user_requirement": "Greet formally and ask for a ticket.",
                                    "required_words": ["Buongiorno", "biglietto", "vorrei"],
                                    "hints": ["Buongiorno", "Vorrei un biglietto", "Un biglietto per favore"],
                                    "invalid_responses": ["Ciao!", "Ticket", "I want ticket"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Certamente! Per dove?",
                                    "user_requirement": "Request a ticket to Florence using 'per'.",
                                    "required_words": ["per", "Firenze"],
                                    "hints": ["Per Firenze", "Un biglietto per Firenze"],
                                    "invalid_responses": ["To Florence", "Florence", "Firenze"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene. Solo andata o andata e ritorno?",
                                    "user_requirement": "Specify one-way or return ticket.",
                                    "required_words": ["solo andata", "ritorno", "andata"],
                                    "hints": ["Solo andata", "Andata e ritorno"],
                                    "invalid_responses": ["One-way", "Return", "Round trip"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! Ecco il biglietto.",
                                    "user_requirement": "Thank them politely.",
                                    "required_words": ["Grazie"],
                                    "hints": ["Grazie", "Grazie mille"],
                                    "invalid_responses": ["Thanks", "Thank you", "OK"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Vacation Plans",
                            "round_description": "Your friend asks about your vacation plans.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Dove vai in vacanza?",
                                    "user_requirement": "Say where you're going using 'vado' + destination.",
                                    "required_words": ["vado", "mare", "montagna", "Roma", "Milano"],
                                    "hints": ["Vado al mare", "Vado in montagna", "Vado a Roma"],
                                    "invalid_responses": ["Sea", "Mountain", "Rome"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Bene! Quando parti?",
                                    "user_requirement": "Say when you're leaving using 'parto' + time marker.",
                                    "required_words": ["parto", "domani", "settimana prossima"],
                                    "hints": ["Parto domani", "Parto settimana prossima"],
                                    "invalid_responses": ["Tomorrow", "Next week", "I leave"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Perfetto! E come vai?",
                                    "user_requirement": "Say how you're traveling using 'vado in' + transport.",
                                    "required_words": ["vado", "in", "treno", "aereo", "macchina"],
                                    "hints": ["Vado in treno", "Vado in aereo", "Vado in macchina"],
                                    "invalid_responses": ["By train", "By plane", "By car"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Ottimo! Buon viaggio!",
                                    "user_requirement": "Thank them and say goodbye informally.",
                                    "required_words": ["Grazie", "Ciao", "A presto"],
                                    "hints": ["Grazie, ciao", "A presto", "Ciao"],
                                    "invalid_responses": ["Thanks bye", "Bye", "See you"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
