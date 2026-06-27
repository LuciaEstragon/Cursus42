from ex0 import Creature, CreatureFactory
from .capabilities import HealCapability, TransformCapability


# Criaturas con curación
class Sprouting(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sprouting", "Grass")

    def attack(self) -> str:
        return "Sprouting uses Vine Whip!"

    def heal(self, target: None = None) -> str:
        return "Sprouting heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: None = None) -> str:
        return "Bloomelle heals itself and others for a large amount"


# Criaturas con transformación
class Shifting(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shifting", "Normal")
        self._transformed = False

    def attack(self) -> str:
        return ("Shifting performs a boosted strike!"
                if self._transformed else "Shifting attacks normally."
                )

    def transform(self) -> str:
        self._transformed = True
        return "Shifting shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shifting returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        return ("Morphagon unleashes a devastating morph strike!"
                if self._transformed else "Morphagon attacks normally."
                )

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."


# Fábricas
class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sprouting()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shifting()

    def create_evolved(self) -> Creature:
        return Morphagon()
