#!/usr/bin/env python3
"""
Exercise 3: Ancient Library
Use functools and operator modules.
"""

import functools
import operator
from collections.abc import Callable
from typing import Any, cast


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using functools.reduce and operator functions."""
    if not spells:
        return 0

    op_map = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }

    if operation not in op_map:
        raise ValueError(f"Unknown operation: {operation}")

    func = cast(Callable[[int, int], int], op_map[operation])
    return functools.reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications for three elements."""
    from functools import partial
    return {
        'fire': partial(base_enchantment, 50, 'fire'),
        'ice': partial(base_enchantment, 50, 'ice'),
        'lightning': partial(base_enchantment, 50, 'lightning'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return nth Fibonacci number with memoization."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@functools.singledispatch
def spell_dispatcher(arg: Any) -> str:
    """Base dispatcher for unknown types."""
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _(arg: int) -> str:
    return f"Damage spell: {arg} damage"


@spell_dispatcher.register(str)
def _(arg: str) -> str:
    return f"Enchantment: {arg}"


@spell_dispatcher.register(list)
def _(arg: list) -> str:
    return f"Multi-cast: {len(arg)} spells"


if __name__ == "__main__":
    # Test spell_reducer
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    # Test partial_enchanter
    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element} enchantment with {power} power on {target}"

    partials = partial_enchanter(enchant)
    print(partials['fire']("Sword"))
    print(partials['ice']("Shield"))
    print(partials['lightning']("Staff"))

    # Test memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    # Test spell_dispatcher
    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher([1, 2, 3]))
    print(spell_dispatcher(3.14))
