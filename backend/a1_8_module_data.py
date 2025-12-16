"""
Module A1.8 data structure - Descriptions & Appearance
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_8_LESSONS = {
    "module_id": "A1.8",
    "title": "Descriptions & Appearance",
    "goal": "Describe people's physical appearance and personality, express likes and preferences using adjective agreement and the verb 'Piacere'.",
    "lessons": [
        {
            "lesson_id": "A1.8.0",
            "title": "Self-Assessment: Descriptions & Appearance",
            "focus": "Assess your confidence with describing people",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel describing people's appearance and personality?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can describe physical appearance (height, build)",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe hair and eye color",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe personality traits",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can express what I like using 'Mi piace'",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.8.1",
            "title": "Physical Description (Basics)",
            "focus": "Height, Age, Build (Essere + Adjective)",
            "vocabulary": [
                {"term": "alto", "translation": "tall (masculine)"},
                {"term": "alta", "translation": "tall (feminine)"},
                {"term": "basso", "translation": "short (masculine)"},
                {"term": "bassa", "translation": "short (feminine)"},
                {"term": "magro", "translation": "thin"},
                {"term": "grasso", "translation": "fat"},
                {"term": "giovane", "translation": "young"},
                {"term": "vecchio", "translation": "old (masculine)"},
                {"term": "bello", "translation": "beautiful/handsome (masculine)"},
                {"term": "brutto", "translation": "ugly (masculine)"},
                {"term": "è", "translation": "is"},
                {"term": "sembra", "translation": "he/she seems"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Adjective Agreement",
                    "correct_answer": "Gender Agreement",
                    "explanation": "Adjectives must agree with the noun they describe:\n\nMasculine: alto (tall), bello (beautiful)\nFeminine: alta (tall), bella (beautiful)\n\nExamples:\n- Lui è alto (He is tall)\n- Lei è alta (She is tall)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "alto",
                    "explanation": "tall (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_alto_183.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "alta",
                    "explanation": "tall (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_alta_184.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "basso",
                    "explanation": "short (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_basso_185.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "magro",
                    "explanation": "thin",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_magro_186.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Physical Descriptions",
                    "pairs": [["alto", "tall (masc)"], ["alta", "tall (fem)"], ["basso", "short (masc)"], ["magro", "thin"], ["grasso", "fat"]],
                    "correct_answer": "match_all",
                    "explanation": "Physical description vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How is the person described?",
                    "audio_text": "Lui è alto e magro.",
                    "options": ["tall and thin", "short and fat", "tall and fat", "short and thin"],
                    "correct_answer": "tall and thin",
                    "explanation": "You heard 'alto e magro' (tall and thin).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "She is tall and beautiful.",
                    "blocks": ["Lei", "è", "alta", "e", "bella"],
                    "correct_answer": "Lei è alta e bella.",
                    "explanation": "Use 'Lei è' + adjective (feminine) + 'e' + adjective (feminine)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Lui è alto",
                    "target_phrase": "Lui è alto",
                    "target_lang": "it",
                    "explanation": "Practice describing people"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Lei è ___.' (tall - feminine)",
                    "options": ["alto", "alta", "alti", "alte"],
                    "correct_answer": "alta",
                    "explanation": "Use 'alta' (feminine) with feminine subjects like 'Lei'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Lui è ___.' (tall - masculine)",
                    "options": ["alto", "alta", "alti", "alte"],
                    "correct_answer": "alto",
                    "explanation": "Use 'alto' (masculine) with masculine subjects like 'Lui'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Com'è lui?'",
                    "context": "He is tall and thin.",
                    "task": "Describe him.",
                    "target_lang": "it",
                    "explanation": "Say 'Lui è alto e magro.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match physical descriptions",
                    "pairs": [["alto", "tall (masc)"], ["alta", "tall (fem)"], ["magro", "thin"], ["bello", "beautiful"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.2",
            "title": "Hair & Eyes (Avere + Noun + Adj)",
            "focus": "Describing features (Plural Agreement)",
            "vocabulary": [
                {"term": "capelli", "translation": "hair"},
                {"term": "occhi", "translation": "eyes"},
                {"term": "lunghi", "translation": "long (masculine plural)"},
                {"term": "corti", "translation": "short (masculine plural)"},
                {"term": "biondi", "translation": "blonde (masculine plural)"},
                {"term": "neri", "translation": "black (masculine plural)"},
                {"term": "castani", "translation": "brown (masculine plural)"},
                {"term": "azzurri", "translation": "blue (masculine plural)"},
                {"term": "verdi", "translation": "green (masculine plural)"},
                {"term": "ha", "translation": "he/she has"},
                {"term": "i", "translation": "the (masculine plural)"},
                {"term": "gli", "translation": "the (masculine plural - before vowels)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Describing Hair and Eyes",
                    "correct_answer": "Avere + Noun + Adjective",
                    "explanation": "Use 'Avere' (to have) to describe hair and eyes:\n\nHa i capelli biondi (He/She has blonde hair)\nHa gli occhi azzurri (He/She has blue eyes)\n\nNote: 'Capelli' and 'occhi' are always plural, so adjectives must be plural too.",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "capelli",
                    "explanation": "hair",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_capelli_187.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "occhi",
                    "explanation": "eyes",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_occhi_188.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "biondi",
                    "explanation": "blonde (masculine plural)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_biondi_189.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "neri",
                    "explanation": "black (masculine plural)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_neri_190.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Hair and Eye Colors",
                    "pairs": [["capelli", "hair"], ["occhi", "eyes"], ["biondi", "blonde"], ["neri", "black"], ["azzurri", "blue"]],
                    "correct_answer": "match_all",
                    "explanation": "Hair and eye vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What color hair does the person have?",
                    "audio_text": "Ha i capelli biondi.",
                    "options": ["blonde", "black", "brown", "red"],
                    "correct_answer": "blonde",
                    "explanation": "You heard 'capelli biondi' (blonde hair).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "He has black hair and blue eyes.",
                    "blocks": ["Ha", "i", "capelli", "neri", "e", "gli", "occhi", "azzurri"],
                    "correct_answer": "Ha i capelli neri e gli occhi azzurri.",
                    "explanation": "Use 'Ha' + article + noun (plural) + adjective (plural)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ha i capelli biondi",
                    "target_phrase": "Ha i capelli biondi",
                    "target_lang": "it",
                    "explanation": "Practice describing hair"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ha i capelli ___.' (long - plural)",
                    "options": ["lunghi", "lungo", "lunga", "lunghe"],
                    "correct_answer": "lunghi",
                    "explanation": "Use 'lunghi' (plural) with plural nouns like 'capelli'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ha gli occhi ___.' (green - plural)",
                    "options": ["verdi", "verde", "verda", "verdo"],
                    "correct_answer": "verdi",
                    "explanation": "Use 'verdi' (plural) with plural nouns like 'occhi'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Com'è? Ha i capelli lunghi o corti?'",
                    "context": "She has long brown hair.",
                    "task": "Describe her hair.",
                    "target_lang": "it",
                    "explanation": "Say 'Ha i capelli lunghi e castani.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match hair and eyes",
                    "pairs": [["capelli", "hair"], ["occhi", "eyes"], ["biondi", "blonde"], ["neri", "black"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.3",
            "title": "Personality & Character",
            "focus": "Describing internal traits",
            "vocabulary": [
                {"term": "simpatico", "translation": "nice/likeable (masculine)"},
                {"term": "antipatico", "translation": "unpleasant (masculine)"},
                {"term": "gentile", "translation": "kind"},
                {"term": "intelligente", "translation": "intelligent"},
                {"term": "divertente", "translation": "funny"},
                {"term": "serio", "translation": "serious"},
                {"term": "timido", "translation": "shy"},
                {"term": "aperto", "translation": "open/outgoing"},
                {"term": "persona", "translation": "person"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "simpatico",
                    "explanation": "nice/likeable (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_simpatico_191.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "gentile",
                    "explanation": "kind",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_gentile_192.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "intelligente",
                    "explanation": "intelligent",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_intelligente_193.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "divertente",
                    "explanation": "funny",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_divertente_194.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "serio",
                    "explanation": "serious",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_serio_195.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Personality Traits",
                    "pairs": [["simpatico", "nice"], ["gentile", "kind"], ["intelligente", "intelligent"], ["divertente", "funny"], ["serio", "serious"]],
                    "correct_answer": "match_all",
                    "explanation": "Personality vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How is the person described?",
                    "audio_text": "È una persona molto simpatica.",
                    "options": ["very nice", "very serious", "very shy", "very intelligent"],
                    "correct_answer": "very nice",
                    "explanation": "You heard 'molto simpatica' (very nice - feminine).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "He is a very kind person.",
                    "blocks": ["È", "una", "persona", "molto", "gentile"],
                    "correct_answer": "È una persona molto gentile.",
                    "explanation": "Use 'È' + article + 'persona' + adverb + adjective."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: È una persona simpatica",
                    "target_phrase": "È una persona simpatica",
                    "target_lang": "it",
                    "explanation": "Practice describing personality"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'È una persona ___.' (nice - feminine)",
                    "options": ["simpatico", "simpatica", "simpatici", "simpatiche"],
                    "correct_answer": "simpatica",
                    "explanation": "Use 'simpatica' (feminine) with feminine nouns like 'persona'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'È una persona ___.' (serious - feminine)",
                    "options": ["serio", "seria", "seri", "serie"],
                    "correct_answer": "seria",
                    "explanation": "Use 'seria' (feminine) with feminine nouns like 'persona'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Com'è? È simpatico?'",
                    "context": "Yes, he's very nice and funny.",
                    "task": "Describe his personality.",
                    "target_lang": "it",
                    "explanation": "Say 'Sì, è molto simpatico e divertente.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match personality traits",
                    "pairs": [["simpatico", "nice"], ["gentile", "kind"], ["divertente", "funny"], ["serio", "serious"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.4",
            "title": "Adjective Agreement (Plurals)",
            "focus": "Grammar drill on O/I and A/E endings",
            "vocabulary": [
                {"term": "ragazzo", "translation": "boy"},
                {"term": "ragazzi", "translation": "boys"},
                {"term": "ragazza", "translation": "girl"},
                {"term": "ragazze", "translation": "girls"},
                {"term": "italiani", "translation": "Italian (masculine plural)"},
                {"term": "americani", "translation": "American (masculine plural)"},
                {"term": "alti", "translation": "tall (masculine plural)"},
                {"term": "alte", "translation": "tall (feminine plural)"},
                {"term": "bravi", "translation": "good/clever (masculine plural)"},
                {"term": "brave", "translation": "good/clever (feminine plural)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Plural Adjective Agreement",
                    "correct_answer": "O/I and A/E Endings",
                    "explanation": "Masculine adjectives: -o (singular) → -i (plural)\nFeminine adjectives: -a (singular) → -e (plural)\n\nExamples:\n- alto → alti (tall - masculine plural)\n- alta → alte (tall - feminine plural)\n- bravo → bravi (good - masculine plural)\n- brava → brave (good - feminine plural)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ragazzi",
                    "explanation": "boys",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ragazzi_196.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ragazze",
                    "explanation": "girls",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ragazze_197.mp3"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Sort adjectives by gender and number",
                    "columns": [
                        {"id": "masc_sing", "label": "Maschile Singolare"},
                        {"id": "masc_plur", "label": "Maschile Plurale"},
                        {"id": "fem_sing", "label": "Femminile Singolare"},
                        {"id": "fem_plur", "label": "Femminile Plurale"}
                    ],
                    "items": [
                        {"text": "alto", "column_id": "masc_sing", "hint": "tall (masculine singular)"},
                        {"text": "alti", "column_id": "masc_plur", "hint": "tall (masculine plural)"},
                        {"text": "alta", "column_id": "fem_sing", "hint": "tall (feminine singular)"},
                        {"text": "alte", "column_id": "fem_plur", "hint": "tall (feminine plural)"}
                    ],
                    "correct_answer": "all_correct",
                    "explanation": "Learn adjective agreement patterns."
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Plural Forms",
                    "pairs": [["ragazzo", "boy"], ["ragazzi", "boys"], ["ragazza", "girl"], ["ragazze", "girls"], ["alti", "tall (masc plural)"], ["alte", "tall (fem plural)"]],
                    "correct_answer": "match_all",
                    "explanation": "Plural agreement vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How are the boys described?",
                    "audio_text": "I ragazzi sono alti.",
                    "options": ["tall", "short", "thin", "fat"],
                    "correct_answer": "tall",
                    "explanation": "You heard 'ragazzi sono alti' (boys are tall - plural).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The girls are tall.",
                    "blocks": ["Le", "ragazze", "sono", "alte"],
                    "correct_answer": "Le ragazze sono alte.",
                    "explanation": "Use plural article + plural noun + plural verb + plural adjective (feminine).",
                    "common_mistakes": [
                        {
                            "pattern": "alta",
                            "explanation": "Use 'alte' (plural) with plural nouns like 'ragazze'."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: I ragazzi sono alti",
                    "target_phrase": "I ragazzi sono alti",
                    "target_lang": "it",
                    "explanation": "Practice plural agreement"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'I ragazzi sono ___.' (tall - masculine plural)",
                    "options": ["alto", "alta", "alti", "alte"],
                    "correct_answer": "alti",
                    "explanation": "Use 'alti' (masculine plural) with masculine plural nouns like 'ragazzi'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Le ragazze sono ___.' (tall - feminine plural)",
                    "options": ["alto", "alta", "alti", "alte"],
                    "correct_answer": "alte",
                    "explanation": "Use 'alte' (feminine plural) with feminine plural nouns like 'ragazze'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Com'è la classe? I ragazzi sono alti?'",
                    "context": "Yes, the boys are tall and the girls are also tall.",
                    "task": "Describe the class.",
                    "target_lang": "it",
                    "explanation": "Say 'Sì, i ragazzi sono alti e anche le ragazze sono alte.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match plural forms",
                    "pairs": [["ragazzi", "boys"], ["ragazze", "girls"], ["alti", "tall (masc plural)"], ["alte", "tall (fem plural)"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.5",
            "title": "Expressing Likes (Mi Piace)",
            "focus": "'It pleases me' (Singular vs Plural)",
            "vocabulary": [
                {"term": "mi piace", "translation": "I like (it pleases me - singular)"},
                {"term": "mi piacciono", "translation": "I like (they please me - plural)"},
                {"term": "ti piace", "translation": "you like (it pleases you - singular)"},
                {"term": "il gelato", "translation": "ice cream"},
                {"term": "la musica", "translation": "music"},
                {"term": "i gatti", "translation": "cats"},
                {"term": "i cani", "translation": "dogs"},
                {"term": "leggere", "translation": "to read"},
                {"term": "viaggiare", "translation": "to travel"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: The Verb 'Piacere'",
                    "correct_answer": "Mi piace vs Mi piacciono",
                    "explanation": "Use 'Mi piace' (it pleases me) with singular nouns.\nUse 'Mi piacciono' (they please me) with plural nouns.\n\nThe verb agrees with what you like, not with 'I'.\n\nExamples:\n- Mi piace il gelato (I like ice cream - singular)\n- Mi piacciono i gatti (I like cats - plural)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi piace",
                    "explanation": "I like (it pleases me - singular)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_piace_105.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi piacciono",
                    "explanation": "I like (they please me - plural)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_piacciono_198.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "gelato",
                    "explanation": "ice cream",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_gelato_199.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "musica",
                    "explanation": "music",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_musica_200.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Likes Expressions",
                    "pairs": [["mi piace", "I like (singular)"], ["mi piacciono", "I like (plural)"], ["ti piace", "you like (singular)"], ["gelato", "ice cream"], ["musica", "music"]],
                    "correct_answer": "match_all",
                    "explanation": "Likes vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person like?",
                    "audio_text": "Mi piace molto la musica.",
                    "options": ["music", "ice cream", "cats", "dogs"],
                    "correct_answer": "music",
                    "explanation": "You heard 'Mi piace la musica' (I like music - singular).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I like cats very much.",
                    "blocks": ["Mi", "piacciono", "molto", "i", "gatti"],
                    "correct_answer": "Mi piacciono molto i gatti.",
                    "explanation": "Use 'Mi piacciono' (plural) with plural nouns like 'gatti'.",
                    "common_mistakes": [
                        {
                            "pattern": "Mi piace i gatti",
                            "explanation": "Use 'Mi piacciono' (plural) with plural nouns like 'gatti'."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi piace il gelato",
                    "target_phrase": "Mi piace il gelato",
                    "target_lang": "it",
                    "explanation": "Practice expressing likes"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ il gelato.' (I like - singular)",
                    "options": ["Mi piace", "Mi piacciono", "Mi piaccio", "Mi piaci"],
                    "correct_answer": "Mi piace",
                    "explanation": "Use 'Mi piace' (singular) with singular nouns like 'gelato'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ i cani.' (I like - plural)",
                    "options": ["Mi piace", "Mi piacciono", "Mi piaccio", "Mi piaci"],
                    "correct_answer": "Mi piacciono",
                    "explanation": "Use 'Mi piacciono' (plural) with plural nouns like 'cani'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Ti piace la musica?'",
                    "context": "Yes, you like music very much.",
                    "task": "Express your like.",
                    "target_lang": "it",
                    "explanation": "Say 'Sì, mi piace molto la musica.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match likes expressions",
                    "pairs": [["mi piace", "I like (singular)"], ["mi piacciono", "I like (plural)"], ["gelato", "ice cream"], ["musica", "music"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.6",
            "title": "Degree & Intensity",
            "focus": "'Very', 'A little', 'Quite'",
            "vocabulary": [
                {"term": "molto", "translation": "very"},
                {"term": "poco", "translation": "a little"},
                {"term": "abbastanza", "translation": "quite/enough"},
                {"term": "troppo", "translation": "too"},
                {"term": "veramente", "translation": "really"},
                {"term": "non molto", "translation": "not very"},
                {"term": "così", "translation": "so/thus"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "molto",
                    "explanation": "very",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_molto_201.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "poco",
                    "explanation": "a little",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_poco_202.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "abbastanza",
                    "explanation": "quite/enough",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_abbastanza_203.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "troppo",
                    "explanation": "too",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_troppo_130.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Adverbs of Degree",
                    "pairs": [["molto", "very"], ["poco", "a little"], ["abbastanza", "quite"], ["troppo", "too"], ["veramente", "really"]],
                    "correct_answer": "match_all",
                    "explanation": "Degree adverbs vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How much does the person like it?",
                    "audio_text": "Mi piace molto il gelato.",
                    "options": ["very much", "a little", "not very much", "too much"],
                    "correct_answer": "very much",
                    "explanation": "You heard 'molto' (very).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I like music a little.",
                    "blocks": ["Mi", "piace", "poco", "la", "musica"],
                    "correct_answer": "Mi piace poco la musica.",
                    "explanation": "Use 'poco' (a little) to express low intensity."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "He is really nice.",
                    "blocks": ["È", "veramente", "simpatico"],
                    "correct_answer": "È veramente simpatico.",
                    "explanation": "Use 'veramente' (really) to emphasize."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi piace molto la musica",
                    "target_phrase": "Mi piace molto la musica",
                    "target_lang": "it",
                    "explanation": "Practice expressing intensity"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Mi piace ___ il gelato.' (very)",
                    "options": ["molto", "poco", "abbastanza", "troppo"],
                    "correct_answer": "molto",
                    "explanation": "Use 'molto' (very) to express high intensity."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Mi piace ___ la musica.' (a little)",
                    "options": ["molto", "poco", "abbastanza", "troppo"],
                    "correct_answer": "poco",
                    "explanation": "Use 'poco' (a little) to express low intensity."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Ti piace il gelato?'",
                    "context": "Yes, you like it very much.",
                    "task": "Express your strong like.",
                    "target_lang": "it",
                    "explanation": "Say 'Sì, mi piace molto il gelato.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match degree adverbs",
                    "pairs": [["molto", "very"], ["poco", "a little"], ["abbastanza", "quite"], ["troppo", "too"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Bello vs. Carino - Nuances of Beauty",
                    "table": {
                        "headers": ["Word", "Meaning", "Intensity", "Tone", "Example", "Use For"],
                        "rows": [
                            ["Bello", "Beautiful, handsome", "Strong, impressive", "Serious admiration", "Che bella ragazza!", "People, places, art, nature"],
                            ["Carino", "Cute, nice, pretty", "Moderate, charming", "Endearing, sweet", "Che carina!", "Small things, children, animals"],
                            ["Bellissimo", "Very beautiful, gorgeous", "Very strong", "Intense admiration", "Sei bellissima!", "When extra impressed"],
                            ["Brutto", "Ugly", "Negative", "Critical", "Non è brutto", "Opposite of bello"]
                        ]
                    },
                    "explanation": "Key difference: 'Bello' = Wow! Impressive! vs 'Carino' = Aww! Sweet! | 'Sei bella' to a woman = serious compliment | 'Sei carina' = sweet, friendly compliment\n\nItalians are expressive with compliments! 'Bella' is commonly used among women greeting each other ('Ciao bella!'). Tip: When in doubt, 'carino' is safer - it's friendly without being too intense!",
                    "sub_text": "Understanding these nuances helps you give appropriate compliments.",
                    "cultural_note": True
                },
                {
                    "type": "info_card",
                    "step": 10,
                    "prompt": "Cultural Note",
                    "correct_answer": "Italian Hand Gestures - Speaking with Your Hands",
                    "explanation": "Italians are famous for talking with their hands - gestures add meaning and emotion:\n\n**Essential gestures:**\n\n1. **Ma che vuoi?** (What do you want?) - Fingertips pinched together, hand moving up and down. Means confusion, frustration, or 'what are you talking about?'\n\n2. **A me?** (Me?) - Index finger pointing at oneself. 'Are you talking to me?'\n\n3. **Perfetto!** - Thumb and index finger making circle, other fingers extended. 'Perfect! Excellent!'\n\n4. **Andiamo!** (Let's go!) - Open hand waving forward. 'Come on! Let's move!'\n\n5. **Non lo so** (I don't know) - Both palms up, shrug. Universal confusion/uncertainty\n\n6. **Buono!** (Good!) - Finger tips to mouth, then opening outward. 'Delicious! Great food!'\n\n7. **Attenzione!** - Index finger pointing at eye. 'Watch out! Pay attention!'\n\n8. **Mamma mia!** - Both hands slapping forehead or cheeks. Surprise, shock, disbelief\n\n**Why gestures matter:**\n• Italians use 250+ documented gestures regularly\n• Gestures can replace entire sentences\n• Regional variations exist (North vs South)\n• Used even on phone calls (speaker can't see!)\n• Part of Italian expressiveness and emotional communication\n\n**Cultural context:**\nGestures aren't just decoration - they're essential communication. An Italian saying goes: 'Tie an Italian's hands and they become mute!' Some gestures are rude or vulgar, so observe before imitating.\n\nTip: Watch how locals gesture when speaking. Mirroring appropriate gestures helps you blend in and makes your Italian sound more authentic!",
                    "sub_text": "Hand gestures are an integral part of Italian communication culture.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.8.BOSS",
            "title": "Boss Fight: The Police Sketch / Dating Profile",
            "type": "conversation_challenge",
            "focus": "Describing people - physical description and personality/likes",
            "vocabulary": [
                {"term": "alto", "translation": "tall"},
                {"term": "capelli", "translation": "hair"},
                {"term": "occhi", "translation": "eyes"},
                {"term": "simpatico", "translation": "nice"},
                {"term": "mi piace", "translation": "I like"},
                {"term": "com'è", "translation": "how is"},
                {"term": "ha", "translation": "he/she has"},
                {"term": "è", "translation": "is"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You need to describe a person: first to a police officer, then to a friend discussing a date.",
                    "scenario": "police_sketch_dating",
                    "ai_prompt": "You are a formal police officer taking a description, then a friend asking about a date.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Police Description",
                            "round_description": "A police officer asks you to describe a missing person.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno. Devo trovare una persona. Può descriverla?",
                                    "user_requirement": "Greet formally and agree to help.",
                                    "required_words": ["Buongiorno", "Sì", "certo"],
                                    "hints": ["Buongiorno", "Sì, certo", "Certamente"],
                                    "invalid_responses": ["Ciao!", "Yes", "OK"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Grazie. Com'è? È alto?",
                                    "user_requirement": "Describe height using 'alto' or 'basso'.",
                                    "required_words": ["È", "alto", "basso", "alta", "bassa"],
                                    "hints": ["È alto", "È basso", "È alta"],
                                    "invalid_responses": ["Tall", "Short", "High"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene. E i capelli? Che colore ha?",
                                    "user_requirement": "Describe hair color using 'ha i capelli'.",
                                    "required_words": ["Ha", "capelli", "biondi", "neri", "castani"],
                                    "hints": ["Ha i capelli biondi", "Ha i capelli neri", "Ha i capelli castani"],
                                    "invalid_responses": ["Blonde", "Black", "Brown hair"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto. E gli occhi?",
                                    "user_requirement": "Describe eye color using 'ha gli occhi'.",
                                    "required_words": ["Ha", "occhi", "azzurri", "verdi", "neri"],
                                    "hints": ["Ha gli occhi azzurri", "Ha gli occhi verdi", "Ha gli occhi neri"],
                                    "invalid_responses": ["Blue", "Green", "Black eyes"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Friend's Questions",
                            "round_description": "Your friend asks about someone you're interested in.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Com'è quella persona?",
                                    "user_requirement": "Say if they're nice using 'simpatico' or 'simpatica'.",
                                    "required_words": ["È", "simpatico", "simpatica"],
                                    "hints": ["È simpatico", "È simpatica", "Molto simpatico"],
                                    "invalid_responses": ["Nice", "Good", "OK"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Interessante! È intelligente?",
                                    "user_requirement": "Confirm or deny using 'Sì' or 'No' and the adjective.",
                                    "required_words": ["Sì", "No", "È", "intelligente"],
                                    "hints": ["Sì, è intelligente", "No, non è intelligente"],
                                    "invalid_responses": ["Yes smart", "No smart", "Intelligent"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "E cosa gli piace?",
                                    "user_requirement": "Say what they like using 'gli piace' or 'le piace'.",
                                    "required_words": ["piace", "piacciono", "musica", "gelato", "gatti"],
                                    "hints": ["Gli piace la musica", "Le piace il gelato", "Gli piacciono i gatti"],
                                    "invalid_responses": ["Likes music", "Likes ice cream", "Likes cats"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! Sembra interessante!",
                                    "user_requirement": "Agree and express your interest.",
                                    "required_words": ["Sì", "mi piace", "interessante"],
                                    "hints": ["Sì, mi piace", "Sì, è interessante", "Mi piace molto"],
                                    "invalid_responses": ["Yes like", "Interesting", "I like"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
