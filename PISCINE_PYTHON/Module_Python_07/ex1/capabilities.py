from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


# Clases abstractas para herencia múltiple (runtime)
class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: None = None) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


# Protocolos runtime_checkable para usar con isinstance
@runtime_checkable
class HealCapable(Protocol):
    def heal(self, target: None = None) -> str: ...


@runtime_checkable
class TransformCapable(Protocol):
    def transform(self) -> str: ...
    def revert(self) -> str: ...
