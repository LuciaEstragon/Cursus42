#!/usr/bin/env python3
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapable, TransformCapable


def main() -> None:
    # Healing
    healing_factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()

    assert isinstance(base, HealCapable)
    assert isinstance(evolved, HealCapable)

    print(f"base: {base.describe()}")
    print(base.attack())
    print(base.heal())

    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    print(evolved.heal())

    # Transform
    transform_factory = TransformCreatureFactory()
    print("\nTesting Creature with transform capability")
    base = transform_factory.create_base()
    evolved = transform_factory.create_evolved()

    assert isinstance(base, TransformCapable)
    assert isinstance(evolved, TransformCapable)

    print(f"base: {base.describe()}")
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
