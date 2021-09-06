import pytest
from .PasswordVerification import PasswordVerification


class TestPasswordVerification:
    password_verification = PasswordVerification()

    def test_should_be_larger_than_8_chars(self):
        with pytest.raises(Exception):
            self.password_verification.verify("abc")

    def test_should_not_be_null(self):
        with pytest.raises(Exception):
            self.password_verification.verify("")

    def test_should_have_at_least_1_uppercase_char(self):
        with pytest.raises(Exception):
            self.password_verification.verify("abcdefghi")

    def test_should_have_at_least_1_lowercase_char(self):
        with pytest.raises(Exception):
            self.password_verification.verify("ABCDEFGHI")

    def test_should_have_at_least_1_number(self):
        with pytest.raises(Exception):
            self.password_verification.verify("aBcde")

    def test_should_be_ok(self):
        assert self.password_verification.verify("1aBcdeFgHI")
        assert self.password_verification.verify("ABcDefGhI")
        assert self.password_verification.verify("ABc2De")
        assert self.password_verification.verify("a2bcd3fgh1")

    def test_should_not_pass_without_1_lowercase_char_even_with_3_rules_ok(self):
        with pytest.raises(Exception):
            self.password_verification.verify("ABCD3FGH1")