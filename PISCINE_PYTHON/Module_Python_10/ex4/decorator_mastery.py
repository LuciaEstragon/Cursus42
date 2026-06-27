#!/usr/bin/env python3
"""
Exercise 4: Master's Tower
Decorators and class methods.
"""

import functools
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """Decorator that times function execution."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates power parameter."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 0 and hasattr(args[0], '__class__'):
                # Es un método de instancia: self, spell_name, power
                if len(args) >= 3:
                    power = args[2]
                else:
                    power = kwargs.get('power', 0)
            else:
                # Es una función normal: power, *args
                if len(args) >= 1:
                    power = args[0]
                else:
                    power = kwargs.get('power', 0)

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a function on exception."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
                    if attempt == max_attempts:
                        return ("Spell casting failed after "
                                f"{max_attempts} attempts")
            return None
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if name is >= 3 chars and contains only letters/spaces."""
        if len(name) < 3:
            return False
        return all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with power validation."""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    # Test spell_timer
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    # Test retry_spell
    print("\nTesting retrying spell...")

    def create_unreliable_spell():
        attempts = 0  # Variable en el closure

        @retry_spell(3)
        def unreliable_spell() -> str:
            nonlocal attempts
            attempts += 1
            if attempts < 3:
                raise RuntimeError("spell failed")
            return "Waaaaaaagh spelled !"

        return unreliable_spell

    unreliable_spell = create_unreliable_spell()
    print(unreliable_spell())

    # Test MageGuild
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))   # True
    print(MageGuild.validate_mage_name("A"))        # False
    print(guild.cast_spell("Lightning", 15))        # valid
    print(guild.cast_spell("Lightning", 5))         # insufficient
