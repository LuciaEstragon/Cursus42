#!/usr/bin/env python3
"""
Exercise 2: Memory Depths
Lexical scoping and closures.
"""

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    """Return a counting closure that increments on each call."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a closure that accumulates power."""
    total = initial_power

    def accumulator(add: int) -> int:
        nonlocal total
        total += add
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return a closure that applies the given enchantment to an item."""
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a dict with 'store' and 'recall' closures."""
    storage = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    # Test mage_counter
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    # Test spell_accumulator
    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    # Test enchantment_factory
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    # Test memory_vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret' = {vault['recall']('secret')}")
    print(f"Recall 'unknown' = {vault['recall']('unknown')}")
