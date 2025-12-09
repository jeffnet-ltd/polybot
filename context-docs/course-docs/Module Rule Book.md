# Module Rule Book: Pedagogical Structure for PolyBot A1 Modules

**Based on Analysis of Module A1.1: Greetings & Introductions**

---

## 📊 Lesson Structure Overview

### Exercise Count Per Lesson

- **Self-Assessment Lesson (Lesson 0):** 1 exercise
- **Regular Lessons (Lessons 1-8):** 8-12 exercises (average: ~9-10 exercises)
- **Boss Fight Lesson:** 1 exercise (boss_fight type)

**Rule:** Regular lessons should contain **8-12 exercises**, with most lessons having **8-10 exercises**. Longer lessons (11-12 exercises) typically include more vocabulary or complex grammar concepts.

---

## 🎯 Exercise Type Categories

### Passive Exercises (Receptive Skills: Reading/Listening)
- **info_card** - Vocabulary/phrase introduction with audio
- **match** - Connecting concepts (Italian ↔ English, or concept matching)
- **listening_comprehension** - Audio-based comprehension questions
- **reading_comprehension** - Text-based comprehension questions

### Active Exercises (Productive Skills: Writing/Speaking)
- **unscramble** - Sentence construction (drag-and-drop word order)
- **echo_chamber** - Pronunciation practice (voice recording)
- **mini_prompt** - Contextual speaking/writing practice
- **free_writing** - Open-ended writing tasks
- **fill_blank** - Fill-in-the-blank exercises
- **multiple_choice** - Multiple choice questions (selection-based)
- **gender_categorize** - Drag-and-drop categorization
- **form_fill** - Form completion exercises

### Special Exercises
- **self_assessment** - Confidence-based assessment (Lesson 0 only)
- **boss_fight** - Conversation practice (Final lesson only)

---

## 📈 Passive vs Active Ratio

**Analysis from A1.1:**
- **Passive exercises:** ~40-45% of total exercises
- **Active exercises:** ~55-60% of total exercises

**Rule:** Maintain a **40:60 to 45:55 ratio** of Passive:Active exercises. This ensures learners receive sufficient input before being asked to produce language.

**Breakdown by lesson:**
- Early lessons (1-2): Slightly more passive (50:50) to build vocabulary
- Middle lessons (3-6): Balanced (40:60) with more active practice
- Later lessons (7-8): More active (35:65) to reinforce production

---

## 🔄 Standard Exercise Sequence Pattern

### Phase 1: Vocabulary Introduction (Steps 1-2)
**Pattern:** `info_card` → `info_card` (optional) → `match`

- **Step 1:** Always start with `info_card`(s) introducing new vocabulary/phrases
  - Can have 1-7 `info_card` exercises at step 1 (depending on vocabulary load)
  - Each `info_card` introduces one term/phrase with audio
  - May include grammar `info_card` (e.g., "Grammar: The Verb 'To Be'")
- **Step 2:** Follow with `match` exercise to connect concepts
  - Sometimes `multiple_choice` or `gender_categorize` at step 2 instead
  - Can have multiple `match` exercises at step 2

### Phase 2: Comprehension Practice (Steps 3-4)
**Pattern:** `listening_comprehension` OR `reading_comprehension` → `unscramble`

- **Step 3-4:** Comprehension exercise (listening OR reading, not both in same lesson usually)
  - `listening_comprehension` appears in most lessons
  - `reading_comprehension` appears in lessons with dialogue/conversation focus
- **Step 3-4:** `unscramble` exercise for sentence construction
  - Often appears after comprehension
  - May include `common_mistakes` array for pattern-based feedback

### Phase 3: Active Practice (Steps 4-7)
**Pattern:** `echo_chamber` → `fill_blank` (optional) → `mini_prompt`

- **Step 4-6:** `echo_chamber` for pronunciation practice
  - Can have 1-2 `echo_chamber` exercises
  - Focuses on specific sounds/phrases from the lesson
- **Step 4-8:** `fill_blank` exercises (optional, appears in grammar-focused lessons)
  - Usually 1-2 per lesson
  - Tests specific grammar points (articles, verb forms, etc.)
- **Step 6-7:** `mini_prompt` for contextual practice
  - Appears in most lessons
  - Provides real-world scenario for language use

### Phase 4: Extended Practice (Steps 7-9)
**Pattern:** `free_writing` (optional) → `form_fill` (optional) → `match` (review)

- **Step 7-8:** `free_writing` (appears in ~50% of lessons)
  - Usually in lessons that build toward complete introductions/conversations
  - Includes `required_elements` array for validation
  - Includes `example_response` for guidance
- **Step 6-8:** `form_fill` (appears in 1-2 lessons per module)
  - Usually in lessons about personal information
  - Includes `form_fields` array with validation rules
- **Step 8-9:** Final `match` exercise with `review: True` flag
  - Always at the end of regular lessons (before extension)
  - Consolidates all key vocabulary from the lesson
  - Uses prompt: "Review: Match [topic]"

### Phase 5: Extension (Step 10, Optional)
**Pattern:** `mini_prompt` with `extension: True` and `optional: True`

- **Step 10:** Optional challenge exercise
  - Only appears in some lessons (not all)
  - Marked with `extension: True` and `optional: True`
  - More complex scenario requiring multiple elements

---

## 📋 Detailed Sequence Rules

### Rule 1: Lesson Opening
- **MUST start with `info_card`(s)** at step 1
- Can have multiple `info_card` exercises at step 1 (all share same step number)
- Grammar `info_card` can appear at step 1 or step 2

### Rule 2: Early Connection
- **After `info_card`(s), use `match`** at step 2
- Alternative: `multiple_choice` or `gender_categorize` at step 2
- Can have multiple exercises at step 2 (all share same step number)

### Rule 3: Comprehension
- **Include at least ONE comprehension exercise** (listening OR reading)
- Usually at step 3 or 4
- `listening_comprehension` is more common than `reading_comprehension`

### Rule 4: Sentence Construction
- **Include `unscramble` exercise** after vocabulary introduction
- Usually at step 3-5
- Can have multiple `unscramble` exercises (all share same step number)
- Include `common_mistakes` array when teaching critical grammar points

### Rule 5: Pronunciation
- **Include 1-2 `echo_chamber` exercises** per lesson
- Usually at step 4-6
- Focus on key phrases/sounds from the lesson

### Rule 6: Grammar Practice
- **Include `fill_blank` exercises** in grammar-focused lessons
- Usually at step 4-8
- Can have multiple `fill_blank` exercises (all share same step number)

### Rule 7: Contextual Practice
- **Include `mini_prompt`** in most lessons
- Usually at step 6-7
- Provides real-world scenario

### Rule 8: Extended Writing
- **Include `free_writing`** in lessons that build complete skills
- Usually at step 7-10
- Not in every lesson (appears in ~50% of lessons)
- Must include `required_elements` and `example_response`

### Rule 9: Form Completion
- **Include `form_fill`** in 1-2 lessons per module
- Usually in lessons about personal information/registration
- Must include `form_fields` array with proper validation

### Rule 10: Lesson Closing
- **MUST end with `match` review exercise** (except Boss Fight)
- Always at step 8-9 (or step 10 if no extension)
- Must have `review: True` flag
- Prompt format: "Review: Match [topic]"

### Rule 11: Extension Activities
- **Optional `mini_prompt` with `extension: True`** at step 10
- Only in some lessons (not required)
- More challenging scenario

---

## 🎨 Special Features Distribution

### Cultural Notes
- **Frequency:** 1-2 per module
- **Type:** `info_card` with `cultural_note: True`
- **Placement:** Usually at step 4-6, after vocabulary introduction
- **Content:** Cultural context relevant to the lesson topic

### Common Mistakes
- **Frequency:** 1-3 per module
- **Type:** `common_mistakes` array within `unscramble` exercises
- **Placement:** In `unscramble` exercises teaching critical grammar
- **Content:** Pattern-based mistake detection with specific explanations

### Review Exercises
- **Frequency:** 1 per regular lesson (not Boss Fight)
- **Type:** `match` with `review: True`
- **Placement:** Always at the end (step 8-9 or step 10)
- **Content:** Consolidates all key vocabulary from the lesson

### Extension Activities
- **Frequency:** 1-2 per module
- **Type:** `mini_prompt` with `extension: True` and `optional: True`
- **Placement:** Step 10 (after review)
- **Content:** More complex, multi-element scenarios

---

## 🏗️ Module-Level Structure

### Lesson 0: Self-Assessment
- **Exercise Count:** 1
- **Exercise Type:** `self_assessment`
- **Purpose:** Assess learner confidence before starting module
- **Features:** `skip_allowed: True`, confidence-based questions

### Lessons 1-8: Content Lessons
- **Exercise Count:** 8-12 exercises each
- **Sequence:** Follows standard sequence pattern above
- **Progression:** Builds complexity gradually
- **Features:** Mix of passive/active, includes review at end

### Final Lesson: Boss Fight
- **Exercise Count:** 1
- **Exercise Type:** `boss_fight`
- **Structure:** Contains `conversation_flow` with 2 rounds
- **Rounds:** 
  - Round 1: Informal conversation (4 turns)
  - Round 2: Formal conversation (4 turns)
- **Features:** `required_words`, `hints`, `invalid_responses` for each turn

---

## 📝 Step Numbering Rules

### Shared Step Numbers
- Multiple exercises can share the same step number
- Common pattern: Multiple `info_card` exercises all at step 1
- Common pattern: Multiple exercises at step 2 (`match`, `multiple_choice`, etc.)
- Common pattern: Multiple exercises at step 4 (`unscramble`, `echo_chamber`, `fill_blank`)

### Sequential Steps
- Steps generally progress sequentially (1, 2, 3, 4...)
- But can have gaps (e.g., step 1, step 2, step 4, step 5)
- Final review is always at the highest step number (8, 9, or 10)

---

## ✅ Quality Checklist for New Modules

When creating a new module, ensure:

1. ✅ Lesson 0 is a self-assessment (1 exercise)
2. ✅ Regular lessons have 8-12 exercises
3. ✅ Each lesson starts with `info_card`(s) at step 1
4. ✅ Each lesson includes at least one comprehension exercise (listening OR reading)
5. ✅ Each lesson includes at least one `unscramble` exercise
6. ✅ Each lesson includes 1-2 `echo_chamber` exercises
7. ✅ Each lesson includes a `mini_prompt` for contextual practice
8. ✅ Each lesson ends with a `match` review exercise (`review: True`)
9. ✅ Passive:Active ratio is approximately 40:60 to 45:55
10. ✅ 1-2 lessons include `free_writing` exercises
11. ✅ 1-2 lessons include `form_fill` exercises (if applicable to module topic)
12. ✅ 1-2 lessons include cultural notes (`info_card` with `cultural_note: True`)
13. ✅ Critical grammar lessons include `common_mistakes` in `unscramble` exercises
14. ✅ Final lesson is a Boss Fight with 2 rounds (informal + formal)
15. ✅ Boss Fight has 4 turns per round with proper `required_words`, `hints`, and `invalid_responses`

---

## 🎯 Exercise Type Usage Frequency (Per Module)

Based on A1.1 analysis:

- **info_card:** 20-30 per module (most common)
- **match:** 10-15 per module
- **unscramble:** 8-12 per module
- **echo_chamber:** 8-12 per module
- **listening_comprehension:** 6-8 per module
- **reading_comprehension:** 2-4 per module
- **fill_blank:** 4-8 per module
- **mini_prompt:** 8-10 per module
- **free_writing:** 2-4 per module
- **multiple_choice:** 2-4 per module
- **gender_categorize:** 1-2 per module (when teaching noun gender)
- **form_fill:** 1-2 per module (when teaching forms/registration)
- **self_assessment:** 1 per module (Lesson 0 only)
- **boss_fight:** 1 per module (Final lesson only)

---

## 🔍 Sequence Examples

### Example 1: Simple Vocabulary Lesson (8 exercises)
1. `info_card` (step 1)
2. `info_card` (step 1)
3. `match` (step 2)
4. `listening_comprehension` (step 3)
5. `unscramble` (step 4)
6. `echo_chamber` (step 5)
7. `mini_prompt` (step 6)
8. `match` review (step 7, `review: True`)

### Example 2: Grammar-Focused Lesson (10 exercises)
1. `info_card` (step 1)
2. `info_card` Grammar (step 2)
3. `match` (step 2)
4. `reading_comprehension` (step 3)
5. `unscramble` with `common_mistakes` (step 4)
6. `echo_chamber` (step 5)
7. `fill_blank` (step 6)
8. `fill_blank` (step 6)
9. `mini_prompt` (step 7)
10. `match` review (step 8, `review: True`)

### Example 3: Comprehensive Lesson (11 exercises)
1. `info_card` (step 1) × 5
2. `match` (step 2) × 2
3. `listening_comprehension` (step 3)
4. `unscramble` (step 4) × 2
5. `echo_chamber` (step 5) × 2
6. `fill_blank` (step 6) × 2
7. `form_fill` (step 7)
8. `mini_prompt` (step 8)
9. `free_writing` (step 9)
10. `match` review (step 10, `review: True`)
11. `mini_prompt` extension (step 11, `extension: True`, `optional: True`)

---

## 📚 Vocabulary Introduction Pattern

### Multiple info_card Exercises
- When introducing 3+ vocabulary terms, use multiple `info_card` exercises
- All share step 1
- Each introduces one term/phrase
- Include audio_url for each
- Can mix "New Phrase" and "New Word" prompts

### Grammar info_card
- Can appear at step 1 or step 2
- Prompt: "Grammar: [Topic]"
- Explains grammar concept with examples
- Usually appears before exercises that practice that grammar

---

## 🎭 Boss Fight Structure

### Required Elements
- **Type:** `boss_fight`
- **Structure:** Contains `conversation_flow` array
- **Rounds:** Exactly 2 rounds
  - Round 1: Informal conversation (4 turns)
  - Round 2: Formal conversation (4 turns)
- **Each Turn Must Include:**
  - `turn`: Turn number (1-4)
  - `ai_message`: AI's message in target language
  - `user_requirement`: Description of what user should do
  - `required_words`: Array of words/phrases user must include
  - `hints`: Array of helpful hints
  - `invalid_responses`: Array of common incorrect responses (for feedback)

### Round Structure
- **Round 1:** Informal conversation
  - Turn 1: Greeting
  - Turn 2: "How are you?" exchange
  - Turn 3: Introduction
  - Turn 4: Goodbye
- **Round 2:** Formal conversation
  - Turn 1: Formal greeting
  - Turn 2: Formal "How are you?" exchange
  - Turn 3: Formal introduction
  - Turn 4: Formal goodbye

---

## 🎓 Pedagogical Principles Embedded

1. **Scaffolding:** Start with passive (receptive) exercises, move to active (productive)
2. **Spaced Repetition:** Review exercises at the end of each lesson
3. **Contextual Learning:** Mini-prompts provide real-world scenarios
4. **Error Prevention:** Common mistakes arrays catch patterns before they become habits
5. **Cultural Awareness:** Cultural notes provide context beyond language
6. **Progressive Complexity:** Lessons build from simple to complex
7. **Multi-Modal Learning:** Combines listening, reading, writing, and speaking
8. **Authentic Practice:** Boss Fight provides realistic conversation practice

---

## 📌 Key Takeaways for Module Creation

1. **Always start with vocabulary introduction** (`info_card` at step 1)
2. **Always end with review** (`match` with `review: True`)
3. **Balance passive and active** (40:60 to 45:55 ratio)
4. **Include pronunciation practice** (`echo_chamber` in every lesson)
5. **Provide contextual practice** (`mini_prompt` in most lessons)
6. **Build toward production** (`free_writing` in lessons that combine skills)
7. **Include cultural context** (1-2 cultural notes per module)
8. **Catch common mistakes** (`common_mistakes` in critical grammar exercises)
9. **End with conversation practice** (Boss Fight with 2 rounds)

---

**Last Updated:** Based on Module A1.1 analysis
**Use Case:** Template for creating Module A1.2 and future modules

