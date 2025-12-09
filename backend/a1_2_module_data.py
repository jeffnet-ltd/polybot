"""
Module A1.2 data structure - Personal Information & Family
Strictly follows the 'Vocab Whitelist' pattern to prevent sequence breaking.
"""

MODULE_A1_2_LESSONS = {
    "module_id": "A1.2",
    "title": "Personal Information & Family",
    "goal": "Ask/answer personal details (Age, Job, Origin) and describe family relationships.",
    "lessons": [
        {
            "lesson_id": "A1.2.0",
            "title": "Self-Assessment: Personal Information & Family",
            "focus": "Assess your confidence with numbers and personal details",
            "exercises": [
                {
                    "type": "self_assessment",
                    "step": 0,
                    "prompt": "How confident do you feel talking about yourself?",
                    "assessment_type": "confidence",
                    "questions": [
                        {
                            "question": "I can say my age and phone number",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can talk about my profession",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can introduce my family members",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        },
                        {
                            "question": "I can fill out a simple registration form",
                            "options": ["Very confident", "Somewhat confident", "Not confident"]
                        }
                    ],
                    "skip_allowed": True,
                    "explanation": "This helps tailor your learning path."
                }
            ]
        },
        {
            "lesson_id": "A1.2.1",
            "title": "Numbers 0-10 & Age",
            "focus": "Numbers 0-10, Verb 'Avere' (To have) for age",
            "vocabulary": [
                {"term": "zero", "translation": "zero"},
                {"term": "uno", "translation": "one"},
                {"term": "due", "translation": "two"},
                {"term": "tre", "translation": "three"},
                {"term": "quattro", "translation": "four"},
                {"term": "cinque", "translation": "five"},
                {"term": "sei", "translation": "six"},
                {"term": "sette", "translation": "seven"},
                {"term": "otto", "translation": "eight"},
                {"term": "nove", "translation": "nine"},
                {"term": "dieci", "translation": "ten"},
                {"term": "Ho ... anni", "translation": "I am ... years old (lit: I have ... years)"},
                {"term": "Quanti anni hai?", "translation": "How old are you?"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Expressing Age",
                    "correct_answer": "Avere (To Have)",
                    "explanation": "In Italian, we use 'Avere' (to have) for age, not 'Essere' (to be).\n\nCorrect: Ho 20 anni (I have 20 years)\nIncorrect: Sono 20 (I am 20)",
                    "sub_text": "Critical Grammar Concept"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "zero",
                    "explanation": "zero",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_zero_0.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "uno",
                    "explanation": "one",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_uno_1.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "due",
                    "explanation": "two",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_due_2.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "tre",
                    "explanation": "three",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tre_3.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quattro",
                    "explanation": "four",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quattro_4.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cinque",
                    "explanation": "five",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cinque_5.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sei",
                    "explanation": "six",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sei_6.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sette",
                    "explanation": "seven",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sette_7.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "otto",
                    "explanation": "eight",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_otto_8.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "nove",
                    "explanation": "nine",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_nove_9.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dieci",
                    "explanation": "ten",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dieci_10.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Quanti anni hai?",
                    "explanation": "How old are you?",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quanti_anni_hai_11.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Ho ... anni",
                    "explanation": "I am ... years old (lit: I have ... years)",
                    "sub_text": "Use with numbers: Ho dieci anni",
                    "audio_url": "/static/audio/it_ho_anni_12.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Numbers 0-5",
                    "pairs": [["zero", "0"], ["uno", "1"], ["due", "2"], ["tre", "3"], ["quattro", "4"], ["cinque", "5"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic number recognition"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Numbers 6-10",
                    "pairs": [["sei", "6"], ["sette", "7"], ["otto", "8"], ["nove", "9"], ["dieci", "10"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic number recognition"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. How old is Marco?",
                    "audio_text": "Ciao, mi chiamo Marco e ho otto anni.",
                    "options": ["8", "10", "5", "9"],
                    "correct_answer": "8",
                    "explanation": "You heard 'otto anni' (eight years).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I am 10 years old.",
                    "blocks": ["Ho", "dieci", "anni", "."],
                    "correct_answer": "Ho dieci anni.",
                    "explanation": "Remembers: Subject (Io) is often omitted. 'Ho' includes 'I'.",
                    "common_mistakes": [
                        {
                            "pattern": "Sono dieci anni",
                            "explanation": "Remember! Use 'Ho' (I have) for age, not 'Sono' (I am)."
                        }
                    ]
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Ho cinque anni",
                    "target_phrase": "Ho cinque anni",
                    "target_lang": "it",
                    "explanation": "Practice the 'H' being silent in 'Ho'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Quanti ___ hai?'",
                    "options": ["anni", "quanti", "ho", "due"],
                    "correct_answer": "anni",
                    "explanation": "Use 'anni' (years) when asking about age"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "A child asks: 'Quanti anni hai?'",
                    "context": "You are roleplaying as a 9-year-old.",
                    "task": "Say you are 9 years old.",
                    "target_lang": "it",
                    "explanation": "Use 'Ho' + number + 'anni'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match numbers",
                    "pairs": [["uno", "1"], ["dieci", "10"], ["cinque", "5"], ["otto", "8"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of Lesson 1 Vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.2",
            "title": "Numbers 11-20 & Phone Numbers",
            "focus": "Numbers 11-20, exchanging phone numbers",
            "vocabulary": [
                {"term": "undici", "translation": "11"},
                {"term": "dodici", "translation": "12"},
                {"term": "tredici", "translation": "13"},
                {"term": "quattordici", "translation": "14"},
                {"term": "quindici", "translation": "15"},
                {"term": "sedici", "translation": "16"},
                {"term": "diciassette", "translation": "17"},
                {"term": "diciotto", "translation": "18"},
                {"term": "diciannove", "translation": "19"},
                {"term": "venti", "translation": "20"},
                {"term": "il numero", "translation": "number"},
                {"term": "Qual è il tuo numero?", "translation": "What is your number?"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Pattern Alert: The 'Teen' Numbers",
                    "correct_answer": "-dici vs. dicia-",
                    "explanation": "11-16 end in -dici (undici, dodici...)\n17-19 start with dicia- (diciassette, diciotto...)",
                    "sub_text": "Notice the pattern shift at 17"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "undici",
                    "explanation": "11",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_undici_13.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dodici",
                    "explanation": "12",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dodici_14.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "tredici",
                    "explanation": "13",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_tredici_15.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quattordici",
                    "explanation": "14",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quattordici_16.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "quindici",
                    "explanation": "15",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_quindici_17.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sedici",
                    "explanation": "16",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sedici_18.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "diciassette",
                    "explanation": "17",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_diciassette_19.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "diciotto",
                    "explanation": "18",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_diciotto_20.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "diciannove",
                    "explanation": "19",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_diciannove_21.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "venti",
                    "explanation": "20",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_venti_22.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Qual è il tuo numero?",
                    "explanation": "What is your number?",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_qual_e_il_tuo_numero_23.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Numbers 11-15",
                    "pairs": [["undici", "11"], ["dodici", "12"], ["tredici", "13"], ["quattordici", "14"], ["quindici", "15"]],
                    "correct_answer": "match_all",
                    "explanation": "Identify the first set of teens"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Numbers 16-20",
                    "pairs": [["sedici", "16"], ["diciassette", "17"], ["diciotto", "18"], ["diciannove", "19"], ["venti", "20"]],
                    "correct_answer": "match_all",
                    "explanation": "Identify the higher teens"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. What is the hotel room number?",
                    "audio_text": "La tua camera è la numero diciotto.",
                    "options": ["18", "12", "8", "19"],
                    "correct_answer": "18",
                    "explanation": "You heard 'diciotto' (18).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "What is your number?",
                    "blocks": ["Qual", "è", "il", "tuo", "numero", "?"],
                    "correct_answer": "Qual è il tuo numero?",
                    "explanation": "Standard question format for phone numbers."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Diciassette",
                    "target_phrase": "Diciassette",
                    "target_lang": "it",
                    "explanation": "Focus on the double 's' and double 't'."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete sequence: Dieci, ____, Dodici",
                    "options": ["Undici", "Tredici", "Venti"],
                    "correct_answer": "Undici",
                    "explanation": "Sequence logic: 10, 11, 12"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Qual è il tuo numero?'",
                    "context": "You are at a registration desk.",
                    "task": "Say your phone number using Italian numbers.",
                    "target_lang": "it",
                    "explanation": "Use Italian numbers you learned (e.g., 'tre, cinque, due...')"
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match all numbers 11-20",
                    "pairs": [["quindici", "15"], ["venti", "20"], ["diciotto", "18"], ["dodici", "12"]],
                    "correct_answer": "match_all",
                    "explanation": "Consolidation of Lesson 2",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.3",
            "title": "Professions (Gender Focus)",
            "focus": "Jobs, masculine/feminine endings, indefinite articles (un/una)",
            "vocabulary": [
                {"term": "lavoro", "translation": "job/work"},
                {"term": "Che lavoro fai?", "translation": "What do you do? (Informal)"},
                {"term": "Faccio...", "translation": "I work as... (lit: I do...)"},
                {"term": "studente", "translation": "student (male)"},
                {"term": "studentessa", "translation": "student (female)"},
                {"term": "insegnante", "translation": "teacher (unisex)"},
                {"term": "impiegato", "translation": "office worker (male)"},
                {"term": "impiegata", "translation": "office worker (female)"},
                {"term": "dottore", "translation": "doctor (male)"},
                {"term": "dottoressa", "translation": "doctor (female)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Talking about jobs",
                    "correct_answer": "Faccio il/la...",
                    "explanation": "In Italian, we often use 'Faccio' (I do) to state our job.\nExample: Faccio l'insegnante (I work as a teacher).",
                    "sub_text": "Verb: Fare (To Do)"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "studente",
                    "explanation": "student (male)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_studente_24.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "studentessa",
                    "explanation": "student (female)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_studentessa_25.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "insegnante",
                    "explanation": "teacher (unisex)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_insegnante_26.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "impiegato",
                    "explanation": "office worker (male)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_impiegato_27.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "impiegata",
                    "explanation": "office worker (female)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_impiegata_28.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dottore",
                    "explanation": "doctor (male)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dottore_29.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "dottoressa",
                    "explanation": "doctor (female)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_dottoressa_30.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Phrase",
                    "correct_answer": "Che lavoro fai?",
                    "explanation": "What do you do? (Informal)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_che_lavoro_fai_31.mp3"
                },
                {
                    "type": "gender_categorize",
                    "step": 2,
                    "prompt": "Sort jobs by gender",
                    "columns": [
                        {"id": "masc", "label": "Maschile (Male)"},
                        {"id": "fem", "label": "Femminile (Female)"}
                    ],
                    "items": [
                        {"text": "Dottore", "column_id": "masc", "hint": "Ends in -e (doctor)"},
                        {"text": "Dottoressa", "column_id": "fem", "hint": "Ends in -essa (female doctor)"},
                        {"text": "Impiegato", "column_id": "masc", "hint": "Ends in -o"},
                        {"text": "Studentessa", "column_id": "fem", "hint": "Ends in -essa"}
                    ],
                    "correct_answer": "all_correct",
                    "explanation": "Many professions change ending based on gender."
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match the job to the person",
                    "pairs": [["Maria (Female)", "Studentessa"], ["Marco (Male)", "Studente"], ["Luisa (Female)", "Dottoressa"]],
                    "correct_answer": "match_all",
                    "explanation": "Matching gendered nouns to names"
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I work as a teacher.",
                    "blocks": ["Faccio", "l'", "insegnante", "."],
                    "correct_answer": "Faccio l'insegnante.",
                    "explanation": "Faccio + article + noun."
                },
                {
                    "type": "echo_chamber",
                    "step": 5,
                    "prompt": "Repeat: Faccio l'insegnante",
                    "target_phrase": "Faccio l'insegnante",
                    "target_lang": "it",
                    "explanation": "Practice 'Faccio' and the article 'l'' before vowel."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Faccio ___ studentessa.' (I work as a student - female)",
                    "options": ["un", "una", "lo", "la"],
                    "correct_answer": "una",
                    "explanation": "Use 'una' with feminine nouns like 'studentessa'"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Someone asks: 'Che lavoro fai?'",
                    "context": "You are a student (female).",
                    "task": "Reply that you are a student.",
                    "target_lang": "it",
                    "explanation": "Use the feminine form 'Studentessa'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Match professions",
                    "pairs": [["impiegato", "office worker"], ["dottore", "doctor"], ["insegnante", "teacher"], ["studente", "student"]],
                    "correct_answer": "match_all",
                    "explanation": "Review of professions",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.4",
            "title": "Immediate Family & Possessives (My/Your)",
            "focus": "Family members, Mio/Tuo (My/Your)",
            "vocabulary": [
                {"term": "madre", "translation": "mother"},
                {"term": "padre", "translation": "father"},
                {"term": "fratello", "translation": "brother"},
                {"term": "sorella", "translation": "sister"},
                {"term": "famiglia", "translation": "family"},
                {"term": "mio", "translation": "my (masculine)"},
                {"term": "mia", "translation": "my (feminine)"},
                {"term": "tuo", "translation": "your (masculine)"},
                {"term": "tua", "translation": "your (feminine)"},
                {"term": "Chi è?", "translation": "Who is he/she?"},
                {"term": "questo", "translation": "this (masculine)"},
                {"term": "questa", "translation": "this (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Possessives",
                    "correct_answer": "Mio vs Mia",
                    "explanation": "The possessive must match the gender of the FAMILY MEMBER, not you.\n\nMio padre (My father) -> Masc\nMia madre (My mother) -> Fem",
                    "sub_text": "Agreement Rule"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "madre",
                    "explanation": "mother",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_madre_32.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "padre",
                    "explanation": "father",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_padre_33.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "fratello",
                    "explanation": "brother",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_fratello_34.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sorella",
                    "explanation": "sister",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sorella_35.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "famiglia",
                    "explanation": "family",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_famiglia_36.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Family Members",
                    "pairs": [["Madre", "Mother"], ["Padre", "Father"], ["Fratello", "Brother"], ["Sorella", "Sister"]],
                    "correct_answer": "match_all",
                    "explanation": "Basic family vocabulary"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Who is this?",
                    "audio_text": "Questa è mia sorella Anna.",
                    "options": ["My sister", "My mother", "My brother", "My father"],
                    "correct_answer": "My sister",
                    "explanation": "You heard 'mia sorella' (my sister).",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "This is my sister.",
                    "blocks": ["Questa", "è", "mia", "sorella", "."],
                    "correct_answer": "Questa è mia sorella.",
                    "explanation": "Questa (This) + è (is) + mia (my) + sorella (sister).",
                    "common_mistakes": [
                        {
                            "pattern": "la mia sorella",
                            "explanation": "Note: In Italian, we usually drop the article 'la' with singular family members! Just 'mia sorella', not 'la mia sorella'."
                        }
                    ]
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: '___ fratello' (My brother)",
                    "options": ["Mio", "Mia"],
                    "correct_answer": "Mio",
                    "explanation": "Fratello is masculine, so use Mio."
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: '___ madre' (My mother)",
                    "options": ["Mio", "Mia"],
                    "correct_answer": "Mia",
                    "explanation": "Madre is feminine, so use Mia."
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat: Mio padre",
                    "target_phrase": "Mio padre",
                    "target_lang": "it",
                    "explanation": "Practice possessive + family member"
                },
                {
                    "type": "mini_prompt",
                    "step": 7,
                    "prompt": "Introduce your father.",
                    "context": "You are showing a photo.",
                    "task": "Say: This is my father.",
                    "target_lang": "it",
                    "explanation": "Use 'Questo è mio padre'."
                },
                {
                    "type": "match",
                    "step": 8,
                    "prompt": "Review: Family & Possessives",
                    "pairs": [["Mio padre", "My father"], ["Mia madre", "My mother"], ["Mio fratello", "My brother"], ["Mia sorella", "My sister"]],
                    "correct_answer": "match_all",
                    "explanation": "Possessive agreement review",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.5",
            "title": "Extended Family (Grandparents & Cousins)",
            "focus": "Extended tree, Suo/Sua (His/Her)",
            "vocabulary": [
                {"term": "nonno", "translation": "grandfather"},
                {"term": "nonna", "translation": "grandmother"},
                {"term": "zio", "translation": "uncle"},
                {"term": "zia", "translation": "aunt"},
                {"term": "cugino", "translation": "cousin (male)"},
                {"term": "cugina", "translation": "cousin (female)"},
                {"term": "figlio", "translation": "son"},
                {"term": "figlia", "translation": "daughter"},
                {"term": "suo", "translation": "his/her (masculine)"},
                {"term": "sua", "translation": "his/her (feminine)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "nonno",
                    "explanation": "grandfather",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_nonno_37.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "nonna",
                    "explanation": "grandmother",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_nonna_38.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "zio",
                    "explanation": "uncle",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_zio_39.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "zia",
                    "explanation": "aunt",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_zia_40.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cugino",
                    "explanation": "cousin (male)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cugino_41.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "cugina",
                    "explanation": "cousin (female)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_cugina_42.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "figlio",
                    "explanation": "son",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_figlio_43.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "figlia",
                    "explanation": "daughter",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_figlia_44.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Extended Family",
                    "pairs": [["Nonno", "Grandfather"], ["Nonna", "Grandmother"], ["Zio", "Uncle"], ["Zia", "Aunt"]],
                    "correct_answer": "match_all",
                    "explanation": "Vocabulary expansion"
                },
                {
                    "type": "listening_comprehension",
                    "step": 3,
                    "prompt": "Listen. Who is she?",
                    "audio_text": "Lei è mia zia Anna.",
                    "options": ["My aunt", "My grandmother", "My sister", "My mother"],
                    "correct_answer": "My aunt",
                    "explanation": "Zia = Aunt.",
                    "allow_replay": True,
                    "max_plays": 3
                },
                {
                    "type": "gender_categorize",
                    "step": 4,
                    "prompt": "Sort into Male/Female Relatives",
                    "columns": [
                        {"id": "masc", "label": "Maschile"},
                        {"id": "fem", "label": "Femminile"}
                    ],
                    "items": [
                        {"text": "Zio", "column_id": "masc", "hint": "Uncle"},
                        {"text": "Zia", "column_id": "fem", "hint": "Aunt"},
                        {"text": "Nonno", "column_id": "masc", "hint": "Grandpa"},
                        {"text": "Figlia", "column_id": "fem", "hint": "Daughter"}
                    ],
                    "correct_answer": "all_correct",
                    "explanation": "Reviewing gender patterns in family words."
                },
                {
                    "type": "unscramble",
                    "step": 5,
                    "prompt": "He is my son.",
                    "blocks": ["Lui", "è", "mio", "figlio", "."],
                    "correct_answer": "Lui è mio figlio.",
                    "explanation": "Simple identification sentence."
                },
                {
                    "type": "fill_blank",
                    "step": 6,
                    "prompt": "Complete: 'Sua ___ è Maria.' (His sister is Maria)",
                    "options": ["sorella", "fratello", "padre"],
                    "correct_answer": "sorella",
                    "explanation": "Use 'sua' (his/her) with feminine nouns like 'sorella'"
                },
                {
                    "type": "echo_chamber",
                    "step": 7,
                    "prompt": "Repeat: Mio nonno",
                    "target_phrase": "Mio nonno",
                    "target_lang": "it",
                    "explanation": "Practice extended family vocabulary"
                },
                {
                    "type": "mini_prompt",
                    "step": 8,
                    "prompt": "Describe your family.",
                    "context": "Someone asks about your family.",
                    "task": "Say you have a grandmother and a cousin (female).",
                    "target_lang": "it",
                    "explanation": "Use 'Ho' + family members: 'Ho una nonna e una cugina'"
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Review: Extended Family",
                    "pairs": [["figlio", "son"], ["figlia", "daughter"], ["cugino", "cousin"], ["zio", "uncle"]],
                    "correct_answer": "match_all",
                    "explanation": "Review vocabulary",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.6",
            "title": "Marital Status & Addresses",
            "focus": "Form filling vocabulary, prepositions 'A' (City) vs 'In' (Country)",
            "vocabulary": [
                {"term": "sposato", "translation": "married (male)"},
                {"term": "sposata", "translation": "married (female)"},
                {"term": "single", "translation": "single"},
                {"term": "celibe", "translation": "single/bachelor (form usage)"},
                {"term": "nubile", "translation": "single/unmarried (form usage)"},
                {"term": "indirizzo", "translation": "address"},
                {"term": "via", "translation": "street"},
                {"term": "piazza", "translation": "square"},
                {"term": "vivo a", "translation": "I live in (city)"},
                {"term": "abito in", "translation": "I live in (country/region)"}
            ],
            "exercises": [
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "Grammar: Prepositions for Place",
                    "correct_answer": "A vs In",
                    "explanation": "Vivo A Roma (City)\nVivo IN Italia (Country)\n\nRule: 'A' for cities, 'IN' for countries.",
                    "sub_text": "Vital rule for location"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sposato",
                    "explanation": "married (male)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sposato_45.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "sposata",
                    "explanation": "married (female)",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_sposata_46.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "single",
                    "explanation": "single",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_single_47.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "indirizzo",
                    "explanation": "address",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_indirizzo_48.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "via",
                    "explanation": "street",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_via_49.mp3"
                },
                {
                    "type": "info_card",
                    "step": 1,
                    "prompt": "New Word",
                    "correct_answer": "piazza",
                    "explanation": "square",
                    "sub_text": "Listen and repeat.",
                    "audio_url": "/static/audio/it_piazza_50.mp3"
                },
                {
                    "type": "match",
                    "step": 2,
                    "prompt": "Match Status",
                    "pairs": [["Sposato", "Married"], ["Single", "Single"], ["Indirizzo", "Address"], ["Via", "Street"]],
                    "correct_answer": "match_all",
                    "explanation": "Form filling vocab"
                },
                {
                    "type": "reading_comprehension",
                    "step": 3,
                    "prompt": "Read the form and answer the question.",
                    "text": "Nome: Maria Rossi\nStato Civile: Sposata\nIndirizzo: Via Roma 10",
                    "question": "What is Maria's marital status?",
                    "options": ["Sposata", "Single", "Celibe"],
                    "correct_answer": "Sposata",
                    "explanation": "The form shows 'Sposata' (married - female).",
                    "highlight_vocab": ["Sposata", "Indirizzo", "Via"]
                },
                {
                    "type": "unscramble",
                    "step": 4,
                    "prompt": "I live in Milan.",
                    "blocks": ["Vivo", "a", "Milano", "."],
                    "correct_answer": "Vivo a Milano.",
                    "explanation": "Use 'a' for cities."
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: 'Vivo ___ Milano.'",
                    "options": ["a", "in"],
                    "correct_answer": "a",
                    "explanation": "Milano is a city, so use 'a'."
                },
                {
                    "type": "fill_blank",
                    "step": 5,
                    "prompt": "Complete: 'Vivo ___ Italia.'",
                    "options": ["a", "in"],
                    "correct_answer": "in",
                    "explanation": "Italia is a country, so use 'in'."
                },
                {
                    "type": "echo_chamber",
                    "step": 6,
                    "prompt": "Repeat: Vivo a Roma",
                    "target_phrase": "Vivo a Roma",
                    "target_lang": "it",
                    "explanation": "Practice preposition 'a' with city names"
                },
                {
                    "type": "form_fill",
                    "step": 7,
                    "prompt": "Complete the Hotel Registration Form",
                    "form_fields": [
                        {
                            "label": "Nome",
                            "type": "text",
                            "required": True,
                            "validation": "name"
                        },
                        {
                            "label": "Stato Civile (Marital Status)",
                            "type": "select",
                            "options": ["Celibe/Nubile", "Sposato/a"],
                            "required": True
                        },
                        {
                            "label": "Indirizzo (Via/Piazza)",
                            "type": "text",
                            "required": True,
                            "hint": "e.g., Via Roma 10"
                        },
                        {
                            "label": "Città",
                            "type": "text",
                            "required": True
                        }
                    ],
                    "correct_answer": "all_fields_filled",
                    "explanation": "You successfully registered at the hotel!"
                },
                {
                    "type": "mini_prompt",
                    "step": 8,
                    "prompt": "You're filling out a form.",
                    "context": "The form asks: 'Dove vivi?' (Where do you live?)",
                    "task": "Say you live in Rome (city).",
                    "target_lang": "it",
                    "explanation": "Use 'Vivo a Roma' (I live in Rome - city)."
                },
                {
                    "type": "match",
                    "step": 9,
                    "prompt": "Review: Address Vocab",
                    "pairs": [["Via", "Street"], ["Piazza", "Square"], ["Vivo a", "I live in (city)"], ["Indirizzo", "Address"]],
                    "correct_answer": "match_all",
                    "explanation": "Review",
                    "review": True
                }
            ]
        },
        {
            "lesson_id": "A1.2.BOSS",
            "title": "Boss Fight: The Library Registration",
            "type": "boss_fight",
            "focus": "Applying numbers, personal info, and spelling in a formal context",
            "vocabulary": [
                {"term": "Vorrei", "translation": "I would like"},
                {"term": "iscrivermi", "translation": "to register myself"},
                {"term": "documento", "translation": "ID document"},
                {"term": "firmi qui", "translation": "sign here"}
            ],
            "exercises": [
                {
                    "type": "boss_fight",
                    "step": 1,
                    "prompt": "You are at the municipal library to get a card.",
                    "scenario": "library_clerk",
                    "ai_prompt": "You are a formal library clerk. Ask for name, age, address, and profession.",
                    "conversation_flow": [
                        {
                            "round": 1,
                            "round_name": "Registration Desk",
                            "round_description": "Provide your details to the clerk.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Buongiorno. Vorrebbe iscriversi?",
                                    "user_requirement": "Say yes and greet formally.",
                                    "required_words": ["Buongiorno", "sì", "vorrei"],
                                    "hints": ["Buongiorno, sì vorrei..."],
                                    "invalid_responses": ["Ciao, sì.", "Voglio iscrivermi."]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Bene. Come si chiama e quanti anni ha?",
                                    "user_requirement": "State name and age (Use 'Ho' for age).",
                                    "required_words": ["Mi chiamo", "ho", "anni"],
                                    "hints": ["Mi chiamo [Nome]", "Ho [Numero] anni"],
                                    "invalid_responses": ["Sono [Numero] anni", "Io sono [Numero]"]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Grazie. Qual è il suo indirizzo?",
                                    "user_requirement": "Give an address (Via/Piazza).",
                                    "required_words": ["Vivo", "a", "via"],
                                    "hints": ["Vivo a [Città]", "in via [Nome]"],
                                    "invalid_responses": ["Address is...", "Il mio indirizzo è..."]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Perfetto. Che lavoro fa?",
                                    "user_requirement": "State your profession.",
                                    "required_words": ["Faccio", "sono"],
                                    "hints": ["Faccio l'insegnante", "Sono studente"],
                                    "invalid_responses": ["Lavoro è...", "Job is..."]
                                }
                            ]
                        },
                        {
                            "round": 2,
                            "round_name": "Casual Chat",
                            "round_description": "Another student asks you about your family.",
                            "turns": [
                                {
                                    "turn": 1,
                                    "ai_message": "Ciao! Sei nuovo qui? Di dove sei?",
                                    "user_requirement": "Say you are new and where you are from.",
                                    "required_words": ["Sì", "sono di"],
                                    "hints": ["Sì, sono nuovo", "Sono di [Città/Paese]"],
                                    "invalid_responses": ["Yes", "From..."]
                                },
                                {
                                    "turn": 2,
                                    "ai_message": "Bello! Hai fratelli o sorelle?",
                                    "user_requirement": "Say yes/no and describe siblings.",
                                    "required_words": ["Ho", "fratello", "sorella"],
                                    "hints": ["Ho un fratello", "Ho una sorella", "No, sono figlio unico"],
                                    "invalid_responses": ["I have...", "Si, brother."]
                                },
                                {
                                    "turn": 3,
                                    "ai_message": "Quanti anni ha tuo fratello?",
                                    "user_requirement": "State his age.",
                                    "required_words": ["Ha", "anni"],
                                    "hints": ["Ha [Numero] anni"],
                                    "invalid_responses": ["È [Numero]", "He is..."]
                                },
                                {
                                    "turn": 4,
                                    "ai_message": "Capisco! Beh, buono studio. Ciao!",
                                    "user_requirement": "Say goodbye casually.",
                                    "required_words": ["Ciao", "grazie"],
                                    "hints": ["Ciao!", "Grazie, a presto!"],
                                    "invalid_responses": ["Arrivederci"]
                                }
                            ]
                        }
                    ],
                    "explanation": "You successfully registered and made a friend!"
                }
            ]
        }
    ]
}
