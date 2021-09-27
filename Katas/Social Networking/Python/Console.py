from IOOutput import IOOutput


class Console(IOOutput):
    def write(self, content: str) -> None:
        print(content)

    def read(self) -> str:
        return input()