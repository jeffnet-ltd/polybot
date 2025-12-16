# Image Selection Guide

A comprehensive guide for working with images in the PolyBot curriculum. This document covers available image categories, how the image system works, and how to select specific images for exercises during testing.

## Available Images by Category

### Social & Communication (10 images)
- **Directory:** `/images/topics/greetings-*.jpg`
- **Files:** greetings-1 through greetings-10
- **Used for:** Greetings, introductions, conversations, social interactions
- **Modules:** A1.1, A1.2

### Food & Dining (4 images)
- **Directory:** `/images/topics/food-*.jpg`
- **Files:** food-1 through food-4
- **Used for:** Food, restaurants, cooking, meals, dining
- **Modules:** A1.4

### Travel & Transportation (3 images)
- **Directory:** `/images/topics/travel-*.jpg`
- **Files:** travel-1 through travel-3
- **Used for:** Travel, transportation, trains, airports, hotels
- **Modules:** A1.9

### People & Professions (3 images)
- **Directory:** `/images/topics/people-*.jpg`
- **Files:** people-1 through people-3
- **Used for:** Family, people, occupations, professions
- **Modules:** A1.2, A1.3, A1.8

### Temporal & Time (4 images)
- **Directory:** `/images/topics/temporal-*.jpg`
- **Files:** temporal-1 through temporal-4
- **Used for:** Time, hours, schedules, daily routines
- **Modules:** A1.7

### Appearance & Descriptors (10 images)
- **Directory:** `/images/topics/appearance-*.jpg`
- **Files:** appearance-1 through appearance-10
- **Used for:** Appearance, adjectives, descriptions, colors, sizes
- **Modules:** A1.5, A1.8

### Nature & Seasons (3 images)
- **Directory:** `/images/topics/nature-*.jpg`
- **Files:** nature-1 through nature-3
- **Used for:** Nature, weather, seasons, outdoor activities
- **Modules:** A1.6

### Lifestyle & Living (3 images)
- **Directory:** `/images/topics/lifestyle-*.jpg`
- **Files:** lifestyle-1 through lifestyle-3
- **Used for:** Home, housing, lifestyle, daily life
- **Modules:** A1.3

### Commerce & Shopping (10 images)
- **Directory:** `/images/topics/commerce-*.jpg`
- **Files:** commerce-1 through commerce-10
- **Used for:** Shopping, prices, commerce, transactions
- **Modules:** A1.5

### Activities & Recreation (4 images)
- **Directory:** `/images/topics/activities-*.jpg`
- **Files:** activities-1 through activities-4
- **Used for:** Activities, hobbies, entertainment, recreation
- **Modules:** A1.7, A1.9

### Professional & Business (2 images)
- **Directory:** `/images/topics/professional-*.jpg`
- **Files:** professional-1 through professional-2
- **Used for:** Professional settings, business, work-related topics
- **Modules:** Various

### Wellness & Health (3 images)
- **Directory:** `/images/topics/wellness-*.jpg`
- **Files:** wellness-1 through wellness-3
- **Used for:** Health, medical, wellness, body, illness
- **Modules:** A1.10

### Default Fallback (3 images)
- **Directory:** `/images/topics/default-*.jpg`
- **Files:** default-1 through default-3
- **Used for:** General/category mismatch fallback
- **Modules:** All

### Number-Specific Images (2 images each)

Numbers have special handling with dedicated image pools:

- **zero:** zero-1.jpg, zero-2.jpg
- **one/uno:** one-1.jpg, one-2.jpg
- **two/due:** two-1.jpg, two-2.jpg
- **three/tre:** three-1.jpg, three-2.jpg
- **four/quattro:** four-1.jpg, four-2.jpg
- **five/cinque:** five-1.jpg, five-2.jpg
- **six/sei:** six-1.jpg, six-2.jpg
- **seven/sette:** seven-1.jpg, seven-2.jpg
- **eight/otto:** eight-1.jpg, eight-2.jpg
- **nine/nove:** nine-1.jpg, nine-2.jpg
- **ten/dieci:** ten-1.jpg, ten-2.jpg

**Path format:** `/images/topics/[number]-[1-2].jpg`

## How the Image System Works

### Automatic Image Selection (Default Behavior)

1. **Category Detection:**
   - System analyzes the module title or vocabulary word
   - Maps keywords to primary categories (e.g., "restaurant" → "food")
   - If no match found, uses "default" pool

2. **Image Pool Shuffling:**
   - Each lesson start triggers a shuffle of the image pool for each category
   - Shuffle uses Fisher-Yates algorithm for randomness
   - Different random order every time a lesson is started

3. **Sequential Selection (from shuffled pool):**
   - System finds first unused image from the shuffled pool
   - Tracks used images within current lesson to avoid repetition
   - When all images are used, cycles back to first image

4. **Result:**
   - Every lesson gets different image order
   - No image repeats within same lesson
   - Fresh visual experience on lesson restart

### Manual Image Selection (For Specific Cards)

During testing, you can specify exactly which image to use for a specific exercise:

```python
{
    "type": "info_card",
    "step": 1,
    "prompt": "New Word",
    "correct_answer": "casa",
    "explanation": "house",
    "sub_text": "Listen and repeat.",
    "image_url": "/images/topics/lifestyle-1.jpg"  # MANUAL SELECTION
}
```

**Key points:**
- `image_url` field is optional
- Takes highest priority (overrides automatic selection)
- Use when testing requires a specific image
- Path must be exact: `/images/topics/category-number.jpg`

## How to Use Manual Image Selection

### Step 1: Identify the Image

Decide which image is appropriate for your card. Browse available images in:
```
d:\PolyBot\polybot\frontend\public\images\topics\
```

Example: `lifestyle-2.jpg`

### Step 2: Add image_url Field

Add the `image_url` field to your exercise definition:

```python
{
    "type": "info_card",
    "step": 1,
    "prompt": "New Word",
    "correct_answer": "cucina",
    "explanation": "kitchen",
    "sub_text": "Listen and repeat.",
    "audio_url": "/static/audio/it_cucina_123.mp3",
    "image_url": "/images/topics/lifestyle-2.jpg"  # NEW FIELD
}
```

### Step 3: Test the Card

Navigate to the lesson and verify the specific image appears.

### Step 4: Remove or Modify (Optional)

- **To return to automatic selection:** Delete the `image_url` line
- **To change the image:** Update the path in `image_url`

## Path Format

All image paths follow this exact format:

```
/images/topics/[category]-[number].jpg
```

Where:
- `[category]` = category name (e.g., `food`, `people`, `lifestyle`)
- `[number]` = sequential number (usually 1-10, sometimes 1-2 for numbers)

**Examples:**
- ✅ `/images/topics/food-3.jpg`
- ✅ `/images/topics/appearance-7.jpg`
- ✅ `/images/topics/zero-1.jpg` (number image)
- ❌ `/images/topics/food3.jpg` (missing hyphen)
- ❌ `/images/topics/Food-3.jpg` (uppercase category)
- ❌ `/images/topics/food-3` (missing .jpg extension)

## Best Practices

### 1. **Use Automatic Selection for Production**
- Provides variety and freshness
- No manual maintenance required
- Users get shuffled experience

### 2. **Use Manual Selection for Testing**
- Specific cards that require particular images
- Ensuring right content-image pairing
- Debugging image display issues

### 3. **Match Image to Content**
When selecting manual images, ensure the image content matches the exercise:
- **Food exercises** → use `food-*.jpg`
- **Family exercises** → use `people-*.jpg`
- **Numbers** → use specific number images (e.g., `five-1.jpg` for "cinque")

### 4. **Preview Before Committing**
- Test the card with your chosen image
- Verify image displays correctly (no cropping)
- Check that content and image are appropriate match

### 5. **Document Manual Selections**
- Add inline comment if selecting unusual image
- Helps future maintainers understand the choice

```python
{
    "type": "info_card",
    "step": 5,
    "prompt": "New Word",
    "correct_answer": "ristorante",
    "explanation": "restaurant",
    # Specific image chosen because it shows traditional Italian trattoria
    "image_url": "/images/topics/food-2.jpg"
}
```

## Image Sizing & Display

### Sizing Rules
- **Height:** Fixed at 256px (h-64)
- **Width:** 100% of container (responsive)
- **Aspect ratio:** Maintained (no distortion)
- **Background:** Light gray (bg-gray-50) for letterboxing

### Why object-contain?
The system uses `object-contain` to ensure:
- ✅ No cropping of important content
- ✅ Complete image visibility
- ✅ Maintained aspect ratio
- ✅ Professional appearance

If an image has empty space, the light gray background fills it.

## Troubleshooting

### Image Not Appearing

1. **Check the file exists:**
   ```
   d:\PolyBot\polybot\frontend\public\images\topics\[filename].jpg
   ```

2. **Verify path format:**
   - Must start with `/images/topics/`
   - Category name must be lowercase
   - Must include .jpg extension
   - Example: `/images/topics/food-3.jpg`

3. **Clear browser cache:**
   - Hard refresh the page (Ctrl+Shift+R)
   - Images are cached by browsers

4. **Check file naming:**
   - Filenames are case-sensitive on some systems
   - Use lowercase for category names

### Same Image Repeating

1. **Within a lesson:** This shouldn't happen (repet prevention is active)
   - Verify lesson was fully reloaded

2. **Across lessons:** This is expected behavior
   - Automatic system cycles through pools

3. **Solution:** Refresh/restart the application

### Image Looks Distorted

1. **Verify `object-contain` is applied:**
   - Image should show completely without cropping
   - Light gray background may appear as letterboxing

2. **Check image dimensions:**
   - Images should be landscape or square
   - Portrait images may appear smaller

3. **Browser compatibility:**
   - Use modern browser (Chrome, Firefox, Safari, Edge)
   - Older IE may have issues

## Technical Details

### Image Pool Categories

The system maps exercise content to image pools via keywords:

```
"restaurant" → "food"
"famiglia", "family" → "people"
"viaggio", "travel" → "travel"
"casa", "home" → "lifestyle"
"numero", "number" → special number pool
```

### Shuffling Behavior

- **Triggered:** When lesson exercises are loaded
- **Method:** Fisher-Yates algorithm (true randomness)
- **Scope:** Per category, per lesson session
- **Result:** Each lesson start = different image order

### Tracking System

- **Scope:** Per lesson session
- **Method:** JavaScript Set tracks used image URLs
- **Resets:** When lesson changes or app reloads
- **Manual images:** Not tracked (always use specified image)

## Examples

### Example 1: Basic Automatic Image Selection

```python
{
    "type": "info_card",
    "step": 1,
    "prompt": "New Word",
    "correct_answer": "cibo",
    "explanation": "food",
    "sub_text": "Listen and repeat.",
    "audio_url": "/static/audio/it_cibo_45.mp3"
    # No image_url = automatic selection from "food" pool
}
```

**Result:** System randomly selects from `food-1.jpg` to `food-4.jpg` (shuffled)

### Example 2: Manual Selection for Specific Image

```python
{
    "type": "info_card",
    "step": 1,
    "prompt": "New Word",
    "correct_answer": "pasta",
    "explanation": "pasta",
    "sub_text": "Listen and repeat.",
    "audio_url": "/static/audio/it_pasta_46.mp3",
    "image_url": "/images/topics/food-1.jpg"  # Always use this specific image
}
```

**Result:** Always displays `food-1.jpg`, never changes

### Example 3: Cultural Note with Manual Image

```python
{
    "type": "info_card",
    "step": 9,
    "prompt": "Cultural Note",
    "correct_answer": "Italian Meal Times",
    "explanation": "Italians eat Pranzo (lunch) at 12:30-2:30 PM...",
    "sub_text": "Understanding meal times helps you adapt to Italian life.",
    "cultural_note": True,
    "image_url": "/images/topics/food-3.jpg"  # Specific food image for cultural context
}
```

**Result:** Yellow cultural note card with specified food image

## Support & Questions

For issues or questions about images:

1. **Check this guide** for common solutions
2. **Verify image files exist** in the public/images/topics/ directory
3. **Review path format** - most issues are path-related
4. **Test with browser dev tools** - check console for errors
5. **Refer to imageUtils.js** for technical implementation details
