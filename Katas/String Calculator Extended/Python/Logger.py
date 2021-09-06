from abc import ABC, abstractmethod


class ILogger(ABC):
    """ILogger provides an interface for a logger"""

    @abstractmethod
    def write(self, content: int) -> None:
        """Write writes the content passed as parameter"""


class Logger(ILogger):
    def write(self, content: int) -> None:
        print(content)