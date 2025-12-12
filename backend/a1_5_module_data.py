"""
Module A1.5 data structure - Shopping & Prices
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_5_LESSONS = {
    "module_id": "A1.5",
    "title": "Shopping & Prices",
    "goal": "Shop for clothes and items, ask about prices, and express opinions about cost and quality.",
    "lessons": [
        {
            "lesson_id": "A1.5.0",
            "title": "Self-Assessment: Shopping & Prices",
            "focus": "Assess your confidence with shopping and prices",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel shopping and asking about prices?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can name basic clothing items",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask how much something costs",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask for sizes and colors",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can express if something is expensive or cheap",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.5.1",
            "title": "Clothing Basics",
            "focus": "Identifying clothes, Gender of nouns",
            "vocabulary": [
                {"term": "vestito", "translation": "dress"},
                {"term": "maglietta", "translation": "t-shirt"},
                {"term": "pantaloni", "translation": "pants/trousers"},
                {"term": "scarpe", "translation": "shoes"},
                {"term": "camicia", "translation": "shirt"},
                {"term": "giacca", "translation": "jacket"},
                {"term": "borsa", "translation": "bag"},
                {"term": "indossare", "translation": "to wear"},
                {"term": "nuovo", "translation": "new (masculine)"},
                {"term": "vecchio", "translation": "old (masculine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Noun Gender",
                    "correct_answer": "Gender Agreement",
                    "explanation": "Italian nouns have gender (masculine/feminine). Articles and adjectives must agree.\n\nMasculine: il vestito (the dress), nuovo (new)\nFeminine: la maglietta (the t-shirt), nuova (new)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "vestito",
                    "explanation": "dress",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vestito_109.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "maglietta",
                    "explanation": "t-shirt",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_maglietta_110.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pantaloni",
                    "explanation": "pants/trousers",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pantaloni_111.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "scarpe",
                    "explanation": "shoes",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_scarpe_112.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "giacca",
                    "explanation": "jacket",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_giacca_113.mp3"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Sort clothing by gender",
                    "columns": [
                        {"id": "masc", "label": "Maschile"},
                        {"id": "fem", "label": "Femminile"}
                    ],
                    "items": [
                        {"text": "vestito", "column_id": "masc", "hint": "dress (masculine)"},
                        {"text": "maglietta", "column_id": "fem", "hint": "t-shirt (feminine)"},
                        {"text": "camicia", "column_id": "fem", "hint": "shirt (feminine)"},
                        {"text": "giacca", "column_id": "fem", "hint": "jacket (feminine)"},
                        {"text": "borsa", "column_id": "fem", "hint": "bag (feminine)"}
                    ],
                    "correct_answer": "all_correct",
                    "explanation": "Learn the gender of clothing nouns."
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Clothing Items",
                    "pairs": [["vestito", "dress"], ["maglietta", "t-shirt"], ["pantaloni", "pants"], ["scarpe", "shoes"], ["giacca", "jacket"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic clothing vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What clothing item did you hear?",
                    "audio_text": "Indosso una maglietta nuova.",
                    "options": ["dress", "t-shirt", "pants", "shoes"],
                    "correct_answer": "t-shirt",
                    "explanation": "You heard 'maglietta' (t-shirt).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I wear a new dress.",
                    "blocks": ["Indosso", "un", "vestito", "nuovo"],
                    "correct_answer": "Indosso un vestito nuovo.",
                    "explanation": "Use 'Indosso' (I wear) + article + noun + adjective (agreement)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Indosso una maglietta nuova",
                    "target_phrase": "Indosso una maglietta nuova",
                    "target_lang": "it",
                    "explanation": "Practice describing what you wear"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Indosso un vestito ___.' (new - masculine)",
                    "options": ["nuovo", "nuova", "nuovi", "nuove"],
                    "correct_answer": "nuovo",
                    "explanation": "Vestito is masculine, so use 'nuovo'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Cosa indossi?'",
                    "context": "You're wearing a new t-shirt.",
                    "task": "Say what you're wearing.",
                    "target_lang": "it",
                    "explanation": "Say 'Indosso una maglietta nuova.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match clothing vocabulary",
                    "pairs": [["vestito", "dress"], ["maglietta", "t-shirt"], ["pantaloni", "pants"], ["scarpe", "shoes"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.2",
            "title": "Numbers 50-100 & Money",
            "focus": "High numbers, Euro currency",
            "vocabulary": [
                {"term": "cinquanta", "translation": "fifty"},
                {"term": "sessanta", "translation": "sixty"},
                {"term": "settanta", "translation": "seventy"},
                {"term": "ottanta", "translation": "eighty"},
                {"term": "novanta", "translation": "ninety"},
                {"term": "cento", "translation": "one hundred"},
                {"term": "euro", "translation": "euro"},
                {"term": "soldi", "translation": "money"},
                {"term": "prezzo", "translation": "price"},
                {"term": "costa", "translation": "it costs"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cinquanta",
                    "explanation": "fifty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cinquanta_50.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sessanta",
                    "explanation": "sixty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sessanta_60.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "settanta",
                    "explanation": "seventy",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_settanta_70.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "ottanta",
                    "explanation": "eighty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ottanta_80.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "novanta",
                    "explanation": "ninety",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_novanta_90.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cento",
                    "explanation": "one hundred",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cento_100.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Numbers",
                    "pairs": [["cinquanta", "fifty"], ["sessanta", "sixty"], ["settanta", "seventy"], ["ottanta", "eighty"], ["novanta", "ninety"], ["cento", "one hundred"]],
                    "correct_answer": "match_all",
                    "explanation": "Numbers 50-100"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How much does it cost?",
                    "audio_text": "Costa settanta euro.",
                    "options": ["fifty euros", "sixty euros", "seventy euros", "eighty euros"],
                    "correct_answer": "seventy euros",
                    "explanation": "You heard 'settanta euro' (seventy euros).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "It costs eighty euros.",
                    "blocks": ["Costa", "ottanta", "euro"],
                    "correct_answer": "Costa ottanta euro.",
                    "explanation": "Use 'Costa' (it costs) + number + 'euro'."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Costa cinquanta euro",
                    "target_phrase": "Costa cinquanta euro",
                    "target_lang": "it",
                    "explanation": "Practice saying prices"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Costa ___ euro.' (ninety)",
                    "options": ["novanta", "ottanta", "settanta", "sessanta"],
                    "correct_answer": "novanta",
                    "explanation": "Use 'novanta' for ninety."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You see a price tag: 60 euro.",
                    "context": "Someone asks how much it costs.",
                    "task": "Say the price.",
                    "target_lang": "it",
                    "explanation": "Say 'Costa sessanta euro.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match numbers and money",
                    "pairs": [["cinquanta", "fifty"], ["sessanta", "sixty"], ["euro", "euro"], ["prezzo", "price"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.3",
            "title": "Asking the Price (Quanto costa?)",
            "focus": "Interrogatives, Singular vs Plural cost (Costa vs Costano)",
            "vocabulary": [
                {"term": "quanto", "translation": "how much"},
                {"term": "costa", "translation": "it costs (singular)"},
                {"term": "costano", "translation": "they cost (plural)"},
                {"term": "questo", "translation": "this (masculine)"},
                {"term": "questa", "translation": "this (feminine)"},
                {"term": "scusa", "translation": "excuse me"},
                {"term": "prezzo", "translation": "price"},
                {"term": "totale", "translation": "total"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Asking Prices",
                    "correct_answer": "Quanto costa?",
                    "explanation": "Use 'Quanto costa?' (How much does it cost?) for singular items.\nUse 'Quanto costano?' (How much do they cost?) for plural items.\n\nExamples:\n- Quanto costa questa maglietta? (How much does this t-shirt cost?)\n- Quanto costano le scarpe? (How much do the shoes cost?)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "quanto",
                    "explanation": "how much",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quanto_114.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "quanto costa",
                    "explanation": "how much does it cost",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quanto_costa_115.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "questo",
                    "explanation": "this (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_questo_116.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "questa",
                    "explanation": "this (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_questa_117.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Price Questions",
                    "pairs": [["quanto", "how much"], ["costa", "it costs"], ["costano", "they cost"], ["questo", "this (masc)"], ["questa", "this (fem)"]],
                    "correct_answer": "match_all",
                    "explanation": "Price vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What is the customer asking?",
                    "audio_text": "Scusa, quanto costa questa maglietta?",
                    "options": ["How much does this t-shirt cost?", "Where is the t-shirt?", "What color is it?", "What size is it?"],
                    "correct_answer": "How much does this t-shirt cost?",
                    "explanation": "You heard 'Quanto costa questa maglietta?' (How much does this t-shirt cost?).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How much does this dress cost?",
                    "blocks": ["Quanto", "costa", "questo", "vestito"],
                    "correct_answer": "Quanto costa questo vestito?",
                    "explanation": "Use 'Quanto costa' + 'questo/questa' + noun + '?'",
                    "common_mistakes": [
                        {
                            "pattern": "costano",
                            "explanation": "Use 'costa' (singular) with singular nouns like 'vestito'."
                        }
                    ]
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How much do the shoes cost?",
                    "blocks": ["Quanto", "costano", "le", "scarpe"],
                    "correct_answer": "Quanto costano le scarpe?",
                    "explanation": "Use 'Quanto costano' (plural) with plural nouns like 'scarpe'."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Quanto costa questa maglietta?",
                    "target_phrase": "Quanto costa questa maglietta?",
                    "target_lang": "it",
                    "explanation": "Practice asking about prices"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Quanto ___ questa maglietta?' (it costs)",
                    "options": ["costa", "costano", "costo", "costiamo"],
                    "correct_answer": "costa",
                    "explanation": "Use 'costa' (singular) with singular nouns."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Quanto ___ queste scarpe?' (they cost)",
                    "options": ["costa", "costano", "costo", "costiamo"],
                    "correct_answer": "costano",
                    "explanation": "Use 'costano' (plural) with plural nouns."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're in a shop. You see a jacket you like.",
                    "context": "You want to know the price.",
                    "task": "Ask how much it costs politely.",
                    "target_lang": "it",
                    "explanation": "Say 'Scusa, quanto costa questa giacca?'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match price questions",
                    "pairs": [["quanto", "how much"], ["costa", "it costs"], ["questo", "this (masc)"], ["questa", "this (fem)"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.4",
            "title": "Sizes & Colors (Adjectives)",
            "focus": "Adjective agreement, Asking for sizes",
            "vocabulary": [
                {"term": "taglia", "translation": "size"},
                {"term": "colore", "translation": "color"},
                {"term": "piccolo", "translation": "small (masculine)"},
                {"term": "grande", "translation": "large/big"},
                {"term": "medio", "translation": "medium"},
                {"term": "rosso", "translation": "red (masculine)"},
                {"term": "blu", "translation": "blue"},
                {"term": "nero", "translation": "black (masculine)"},
                {"term": "bianco", "translation": "white (masculine)"},
                {"term": "c'è", "translation": "there is"},
                {"term": "avete", "translation": "do you have"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "taglia",
                    "explanation": "size",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_taglia_118.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "colore",
                    "explanation": "color",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_colore_119.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "piccolo",
                    "explanation": "small (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_piccolo_120.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "grande",
                    "explanation": "large/big",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_grande_121.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "medio",
                    "explanation": "medium",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_medio_122.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Sizes and Colors",
                    "pairs": [["taglia", "size"], ["piccolo", "small"], ["grande", "large"], ["medio", "medium"], ["rosso", "red"], ["blu", "blue"]],
                    "correct_answer": "match_all",
                    "explanation": "Size and color vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What size does the customer want?",
                    "audio_text": "Avete questa maglietta in taglia media?",
                    "options": ["small", "medium", "large", "extra large"],
                    "correct_answer": "medium",
                    "explanation": "You heard 'taglia media' (medium size).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Do you have this t-shirt in a large size?",
                    "blocks": ["Avete", "questa", "maglietta", "taglia", "grande"],
                    "correct_answer": "Avete questa maglietta in taglia grande?",
                    "explanation": "Use 'Avete' (do you have) + 'questa' + noun + 'in taglia' + size."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Avete questa maglietta in taglia media?",
                    "target_phrase": "Avete questa maglietta in taglia media?",
                    "target_lang": "it",
                    "explanation": "Practice asking for sizes"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Avete questo vestito in taglia ___?' (small - masculine)",
                    "options": ["piccolo", "piccola", "piccoli", "piccole"],
                    "correct_answer": "piccolo",
                    "explanation": "Use 'piccolo' (masculine) with masculine nouns like 'vestito'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Avete questa maglietta in taglia ___?' (small - feminine)",
                    "options": ["piccolo", "piccola", "piccoli", "piccole"],
                    "correct_answer": "piccola",
                    "explanation": "Use 'piccola' (feminine) with feminine nouns like 'maglietta'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're in a shop. You see a jacket you like.",
                    "context": "You want to know if they have it in your size (large).",
                    "task": "Ask if they have it in a large size.",
                    "target_lang": "it",
                    "explanation": "Say 'Avete questa giacca in taglia grande?'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match sizes and colors",
                    "pairs": [["taglia", "size"], ["piccolo", "small"], ["grande", "large"], ["colore", "color"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.5",
            "title": "Demonstratives (This/That)",
            "focus": "Pointing at objects (Singular focus)",
            "vocabulary": [
                {"term": "questo", "translation": "this (masculine)"},
                {"term": "questa", "translation": "this (feminine)"},
                {"term": "quello", "translation": "that (masculine)"},
                {"term": "quella", "translation": "that (feminine)"},
                {"term": "maglione", "translation": "sweater"},
                {"term": "cappello", "translation": "hat"},
                {"term": "sciarpa", "translation": "scarf"},
                {"term": "mi piace", "translation": "I like"},
                {"term": "voglio", "translation": "I want"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Demonstratives (This/That)",
                    "correct_answer": "Questo/Quello",
                    "explanation": "Use 'questo/questa' (this) for things near you.\nUse 'quello/quella' (that) for things far from you.\n\nMasculine: questo vestito (this dress), quello vestito (that dress)\nFeminine: questa maglietta (this t-shirt), quella maglietta (that t-shirt)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "questo",
                    "explanation": "this (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_questo_116.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "questa",
                    "explanation": "this (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_questa_117.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quello",
                    "explanation": "that (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quello_123.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quella",
                    "explanation": "that (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quella_124.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "maglione",
                    "explanation": "sweater",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_maglione_125.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Demonstratives",
                    "pairs": [["questo", "this (masc)"], ["questa", "this (fem)"], ["quello", "that (masc)"], ["quella", "that (fem)"]],
                    "correct_answer": "match_all",
                    "explanation": "Demonstrative pronouns"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Which item does the customer want?",
                    "audio_text": "Mi piace questo maglione.",
                    "options": ["this sweater", "that sweater", "this hat", "that hat"],
                    "correct_answer": "this sweater",
                    "explanation": "You heard 'questo maglione' (this sweater).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I like this sweater.",
                    "blocks": ["Mi", "piace", "questo", "maglione"],
                    "correct_answer": "Mi piace questo maglione.",
                    "explanation": "Use 'Mi piace' + 'questo/questa' + noun."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I want that hat.",
                    "blocks": ["Voglio", "quello", "cappello"],
                    "correct_answer": "Voglio quello cappello.",
                    "explanation": "Use 'Voglio' + 'quello/quella' + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi piace questo maglione",
                    "target_phrase": "Mi piace questo maglione",
                    "target_lang": "it",
                    "explanation": "Practice using demonstratives"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Mi piace ___ maglietta.' (this - feminine)",
                    "options": ["questo", "questa", "quello", "quella"],
                    "correct_answer": "questa",
                    "explanation": "Use 'questa' (feminine) with feminine nouns like 'maglietta'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Voglio ___ cappello.' (that - masculine)",
                    "options": ["questo", "questa", "quello", "quella"],
                    "correct_answer": "quello",
                    "explanation": "Use 'quello' (masculine) with masculine nouns like 'cappello'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're in a shop. You see a scarf you like.",
                    "context": "You want to say you like this scarf.",
                    "task": "Express that you like it using 'Mi piace'.",
                    "target_lang": "it",
                    "explanation": "Say 'Mi piace questa sciarpa.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match demonstratives",
                    "pairs": [["questo", "this (masc)"], ["questa", "this (fem)"], ["quello", "that (masc)"], ["quella", "that (fem)"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.6",
            "title": "Opinions (Cheap vs. Expensive)",
            "focus": "Evaluating items, 'Troppo' (Too)",
            "vocabulary": [
                {"term": "caro", "translation": "expensive (masculine)"},
                {"term": "costoso", "translation": "expensive"},
                {"term": "economico", "translation": "cheap/inexpensive"},
                {"term": "bello", "translation": "beautiful/nice (masculine)"},
                {"term": "brutto", "translation": "ugly (masculine)"},
                {"term": "troppo", "translation": "too"},
                {"term": "molto", "translation": "very"},
                {"term": "sconto", "translation": "discount"},
                {"term": "saldi", "translation": "sales"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "caro",
                    "explanation": "expensive (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_caro_126.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "costoso",
                    "explanation": "expensive",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_costoso_127.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "economico",
                    "explanation": "cheap/inexpensive",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_economico_128.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "bello",
                    "explanation": "beautiful/nice (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_bello_129.mp3"
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
                    "prompt": "Match Opinions",
                    "pairs": [["caro", "expensive"], ["economico", "cheap"], ["bello", "beautiful"], ["brutto", "ugly"], ["troppo", "too"]],
                    "correct_answer": "match_all",
                    "explanation": "Opinion vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the customer think?",
                    "audio_text": "Questo vestito è troppo caro.",
                    "options": ["It's too expensive", "It's very cheap", "It's beautiful", "It's ugly"],
                    "correct_answer": "It's too expensive",
                    "explanation": "You heard 'troppo caro' (too expensive).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "This dress is too expensive.",
                    "blocks": ["Questo", "vestito", "è", "troppo", "caro"],
                    "correct_answer": "Questo vestito è troppo caro.",
                    "explanation": "Use 'Questo/Questa' + noun + 'è' + 'troppo' + adjective."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "This t-shirt is very cheap.",
                    "blocks": ["Questa", "maglietta", "è", "molto", "economica"],
                    "correct_answer": "Questa maglietta è molto economica.",
                    "explanation": "Use 'molto' (very) + adjective (with agreement)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Questo vestito è troppo caro",
                    "target_phrase": "Questo vestito è troppo caro",
                    "target_lang": "it",
                    "explanation": "Practice expressing opinions about prices"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Questa maglietta è troppo ___.' (expensive - feminine)",
                    "options": ["caro", "cara", "cari", "care"],
                    "correct_answer": "cara",
                    "explanation": "Use 'cara' (feminine) with feminine nouns like 'maglietta'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Questo vestito è molto ___.' (beautiful - masculine)",
                    "options": ["bello", "bella", "belli", "belle"],
                    "correct_answer": "bello",
                    "explanation": "Use 'bello' (masculine) with masculine nouns like 'vestito'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Quanto costa questa giacca?' You think it's too expensive.",
                    "context": "You're shopping together.",
                    "task": "Express that it's too expensive.",
                    "target_lang": "it",
                    "explanation": "Say 'È troppo cara.' or 'Questa giacca è troppo cara.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match opinions",
                    "pairs": [["caro", "expensive"], ["economico", "cheap"], ["bello", "beautiful"], ["troppo", "too"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Italian Sizing vs. US/UK Sizes",
                    "explanation": "Italian clothing sizes differ from US and UK sizing systems:\n\n**Women's Clothing:**\n• US 2 = IT 38 | US 4 = IT 40 | US 6 = IT 42 | US 8 = IT 44\n• US 10 = IT 46 | US 12 = IT 48\n\n**Men's Clothing:**\n• US/UK S = IT 46 | US/UK M = IT 48-50 | US/UK L = IT 52-54\n• US/UK XL = IT 56\n\n**Shoes:**\n• Women: US 6 = IT 36 | US 7 = IT 37 | US 8 = IT 38 | US 9 = IT 39\n• Men: US 8 = IT 41 | US 9 = IT 42 | US 10 = IT 43 | US 11 = IT 44\n\nUseful shopping phrases:\n• 'Che taglia?' (What size?)\n• 'Posso provare?' (Can I try it on?)\n• 'Avete la taglia più grande/piccola?' (Do you have a bigger/smaller size?)\n\nTip: Italian sizing tends to run smaller than American sizing. When in doubt, try it on!",
                    "sub_text": "Knowing Italian sizes saves time and frustration when shopping.",
                    "cultural_note": True
                },
                {
                    "type": "info_card",
                    "step": 10,
                    "prompt": "Cultural Note",
                    "correct_answer": "Politeness: Vorrei vs. Voglio",
                    "explanation": "In Italian, how you express desire matters for politeness:\n\n**Vorrei** (I would like) - Conditional form, ALWAYS polite\n• 'Vorrei una maglietta' (I would like a t-shirt)\n• Use in shops, restaurants, formal situations\n• Safe choice in all contexts\n\n**Voglio** (I want) - Present indicative, DIRECT and can sound rude\n• 'Voglio un caffè' (I want a coffee) - Sounds demanding!\n• Only acceptable with friends/family or when making strong statements\n• Children can say 'voglio' but adults should avoid it with strangers\n\n**Why the difference?**\nItalian culture values indirect communication and formality. Using 'vorrei' shows respect and good manners. Using 'voglio' in a shop or restaurant marks you as either a child, rude, or a foreigner who doesn't know better.\n\nAlways use 'Vorrei' when:\n• Shopping | Ordering food/drinks | Asking for help | Making requests\n\nRemember: 'Vorrei' = polite and educated. 'Voglio' = demanding and rude (unless with close friends).",
                    "sub_text": "This distinction is crucial for sounding polite and respectful in Italian.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.5.BOSS",
            "title": "Boss Fight: The Souvenir Shop",
            "type": "conversation_challenge",
            "focus": "Buying a gift in Rome - asking price and checking size, then commenting on price",
            "vocabulary": [
                {"term": "negozio", "translation": "shop"},
                {"term": "maglietta", "translation": "t-shirt"},
                {"term": "quanto costa", "translation": "how much does it cost"},
                {"term": "questa", "translation": "this (feminine)"},
                {"term": "taglia", "translation": "size"},
                {"term": "caro", "translation": "expensive"},
                {"term": "troppo", "translation": "too"},
                {"term": "comprare", "translation": "to buy"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You are in a souvenir shop in Rome buying a gift.",
                    "scenario": "souvenir_shop",
                    "ai_prompt": "You are a formal shopkeeper helping a customer, then a friend commenting on the purchase.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Shopkeeper Interaction",
                            "round_description": "The shopkeeper helps you find and check the item.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno! Posso aiutarla?",
                                    "user_requirement": "Greet and ask about a t-shirt using 'questa'.",
                                    "required_words": ["Buongiorno", "questa", "maglietta"],
                                    "hints": ["Buongiorno", "Quanto costa questa maglietta?", "Questa maglietta"],
                                    "invalid_responses": ["Ciao!", "Maglietta", "I want t-shirt"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Questa maglietta costa trenta euro.",
                                    "user_requirement": "Ask if they have it in your size.",
                                    "required_words": ["Avete", "taglia"],
                                    "hints": ["Avete questa maglietta in taglia...?", "Che taglia avete?"],
                                    "invalid_responses": ["Size?", "What size?", "Taglia?"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Sì, abbiamo la taglia media e grande.",
                                    "user_requirement": "Ask to see it or confirm you want it.",
                                    "required_words": ["Vorrei", "Voglio", "Posso"],
                                    "hints": ["Vorrei vedere", "Vorrei questa", "Posso vedere"],
                                    "invalid_responses": ["I want", "Can I", "Show me"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! Vuole comprarla?",
                                    "user_requirement": "Say yes and ask about payment.",
                                    "required_words": ["Sì", "Quanto", "totale"],
                                    "hints": ["Sì, quanto costa?", "Sì, qual è il totale?"],
                                    "invalid_responses": ["Yes", "OK", "How much"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Friend's Comment",
                            "round_description": "Your friend comments on the price you paid.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Hai comprato qualcosa?",
                                    "user_requirement": "Say yes and mention what you bought.",
                                    "required_words": ["Sì", "maglietta", "comprare"],
                                    "hints": ["Sì, ho comprato una maglietta", "Sì, questa maglietta"],
                                    "invalid_responses": ["Yes", "T-shirt", "I bought"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Bene! Quanto costa?",
                                    "user_requirement": "Tell them the price.",
                                    "required_words": ["Costa", "euro", "trenta"],
                                    "hints": ["Costa trenta euro", "Trenta euro"],
                                    "invalid_responses": ["30", "Thirty", "Euro"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Trenta euro? È troppo cara!",
                                    "user_requirement": "Agree or disagree about the price.",
                                    "required_words": ["Sì", "È", "caro", "cara", "troppo"],
                                    "hints": ["Sì, è troppo cara", "No, non è cara"],
                                    "invalid_responses": ["Yes expensive", "Too much", "Expensive"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Hai ragione. Ma è bella!",
                                    "user_requirement": "Agree about it being nice or express your opinion.",
                                    "required_words": ["Sì", "bello", "bella", "mi piace"],
                                    "hints": ["Sì, è bella", "Mi piace molto"],
                                    "invalid_responses": ["Yes nice", "I like", "Beautiful"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
