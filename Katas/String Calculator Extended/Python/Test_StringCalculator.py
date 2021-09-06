import pytest
from .StringCalculator import StringCalculator, Error
from .Logger import Logger


class TestStringCalculator:
    logger = Logger()
    string_calculator = StringCalculator(logger)

    def test_should_return_0_for_empty_string(self):
        assert self.string_calculator.add("") == 0

    def test_should_return_two_numbers_sum(self):
        assert self.string_calculator.add("1,2") == 3

    def test_should_return_multiple_numbers_sum(self):
        assert self.string_calculator.add("1,2,3,4") == 10

    def test_should_return_numbers_sum_when_separated_with_new_lines(self):
        assert self.string_calculator.add("1\n2,3") == 6

    def test_should_return_numbers_sum_with_custom_delimiter(self):
        assert self.string_calculator.add("//;\n1;2") == 3

    def test_should_throw_exception_for_negative_num(self):
        with pytest.raises(Error) as excinfo:
            self.string_calculator.add("-1")
        assert "negatives not allowed: -1" == str(excinfo.value)

    def test_should_throw_exception_for_multiple_negative_num(self):
        with pytest.raises(Error) as excinfo:
            self.string_calculator.add("-1,2,3,-4,5")
        assert "negatives not allowed: -1,-4" == str(excinfo.value)

    def test_should_ignore_numbers_bigger_than_1000(self):
        assert self.string_calculator.add("1001,2") == 2

    def test_should_return_numbers_sum_with_custom_delimiter_of_any_length(self):
        assert self.string_calculator.add("//[***]\n1***2***3") == 6

    def test_should_return_number_sum_with_multiple_custom_delimiters(self):
        assert self.string_calculator.add("//[*][%]\n1*2%3") == 6

    def test_should_return_number_sum_with_multiple_custom_delimiters_longer_than_1_char(
        self,
    ):
        assert self.string_calculator.add("//[***][%%%]\n1***2%%%3") == 6

    def test_should_use_the_logger(self, mocker):
        logger = mocker.Mock()
        string_calculator_logger = StringCalculator(logger)
        _ = string_calculator_logger.add("//[*][%]\n1*2%3")
        logger.write.assert_called()
        logger.write.assert_called_with(6)
