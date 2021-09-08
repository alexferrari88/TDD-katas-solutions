from abc import ABC, abstractmethod


class IOutput(ABC):
    @abstractmethod
    def write(self, content: str) -> None:
        """Writes content to output"""

    @abstractmethod
    def read(self) -> str:
        """Reads from input"""