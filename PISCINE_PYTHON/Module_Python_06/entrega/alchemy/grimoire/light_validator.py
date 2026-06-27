def validate_ingredients(ingredients: str) -> str:
    # Importación diferida para evitar circular
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    valid = any(allowed_ing in ing_lower for allowed_ing in allowed)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
