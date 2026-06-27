#!/usr/bin/env python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory
# from ex0.creature import Creature


def test_factory(factory: CreatureFactory, name: str) -> None:
    print(f"Testing factory {name}")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(f"{c1.describe()} vs. {c2.describe()} fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame, "Flameling")
    test_factory(aqua, "Aquabub")
    fight(flame, aqua)


if __name__ == "__main__":
    main()
