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

        separator_pattern = self._make_separators_pattern(separators)
        numbers_array = re.split(separator_pattern, numbers)

        negative_numbers = list(filter(lambda x: int(x) < 0, numbers_array))
        if negative_numbers:
            negative_numbers_string = ",".join(negative_numbers)
            raise Error(f"negatives not allowed: {negative_numbers_string}")
        return sum(int(n) for n in numbers_array if int(n) <= 1000)

    def _make_separators_pattern(self, separators: List[str]) -> str:
        regex_ready_separators = [f"(?:{re.escape(sep)})" for sep in separators]
        return "|".join(regex_ready_separators)
