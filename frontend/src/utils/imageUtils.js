/**
 * imageUtils.js
 *
 * Utility functions for selecting topic-based images.
 * This allows for a dynamic and visually rich curriculum presentation.
 *
 * Consolidation Strategy:
 * - Similar categories share image pools to avoid redundancy
 * - Keyword aliases map related terms to primary categories
 * - Each image file appears only once, never duplicated across pools
 */

/**
 * Fisher-Yates shuffle algorithm
 * Returns a new shuffled array without modifying the original
 */
const shuffleArray = (array) => {
  const shuffled = [...array];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
};

// A mapping of keywords to a pool of available images for module headers.
// Consolidated categories cover all A1 lesson topics efficiently.
const topicImagePool = {
  // Social & Communication (greetings, introductions, conversations)
  social: [
    '/images/topics/greetings-1.jpg',
    '/images/topics/greetings-2.jpg',
    '/images/topics/greetings-3.jpg',
    '/images/topics/greetings-4.jpg',
    '/images/topics/greetings-5.jpg',
    '/images/topics/greetings-6.jpg',
    '/images/topics/greetings-7.jpg',
    '/images/topics/greetings-8.jpg',
    '/images/topics/greetings-9.jpg',
    '/images/topics/greetings-10.jpg',
  ],

  // Food & Dining (food, restaurants, cooking, meals)
  food: [
    '/images/topics/food-1.jpg',
    '/images/topics/food-2.jpg',
    '/images/topics/food-3.jpg',
  ],

  // Travel & Exploration (travel, transportation, hotels, airports)
  travel: [
    '/images/topics/travel-1.jpg',
    '/images/topics/travel-2.jpg',
    '/images/topics/travel-3.jpg',
  ],

  // People & Professions (family, people, jobs, occupations)
  people: [
    '/images/topics/people-1.jpg',
    '/images/topics/people-2.jpg',
    '/images/topics/people-3.jpg',
  ],

  // Temporal (numbers, time, days, seasons, months)
  temporal: [
    '/images/topics/temporal-1.jpg',
    '/images/topics/temporal-2.jpg',
    '/images/topics/temporal-3.jpg',
    '/images/topics/temporal-4.jpg',
  ],

  // Appearance (colors, descriptions, appearance, characteristics)
  appearance: [
    '/images/topics/appearance-1.jpg',
    '/images/topics/appearance-2.jpg',
    '/images/topics/appearance-3.jpg',
    '/images/topics/appearance-4.jpg',
    '/images/topics/appearance-5.jpg',
    '/images/topics/appearance-6.jpg',
    '/images/topics/appearance-7.jpg',
    '/images/topics/appearance-8.jpg',
    '/images/topics/appearance-9.jpg',
    '/images/topics/appearance-10.jpg',
  ],

  // Nature & Environment (nature, weather, animals, wildlife, seasons, landscapes)
  nature: [
    '/images/topics/nature-1.jpg',
    '/images/topics/nature-2.jpg',
    '/images/topics/nature-3.jpg',
  ],

  // Lifestyle (home, furniture, clothing, apartments, houses, rooms)
  lifestyle: [
    '/images/topics/lifestyle-1.jpg',
    '/images/topics/lifestyle-2.jpg',
    '/images/topics/lifestyle-3.jpg',
  ],

  // Commerce (shopping, money, markets, currency, purchases)
  commerce: [
    '/images/topics/commerce-1.jpg',
    '/images/topics/commerce-2.jpg',
    '/images/topics/commerce-3.jpg',
    '/images/topics/commerce-4.jpg',
    '/images/topics/commerce-5.jpg',
    '/images/topics/commerce-6.jpg',
    '/images/topics/commerce-7.jpg',
    '/images/topics/commerce-8.jpg',
    '/images/topics/commerce-9.jpg',
    '/images/topics/commerce-10.jpg',
  ],

  // Activities & Leisure (sports, hobbies, entertainment, games, fun, activities)
  activities: [
    '/images/topics/activities-1.jpg',
    '/images/topics/activities-2.jpg',
    '/images/topics/activities-3.jpg',
    '/images/topics/activities-4.jpg',
  ],

  // Professional (education, work, school, office, classroom, learning)
  professional: [
    '/images/topics/professional-1.jpg',
    '/images/topics/professional-2.jpg',
  ],

  // Wellness (health, body, medicine, emotions, feelings, mood)
  wellness: [
    '/images/topics/wellness-1.jpg',
    '/images/topics/wellness-2.jpg',
    '/images/topics/wellness-3.jpg',
  ],

  // Individual Numbers (0-10) - Specific number recognition
  zero: [
    '/images/topics/zero-1.jpg',
    '/images/topics/zero-2.jpg',
  ],

  uno: [
    '/images/topics/one-1.jpg',
    '/images/topics/one-2.jpg',
  ],

  due: [
    '/images/topics/two-1.jpg',
    '/images/topics/two-2.jpg',
  ],

  tre: [
    '/images/topics/three-1.jpg',
    '/images/topics/three-2.jpg',
  ],

  quattro: [
    '/images/topics/four-1.jpg',
    '/images/topics/four-2.jpg',
  ],

  cinque: [
    '/images/topics/five-1.jpg',
    '/images/topics/five-2.jpg',
  ],

  sei: [
    '/images/topics/six-1.jpg',
    '/images/topics/six-2.jpg',
  ],

  sette: [
    '/images/topics/seven-1.jpg',
    '/images/topics/seven-2.jpg',
  ],

  otto: [
    '/images/topics/eight-1.jpg',
    '/images/topics/eight-2.jpg',
  ],

  nove: [
    '/images/topics/nine-1.jpg',
    '/images/topics/nine-2.jpg',
  ],

  dieci: [
    '/images/topics/ten-1.jpg',
    '/images/topics/ten-2.jpg',
  ],

  // Default fallback
  default: [
    '/images/topics/default-1.jpg',
    '/images/topics/default-2.jpg',
    '/images/topics/default-3.jpg',
  ],
};

// Map related keywords to primary category keys
// Covers all A1 curriculum topics with broad semantic categories
const topicAliases = {
  // Social & Communication
  greetings: 'social',
  greeting: 'social',
  introduction: 'social',
  introduce: 'social',
  conversation: 'social',

  // Food & Dining
  restaurant: 'food',
  cooking: 'food',
  cuisine: 'food',
  diner: 'food',
  meal: 'food',

  // Travel & Exploration
  transportation: 'travel',
  hotel: 'travel',
  airport: 'travel',
  flight: 'travel',

  // People & Professions
  family: 'people',
  professions: 'people',
  profession: 'people',
  occupation: 'people',
  job: 'people',
  careers: 'people',

  // Temporal
  numbers: 'temporal',
  time: 'temporal',
  days: 'temporal',
  day: 'temporal',
  months: 'temporal',
  month: 'temporal',
  seasons: 'temporal',
  season: 'temporal',

  // Appearance
  colors: 'appearance',
  color: 'appearance',
  descriptions: 'appearance',
  describe: 'appearance',

  // Nature & Environment
  animals: 'nature',
  wildlife: 'nature',
  weather: 'nature',
  environment: 'nature',
  landscape: 'nature',

  // Lifestyle
  home: 'lifestyle',
  house: 'lifestyle',
  furniture: 'lifestyle',
  apartment: 'lifestyle',
  room: 'lifestyle',
  clothes: 'lifestyle',
  clothing: 'lifestyle',
  outfit: 'lifestyle',
  dress: 'lifestyle',

  // Commerce
  shopping: 'commerce',
  market: 'commerce',
  money: 'commerce',
  currency: 'commerce',
  purchase: 'commerce',

  // Activities & Leisure
  sports: 'activities',
  hobbies: 'activities',
  hobby: 'activities',
  entertainment: 'activities',
  leisure: 'activities',
  fun: 'activities',
  activity: 'activities',
  games: 'activities',

  // Professional
  education: 'professional',
  school: 'professional',
  classroom: 'professional',
  learning: 'professional',
  work: 'professional',
  office: 'professional',

  // Wellness
  health: 'wellness',
  doctor: 'wellness',
  hospital: 'wellness',
  medicine: 'wellness',
  body: 'wellness',
  emotions: 'wellness',
  feelings: 'wellness',
  mood: 'wellness',
  sentiment: 'wellness',

  // Individual Number Words - English to Italian categories
  zero: 'zero',
  one: 'uno',
  two: 'due',
  three: 'tre',
  four: 'quattro',
  five: 'cinque',
  six: 'sei',
  seven: 'sette',
  eight: 'otto',
  nine: 'nove',
  ten: 'dieci',

  // Digit Aliases - Maps digit strings to Italian number categories
  '0': 'zero',
  '1': 'uno',
  '2': 'due',
  '3': 'tre',
  '4': 'quattro',
  '5': 'cinque',
  '6': 'sei',
  '7': 'sette',
  '8': 'otto',
  '9': 'nove',
  '10': 'dieci',
};

/**
 * Selects a random image for a given module title based on keywords.
 * Checks topic aliases first, then direct category matches.
 * @param {string} moduleTitle - The title of the module.
 * @returns {string} A URL to a randomly selected image.
 */
export const getModuleImage = (moduleTitle) => {
  const title = moduleTitle.toLowerCase();

  // First, check if any alias keyword matches (e.g., "restaurant" -> "food")
  let primaryCategory = null;
  const aliasMatch = Object.keys(topicAliases).find(alias => title.includes(alias));
  if (aliasMatch) {
    primaryCategory = topicAliases[aliasMatch];
  }

  // If no alias matched, try direct category match
  if (!primaryCategory) {
    primaryCategory = Object.keys(topicImagePool).find(
      keyword => keyword !== 'default' && title.includes(keyword)
    );
  }

  const pool = topicImagePool[primaryCategory] || topicImagePool.default;

  return pool[Math.floor(Math.random() * pool.length)];
};

// Exercise images - consolidated categories for grammar and vocabulary
// Covers all language learning exercise types at A1 level
const exerciseImagePool = {
  // Grammar (verbs, nouns, adjectives, pronouns, parts of speech)
  grammar: [
    '/images/exercises/grammar-1.jpg',
    '/images/exercises/grammar-2.jpg',
    '/images/exercises/grammar-3.jpg',
  ],

  // Vocabulary (animals, food, colors, numbers, clothing, objects, body parts, sports)
  vocabulary: [
    '/images/exercises/vocabulary-1.jpg',
    '/images/exercises/vocabulary-2.jpg',
    '/images/exercises/vocabulary-3.jpg',
    '/images/exercises/vocabulary-4.jpg',
  ],

  // Actions (all physical actions and verbs: running, walking, eating, playing, etc.)
  actions: [
    '/images/exercises/actions-1.jpg',
    '/images/exercises/actions-2.jpg',
    '/images/exercises/actions-3.jpg',
  ],

  // Scenarios (shopping, home, school, travel, work, restaurants)
  scenarios: [
    '/images/exercises/scenarios-1.jpg',
    '/images/exercises/scenarios-2.jpg',
    '/images/exercises/scenarios-3.jpg',
    '/images/exercises/scenarios-4.jpg',
  ],

  // Emotions & States (feelings, moods, emotional expressions)
  emotions: [
    '/images/exercises/emotions-1.jpg',
    '/images/exercises/emotions-2.jpg',
  ],

  // Individual Numbers (0-10) - For number recognition exercises
  // Reuses topic images per consolidation strategy (no duplication)
  zero: [
    '/images/topics/zero-1.jpg',
    '/images/topics/zero-2.jpg',
  ],

  uno: [
    '/images/topics/one-1.jpg',
    '/images/topics/one-2.jpg',
  ],

  due: [
    '/images/topics/two-1.jpg',
    '/images/topics/two-2.jpg',
  ],

  tre: [
    '/images/topics/three-1.jpg',
    '/images/topics/three-2.jpg',
  ],

  quattro: [
    '/images/topics/four-1.jpg',
    '/images/topics/four-2.jpg',
  ],

  cinque: [
    '/images/topics/five-1.jpg',
    '/images/topics/five-2.jpg',
  ],

  sei: [
    '/images/topics/six-1.jpg',
    '/images/topics/six-2.jpg',
  ],

  sette: [
    '/images/topics/seven-1.jpg',
    '/images/topics/seven-2.jpg',
  ],

  otto: [
    '/images/topics/eight-1.jpg',
    '/images/topics/eight-2.jpg',
  ],

  nove: [
    '/images/topics/nine-1.jpg',
    '/images/topics/nine-2.jpg',
  ],

  dieci: [
    '/images/topics/ten-1.jpg',
    '/images/topics/ten-2.jpg',
  ],

  // Default fallback
  default: [
    '/images/exercises/default-1.jpg',
    '/images/exercises/default-2.jpg',
  ],
};

// Map related keywords to primary exercise categories
// All 40+ lesson keywords map efficiently to 5 consolidated categories
const exerciseAliases = {
  // Grammar (parts of speech)
  verb: 'grammar',
  noun: 'grammar',
  adjective: 'grammar',
  pronoun: 'grammar',
  syntax: 'grammar',
  conjugate: 'grammar',
  tense: 'grammar',

  // Vocabulary
  animals: 'vocabulary',
  animal: 'vocabulary',
  food: 'vocabulary',
  colors: 'vocabulary',
  color: 'vocabulary',
  numbers: 'vocabulary',
  number: 'vocabulary',
  clothing: 'vocabulary',
  clothes: 'vocabulary',
  outfit: 'vocabulary',
  dress: 'vocabulary',
  objects: 'vocabulary',
  body: 'vocabulary',
  sports: 'vocabulary',
  furniture: 'vocabulary',

  // Actions (physical actions & verbs)
  running: 'actions',
  walking: 'actions',
  eating: 'actions',
  playing: 'actions',
  reading: 'actions',
  writing: 'actions',
  talking: 'actions',
  listening: 'actions',
  jumping: 'actions',
  dancing: 'actions',
  cooking: 'actions',

  // Scenarios (situational contexts)
  shopping: 'scenarios',
  restaurant: 'scenarios',
  home: 'scenarios',
  house: 'scenarios',
  room: 'scenarios',
  apartment: 'scenarios',
  school: 'scenarios',
  classroom: 'scenarios',
  travel: 'scenarios',
  work: 'scenarios',
  office: 'scenarios',

  // Emotions & States
  emotion: 'emotions',
  feeling: 'emotions',
  happy: 'emotions',
  sad: 'emotions',
  angry: 'emotions',
  mood: 'emotions',
  sentiment: 'emotions',

  // Individual Number Words - English to Italian categories
  zero: 'zero',
  one: 'uno',
  two: 'due',
  three: 'tre',
  four: 'quattro',
  five: 'cinque',
  six: 'sei',
  seven: 'sette',
  eight: 'otto',
  nine: 'nove',
  ten: 'dieci',

  // Digit Aliases - Maps digit strings to Italian number categories
  '0': 'zero',
  '1': 'uno',
  '2': 'due',
  '3': 'tre',
  '4': 'quattro',
  '5': 'cinque',
  '6': 'sei',
  '7': 'sette',
  '8': 'otto',
  '9': 'nove',
  '10': 'dieci',
};

/**
 * Selects a random image for a given set of exercise-related keywords.
 * Checks exercise aliases first, then direct category matches.
 * @param {string | string[]} keywords - A single keyword or an array of keywords to match.
 * @returns {string} A URL to a randomly selected image.
 */
export const getExerciseImage = (keywords) => {
  if (!keywords) {
    const pool = exerciseImagePool.default;
    return pool[Math.floor(Math.random() * pool.length)];
  }

  const searchKeywords = Array.isArray(keywords) ? keywords.map(k => k.toLowerCase()) : [keywords.toLowerCase()];

  // First, check if any alias keyword matches (e.g., "running" -> "actions")
  let primaryCategory = null;
  const aliasMatch = searchKeywords.find(keyword => exerciseAliases[keyword]);
  if (aliasMatch) {
    primaryCategory = exerciseAliases[aliasMatch];
  }

  // If no alias matched, try direct category match
  if (!primaryCategory) {
    primaryCategory = Object.keys(exerciseImagePool).find(poolKeyword =>
      poolKeyword !== 'default' && searchKeywords.includes(poolKeyword)
    );
  }

  const pool = exerciseImagePool[primaryCategory] || exerciseImagePool.default;

  return pool[Math.floor(Math.random() * pool.length)];
};

/**
 * Gets a module icon image based on the module title/category.
 * Returns the first image from the matching category pool.
 * @param {string} moduleTitle - The title of the module.
 * @returns {string} A URL to the module icon image.
 */
export const getModuleIcon = (moduleTitle) => {
  const title = moduleTitle.toLowerCase();

  // First, check if any alias keyword matches
  let primaryCategory = null;
  const aliasMatch = Object.keys(topicAliases).find(alias => title.includes(alias));
  if (aliasMatch) {
    primaryCategory = topicAliases[aliasMatch];
  }

  // If no alias matched, try direct category match
  if (!primaryCategory) {
    primaryCategory = Object.keys(topicImagePool).find(
      keyword => keyword !== 'default' && title.includes(keyword)
    );
  }

  const pool = topicImagePool[primaryCategory] || topicImagePool.default;
  // Return the first image in the pool for consistency
  return pool[0];
};

/**
 * Gets next unused module image from category pool.
 * Cycles through pool to avoid repetition within a lesson.
 * @param {string} moduleTitle - The title of the module
 * @param {Set} usedImages - Set of already-used image URLs
 * @returns {string} URL to next unused image from pool
 */
export const getNextModuleImage = (moduleTitle, usedImages = new Set(), shuffledPools = {}) => {
  const title = moduleTitle.toLowerCase();

  // Determine category using same logic as getModuleIcon
  let primaryCategory = null;
  const aliasMatch = Object.keys(topicAliases).find(alias => title.includes(alias));
  if (aliasMatch) {
    primaryCategory = topicAliases[aliasMatch];
  }

  if (!primaryCategory) {
    primaryCategory = Object.keys(topicImagePool).find(
      keyword => keyword !== 'default' && title.includes(keyword)
    );
  }

  // Get or create shuffled pool for this category
  if (!shuffledPools[primaryCategory]) {
    const originalPool = topicImagePool[primaryCategory] || topicImagePool.default;
    shuffledPools[primaryCategory] = shuffleArray(originalPool);
  }

  const pool = shuffledPools[primaryCategory];

  // Find first unused image in shuffled pool
  const unusedImage = pool.find(img => !usedImages.has(img));

  // If all images used, reset and use first image (edge case)
  return unusedImage || pool[0];
};