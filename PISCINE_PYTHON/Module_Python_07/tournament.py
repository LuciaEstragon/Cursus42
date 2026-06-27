#!/usr/bin/env python3
from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError, BattleStrategy
)


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    n = len(opponents)
    print(f"** Tournament ** {n} opponents involved")
    for i in range(n):
        for j in range(i + 1, n):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(f"* Battle * {creature1.describe()} "
                  f"vs. {creature2.describe()} now fight!")
            try:
                if not strategy1.is_valid(creature1):
                    raise InvalidStrategyError(
                        f"Invalid Creature '{creature1.name}' "
                        f"for this {type(strategy1).__name__}"
                    )
                if not strategy2.is_valid(creature2):
                    raise InvalidStrategyError(
                        f"Invalid Creature '{creature2.name}' "
                        f"for this {type(strategy2).__name__}"
                    )
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic) [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error) "
          "[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple) [ (Aquabub+Normal), "
          "(Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
