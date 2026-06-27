# Importación a nivel superior - causa dependencia circular
from .dark_spellbook import dark_spell_allowed_ingredients  # noqa


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ing_lower = ingredients.lower()
    valid = any(allowed_ing in ing_lower for allowed_ing in allowed)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
