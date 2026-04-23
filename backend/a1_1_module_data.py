"""
Module A1.1 data structure - can be imported by server.py
"""

MODULE_A1_1_LESSONS = {
    "module_id": "A1.1",
    "title": "Greetings & Introductions",
    "goal": "Navigate specific social hierarchies (Friend vs. Boss) and introduce oneself with correct pronunciation.",
    "lessons": [
        {
            "lesson_id": "A1.1.0",
            "title": "Self-Assessment: Greetings & Introductions",
            "focus": "Assess your confidence with basic greetings",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel with greetings and introductions?",
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
            "focus": "Casual interactions, vowels, 'Tu' (You)",
            "vocabulary": [
                {"term": "Ciao", "translation": "Hi/Bye"},
                {"term": "Come stai?", "translation": "How are you? (Informal)"},
                {"term": "Bene", "translation": "Well/Good"},
                {"term": "E tu?", "translation": "And you?"},
                {"term": "Grazie", "translation": "Thank you"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Ciao",
                    "explanation": "Hi/Bye",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ciao_0.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Come stai?",
                    "explanation": "How are you? (Informal)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_come_stai__1.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Audio to Text",
                    "pairs": [["Ciao", "Hi/Bye"], ["Come stai?", "How are you?"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect sound to meaning"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen to the audio. What greeting did you hear?",
                    "audio_text": "Ciao! Come stai?",
                    "options": ["Ciao", "Buongiorno", "Buonasera", "Salve"],
                    "correct_answer": "Ciao",
                    "explanation": "You heard 'Ciao', the informal greeting used with friends.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How are you? (Informal)",
                    "blocks": ["Come", "stai"],
                    "correct_answer": "Come stai?",
                    "explanation": "Use 'Come stai?' for informal greetings — 'tu' is implied, not stated."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat after me",
                    "target_phrase": "Come stai?",
                    "target_lang": "it",
                    "explanation": "Tests vowel clarity (A-I sound)"
                },
                {
                    "type": "reading_comprehension",
                    "step": 6,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Marco: Ciao! Come stai?\nSofia: Bene, grazie! E tu?",
                    "question": "How does Marco greet Sofia?",
                    "options": ["Ciao", "Buongiorno", "Arrivederci"],
                    "correct_answer": "Ciao",
                    "explanation": "Marco uses 'Ciao', the informal greeting for friends.",
                    "highlight_vocab": ["Ciao", "Come stai", "Bene", "grazie"]
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Your friend Marco arrives.",
                    "context": "Your friend Marco arrives.",
                    "task": "Greet him.",
                    "target_lang": "it",
                    "explanation": "This is a friend, so use a casual greeting. What informal greeting did you learn?"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match the informal greetings",
                    "pairs": [["Ciao", "Hi/Bye"], ["Come stai?", "How are you?"], ["Bene", "Well"], ["Grazie", "Thank you"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the informal greetings.",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Ciao vs. Salve - When to Use Each",
                    "explanation": "While 'Ciao' is the most common greeting among friends, 'Salve' is a safer choice when you're unsure:\n\n• Ciao - Very informal, use with friends, family, and peers\n• Salve - Neutral formality, works in most situations\n• Buongiorno/Buonasera - More formal, safer with strangers and elders\n\nTip: When in doubt, use 'Buongiorno' before 2 PM and 'Buonasera' after!",
                    "sub_text": "Understanding these nuances helps you make a great first impression.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.2",
            "title": "Formal Greetings & Time-Based Expressions",
            "focus": "'Lei' (Formal You), Time-based greetings",
            "vocabulary": [
                {"term": "Buongiorno", "translation": "Good morning (Formal)"},
                {"term": "Buonasera", "translation": "Good evening (Formal)"},
                {"term": "Arrivederci", "translation": "Goodbye (Formal)"},
                {"term": "Come sta?", "translation": "How are you? (Formal)"},
                {"term": "Lei", "translation": "You (Formal)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buongiorno",
                    "explanation": "Good morning (Formal)",
                    "sub_text": "Use before evening",
                    "audio_url": "/static/audio/it_buongiorno_5.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Buonasera",
                    "explanation": "Good evening (Formal)",
                    "sub_text": "Use after afternoon",
                    "audio_url": "/static/audio/it_buonasera_6.mp3"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "You meet a Professor. Select the greeting.",
                    "options": ["Ciao", "Buongiorno", "E tu?"],
                    "correct_answer": "Buongiorno",
                    "explanation": "Formal situation requires formal greeting"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What formal greeting did you hear?",
                    "audio_text": "Buonasera, come sta?",
                    "options": ["Buongiorno", "Buonasera", "Ciao", "Salve"],
                    "correct_answer": "Buonasera",
                    "explanation": "You heard 'Buonasera' (Good evening), used in formal situations after afternoon.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How are you? (Formal)",
                    "blocks": ["Lei", "come", "sta"],
                    "correct_answer": "Come sta Lei?",
                    "explanation": "Reinforces Lei and Sta (3rd person conjugation)"
                },
                {
                    "type": "info_card",
                    "step": 5,
                    "prompt": "Cultural Note",
                    "correct_answer": "Formal vs. Informal in Italy",
                    "explanation": "In Italy, choosing between 'Tu' (informal) and 'Lei' (formal) depends on:\n• Age difference\n• Social hierarchy\n• Setting (work vs. social)\n\nUse 'Tu' with friends, peers, and family.\nUse 'Lei' with elders, authority figures, and in professional settings.",
                    "sub_text": "Understanding this cultural context helps you choose the right greeting.",
                    "cultural_note": True
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat after me",
                    "target_phrase": "Arrivederci",
                    "target_lang": "it",
                    "explanation": "High difficulty. Tests the 'R' roll and the soft 'C'"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "It is 7 PM. You see Dr. Rossi.",
                    "context": "It is 7 PM. You see Dr. Rossi.",
                    "task": "Greet him.",
                    "target_lang": "it",
                    "explanation": "It's evening (7 PM). What time-based greeting is appropriate for this time of day?"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match the formal greetings",
                    "pairs": [["Buongiorno", "Good morning"], ["Buonasera", "Good evening"], ["Arrivederci", "Goodbye"], ["Come sta?", "How are you? (Formal)"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the formal greetings.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.3",
            "title": "Introducing Yourself (Pronunciation & Verbs)",
            "focus": "Reflexive verbs (Mi chiamo), Hard vs. Soft C",
            "vocabulary": [
                {"term": "Mi chiamo", "translation": "My name is"},
                {"term": "Sono", "translation": "I am"},
                {"term": "Piacere", "translation": "Nice to meet you"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Mi chiamo",
                    "explanation": "My name is (reflexive)",
                    "sub_text": "Shows two ways to say the same thing",
                    "audio_url": "/static/audio/it_mi_chiamo_11.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Sono",
                    "explanation": "I am",
                    "sub_text": "Alternative way to introduce yourself",
                    "audio_url": "/static/audio/it_sono_12.mp3",
                    "image_url": "/images/topics/greetings-11.jpg"
                },
                {
                    "type": "unscramble",
                    "step": 2,
                    "prompt": "My name is Paolo.",
                    "blocks": ["Mi", "Paolo", "chiamo"],
                    "correct_answer": "Mi chiamo Paolo",
                    "explanation": "Critical. Teaches reflexive pronoun goes before the verb",
                    "common_mistakes": [
                        {
                            "pattern": "chiamo mi",
                            "explanation": "In Italian, the reflexive pronoun 'Mi' comes before the verb 'chiamo'. The correct order is 'Mi chiamo'."
                        },
                        {
                            "pattern": "io mi chiamo",
                            "explanation": "Good! 'Io mi chiamo' is also correct, though 'Mi chiamo' is more common. Both are acceptable!"
                        }
                    ]
                },
                {
                    "type": "info_card",
                    "step": 2,
                    "prompt": "Grammar: The Verb 'To Be'",
                    "correct_answer": "Essere (To Be)",
                    "table": {
                        "headers": ["Italian", "English"],
                        "rows": [
                            ["Io sono", "I am"],
                            ["Tu sei", "You are"],
                            ["Lui/Lei è", "He/She is"]
                        ]
                    },
                    "sub_text": "Learn the verb 'essere' (to be)",
                    "image_url": "/images/topics/greetings-1.jpg"
                },
                {
                    "type": "match",
                    "step": 3,
                    "prompt": "Match the pronoun to the verb form",
                    "pairs": [["Io", "sono"], ["Tu", "sei"], ["Lui/Lei", "è"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect pronouns with their 'essere' forms"
                },
                {
                    "type": "reading_comprehension",
                    "step": 4,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Marco: Ciao! Come stai?\nSofia: Bene, grazie! E tu?\nMarco: Bene anche io! Piacere! Mi chiamo Marco.",
                    "question": "How does Marco introduce himself?",
                    "options": ["Mi chiamo Marco", "Sono Marco", "Io sono Marco", "Il mio nome è Marco"],
                    "correct_answer": "Mi chiamo Marco",
                    "explanation": "Marco says 'Mi chiamo Marco' which means 'My name is Marco' - this is the reflexive verb form for introducing yourself.",
                    "highlight_vocab": ["Ciao", "Come stai", "Bene", "grazie", "Mi chiamo"]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Piacere",
                    "target_phrase": "Piacere",
                    "target_lang": "it",
                    "explanation": "Part A: Soft C sound"
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat: Mi chiamo",
                    "target_phrase": "Mi chiamo",
                    "target_lang": "it",
                    "explanation": "Part B: Hard K sound (Ch)"
                },
                {
                    "type": "fill_blank",
                    "step": 7,
                    "prompt": "Complete: '____ chiamo Maria.'",
                    "options": ["Mi", "Io", "Me"],
                    "correct_answer": "Mi",
                    "explanation": "Testing memory of the reflexive pronoun"
                },
                {
                    "type": "fill_blank",
                    "step": 8,
                    "prompt": "Complete: 'Io ___ Maria.' (I am Maria)",
                    "options": ["sono", "sei", "è"],
                    "correct_answer": "sono",
                    "explanation": "Practice 'essere' conjugation: Io sono = I am"
                },
                {
                    "type": "mini_prompt",
                    "step": 9,
                    "prompt": "Someone says 'Piacere'.",
                    "context": "Someone says 'Piacere'.",
                    "task": "Introduce yourself.",
                    "target_lang": "it",
                    "explanation": "Someone said 'Piacere' to you. How do you introduce yourself in Italian? What phrase did you learn for saying your name?"
                },
                {
                    "type": "free_writing",
                    "step": 10,
                    "prompt": "Write a simple introduction about yourself.",
                    "context": "You're meeting someone new at a café.",
                    "task": "Write 2-3 sentences introducing yourself. Include: your name and a greeting.",
                    "target_lang": "it",
                    "required_elements": ["name", "greeting"],
                    "example_response": "Ciao! Mi chiamo Maria.",
                    "validation_mode": "ai",
                    "explanation": "Great! You included your name and a greeting. Perfect introduction!"
                },
                {
                    "type": "info_card",
                    "step": 11,
                    "prompt": "Cultural Note",
                    "correct_answer": "Hard vs. Soft C: Chi and Ci Sounds",
                    "explanation": "In Italian, the letter 'C' has two very different sounds depending on what letter comes after it. This is crucial for pronunciation!\n\n**Soft C (sounds like 'ch' in 'cheese'):**\n• Used before E or I: Ci, Ce\n• Examples: Piacere (nice to meet you), Ciao (hello/bye), Dolce (sweet)\n• Your mouth is more open, tongue forward\n\n**Hard C (sounds like 'k' in 'kite'):**\n• Used before A, O, or U: Ca, Co, Cu\n• Used before H with E or I: Chi, Che\n• Examples: Caffè (coffee), Casa (house), Chi sei? (Who are you?)\n• Your mouth is more closed, tongue back\n\n**Why it matters:**\n• 'Ci' (soft C) in 'Ciao' sounds like 'ch', not 'k'\n• 'Chi' (hard C + H) in 'Chi?' sounds like 'k', not 'ch'\n• Mixing these up makes your accent very obvious to natives\n\n**Practice tip:** Listen to 'Ciao' (soft - ch-OW) vs. 'Casa' (hard - KA-sa) and repeat the sounds slowly!",
                    "sub_text": "These two sounds are essential for sounding natural in Italian.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.4",
            "title": "Polite Expressions & Closings",
            "focus": "Salve (The safe word), Polite closings",
            "vocabulary": [
                {"term": "Salve", "translation": "Hello (Safe/Neutral)"},
                {"term": "Per favore", "translation": "Please"},
                {"term": "Prego", "translation": "You're welcome"},
                {"term": "A presto", "translation": "See you soon"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Salve",
                    "explanation": "The safe word (usable anywhere)",
                    "sub_text": "Visual metaphor for 'usable anywhere'",
                    "audio_url": "/static/audio/it_salve_13.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Pairs",
                    "pairs": [["Grazie", "Thanks"], ["Prego", "You're welcome"]],
                    "correct_answer": "match_all",
                    "explanation": "Teaches the polite response pair"
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "A coffee, please.",
                    "blocks": ["caffè", "Un", "favore", "per"],
                    "correct_answer": "Un caffè, per favore",
                    "explanation": "Noun + Polite Marker placement"
                },
                {
                    "type": "info_card",
                    "step": 4,
                    "prompt": "Cultural Note",
                    "correct_answer": "Italian Coffee Culture - 'Un Caffè, Per Favore'",
                    "table": {
                        "headers": ["Italian", "English", "Description", "When to Order"],
                        "rows": [
                            ["Caffè", "Espresso", "Small, strong shot", "Any time"],
                            ["Caffè americano", "American coffee", "Diluted espresso", "Any time"],
                            ["Cappuccino", "Cappuccino", "Milk-based drink", "Breakfast ONLY (before 11 AM)"],
                            ["Caffè macchiato", "Stained espresso", "Espresso with a drop of milk", "Any time"]
                        ]
                    },
                    "explanation": "Italians typically drink coffee at the bar counter, standing up, and it takes less than 5 minutes.",
                    "sub_text": "Ordering a cappuccino after lunch marks you as a tourist!",
                    "cultural_note": True
                },
                {
                    "type": "listening_comprehension",
                    "step": 5,
                    "prompt": "Listen. What polite expression did you hear?",
                    "audio_text": "Salve, per favore.",
                    "options": ["Salve", "Ciao", "Buongiorno", "Arrivederci"],
                    "correct_answer": "Salve",
                    "explanation": "You heard 'Salve', the safe, neutral greeting that works in any situation.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat after me",
                    "target_phrase": "A presto",
                    "target_lang": "it",
                    "explanation": "Testing the 'Pre' cluster sound"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You are leaving a shop.",
                    "context": "You are leaving a shop.",
                    "task": "Say goodbye politely.",
                    "target_lang": "it",
                    "explanation": "Think about how to say goodbye politely in Italian. What phrases have you learned for polite closings?"
                },
                {
                    "type": "free_writing",
                    "step": 8,
                    "prompt": "Write a polite goodbye message.",
                    "context": "You are leaving a shop after buying something.",
                    "task": "Write 1-2 sentences saying goodbye politely. Include a thank you.",
                    "target_lang": "it",
                    "required_elements": ["goodbye", "thank you"],
                    "example_response": "Grazie! Arrivederci!",
                    "validation_mode": "ai",
                    "explanation": "Great! You used polite expressions correctly. 'Grazie' (thank you) and 'Arrivederci' (goodbye) are perfect for leaving a shop."
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Review: Match the polite expressions",
                    "pairs": [["Salve", "Hello (Safe/Neutral)"], ["Per favore", "Please"], ["Prego", "You're welcome"], ["A presto", "See you soon"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the polite expressions.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.5",
            "title": "Subject Pronouns & The Verb 'To Be'",
            "focus": "Subject pronouns (Io, Tu, Lui, Lei) and 'Essere' conjugation",
            "vocabulary": [
                {"term": "Io", "translation": "I"},
                {"term": "Tu", "translation": "You (informal)"},
                {"term": "Lui", "translation": "He"},
                {"term": "Lei", "translation": "She"},
                {"term": "Sono", "translation": "I am"},
                {"term": "Sei", "translation": "You are"},
                {"term": "È", "translation": "He/She is"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Io",
                    "explanation": "I (subject pronoun)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_io_14.mp3",
                    "image_url": "/images/topics/greetings-12.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Tu",
                    "explanation": "You (informal, singular)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tu_15.mp3",
                    "image_url": "/images/topics/greetings-13.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Lui",
                    "explanation": "He (subject pronoun)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_lui_16.mp3",
                    "image_url": "/images/topics/appearance-8.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Lei",
                    "explanation": "She (subject pronoun) - Note: Same spelling as formal 'You'",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_lei_17.mp3",
                    "image_url": "/images/topics/appearance-2.jpg"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Pronouns to English",
                    "pairs": [["Io", "I"], ["Tu", "You"], ["Lui", "He"], ["Lei", "She"]],
                    "correct_answer": "match_all",
                    "explanation": "Connect Italian pronouns with their English meanings"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the dialogue and answer the question.",
                    "text": "Persona 1: Chi sei?\nPersona 2: Io sono Maria. E tu?\nPersona 1: Io sono Luca.",
                    "question": "What does 'Io sono' mean?",
                    "options": ["I am", "You are", "He is", "We are"],
                    "correct_answer": "I am",
                    "explanation": "'Io sono' means 'I am' in Italian. It's used to introduce yourself or describe yourself.",
                    "highlight_vocab": ["Chi sei", "Io sono", "E tu"]
                },
                {
                    "type": "info_card",
                    "step": 4,
                    "prompt": "Grammar: The Verb 'Essere' (To Be)",
                    "correct_answer": "Essere (To Be)",
                    "table": {
                        "headers": ["Italian", "English"],
                        "rows": [
                            ["Io sono", "I am"],
                            ["Tu sei", "You are"],
                            ["Lui/Lei è", "He/She is"]
                        ]
                    },
                    "sub_text": "Learn how to say 'I am', 'You are', 'He/She is'",
                    "image_url": "/images/topics/appearance-11.jpg"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "I am Italian.",
                    "blocks": ["Io", "sono", "italiano"],
                    "correct_answer": "Io sono italiano.",
                    "explanation": "Subject pronoun + verb + adjective. Teaches word order with 'essere'"
                },
                {
                    "type": "unscramble",
                    "step": 6,
                    "prompt": "You are well.",
                    "blocks": ["Tu", "sei", "bene"],
                    "correct_answer": "Tu sei bene.",
                    "explanation": "Practice 'tu sei' form"
                },
                {
                    "type": "echo_chamber",
                    "step": 7,
                    "prompt": "Repeat: Io sono",
                    "target_phrase": "Io sono",
                    "target_lang": "it",
                    "explanation": "Practice 'I am' - focus on the 'o' sound in 'sono'"
                },
                {
                    "type": "echo_chamber",
                    "step": 8,
                    "prompt": "Repeat: Lui è",
                    "target_phrase": "Lui è",
                    "target_lang": "it",
                    "explanation": "Practice 'He is' - focus on the open 'è' sound"
                },
                {
                    "type": "fill_blank",
                    "step": 9,
                    "prompt": "Complete: '___ sono Maria.'",
                    "options": ["Io", "Tu", "Lui"],
                    "correct_answer": "Io",
                    "explanation": "Choose the correct subject pronoun for 'I am'"
                },
                {
                    "type": "fill_blank",
                    "step": 10,
                    "prompt": "Complete: 'Lui ___ italiano.'",
                    "options": ["sono", "sei", "è"],
                    "correct_answer": "è",
                    "explanation": "Choose the correct verb form for 'he'"
                },
                {
                    "type": "mini_prompt",
                    "step": 11,
                    "prompt": "Someone asks: 'Chi sei?' (Who are you?)",
                    "context": "Someone asks: 'Chi sei?' (Who are you?)",
                    "task": "Respond with your name using 'Io sono'.",
                    "target_lang": "it",
                    "explanation": "Use 'Io sono' followed by your name to answer 'Who are you?'"
                },
                {
                    "type": "match",
                    "step": 12,
                    "prompt": "Review: Match the pronouns and verb forms",
                    "pairs": [["Io", "I"], ["Tu", "You"], ["Lui", "He"], ["Lei", "She"], ["Io sono", "I am"], ["Tu sei", "You are"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered all the pronouns and their 'essere' forms.",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.6",
            "title": "Introduction to Nouns",
            "focus": "Singular nouns, gender (masculine/feminine), basic patterns",
            "vocabulary": [
                {"term": "caffè", "translation": "coffee (masculine)"},
                {"term": "casa", "translation": "house (feminine)"},
                {"term": "amico", "translation": "friend (masculine)"},
                {"term": "amica", "translation": "friend (feminine)"},
                {"term": "libro", "translation": "book (masculine)"},
                {"term": "penna", "translation": "pen (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Nouns Have Gender",
                    "correct_answer": "Maschile & Femminile",
                    "explanation": "Italian nouns are either masculine (il) or feminine (la)",
                    "sub_text": "Learn about noun gender",
                    "image_url": "/images/topics/appearance-12.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "caffè",
                    "explanation": "coffee (masculine - ends in -è)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_caffe_18.mp3",
                    "image_url": "/images/topics/food-1.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "casa",
                    "explanation": "house (feminine - ends in -a)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_casa_19.mp3",
                    "image_url": "/images/topics/lifestyle-4.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "amico",
                    "explanation": "friend (masculine - ends in -o)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_amico_20.mp3",
                    "image_url": "/images/topics/greetings-5.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "amica",
                    "explanation": "friend (feminine - ends in -a)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_amica_21.mp3",
                    "image_url": "/images/topics/greetings-7.jpg"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Drag each word to the correct gender column",
                    "words": ["caffè", "casa", "amico", "amica"],
                    "correct_answers": {
                        "caffè": "maschile",
                        "casa": "femminile",
                        "amico": "maschile",
                        "amica": "femminile"
                    },
                    "correct_answer": "all_correct",
                    "explanation": "Learn to identify noun gender: words ending in -o/-è are usually masculine, words ending in -a are usually feminine"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "What gender is 'libro' (book)?",
                    "options": ["Maschile", "Femminile"],
                    "correct_answer": "Maschile",
                    "explanation": "Words ending in -o are usually masculine"
                },
                {
                    "type": "multiple_choice",
                    "step": 2,
                    "prompt": "What gender is 'penna' (pen)?",
                    "options": ["Maschile", "Femminile"],
                    "correct_answer": "Femminile",
                    "explanation": "Words ending in -a are usually feminine"
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "A coffee, please.",
                    "blocks": ["Un", "caffè", "per", "favore"],
                    "correct_answer": "Un caffè, per favore",
                    "explanation": "Practice noun + article. 'Un' is used with masculine nouns"
                },
                {
                    "type": "unscramble",
                    "step": 3,
                    "prompt": "The house is big.",
                    "blocks": ["La", "casa", "è", "grande"],
                    "correct_answer": "La casa è grande.",
                    "explanation": "Practice noun + article. 'La' is used with feminine nouns"
                },
                {
                    "type": "echo_chamber",
                    "step": 4,
                    "prompt": "Repeat: un caffè",
                    "target_phrase": "un caffè",
                    "target_lang": "it",
                    "explanation": "Practice masculine noun with article"
                },
                {
                    "type": "echo_chamber",
                    "step": 4,
                    "prompt": "Repeat: la casa",
                    "target_phrase": "la casa",
                    "target_lang": "it",
                    "explanation": "Practice feminine noun with article"
                },
                {
                    "type": "fill_blank",
                    "step": 4,
                    "prompt": "Complete: '___ caffè' (a coffee)",
                    "options": ["Un", "Una"],
                    "correct_answer": "Un",
                    "explanation": "Choose the correct article for masculine noun"
                },
                {
                    "type": "fill_blank",
                    "step": 4,
                    "prompt": "Complete: '___ casa' (the house)",
                    "options": ["Il", "La"],
                    "correct_answer": "La",
                    "explanation": "Choose the correct article for feminine noun"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "A coffee, please.",
                    "blocks": ["Un", "caffè", "per", "favore"],
                    "correct_answer": "Un caffè, per favore",
                    "explanation": "Practice noun + article. 'Un' is used with masculine nouns",
                    "common_mistakes": [
                        {
                            "pattern": "una caffè",
                            "explanation": "Remember: 'caffè' is masculine, so use 'un' (not 'una'). 'Una' is for feminine nouns."
                        },
                        {
                            "pattern": "caffè per favore",
                            "explanation": "Good! But don't forget the article 'un' before 'caffè'. In Italian, nouns usually need an article."
                        }
                    ]
                },
                {
                    "type": "mini_prompt",
                    "step": 6,
                    "prompt": "You're in a café. You want to order a coffee.",
                    "context": "You're in a café. You want to order a coffee.",
                    "task": "Order a coffee using the noun you learned.",
                    "target_lang": "it",
                    "explanation": "Use 'un caffè' to order a coffee. Remember: 'caffè' is masculine, so use 'un'."
                },
                {
                    "type": "match",
                    "step": 7,
                    "prompt": "Review: Match the nouns and their gender",
                    "pairs": [["caffè", "coffee (masculine)"], ["casa", "house (feminine)"], ["amico", "friend (masculine)"], ["amica", "friend (feminine)"]],
                    "correct_answer": "match_all",
                    "explanation": "Great review! You remembered the nouns and their genders.",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "Cultural Note",
                    "correct_answer": "Pronunciation: Double Consonants Change Meaning",
                    "explanation": "In Italian, double consonants are pronounced longer and can completely change word meanings:\n\n• Pena (sorrow) vs. Penna (pen)\n• Caro (dear/expensive) vs. Carro (cart)\n• Nono (ninth) vs. Nonno (grandfather)\n\nHold the consonant sound twice as long when you see double letters. This distinction is crucial and natives will notice!",
                    "sub_text": "Practice makes perfect - exaggerate at first, then refine.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.1.7",
            "title": "Where Are You From? (Countries & Nationalities)",
            "focus": "Asking about origin, countries, and nationalities",
            "vocabulary": [
                {"term": "Di dove sei?", "translation": "Where are you from? (Informal)"},
                {"term": "Di dove è?", "translation": "Where are you from? (Formal)"},
                {"term": "Sono di", "translation": "I'm from"},
                {"term": "Italia", "translation": "Italy"},
                {"term": "italiano", "translation": "Italian (masculine)"},
                {"term": "italiana", "translation": "Italian (feminine)"},
                {"term": "Francia", "translation": "France"},
                {"term": "francese", "translation": "French"},
                {"term": "Spagna", "translation": "Spain"},
                {"term": "spagnolo", "translation": "Spanish (masculine)"},
                {"term": "spagnola", "translation": "Spanish (feminine)"},
                {"term": "Stati Uniti", "translation": "United States"},
                {"term": "americano", "translation": "American (masculine)"},
                {"term": "americana", "translation": "American (feminine)"},
                {"term": "Regno Unito", "translation": "United Kingdom"},
                {"term": "inglese", "translation": "English"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Di dove sei?",
                    "explanation": "Where are you from? (Informal - use with friends)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_di_dove_sei_22.mp3",
                    "image_url": "/images/topics/default-1.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Sono di",
                    "explanation": "I'm from (used with country name)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sono_di_23.mp3",
                    "image_url": "/images/topics/country-2.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Italia",
                    "explanation": "Italy",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_italia_24.mp3",
                    "image_url": "/images/topics/country-3.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Francia",
                    "explanation": "France",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_francia_29.mp3",
                    "image_url": "/images/topics/france.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Spagna",
                    "explanation": "Spain",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_spagna_30.mp3",
                    "image_url": "/images/topics/spain.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Stati Uniti",
                    "explanation": "United States",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_stati_uniti_31.mp3",
                    "image_url": "/images/topics/usa.jpg"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "Regno Unito",
                    "explanation": "United Kingdom",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_regno_unito_27.mp3",
                    "image_url": "/images/topics/uk.jpg"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Countries to English",
                    "pairs": [["Italia", "Italy"], ["Francia", "France"], ["Spagna", "Spain"], ["Stati Uniti", "United States"], ["Regno Unito", "United Kingdom"]],
                    "correct_answer": "match_all",
                    "explanation": "Match each Italian country name with its English translation"
                },
                {
                    "type": "info_card",
                    "step": 3,
                    "prompt": "Cultural Note",
                    "correct_answer": "Alternative Names for Countries",
                    "explanation": "Some countries have multiple names or components that Italians refer to:\n\n**Regno Unito (United Kingdom):**\nThe UK is made up of four countries:\n• Inghilterra (England)\n• Scozia (Scotland)\n• Galles (Wales)\n• Irlanda del Nord (Northern Ireland)\n\nYou might also hear 'Gran Bretagna' (Great Britain), which refers to the island containing England, Scotland, and Wales.\n\nPeople often say 'Sono di Inghilterra' (I'm from England) or 'Sono di Scozia' (I'm from Scotland) instead of 'Sono di Regno Unito'.\n\n**Stati Uniti (United States):**\nItalians commonly use:\n• America (very common in conversation)\n• USA (used in writing)\n• Stati Uniti d'America (full formal name)\n\nSo you'll hear 'Sono di Stati Uniti', 'Sono di America', or 'Sono degli Stati Uniti' - they're all correct!",
                    "sub_text": "Understanding these alternatives helps you sound more natural in Italian.",
                    "image_url": "/images/topics/default-2.jpg",
                    "cultural_note": True
                },
                {
                    "type": "reading_comprehension",
                    "step": 4,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Marco: Di dove sei?\nSofia: Sono di Italia. E tu?\nMarco: Sono di Francia.",
                    "question": "Where is Sofia from?",
                    "options": ["Italia", "Francia", "Spagna", "Stati Uniti"],
                    "correct_answer": "Italia",
                    "explanation": "Sofia says 'Sono di Italia' which means 'I'm from Italy'.",
                    "highlight_vocab": ["Di dove sei", "Sono di", "Italia", "Francia"]
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "I'm from Italy.",
                    "blocks": ["Sono", "di", "Italia"],
                    "correct_answer": "Sono di Italia.",
                    "explanation": "Practice saying where you're from: Sono + di + country"
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "Where are you from? (Informal)",
                    "blocks": ["dove", "Di", "sei"],
                    "correct_answer": "Di dove sei?",
                    "explanation": "Question word order: Di dove + sei"
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Di dove sei?",
                    "target_phrase": "Di dove sei?",
                    "target_lang": "it",
                    "explanation": "Practice asking where someone is from"
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Sono di Italia",
                    "target_phrase": "Sono di Italia",
                    "target_lang": "it",
                    "explanation": "Practice saying where you're from"
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: '___ dove sei?' (Where are you from?)",
                    "options": ["Di", "Da", "In"],
                    "correct_answer": "Di",
                    "explanation": "Use 'Di' when asking about origin"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Sono ___ Italia.' (I'm from Italy)",
                    "options": ["di", "da", "in"],
                    "correct_answer": "di",
                    "explanation": "Use 'di' when saying where you're from"
                },
                {
                    "type": "form_fill",
                    "step": 11,
                    "prompt": "Fill out this registration form with your information.",
                    "form_fields": [
                        {
                            "label": "Nome (Name)",
                            "type": "text",
                            "required": True,
                            "validation": "name",
                            "hint": "Use 'Mi chiamo [name]' or 'Sono [name]' format"
                        },
                        {
                            "label": "Nazionalità (Nationality)",
                            "type": "select",
                            "options": ["italiano", "italiana", "francese", "spagnolo", "spagnola", "americano", "americana", "inglese"],
                            "required": True
                        },
                        {
                            "label": "Di dove sei? (Where are you from?)",
                            "type": "text",
                            "required": True,
                            "validation": "origin",
                            "hint": "Use 'Sono di [country]' format"
                        }
                    ],
                    "correct_answer": "all_fields_filled",
                    "explanation": "Perfect! You filled out all the required information correctly."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks you: 'Di dove sei?'",
                    "context": "Someone asks you: 'Di dove sei?' (Where are you from?)",
                    "task": "Respond by saying where you're from.",
                    "target_lang": "it",
                    "explanation": "Use 'Sono di' followed by a country name. For example: 'Sono di Italia' or 'Sono di Stati Uniti'"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "Grammar: Gender Patterns in Italian",
                    "correct_answer": "Nationality Adjectives",
                    "explanation": "Many Italian nationality adjectives change endings based on gender. Look for these patterns:",
                    "tables": [
                        {
                            "title": "Masculine Forms (end in -o)",
                            "headers": ["Singular", "Translation"],
                            "rows": [
                                ["italiano", "Italian man"],
                                ["spagnolo", "Spanish man"],
                                ["americano", "American man"]
                            ]
                        },
                        {
                            "title": "Feminine Forms (end in -a)",
                            "headers": ["Singular", "Translation"],
                            "rows": [
                                ["italiana", "Italian woman"],
                                ["spagnola", "Spanish woman"],
                                ["americana", "American woman"]
                            ]
                        },
                        {
                            "title": "Plural Forms",
                            "headers": ["Masculine", "Feminine"],
                            "rows": [
                                ["italiani", "italiane"],
                                ["spagnoli", "spagnole"],
                                ["americani", "americane"]
                            ]
                        }
                    ],
                    "sub_text": "Understanding gender patterns helps you use the right form.",
                    "image_url": "/images/topics/appearance-11.jpg",
                    "cultural_note": False
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "italiano",
                    "explanation": "Italian (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_italiano_25.mp3",
                    "image_url": "/images/topics/italiano.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "italiana",
                    "explanation": "Italian (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_italiana_26.mp3",
                    "image_url": "/images/topics/italiana.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "spagnolo",
                    "explanation": "Spanish (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_spagnolo_33.mp3",
                    "image_url": "/images/topics/spagnolo.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "spagnola",
                    "explanation": "Spanish (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_spagnola_34.mp3",
                    "image_url": "/images/topics/spagnola.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "americano",
                    "explanation": "American (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_americano_35.mp3",
                    "image_url": "/images/topics/americano.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "americana",
                    "explanation": "American (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_americana_36.mp3",
                    "image_url": "/images/topics/americana.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "Grammar: Nationality Adjectives with -e",
                    "correct_answer": "Adjectives for Both Genders",
                    "explanation": "Some nationality adjectives end in -e and work for BOTH masculine and feminine. They are easier to use because you don't need to change them for gender!",
                    "tables": [
                        {
                            "title": "Singular (same form for both genders)",
                            "headers": ["Form", "Translation"],
                            "rows": [
                                ["francese", "French (masculine or feminine)"],
                                ["inglese", "English (masculine or feminine)"]
                            ]
                        },
                        {
                            "title": "Plural (add -i for both genders)",
                            "headers": ["Form", "Translation"],
                            "rows": [
                                ["francesi", "French people (any gender)"],
                                ["inglesi", "English people (any gender)"]
                            ]
                        }
                    ],
                    "sub_text": "These adjectives work the same for all genders!",
                    "cultural_note": False
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "francese",
                    "explanation": "French",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_francese_32.mp3",
                    "image_url": "/images/topics/french.jpg"
                },
                {
                    "type": "info_card",
                    "step": 8,
                    "prompt": "New Word",
                    "correct_answer": "inglese",
                    "explanation": "English",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_inglese_28.mp3",
                    "image_url": "/images/topics/english.jpg"
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Match Nationalities to English",
                    "pairs": [["italiano", "Italian (masculine)"], ["italiana", "Italian (feminine)"], ["francese", "French"], ["spagnolo", "Spanish (masculine)"], ["spagnola", "Spanish (feminine)"], ["americano", "American (masculine)"], ["americana", "American (feminine)"], ["inglese", "English"]],
                    "correct_answer": "match_all",
                    "explanation": "Match each Italian nationality with its English translation"
                },
                {
                    "type": "gender_categorize",
                    "step": 10,
                    "prompt": "Drag each word to the correct column: Maschile, Femminile, or BOTH (for adjectives that work for all genders)",
                    "words": ["italiano", "italiana", "francese", "spagnolo", "spagnola", "americano", "americana", "inglese"],
                    "correct_answers": {
                        "italiano": "maschile",
                        "italiana": "femminile",
                        "francese": "both",
                        "spagnolo": "maschile",
                        "spagnola": "femminile",
                        "americano": "maschile",
                        "americana": "femminile",
                        "inglese": "both"
                    },
                    "correct_answer": "all_correct",
                    "explanation": "Perfect! You remembered the patterns:\n\n**Maschile (-o):** italiano, spagnolo, americano\n**Femminile (-a):** italiana, spagnola, americana\n**BOTH (-e):** francese, inglese\n\nAs you learned in the grammar cards:\n• Adjectives ending in -o are masculine only\n• Adjectives ending in -a are feminine only\n• Adjectives ending in -e work for both masculine and feminine!\n\nThis is why francese and inglese belong in the BOTH category - they describe people of any gender the same way."
                },
                {
                    "type": "reading_comprehension",
                    "step": 12,
                    "prompt": "Read this conversation and answer the question.",
                    "text": "Marco: Tu che nazionalità hai?\nSofia: Sono italiana. E tu?\nMarco: Io sono francese.",
                    "question": "What nationality is Sofia?",
                    "options": ["italiana", "francese", "spagnola", "americana"],
                    "correct_answer": "italiana",
                    "explanation": "Sofia says 'Sono italiana' which means 'I am Italian (feminine)'.",
                    "highlight_vocab": ["nazionalità", "Sono italiana", "francese"]
                },
                {
                    "type": "mini_prompt",
                    "step": 13,
                    "prompt": "Someone asks you: 'Che nazionalità hai?' (What nationality are you?)",
                    "context": "Someone asks you your nationality.",
                    "task": "Respond with your nationality.",
                    "target_lang": "it",
                    "explanation": "Use 'Sono' followed by the appropriate nationality adjective. For example: 'Sono italiano' (if male) or 'Sono italiana' (if female), 'Sono francese', 'Sono spagnolo/spagnola', etc."
                },
                {
                    "type": "free_writing",
                    "step": 14,
                    "prompt": "Write a complete introduction about yourself.",
                    "context": "You're meeting someone new at a language exchange event.",
                    "task": "Write 2-3 sentences introducing yourself. Include: your name, where you're from, your greeting, and your nationality.",
                    "target_lang": "it",
                    "required_elements": ["name", "greeting", "origin", "nationality"],
                    "example_response": "Ciao! Mi chiamo Maria. Sono di Italia e sono italiana.",
                    "validation_mode": "ai",
                    "explanation": "Excellent! You included your name, a greeting, where you're from, and your nationality. Perfect introduction!"
                },
                {
                    "type": "match",
                    "step": 15,
                    "prompt": "Review: Match all the greetings, introductions, and nationalities you've learned",
                    "pairs": [
                        ["Ciao", "Hi/Bye"],
                        ["Buongiorno", "Good morning"],
                        ["Mi chiamo", "My name is"],
                        ["Di dove sei?", "Where are you from?"],
                        ["Sono di", "I'm from"],
                        ["italiano", "Italian (masculine)"],
                        ["italiana", "Italian (feminine)"],
                        ["francese", "French"],
                        ["spagnolo", "Spanish (masculine)"]
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
                    "task": "Use: greeting, introduction with name and origin, asking 'Di dove sei?', asking about nationality, and responding with your nationality.",
                    "target_lang": "it",
                    "extension": True,
                    "optional": True,
                    "explanation": "Excellent! You used all the required elements including nationality in a natural conversation."
                }
            ]
        },
        {
            "lesson_id": "A1.1.BOSS",
            "title": "Conversation Practice: Meeting a Neighbor - Informal & Formal",
            "type": "conversation_challenge",
            "focus": "Casual but polite greeting conversation",
            "vocabulary": [
                {"term": "Ciao", "translation": "Hi/Bye"},
                {"term": "Buongiorno", "translation": "Good morning (Formal)"},
                {"term": "Buonasera", "translation": "Good evening (Formal)"},
                {"term": "Salve", "translation": "Hello (Safe/Neutral)"},
                {"term": "Come stai?", "translation": "How are you? (Informal)"},
                {"term": "Come sta?", "translation": "How are you? (Formal)"},
                {"term": "Grazie", "translation": "Thank you"},
                {"term": "Arrivederci", "translation": "Goodbye (Formal)"},
                {"term": "A presto", "translation": "See you soon"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You meet your neighbor Signora Rossi on the street.",
                    "scenario": "neighbor",
                    "ai_prompt": "You are Signora Rossi, a friendly neighbor. Keep the conversation casual but polite. Use informal greetings.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Informal Conversation",
                            "round_description": "Have a casual conversation with your neighbor Signora Rossi",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao!",
                                    "user_requirement": "Respond with any greeting",
                                    "required_words": ["Ciao", "Buongiorno", "Buonasera", "Salve"],
                                    "hints": ["Ciao", "Salve"],
                                    "invalid_responses": ["Ciao! Come stai?", "Salve! Come va?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Come stai?",
                                    "user_requirement": "Respond with how you are AND ask back",
                                    "required_words": ["Bene", "E tu?"],
                                    "hints": ["Bene", "E tu?"],
                                    "invalid_responses": ["Bene! E tu?", "Sto bene! Come stai tu?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene anche io! Piacere! Come ti chiami?",
                                    "user_requirement": "Introduce yourself",
                                    "required_words": ["Mi chiamo", "Sono"],
                                    "hints": ["Mi chiamo [name]", "Sono [name]"],
                                    "invalid_responses": ["Piacere! Mi chiamo...", "Il mio nome è..."]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Piacere! A presto!",
                                    "user_requirement": "Say goodbye politely",
                                    "required_words": ["Grazie", "A presto", "Ciao"],
                                    "hints": ["Grazie", "A presto", "Ciao"],
                                    "invalid_responses": ["Grazie! A presto!", "Perfetto! Ciao!"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Formal Conversation",
                            "round_description": "Have a formal conversation with Professor Bianchi",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Come posso aiutarla?",
                                    "user_requirement": "Respond with formal greeting",
                                    "required_words": ["Buongiorno", "Buonasera", "Salve"],
                                    "hints": ["Buongiorno", "Buonasera", "Salve"],
                                    "invalid_responses": ["Ciao!", "Buongiorno! Come stai?"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Come sta?",
                                    "user_requirement": "Respond formally AND ask back",
                                    "required_words": ["Sto bene", "E Lei?"],
                                    "hints": ["Sto bene", "E Lei?"],
                                    "invalid_responses": ["Bene! E tu?", "Sto bene! Come stai tu?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Sto bene, grazie. E Lei, come si chiama?",
                                    "user_requirement": "Respond formally AND introduce yourself",
                                    "required_words": ["Mi chiamo", "E Lei?"],
                                    "hints": ["Mi chiamo [name]", "E Lei?"],
                                    "invalid_responses": ["Bene! Mi chiamo... E tu?", "Sto bene! Il mio nome è...", "Mi chiamo... E tu?"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Mi chiamo Professor Bianchi. Piacere di conoscerla! Arrivederci!",
                                    "user_requirement": "Say goodbye formally",
                                    "required_words": ["Grazie", "Arrivederci"],
                                    "hints": ["Arrivederci", "Grazie"],
                                    "invalid_responses": ["Grazie! Ciao!", "Grazie mille! A presto!", "Ciao!"]
                                }
                            ]
                        }
                    ],
                    "explanation": "Complete both informal and formal greeting conversations using the greetings you've learned"
                }
            ]
        }
    ]
}

