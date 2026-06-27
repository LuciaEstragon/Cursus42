from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.capabilities import HealCapable, TransformCapable


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapable)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this aggressive strategy")
        # Ayuda a mypy a saber que tiene transform/revert
        assert isinstance(creature, TransformCapable)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapable)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' "
                                       "for this defensive strategy")
        assert isinstance(creature, HealCapable)
        print(creature.attack())
        print(creature.heal())
