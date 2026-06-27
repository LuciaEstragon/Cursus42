# Dependencia circular - dark_validator también importa de aquí
# Importación a nivel superior - causa dependencia circular
from .dark_validator import validate_ingredients  # noqa


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    return f"Dark spell recorded: {spell_name} ({result})"
