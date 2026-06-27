# Para evitar circularidad, importamos el validador DENTRO de la función,
# no al inicio del módulo.
def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Importación tardía para romper la dependencia circular
    from .light_validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
