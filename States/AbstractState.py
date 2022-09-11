from abc import ABC, abstractmethod


class AbstractState(ABC):
    @abstractmethod
    def action() -> None:
        pass
