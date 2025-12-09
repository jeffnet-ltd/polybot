"""
Caching and Template System for Practice Mode
Pre-computes and caches common prompts, responses, and templates for faster performance
"""

from typing import Dict, Optional, Tuple
from functools import lru_cache
from scenario_templates import ScenarioTemplate, build_stage_manager_prompt, get_scenario_template

# Cache for system prompts (key: (scenario_id, target_lang, native_lang))
_system_prompt_cache: Dict[Tuple[str, str, str], str] = {}

# Cache for scenario-specific vocabulary prompts
_vocabulary_prompt_cache: Dict[str, str] = {}

# Response templates for common interactions
RESPONSE_TEMPLATES = {
    "coffee_order": {
        "greetings": {
            "it": [
                "Buongiorno! Cosa desidera?",
                "Buongiorno! Come posso aiutarla?",
                "Ciao! Cosa prendi?",
                "Buongiorno! Prego, dimmi pure."
            ],
            "en": [
                "Good morning! What would you like?",
                "Good morning! How can I help you?",
                "Hello! What can I get you?",
                "Good morning! Please, tell me."
            ]
        },
        "confirmations": {
            "it": [
                "Perfetto!",
                "Va bene!",
                "Ottimo!",
                "Certamente!"
            ],
            "en": [
                "Perfect!",
                "Very well!",
                "Excellent!",
                "Certainly!"
            ]
        },
        "asking_seating": {
            "it": [
                "Al banco o al tavolo?",
                "Preferisce al banco o al tavolo?",
                "Vuole stare al banco o al tavolo?"
            ],
            "en": [
                "At the bar or at a table?",
                "Do you prefer at the bar or at a table?",
                "Would you like to sit at the bar or at a table?"
            ]
        },
        "stating_price": {
            "it": [
                "Sono {price} euro in totale.",
                "In totale fa {price} euro.",
                "Totale: {price} euro."
            ],
            "en": [
                "That's {price} euros total.",
                "The total is {price} euros.",
                "Total: {price} euros."
            ]
        }
    }
}


@lru_cache(maxsize=128)
def get_cached_system_prompt(scenario_id: str, target_lang: str, native_lang: str) -> str:
    """
    Get or build and cache system prompt for a scenario
    Uses LRU cache for fast lookups
    """
    cache_key = (scenario_id, target_lang, native_lang)
    
    if cache_key not in _system_prompt_cache:
        scenario = get_scenario_template(scenario_id)
        if scenario:
            _system_prompt_cache[cache_key] = build_stage_manager_prompt(scenario, target_lang, native_lang)
        else:
            return ""
    
    return _system_prompt_cache.get(cache_key, "")


def get_cached_vocabulary_prompt(scenario_id: str) -> str:
    """
    Get cached vocabulary primer prompt for a scenario
    """
    if scenario_id not in _vocabulary_prompt_cache:
        scenario = get_scenario_template(scenario_id)
        if scenario and scenario.vocabulary_primer:
            vocab_text = ", ".join(scenario.vocabulary_primer)
            _vocabulary_prompt_cache[scenario_id] = f"Key vocabulary for this scenario: {vocab_text}"
        else:
            _vocabulary_prompt_cache[scenario_id] = ""
    
    return _vocabulary_prompt_cache.get(scenario_id, "")


def get_template_response(scenario_id: str, response_type: str, target_lang: str, **kwargs) -> Optional[str]:
    """
    Get a template-based response for common interactions
    Returns None if no template matches, allowing LLM generation
    """
    if scenario_id not in RESPONSE_TEMPLATES:
        return None
    
    templates = RESPONSE_TEMPLATES[scenario_id]
    if response_type not in templates:
        return None
    
    lang_templates = templates[response_type].get(target_lang)
    if not lang_templates:
        return None
    
    # For now, return first template (could add logic to select based on context)
    template = lang_templates[0]
    
    # Format template with kwargs if needed
    try:
        return template.format(**kwargs)
    except KeyError:
        return template


def clear_cache():
    """Clear all caches (useful for testing or memory management)"""
    global _system_prompt_cache, _vocabulary_prompt_cache
    _system_prompt_cache.clear()
    _vocabulary_prompt_cache.clear()
    get_cached_system_prompt.cache_clear()

