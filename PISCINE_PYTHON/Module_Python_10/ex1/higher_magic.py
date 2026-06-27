#!/usr/bin/env python3
"""
Exercise 1: Higher Realm
Higher-order functions that operate on other functions.
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new function that calls both spells and returns a tuple."""
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a function that multiplies power before casting."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a function that casts spell only if condition is True."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    # Sample spells
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}, damage {power}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target}"

    # Test spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    # Test power_amplifier
    print("\nTesting power amplifier...")
    original = fireball("Goblin", 10)
    amp = power_amplifier(fireball, 3)
    amplified = amp("Goblin", 10)
    print(f"Original: {original}")
    print(f"Amplified: {amplified}")

    # Test conditional_caster
    print("\nTesting conditional caster...")
    cond = conditional_caster(lambda t, p: p > 20, fireball)
    print(cond("Orc", 15))   # should fizzle
    print(cond("Orc", 25))   # should cast

    # Test spell_sequence
    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal, lightning])
    results = seq("Target", 5)
    for r in results:
        print(r)
