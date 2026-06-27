"""
print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
# La siguiente línea provocará el ImportError
from alchemy.grimoire.dark_spellbook import dark_spell_record
# Si se llegara a importar (no ocurre), llamaríamos a dark_spell_record
"""
# esta funcionando bien como arriba:

print("== Kaboom 1 ==")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
try:
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    _ = dark_spell_record
except ImportError as e:
    print(f"Caught expected ImportError: {e}")
