# Solution for the TDD-Kata https://osherove.com/tdd-kata-1

import re
from typing import List
from .Logger import Logger
from .Webservice import Webservice


class Error(Exception):
    pass


class StringCalculator:
    def __init__(self, logger: Logger, web_service: Webservice) -> None:
        self.logger = logger
        self.web_service = web_service

    def add(self, numbers: str) -> None:
        """Given a string of separated numbers, returns its sum.
        The numbers can be separated by comma, new-line, or custom(s) delimiters.
        When using custom delimiter(s), pass them at the beginning of the numbers parameters.
        Custom delimiter(s) format:
        //[delimiter]\n

        e.g. if you want to use $$$ as delimiter, then pass this parameter:
        //[$$$]\n1$$$2$$$3      # will return 6

        You can use multiple custom delimiters and these can be of any length.
        e.g. //[***][%%%]\n1***2%%%3    # will return 6
        """

        numbers_array = []
        if not numbers:
            self.log(0)
            print(0)
            return 0

        # default separators
        separators = ["\n", ","]

        # check if custom separator(s) are provided
        custom_separator = re.findall(r"^//(.+)\n", numbers)

        if custom_separator and (
            multiple_custom_separators := re.findall(r"(?<=\[).+?(?=\])", numbers)
        ):
            separators = multiple_custom_separators
            numbers = numbers[numbers.index("\n") + 1 :]
        elif custom_separator:
            # it is possible to pass a single custom separator without brackets
            # (see specs for the Kata)
            separators = custom_separator
            numbers = numbers[numbers.index("\n") + 1 :]

        separator_pattern = self._make_separators_pattern(separators)
        numbers_array = re.split(separator_pattern, numbers)

        negative_numbers = list(filter(lambda x: int(x) < 0, numbers_array))
        if negative_numbers:
            negative_numbers_string = ",".join(negative_numbers)
            raise Error(f"negatives not allowed: {negative_numbers_string}")

        sum_to_return = sum(int(n) for n in numbers_array if int(n) <= 1000)
        self.log(sum_to_return)
        print(sum_to_return)

        return sum_to_return

    def log(self, content: str):
        try:
            self.logger.write(content)
        except Exception as err:
            self.web_service.notify(f"Logging has failed with error: {err}")

    def _make_separators_pattern(self, separators: List[str]) -> str:
        """Private method that creates a regex pattern for separators"""
        regex_ready_separators = [f"(?:{re.escape(sep)})" for sep in separators]
        return "|".join(regex_ready_separators)
