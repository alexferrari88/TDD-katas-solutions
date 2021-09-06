import re
from typing import List


class Error(Exception):
    pass


class StringCalculator:
    def add(self, numbers: str) -> int:
        numbers_array = []
        if not numbers:
            return 0
        separators = ["\n", ","]

        custom_separator = re.findall(r"^//(.+)\n", numbers)
        if custom_separator and (
            multiple_custom_separators := re.findall(r"(?<=\[).+?(?=\])", numbers)
        ):
            separators = multiple_custom_separators
            numbers = numbers[numbers.index("\n") + 1 :]
        elif custom_separator:
            separators = custom_separator
            numbers = numbers[numbers.index("\n") + 1 :]

        if len(separators) > 1:
            separator_pattern = self._make_separators_pattern(separators)
            numbers_array = re.split(separator_pattern, numbers)
        else:
            numbers_array = numbers.split(*separators)

        negative_numbers = list(filter(lambda x: int(x) < 0, numbers_array))
        if negative_numbers:
            negative_numbers_string = ",".join(negative_numbers)
            raise Error(f"negatives not allowed: {negative_numbers_string}")
        return sum(int(n) for n in numbers_array if int(n) <= 1000)

    def _split_numbers(self, numbers: str, separators: List[str]) -> List[str]:
        if not separators:
            return numbers
        sep = separators.pop()
        for num in numbers:
            num = num.split(sep)
        return self._split_numbers(numbers, separators)

    def _make_separators_pattern(self, separators: List[str]) -> str:
        return f"[{'|'.join(separators)}]"
