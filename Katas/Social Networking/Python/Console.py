from .IOutput import IOutput


class Console(IOutput):
    def write(self, content: str) -> None:
        print(content)

    def read(self) -> str:
        return input()