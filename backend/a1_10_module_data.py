"""
Module A1.10 data structure - Health & Emergencies
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_10_LESSONS = {
    "module_id": "A1.10",
    "title": "Health & Emergencies",
    "goal": "Describe health symptoms, communicate at pharmacies and with doctors, and handle emergency situations using modal verbs and body vocabulary.",
    "lessons": [
        {
            "lesson_id": "A1.10.0",
            "title": "Self-Assessment: Health & Emergencies",
            "focus": "Assess your confidence with health and emergency situations",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel talking about health and emergencies?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can name body parts",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can describe symptoms and pain",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask for medicine at a pharmacy",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can ask for help in an emergency",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.10.1",
            "title": "The Body (Head & Torso)",
            "focus": "Basic anatomy, Singular nouns",
            "vocabulary": [
                {"term": "testa", "translation": "head"},
                {"term": "collo", "translation": "neck"},
                {"term": "pancia", "translation": "belly/stomach"},
                {"term": "schiena", "translation": "back"},
                {"term": "stomaco", "translation": "stomach"},
                {"term": "cuore", "translation": "heart"},
                {"term": "corpo", "translation": "body"},
                {"term": "faccia", "translation": "face"},
                {"term": "bocca", "translation": "mouth"},
                {"term": "naso", "translation": "nose"},
                {"term": "occhi", "translation": "eyes"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "testa",
                    "explanation": "head",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_testa_228.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "collo",
                    "explanation": "neck",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_collo_229.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pancia",
                    "explanation": "belly/stomach",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pancia_230.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "schiena",
                    "explanation": "back",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_schiena_231.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cuore",
                    "explanation": "heart",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cuore_232.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Body Parts",
                    "pairs": [["testa", "head"], ["collo", "neck"], ["pancia", "belly"], ["schiena", "back"], ["cuore", "heart"], ["faccia", "face"], ["bocca", "mouth"], ["naso", "nose"]],
                    "correct_answer": "match_all",
                    "explanation": "Body vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Which body part is mentioned?",
                    "audio_text": "Mi fa male la testa.",
                    "options": ["head", "neck", "back", "stomach"],
                    "correct_answer": "head",
                    "explanation": "You heard 'la testa' (the head).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "The head hurts.",
                    "blocks": ["La", "testa", "fa", "male"],
                    "correct_answer": "La testa fa male.",
                    "explanation": "Use article + body part + 'fa male' (hurts)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: La testa fa male",
                    "target_phrase": "La testa fa male",
                    "target_lang": "it",
                    "explanation": "Practice describing pain"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'La ___ fa male.' (head)",
                    "options": ["testa", "collo", "pancia", "schiena"],
                    "correct_answer": "testa",
                    "explanation": "Use 'testa' (head) for head pain."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove ti fa male?'",
                    "context": "Your back hurts.",
                    "task": "Tell them where it hurts.",
                    "target_lang": "it",
                    "explanation": "Say 'Mi fa male la schiena.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match body parts",
                    "pairs": [["testa", "head"], ["collo", "neck"], ["pancia", "belly"], ["schiena", "back"], ["cuore", "heart"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.2",
            "title": "Limbs & Irregular Plurals",
            "focus": "Arms/Legs and the weird -o/-a plural shift",
            "vocabulary": [
                {"term": "mano", "translation": "hand"},
                {"term": "mani", "translation": "hands"},
                {"term": "braccio", "translation": "arm"},
                {"term": "braccia", "translation": "arms"},
                {"term": "gamba", "translation": "leg"},
                {"term": "gambe", "translation": "legs"},
                {"term": "piede", "translation": "foot"},
                {"term": "piedi", "translation": "feet"},
                {"term": "dito", "translation": "finger"},
                {"term": "dita", "translation": "fingers"},
                {"term": "destro", "translation": "right"},
                {"term": "sinistro", "translation": "left"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Irregular Body Plurals",
                    "correct_answer": "Braccio/Braccia",
                    "explanation": "Some body parts have irregular plurals:\n\n- braccio → braccia (arm → arms)\n- mano → mani (hand → hands)\n- dito → dita (finger → fingers)\n\nRegular plurals:\n- gamba → gambe (leg → legs)\n- piede → piedi (foot → feet)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "braccio",
                    "explanation": "arm",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_braccio_233.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "braccia",
                    "explanation": "arms",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_braccia_234.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "gamba",
                    "explanation": "leg",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_gamba_235.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "piede",
                    "explanation": "foot",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_piede_236.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Limbs",
                    "pairs": [["braccio", "arm"], ["braccia", "arms"], ["gamba", "leg"], ["gambe", "legs"], ["piede", "foot"], ["piedi", "feet"], ["mano", "hand"], ["mani", "hands"]],
                    "correct_answer": "match_all",
                    "explanation": "Limbs vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Which body part is mentioned?",
                    "audio_text": "Mi fanno male le braccia.",
                    "options": ["arms", "legs", "hands", "feet"],
                    "correct_answer": "arms",
                    "explanation": "You heard 'le braccia' (the arms).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "My legs hurt.",
                    "blocks": ["Mi", "fanno", "male", "le", "gambe"],
                    "correct_answer": "Mi fanno male le gambe.",
                    "explanation": "Use 'Mi fanno male' (they hurt me) + article + plural body part."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "My right arm hurts.",
                    "blocks": ["Mi", "fa", "male", "il", "braccio", "destro"],
                    "correct_answer": "Mi fa male il braccio destro.",
                    "explanation": "Use 'Mi fa male' (it hurts me) + article + singular body part + adjective."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Mi fanno male le braccia",
                    "target_phrase": "Mi fanno male le braccia",
                    "target_lang": "it",
                    "explanation": "Practice describing pain in plural body parts"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Mi fanno male le ___.' (arms)",
                    "options": ["braccia", "braccio", "bracci", "braccie"],
                    "correct_answer": "braccia",
                    "explanation": "Use 'braccia' (irregular plural of 'braccio')."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Mi fanno male le ___.' (hands)",
                    "options": ["mani", "mano", "manos", "mane"],
                    "correct_answer": "mani",
                    "explanation": "Use 'mani' (irregular plural of 'mano')."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Dove ti fa male?'",
                    "context": "Your left leg hurts.",
                    "task": "Tell them where it hurts.",
                    "target_lang": "it",
                    "explanation": "Say 'Mi fa male la gamba sinistra.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match limbs and plurals",
                    "pairs": [["braccio", "arm"], ["braccia", "arms"], ["gamba", "leg"], ["piede", "foot"], ["mano", "hand"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 2 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.3",
            "title": "Symptoms (Ho mal di...)",
            "focus": "Using 'Avere' to describe pain",
            "vocabulary": [
                {"term": "ho", "translation": "I have"},
                {"term": "hai", "translation": "you have"},
                {"term": "ha", "translation": "he/she has"},
                {"term": "male", "translation": "pain/hurt"},
                {"term": "mal di", "translation": "ache/pain in"},
                {"term": "testa", "translation": "head"},
                {"term": "gola", "translation": "throat"},
                {"term": "denti", "translation": "teeth"},
                {"term": "pancia", "translation": "belly"},
                {"term": "febbre", "translation": "fever"},
                {"term": "raffreddore", "translation": "cold"},
                {"term": "tosse", "translation": "cough"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Avere mal di...",
                    "correct_answer": "To Have an Ache",
                    "explanation": "Use 'Avere' (to have) + 'mal di' + body part to describe pain:\n\n- Ho mal di testa (I have a headache)\n- Ho mal di gola (I have a sore throat)\n- Ho mal di pancia (I have a stomachache)\n- Ho mal di denti (I have a toothache)\n\nFor fever/cold:\n- Ho la febbre (I have a fever)\n- Ho il raffreddore (I have a cold)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "ho mal di testa",
                    "explanation": "I have a headache",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ho_mal_di_testa_237.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "ho mal di gola",
                    "explanation": "I have a sore throat",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_ho_mal_di_gola_238.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "febbre",
                    "explanation": "fever",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_febbre_239.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "raffreddore",
                    "explanation": "cold",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_raffreddore_240.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Symptoms",
                    "pairs": [["ho mal di testa", "I have a headache"], ["ho mal di gola", "I have a sore throat"], ["ho mal di pancia", "I have a stomachache"], ["ho la febbre", "I have a fever"], ["ho il raffreddore", "I have a cold"]],
                    "correct_answer": "match_all",
                    "explanation": "Symptoms vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What symptom does the person have?",
                    "audio_text": "Ho mal di testa.",
                    "options": ["headache", "sore throat", "stomachache", "toothache"],
                    "correct_answer": "headache",
                    "explanation": "You heard 'mal di testa' (headache).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I have a sore throat.",
                    "blocks": ["Ho", "mal", "di", "gola"],
                    "correct_answer": "Ho mal di gola.",
                    "explanation": "Use 'Ho mal di' + body part."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I have a fever.",
                    "blocks": ["Ho", "la", "febbre"],
                    "correct_answer": "Ho la febbre.",
                    "explanation": "Use 'Ho la febbre' (I have the fever) - note the article."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ho mal di testa",
                    "target_phrase": "Ho mal di testa",
                    "target_lang": "it",
                    "explanation": "Practice describing symptoms"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ho ___ di testa.' (pain)",
                    "options": ["mal", "male", "dolore", "fa"],
                    "correct_answer": "mal",
                    "explanation": "Use 'mal di' (ache/pain in) with body parts."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Ho ___ febbre.' (the)",
                    "options": ["la", "il", "un", "una"],
                    "correct_answer": "la",
                    "explanation": "Use 'Ho la febbre' (I have the fever) - feminine article."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A doctor asks: 'Cosa non va?'",
                    "context": "You have a stomachache.",
                    "task": "Tell them your symptom.",
                    "target_lang": "it",
                    "explanation": "Say 'Ho mal di pancia.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match symptoms",
                    "pairs": [["ho mal di testa", "headache"], ["ho mal di gola", "sore throat"], ["ho la febbre", "fever"], ["ho il raffreddore", "cold"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 3 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.4",
            "title": "At the Pharmacy",
            "focus": "Asking for remedies",
            "vocabulary": [
                {"term": "farmacia", "translation": "pharmacy"},
                {"term": "farmacista", "translation": "pharmacist"},
                {"term": "medicina", "translation": "medicine"},
                {"term": "aspirina", "translation": "aspirin"},
                {"term": "sciroppo", "translation": "syrup"},
                {"term": "pastiglia", "translation": "pill"},
                {"term": "cerotto", "translation": "bandage"},
                {"term": "crema", "translation": "cream"},
                {"term": "per", "translation": "for"},
                {"term": "contro", "translation": "against/for"},
                {"term": "prendere", "translation": "to take"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "farmacia",
                    "explanation": "pharmacy",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_farmacia_241.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "farmacista",
                    "explanation": "pharmacist",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_farmacista_242.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "medicina",
                    "explanation": "medicine",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_medicina_243.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "aspirina",
                    "explanation": "aspirin",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_aspirina_244.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "pastiglia",
                    "explanation": "pill",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pastiglia_245.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Pharmacy Terms",
                    "pairs": [["farmacia", "pharmacy"], ["farmacista", "pharmacist"], ["medicina", "medicine"], ["aspirina", "aspirin"], ["pastiglia", "pill"], ["cerotto", "bandage"], ["crema", "cream"]],
                    "correct_answer": "match_all",
                    "explanation": "Pharmacy vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person want?",
                    "audio_text": "Vorrei un'aspirina per il mal di testa.",
                    "options": ["aspirin for headache", "syrup for cough", "cream for back", "bandage for arm"],
                    "correct_answer": "aspirin for headache",
                    "explanation": "You heard 'aspirina per il mal di testa' (aspirin for the headache).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I would like medicine for the fever.",
                    "blocks": ["Vorrei", "una", "medicina", "per", "la", "febbre"],
                    "correct_answer": "Vorrei una medicina per la febbre.",
                    "explanation": "Use 'Vorrei' (I would like) + article + medicine + 'per' (for) + symptom."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Vorrei un'aspirina per il mal di testa",
                    "target_phrase": "Vorrei un'aspirina per il mal di testa",
                    "target_lang": "it",
                    "explanation": "Practice asking for medicine"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei una medicina ___ il mal di gola.' (for)",
                    "options": ["per", "contro", "a", "in"],
                    "correct_answer": "per",
                    "explanation": "Use 'per' (for) when asking for medicine for a symptom."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Vorrei una ___ per il mal di testa.' (aspirin)",
                    "options": ["aspirina", "medicina", "pastiglia", "crema"],
                    "correct_answer": "aspirina",
                    "explanation": "Use 'aspirina' (aspirin) for headaches."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "You're at a pharmacy. You have a headache.",
                    "context": "You're speaking to the pharmacist.",
                    "task": "Ask for aspirin politely.",
                    "target_lang": "it",
                    "explanation": "Say 'Vorrei un'aspirina per il mal di testa, per favore.'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match pharmacy vocabulary",
                    "pairs": [["farmacia", "pharmacy"], ["farmacista", "pharmacist"], ["medicina", "medicine"], ["aspirina", "aspirin"], ["pastiglia", "pill"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 4 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.5",
            "title": "Doctor's Orders (Modals)",
            "focus": "'You must' (Devi) and 'You can' (Puoi)",
            "vocabulary": [
                {"term": "dovere", "translation": "to must/have to"},
                {"term": "devo", "translation": "I must"},
                {"term": "devi", "translation": "you must"},
                {"term": "potere", "translation": "to can/be able to"},
                {"term": "posso", "translation": "I can"},
                {"term": "puoi", "translation": "you can"},
                {"term": "riposare", "translation": "to rest"},
                {"term": "mangiare", "translation": "to eat"},
                {"term": "dormire", "translation": "to sleep"},
                {"term": "stare", "translation": "to stay/be"},
                {"term": "casa", "translation": "home"},
                {"term": "letto", "translation": "bed"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Modal Verbs",
                    "correct_answer": "Dovere & Potere",
                    "explanation": "Modal verbs express necessity and ability:\n\nDovere (must/have to):\n- Io devo (I must)\n- Tu devi (You must)\n- Devo riposare (I must rest)\n\nPotere (can/be able to):\n- Io posso (I can)\n- Tu puoi (You can)\n- Posso mangiare (I can eat)\n\nModal verbs are followed by infinitive verbs.",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "devo",
                    "explanation": "I must",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_devo_246.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "devi",
                    "explanation": "you must",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_devi_247.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "posso",
                    "explanation": "I can",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_posso_248.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "puoi",
                    "explanation": "you can",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_puoi_249.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Modal Verbs",
                    "pairs": [["devo", "I must"], ["devi", "you must"], ["posso", "I can"], ["puoi", "you can"], ["riposare", "to rest"], ["dormire", "to sleep"]],
                    "correct_answer": "match_all",
                    "explanation": "Modal verbs vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the doctor say?",
                    "audio_text": "Devi riposare a casa.",
                    "options": ["You must rest at home", "You can rest at home", "You must sleep", "You can eat"],
                    "correct_answer": "You must rest at home",
                    "explanation": "You heard 'Devi riposare' (You must rest).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "You must stay in bed.",
                    "blocks": ["Devi", "stare", "a", "letto"],
                    "correct_answer": "Devi stare a letto.",
                    "explanation": "Use 'Devi' (You must) + infinitive verb + preposition + noun."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "You can eat now.",
                    "blocks": ["Puoi", "mangiare", "adesso"],
                    "correct_answer": "Puoi mangiare adesso.",
                    "explanation": "Use 'Puoi' (You can) + infinitive verb + time marker."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Devi riposare a casa",
                    "target_phrase": "Devi riposare a casa",
                    "target_lang": "it",
                    "explanation": "Practice doctor's orders"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ riposare.' (You must)",
                    "options": ["Devi", "Devo", "Puoi", "Posso"],
                    "correct_answer": "Devi",
                    "explanation": "Use 'Devi' (you must) for second person singular."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ mangiare?' (Can I)",
                    "options": ["Posso", "Puoi", "Devo", "Devi"],
                    "correct_answer": "Posso",
                    "explanation": "Use 'Posso' (I can) for first person singular."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A doctor says: 'Devi riposare.'",
                    "context": "You want to ask if you can eat.",
                    "task": "Ask if you can eat.",
                    "target_lang": "it",
                    "explanation": "Say 'Posso mangiare?'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match modal verbs",
                    "pairs": [["devo", "I must"], ["devi", "you must"], ["posso", "I can"], ["puoi", "you can"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 5 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.6",
            "title": "Emergencies (Help!)",
            "focus": "Urgent phrases and 112",
            "vocabulary": [
                {"term": "aiuto", "translation": "help"},
                {"term": "emergenza", "translation": "emergency"},
                {"term": "ambulanza", "translation": "ambulance"},
                {"term": "ospedale", "translation": "hospital"},
                {"term": "pronto soccorso", "translation": "emergency room"},
                {"term": "chiamate", "translation": "call (plural)"},
                {"term": "polizia", "translation": "police"},
                {"term": "sto male", "translation": "I feel bad/I'm sick"},
                {"term": "grave", "translation": "serious"},
                {"term": "urgente", "translation": "urgent"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "aiuto",
                    "explanation": "help",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_aiuto_250.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "emergenza",
                    "explanation": "emergency",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_emergenza_251.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "pronto soccorso",
                    "explanation": "emergency room",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_pronto_soccorso_252.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "sto male",
                    "explanation": "I feel bad/I'm sick",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sto_male_253.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Cultural Note",
                    "correct_answer": "Emergency Number",
                    "explanation": "In Italy, the emergency number is 112 (single number for police, ambulance, and fire).\n\n- 112: All emergencies\n- 'Aiuto!' means 'Help!'\n- 'Chiamate un'ambulanza!' means 'Call an ambulance!'",
                    "sub_text": "Important Information"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Emergency Terms",
                    "pairs": [["aiuto", "help"], ["emergenza", "emergency"], ["ambulanza", "ambulance"], ["ospedale", "hospital"], ["pronto soccorso", "emergency room"], ["polizia", "police"]],
                    "correct_answer": "match_all",
                    "explanation": "Emergency vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What does the person need?",
                    "audio_text": "Aiuto! Chiamate un'ambulanza!",
                    "options": ["ambulance", "police", "hospital", "pharmacy"],
                    "correct_answer": "ambulance",
                    "explanation": "You heard 'Chiamate un'ambulanza!' (Call an ambulance!).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "Help! Call an ambulance!",
                    "blocks": ["Aiuto", "Chiamate", "un'ambulanza"],
                    "correct_answer": "Aiuto! Chiamate un'ambulanza!",
                    "explanation": "Use 'Aiuto!' (Help!) + imperative 'Chiamate' (Call) + article + noun."
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I feel bad. It's urgent.",
                    "blocks": ["Sto", "male", "È", "urgente"],
                    "correct_answer": "Sto male. È urgente.",
                    "explanation": "Use 'Sto male' (I feel bad) + 'È urgente' (It's urgent)."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Aiuto! Chiamate un'ambulanza!",
                    "target_phrase": "Aiuto! Chiamate un'ambulanza!",
                    "target_lang": "it",
                    "explanation": "Practice emergency phrases"
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___! Chiamate un'ambulanza!' (Help)",
                    "options": ["Aiuto", "Emergenza", "Urgente", "Grave"],
                    "correct_answer": "Aiuto",
                    "explanation": "Use 'Aiuto!' (Help!) to call for help."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: '___ male.' (I feel bad)",
                    "options": ["Sto", "Sono", "Ho", "Faccio"],
                    "correct_answer": "Sto",
                    "explanation": "Use 'Sto male' (I feel bad/I'm sick) - 'stare' + 'male'."
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "There's an emergency. Someone needs an ambulance.",
                    "context": "You need to call for help.",
                    "task": "Shout for help and ask someone to call an ambulance.",
                    "target_lang": "it",
                    "explanation": "Say 'Aiuto! Chiamate un'ambulanza!'"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match emergency vocabulary",
                    "pairs": [["aiuto", "help"], ["emergenza", "emergency"], ["ambulanza", "ambulance"], ["ospedale", "hospital"], ["pronto soccorso", "emergency room"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 6 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.10.BOSS",
            "title": "Boss Fight: The Medical Check",
            "type": "boss_fight",
            "focus": "Seeing a doctor and canceling plans - describing symptoms and canceling plans",
            "vocabulary": [
                {"term": "dove fa male", "translation": "where does it hurt"},
                {"term": "ha la febbre", "translation": "do you have a fever"},
                {"term": "ho mal di", "translation": "I have an ache in"},
                {"term": "sto male", "translation": "I feel bad"},
                {"term": "non posso venire", "translation": "I can't come"},
                {"term": "devo", "translation": "I must"},
                {"term": "riposare", "translation": "to rest"},
                {"term": "dottore", "translation": "doctor"}
            ],
            "exercises": [
                {
                    "type": "boss_fight",
                    "step": 1,
                    "prompt": "You need medical help: describe your symptoms to a doctor, then cancel dinner plans with a friend.",
                    "scenario": "medical_check",
                    "ai_prompt": "You are a formal doctor asking about symptoms, then a friend asking about dinner plans.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Doctor's Visit",
                            "round_description": "A doctor asks about your symptoms.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno. Come sta?",
                                    "user_requirement": "Greet formally and say you don't feel well.",
                                    "required_words": ["Buongiorno", "sto male", "non", "bene"],
                                    "hints": ["Buongiorno, sto male", "Non sto bene", "Sto male"],
                                    "invalid_responses": ["Ciao!", "I'm sick", "Not good"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Mi dispiace. Dove Le fa male?",
                                    "user_requirement": "Describe where it hurts using 'ho mal di' or 'mi fa male'.",
                                    "required_words": ["ho mal di", "testa", "gola", "pancia", "mi fa male"],
                                    "hints": ["Ho mal di testa", "Ho mal di gola", "Mi fa male la pancia"],
                                    "invalid_responses": ["Head hurts", "Throat", "Stomach"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Capisco. Ha la febbre?",
                                    "user_requirement": "Answer yes or no about having a fever.",
                                    "required_words": ["Sì", "No", "ho", "febbre"],
                                    "hints": ["Sì, ho la febbre", "No, non ho la febbre"],
                                    "invalid_responses": ["Yes fever", "No fever", "Fever"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Bene. Deve riposare a casa.",
                                    "user_requirement": "Acknowledge the doctor's advice.",
                                    "required_words": ["Grazie", "va bene", "certo"],
                                    "hints": ["Grazie, dottore", "Va bene", "Certo"],
                                    "invalid_responses": ["Thanks", "OK", "Sure"]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Canceling Plans",
                            "round_description": "Your friend calls about dinner plans.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Ci vediamo stasera per cena?",
                                    "user_requirement": "Say you can't come because you're sick.",
                                    "required_words": ["non posso", "venire", "sto male"],
                                    "hints": ["Non posso venire, sto male", "Sto male, non posso venire"],
                                    "invalid_responses": ["Can't come", "I'm sick", "No come"]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Mi dispiace! Cosa hai?",
                                    "user_requirement": "Tell them your symptom briefly.",
                                    "required_words": ["ho mal di", "febbre", "raffreddore"],
                                    "hints": ["Ho mal di testa", "Ho la febbre", "Ho il raffreddore"],
                                    "invalid_responses": ["Headache", "Fever", "Cold"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Povero! Devo riposare?",
                                    "user_requirement": "Confirm you must rest using 'devo'.",
                                    "required_words": ["Sì", "devo", "riposare"],
                                    "hints": ["Sì, devo riposare", "Devo riposare a casa"],
                                    "invalid_responses": ["Yes rest", "Must rest", "Rest"]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Capisco. Riposati bene!",
                                    "user_requirement": "Thank them and say goodbye informally.",
                                    "required_words": ["Grazie", "ciao", "a presto"],
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
