"""
Module A1.4 data structure - Ordering Food & Drinks
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_4_LESSONS = {
    "module_id": "A1.4",
    "title": "Ordering Food & Drinks",
    "goal": "Order food and drinks in cafés, bars, and restaurants using polite expressions.",
    "lessons": [
        {
            "lesson_id": "A1.4.0",
            "title": "Self-Assessment: Ordering Food & Drinks",
            "focus": "Assess your confidence with ordering food and drinks",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel ordering food and drinks?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can order coffee and breakfast items at a café",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can order lunch items (panini, pizza)",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can order a full meal at a restaurant",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask for the bill and pay",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.4.1",
            "title": "The Café Basics (Breakfast)",
            "focus": "Ordering coffee/pastry, 'Vorrei'",
            "vocabulary": [
                {"term": "caffè", "translation": "coffee"},
                {"term": "cappuccino", "translation": "cappuccino"},
                {"term": "cornetto", "translation": "croissant"},
                {"term": "brioche", "translation": "brioche/pastry"},
                {"term": "vorrei", "translation": "I would like"},
                {"term": "per favore", "translation": "please"},
                {"term": "grazie", "translation": "thank you"},
                {"term": "zucchero", "translation": "sugar"},
                {"term": "latte", "translation": "milk"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Polite Requests",
                    "correct_answer": "Vorrei (I would like)",
                    "explanation": "Use 'Vorrei' (I would like) for polite requests. Avoid 'Voglio' (I want) - it's too direct and can sound rude.\n\nCorrect: Vorrei un caffè (I would like a coffee)\nAvoid: Voglio un caffè (I want a coffee - too direct)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "caffè",
                    "explanation": "coffee",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_caffe_84.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cappuccino",
                    "explanation": "cappuccino",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cappuccino_85.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cornetto",
                    "explanation": "croissant",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cornetto_86.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "brioche",
                    "explanation": "brioche/pastry",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_brioche_87.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "vorrei",
                    "explanation": "I would like",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_vorrei_88.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Breakfast Items",
                    "pairs": [["caffè", "coffee"], ["cappuccino", "cappuccino"], ["cornetto", "croissant"], ["brioche", "brioche"], ["vorrei", "I would like"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic café vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the customer want?",
                    "audio_text": "Vorrei un caffè, per favore.",
                    "options": ["coffee", "cappuccino", "cornetto", "brioche"],
                    "correct_answer": "coffee",
                    "explanation": "You heard 'Vorrei un caffè' (I would like a coffee).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I would like a cappuccino, please.",
                    "blocks": ["Vorrei", "un", "cappuccino", "per", "favore"],
                    "correct_answer": "Vorrei un cappuccino, per favore.",
                    "explanation": "Use 'Vorrei' for polite requests, followed by article + item + 'per favore'."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vorrei un caffè, per favore",
                    "target_phrase": "Vorrei un caffè, per favore",
                    "target_lang": "it",
                    "explanation": "Practice polite ordering"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ un cappuccino, per favore.' (I would like)",
                    "options": ["Vorrei", "Voglio", "Prendo", "Desidero"],
                    "correct_answer": "Vorrei",
                    "explanation": "Use 'Vorrei' (I would like) for polite requests."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at a café. The barista asks: 'Cosa desidera?'",
                    "context": "You want a coffee and a croissant.",
                    "task": "Order politely using 'Vorrei'.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei un caffè e un cornetto, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match café vocabulary",
                    "pairs": [["caffè", "coffee"], ["cappuccino", "cappuccino"], ["vorrei", "I would like"], ["per favore", "please"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Italian Coffee Culture - The Cappuccino Rule",
                    "explanation": "In Italy, coffee drinking follows strict unwritten rules:\n\n• Cappuccino is ONLY for breakfast (before 11 AM). Ordering it after lunch marks you as a tourist!\n• After meals, Italians drink espresso (caffè) - never cappuccino. Milk after a meal is considered heavy and disrupts digestion\n• Caffè = Espresso by default. If you want American coffee, order 'caffè americano'\n• Coffee is consumed quickly at the bar (1-2 minutes), standing up. Sitting doubles the price!\n• Caffè macchiato = espresso with a drop of milk (acceptable anytime)\n• Latte = just milk! Order 'caffè latte' if you want coffee with milk\n\nWhy? Italians believe milk-based drinks are too filling for after meals. When in doubt, order 'un caffè' - you'll fit right in!",
                    "sub_text": "Following coffee etiquette helps you blend in like a local.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.2",
            "title": "At the Bar (Banco vs. Tavolo)",
            "focus": "Bar culture, prepositions 'al'",
            "vocabulary": [
                {"term": "banco", "translation": "counter/bar"},
                {"term": "tavolo", "translation": "table"},
                {"term": "consumazione", "translation": "consumption/drink"},
                {"term": "cassa", "translation": "cash register"},
                {"term": "scontrino", "translation": "receipt"},
                {"term": "al", "translation": "at the (masculine)"},
                {"term": "prendo", "translation": "I take/I'll have"},
                {"term": "un", "translation": "a/an (masculine)"},
                {"term": "una", "translation": "a/an (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Cultural Note: Italian Bar Culture",
                    "correct_answer": "Bar Culture",
                    "explanation": "In Italy, 'bar' means café. You can order 'al banco' (at the counter - cheaper) or 'al tavolo' (at a table - more expensive). Always pay at the 'cassa' (cash register) first, then show your 'scontrino' (receipt) to order.",
                    "sub_text": "Cultural Context",
                    "cultural_note": True
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "banco",
                    "explanation": "counter/bar",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_banco_89.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "tavolo",
                    "explanation": "table",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tavolo_90.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "scontrino",
                    "explanation": "receipt",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_scontrino_91.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Preposition 'Al'",
                    "correct_answer": "Al (At the)",
                    "explanation": "'Al' = 'a' (at) + 'il' (the) = 'at the' (masculine).\n\nExamples:\n- Al banco (at the counter)\n- Al tavolo (at the table)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Bar Terms",
                    "pairs": [["banco", "counter"], ["tavolo", "table"], ["cassa", "cash register"], ["scontrino", "receipt"], ["al", "at the"]],
                    "correct_answer": "match_all",
                    "explanation": "Bar vocabulary"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read: 'Prendo un caffè al banco.' What does this mean?",
                    "text": "Prendo un caffè al banco.",
                    "questions": [
                        {
                            "question": "Where is the person ordering?",
                            "options": ["at the counter", "at a table", "outside", "at home"],
                            "correct_answer": "at the counter"
                        }
                    ],
                    "explanation": "'Al banco' means 'at the counter'."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I'll have a coffee at the counter.",
                    "blocks": ["Prendo", "un", "caffè", "al", "banco"],
                    "correct_answer": "Prendo un caffè al banco.",
                    "explanation": "Use 'Prendo' (I'll have) + article + item + 'al banco' (at the counter)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Prendo un caffè al banco",
                    "target_phrase": "Prendo un caffè al banco",
                    "target_lang": "it",
                    "explanation": "Practice ordering at the counter"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Prendo un caffè ___ banco.' (at the)",
                    "options": ["al", "alla", "nel", "sul"],
                    "correct_answer": "al",
                    "explanation": "Use 'al' (at the) with masculine nouns like 'banco'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at a bar. You want to order at the counter.",
                    "context": "You want a cappuccino.",
                    "task": "Say you'll have it at the counter.",
                    "target_lang": "it",
                    "explanation": "Say 'Prendo un cappuccino al banco.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match bar vocabulary",
                    "pairs": [["banco", "counter"], ["tavolo", "table"], ["al", "at the"], ["prendo", "I'll have"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.3",
            "title": "Lunch Snacks (Panini & Pizza)",
            "focus": "Quick lunch items, Plurals (Intro: -o/-i, -a/-e)",
            "vocabulary": [
                {"term": "panino", "translation": "sandwich (singular)"},
                {"term": "panini", "translation": "sandwiches (plural)"},
                {"term": "pizza", "translation": "pizza (singular)"},
                {"term": "pizze", "translation": "pizzas (plural)"},
                {"term": "tramezzino", "translation": "triangle sandwich"},
                {"term": "insalata", "translation": "salad"},
                {"term": "acqua", "translation": "water"},
                {"term": "naturale", "translation": "still (water)"},
                {"term": "frizzante", "translation": "sparkling (water)"},
                {"term": "da portare via", "translation": "to take away"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Plural Forms",
                    "correct_answer": "Plurals",
                    "explanation": "Masculine nouns ending in -o become -i in plural.\nFeminine nouns ending in -a become -e in plural.\n\nExamples:\n- panino → panini (sandwich → sandwiches)\n- pizza → pizze (pizza → pizzas)",
                    "sub_text": "Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "panino",
                    "explanation": "sandwich (singular)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_panino_92.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "panini",
                    "explanation": "sandwiches (plural)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_panini_93.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pizza",
                    "explanation": "pizza (singular)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pizza_94.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pizze",
                    "explanation": "pizzas (plural)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pizze_95.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "acqua",
                    "explanation": "water",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_acqua_96.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Lunch Items",
                    "pairs": [["panino", "sandwich"], ["panini", "sandwiches"], ["pizza", "pizza"], ["pizze", "pizzas"], ["acqua", "water"]],
                    "correct_answer": "match_all",
                    "explanation": "Lunch vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the customer want?",
                    "audio_text": "Vorrei due panini e un'acqua naturale, per favore.",
                    "options": ["two sandwiches and water", "one sandwich and water", "two pizzas", "one pizza"],
                    "correct_answer": "two sandwiches and water",
                    "explanation": "You heard 'due panini' (two sandwiches) and 'un'acqua naturale' (a still water).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I would like two sandwiches, please.",
                    "blocks": ["Vorrei", "due", "panini", "per", "favore"],
                    "correct_answer": "Vorrei due panini, per favore.",
                    "explanation": "Use 'Vorrei' + number + plural noun + 'per favore'.",
                    "common_mistakes": [
                        {
                            "pattern": "panino",
                            "explanation": "Use 'panini' (plural) when ordering more than one."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vorrei un panino, per favore",
                    "target_phrase": "Vorrei un panino, per favore",
                    "target_lang": "it",
                    "explanation": "Practice ordering a sandwich"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei due ___.' (sandwiches)",
                    "options": ["panino", "panini", "panina", "panine"],
                    "correct_answer": "panini",
                    "explanation": "Use plural 'panini' when ordering more than one."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei due ___.' (pizzas)",
                    "options": ["pizza", "pizze", "pizzi", "pizza"],
                    "correct_answer": "pizze",
                    "explanation": "Use plural 'pizze' when ordering more than one."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're ordering lunch. You want two sandwiches and water.",
                    "context": "You're at a bar ordering to take away.",
                    "task": "Order using 'Vorrei' and 'da portare via'.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei due panini e un'acqua, da portare via, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match lunch vocabulary",
                    "pairs": [["panino", "sandwich"], ["panini", "sandwiches"], ["pizza", "pizza"], ["acqua", "water"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Italian Meal Timing - When Italians Eat",
                    "explanation": "Italians eat at different times than Americans or British people:\n\n• Colazione (Breakfast): 7-10 AM - Light! Just coffee and a cornetto (croissant). No eggs or bacon\n• Pranzo (Lunch): 12:30-2:30 PM - The main meal of the day! Restaurants fill up 1-2 PM. Many shops close for 'riposo' (afternoon break)\n• Cena (Dinner): 8-10 PM (or later!) - Italians eat dinner late. Restaurants open around 7:30 PM but locals arrive after 8:30 PM. Showing up at 6 PM marks you as a tourist!\n• Aperitivo: 6-8 PM - Pre-dinner drinks with snacks to tide you over\n\nRestaurants serving 'pranzo' often close 3-7 PM. Expect to wait if you arrive at peak times! Many family-run places close one day per week (often Monday).",
                    "sub_text": "Timing your meals like a local enhances your Italian experience.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.4",
            "title": "Restaurant Dinner (The Menu)",
            "focus": "Course structure (Antipasto, Primo, Secondo)",
            "vocabulary": [
                {"term": "ristorante", "translation": "restaurant"},
                {"term": "menu", "translation": "menu"},
                {"term": "antipasto", "translation": "appetizer/starter"},
                {"term": "primo", "translation": "first course (pasta/rice)"},
                {"term": "secondo", "translation": "second course (meat/fish)"},
                {"term": "dolce", "translation": "dessert"},
                {"term": "carne", "translation": "meat"},
                {"term": "pesce", "translation": "fish"},
                {"term": "pasta", "translation": "pasta"},
                {"term": "vino", "translation": "wine"},
                {"term": "birra", "translation": "beer"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Cultural Note: Italian Meal Structure",
                    "correct_answer": "Meal Courses",
                    "explanation": "Italian meals typically have courses: Antipasto (starter), Primo (first course - pasta/rice), Secondo (second course - meat/fish), Dolce (dessert). You don't have to order all courses!",
                    "sub_text": "Cultural Context",
                    "cultural_note": True
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
                    "correct_answer": "menu",
                    "explanation": "menu",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_menu_98.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "antipasto",
                    "explanation": "appetizer/starter",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_antipasto_99.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "primo",
                    "explanation": "first course (pasta/rice)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_primo_100.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "secondo",
                    "explanation": "second course (meat/fish)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_secondo_101.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Meal Courses",
                    "pairs": [["antipasto", "appetizer"], ["primo", "first course"], ["secondo", "second course"], ["dolce", "dessert"], ["menu", "menu"]],
                    "correct_answer": "match_all",
                    "explanation": "Restaurant vocabulary"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the menu. What is 'primo'?",
                    "text": "MENU\nAntipasto: Insalata\nPrimo: Pasta al pomodoro\nSecondo: Carne\nDolce: Tiramisù",
                    "questions": [
                        {
                            "question": "What is 'primo'?",
                            "options": ["appetizer", "first course", "second course", "dessert"],
                            "correct_answer": "first course"
                        }
                    ],
                    "explanation": "'Primo' is the first course, usually pasta or rice."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I would like a first course and a second course.",
                    "blocks": ["Vorrei", "un", "primo", "e", "un", "secondo"],
                    "correct_answer": "Vorrei un primo e un secondo.",
                    "explanation": "Order courses using 'Vorrei' + article + course name."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vorrei un primo, per favore",
                    "target_phrase": "Vorrei un primo, per favore",
                    "target_lang": "it",
                    "explanation": "Practice ordering a first course"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei un ___ e un secondo.' (first course)",
                    "options": ["antipasto", "primo", "secondo", "dolce"],
                    "correct_answer": "primo",
                    "explanation": "Use 'primo' for the first course (pasta/rice)."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at a restaurant. The waiter asks: 'Cosa desidera?'",
                    "context": "You want pasta (primo) and meat (secondo).",
                    "task": "Order both courses politely.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei un primo e un secondo, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match restaurant vocabulary",
                    "pairs": [["ristorante", "restaurant"], ["primo", "first course"], ["secondo", "second course"], ["dolce", "dessert"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                },
                {
                    "type": "info_card",
                    "step": 9,
                    "prompt": "Cultural Note",
                    "correct_answer": "Water Choice - Naturale vs. Frizzante",
                    "explanation": "In Italy, when you order water at a restaurant, you'll always be asked: 'Naturale o frizzante?'\n\n• Acqua naturale - Still water (no bubbles)\n• Acqua frizzante (or gassata) - Sparkling water (with bubbles)\n\nImportant notes:\n• Tap water is safe to drink in Italy, but restaurants rarely serve it. They'll bring bottled water and charge for it (usually €2-4 per bottle)\n• If you want tap water, ask for 'acqua del rubinetto' - but expect puzzled looks and possible refusal in some regions\n• San Pellegrino (sparkling) and Acqua Panna (still) are the most famous Italian bottled waters\n• Most Italians prefer frizzante with meals, believing it aids digestion\n\nAt bars, a small bottle is called 'una bottiglietta' - perfect for taking away!",
                    "sub_text": "Knowing your water preference is essential for Italian dining.",
                    "cultural_note": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.5",
            "title": "Asking for the Bill",
            "focus": "Payment vocabulary, Numbers 20-50 (Prices)",
            "vocabulary": [
                {"term": "il conto", "translation": "the bill"},
                {"term": "quanto costa", "translation": "how much does it cost"},
                {"term": "quant'è", "translation": "how much is it"},
                {"term": "pagare", "translation": "to pay"},
                {"term": "carta", "translation": "card"},
                {"term": "contanti", "translation": "cash"},
                {"term": "euro", "translation": "euro"},
                {"term": "venti", "translation": "twenty"},
                {"term": "trenta", "translation": "thirty"},
                {"term": "quaranta", "translation": "forty"},
                {"term": "cinquanta", "translation": "fifty"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "il conto",
                    "explanation": "the bill",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_il_conto_102.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "quanto costa",
                    "explanation": "how much does it cost",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quanto_costa_103.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "quant'è",
                    "explanation": "how much is it",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quante_104.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "venti",
                    "explanation": "twenty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_venti_20.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "trenta",
                    "explanation": "thirty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_trenta_30.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quaranta",
                    "explanation": "forty",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quaranta_40.mp3"
                },
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
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Payment Terms",
                    "pairs": [["il conto", "the bill"], ["quanto costa", "how much does it cost"], ["pagare", "to pay"], ["carta", "card"], ["contanti", "cash"]],
                    "correct_answer": "match_all",
                    "explanation": "Payment vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How much is the bill?",
                    "audio_text": "Il conto è trenta euro.",
                    "options": ["twenty euros", "thirty euros", "forty euros", "fifty euros"],
                    "correct_answer": "thirty euros",
                    "explanation": "You heard 'trenta euro' (thirty euros).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "How much is it?",
                    "blocks": ["Quant'è"],
                    "correct_answer": "Quant'è?",
                    "explanation": "Use 'Quant'è?' to ask for the total price."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The bill, please.",
                    "blocks": ["Il", "conto", "per", "favore"],
                    "correct_answer": "Il conto, per favore.",
                    "explanation": "Politely ask for the bill."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Il conto, per favore",
                    "target_phrase": "Il conto, per favore",
                    "target_lang": "it",
                    "explanation": "Practice asking for the bill"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ costa?' (How much does it cost)",
                    "options": ["Quanto", "Quant'è", "Quanti", "Quante"],
                    "correct_answer": "Quanto",
                    "explanation": "Use 'Quanto costa?' to ask the price of something."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You've finished your meal. You want to pay.",
                    "context": "You're ready to leave the restaurant.",
                    "task": "Ask for the bill politely.",
                    "target_lang": "it",
                    "explanation": "Say 'Il conto, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match payment vocabulary",
                    "pairs": [["il conto", "the bill"], ["quanto costa", "how much"], ["pagare", "to pay"], ["euro", "euro"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.6",
            "title": "Taste & Preferences (Mi piace)",
            "focus": "Expressing likes simple (Mi piace + singular)",
            "vocabulary": [
                {"term": "mi piace", "translation": "I like (it pleases me)"},
                {"term": "non mi piace", "translation": "I don't like"},
                {"term": "buono", "translation": "good (masculine)"},
                {"term": "buona", "translation": "good (feminine)"},
                {"term": "caldo", "translation": "hot"},
                {"term": "freddo", "translation": "cold"},
                {"term": "piccante", "translation": "spicy"},
                {"term": "molto", "translation": "very"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Expressing Likes",
                    "correct_answer": "Mi piace (I like)",
                    "explanation": "In Italian, we say 'Mi piace' (it pleases me) to express likes.\n\nMi piace la pizza (I like pizza - singular)\nNon mi piace la pasta (I don't like pasta)\n\nNote: 'Mi piace' is used with singular nouns. The verb agrees with what you like, not with 'I'.",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "mi piace",
                    "explanation": "I like (it pleases me)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_mi_piace_105.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "non mi piace",
                    "explanation": "I don't like",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_non_mi_piace_106.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "buono",
                    "explanation": "good (masculine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_buono_107.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "buona",
                    "explanation": "good (feminine)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_buona_108.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Taste Expressions",
                    "pairs": [["mi piace", "I like"], ["non mi piace", "I don't like"], ["buono", "good"], ["caldo", "hot"], ["freddo", "cold"]],
                    "correct_answer": "match_all",
                    "explanation": "Taste vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Does the person like pizza?",
                    "audio_text": "Mi piace molto la pizza.",
                    "options": ["yes, very much", "no", "a little", "not sure"],
                    "correct_answer": "yes, very much",
                    "explanation": "You heard 'Mi piace molto la pizza' (I like pizza very much).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I like pizza very much.",
                    "blocks": ["Mi", "piace", "molto", "la", "pizza"],
                    "correct_answer": "Mi piace molto la pizza.",
                    "explanation": "Use 'Mi piace' + 'molto' (very) + article + noun.",
                    "common_mistakes": [
                        {
                            "pattern": "Mi piacciono",
                            "explanation": "Use 'Mi piace' (singular) with singular nouns like 'la pizza'."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi piace la pizza",
                    "target_phrase": "Mi piace la pizza",
                    "target_lang": "it",
                    "explanation": "Practice expressing likes"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ la pasta.' (I like)",
                    "options": ["Mi piace", "Mi piacciono", "Mi piace", "Mi piaccio"],
                    "correct_answer": "Mi piace",
                    "explanation": "Use 'Mi piace' (singular) with singular nouns."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La pizza è ___.' (good - feminine)",
                    "options": ["buono", "buona", "buoni", "buone"],
                    "correct_answer": "buona",
                    "explanation": "Pizza is feminine, so use 'buona'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A friend asks: 'Ti piace la pizza?'",
                    "context": "You really like pizza.",
                    "task": "Say you like it very much.",
                    "target_lang": "it",
                    "explanation": "Say 'Sì, mi piace molto la pizza.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match taste vocabulary",
                    "pairs": [["mi piace", "I like"], ["buono", "good"], ["caldo", "hot"], ["freddo", "cold"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.4.BOSS",
            "title": "Boss Fight: The Trattoria Dinner",
            "type": "conversation_challenge",
            "focus": "A 3-course dinner order - ordering food and discussing it",
            "vocabulary": [
                {"term": "ristorante", "translation": "restaurant"},
                {"term": "primo", "translation": "first course"},
                {"term": "secondo", "translation": "second course"},
                {"term": "dolce", "translation": "dessert"},
                {"term": "vorrei", "translation": "I would like"},
                {"term": "buono", "translation": "good"},
                {"term": "mi piace", "translation": "I like"},
                {"term": "il conto", "translation": "the bill"}
            ],
            "exercises": [
                {
                    "type": "conversation_challenge",
                    "step": 1,
                    "prompt": "You are at a trattoria ordering a 3-course dinner.",
                    "scenario": "trattoria_dinner",
                    "ai_prompt": "You are a formal waiter taking an order, then a friend discussing the food.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Taking the Order",
                            "round_description": "The waiter takes your order for drinks and food.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buonasera! Prego, si accomodi. Cosa desidera da bere?",
                                    "user_requirement": "Order a drink politely using 'Vorrei'.",
                                    "required_words": ["Vorrei", "vino", "birra", "acqua"],
                                    "hints": ["Vorrei un vino", "Vorrei una birra", "Vorrei un'acqua"],
                                    "invalid_responses": ["Voglio vino", "I want wine", "Vino"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Perfetto. E per mangiare?",
                                    "user_requirement": "Order a first course (primo) using 'Vorrei'.",
                                    "required_words": ["Vorrei", "primo", "pasta"],
                                    "hints": ["Vorrei un primo", "Vorrei una pasta"],
                                    "invalid_responses": ["Voglio pasta", "Pasta", "I want pasta"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Bene. E come secondo?",
                                    "user_requirement": "Order a second course (secondo) using 'Vorrei'.",
                                    "required_words": ["Vorrei", "secondo", "carne", "pesce"],
                                    "hints": ["Vorrei un secondo", "Vorrei carne", "Vorrei pesce"],
                                    "invalid_responses": ["Voglio carne", "Carne", "I want meat"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Ottimo. E per dolce?",
                                    "user_requirement": "Order dessert or decline politely, then ask for the bill.",
                                    "required_words": ["Vorrei", "dolce", "il conto"],
                                    "hints": ["Vorrei un dolce", "No, grazie", "Il conto, per favore"],
                                    "invalid_responses": ["I want dessert", "Bill please", "Check"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Discussing the Food",
                            "round_description": "Your friend asks if you like the food.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Com'è il cibo?",
                                    "user_requirement": "Say if the food is good using 'buono' or 'buona'.",
                                    "required_words": ["È", "buono", "buona"],
                                    "hints": ["È buono", "È buona", "Molto buono"],
                                    "invalid_responses": ["Good", "It's nice", "Yes"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Ti piace la pasta?",
                                    "user_requirement": "Say if you like the pasta using 'Mi piace'.",
                                    "required_words": ["Mi piace", "Sì", "Non mi piace"],
                                    "hints": ["Sì, mi piace", "Mi piace molto"],
                                    "invalid_responses": ["I like", "Yes like", "Piace"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "E il secondo? È buono?",
                                    "user_requirement": "Confirm if the second course is good.",
                                    "required_words": ["Sì", "È", "buono", "buona"],
                                    "hints": ["Sì, è buono", "Sì, è buona"],
                                    "invalid_responses": ["Yes good", "It's nice", "Good"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto! Allora, vuoi ordinare il dolce?",
                                    "user_requirement": "Say yes or no, and express your preference.",
                                    "required_words": ["Sì", "No", "Vorrei", "Mi piace"],
                                    "hints": ["Sì, vorrei", "No, grazie", "Mi piace il dolce"],
                                    "invalid_responses": ["Yes want", "No want", "I like dessert"]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
