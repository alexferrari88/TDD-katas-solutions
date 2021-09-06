import re
from typing import Optional, List, Tuple


class PasswordVerification:
    class Rule:
        def __init__(
            self, value: bool, error_msg: str, critical: Optional[bool] = False
        ) -> None:
            self.value = value
            self.error_msg = error_msg
            self.critical = critical

    def _has_critical_rule(self, rules: List[Rule]) -> Tuple[bool, str]:
        for rule in rules:
            if not rule.value and rule.critical:
                return True, rule.error_msg
        return False, None

    def verify(self, pwd: str) -> bool:
        MIN_RULES_TO_PASS = 3
        rules = [
            self.Rule(len(pwd) >= 8, "password should be longer than 8 characters"),
            self.Rule(
                bool(re.search(r"[A-Z]", pwd)),
                "password should have one uppercase letter at least",
            ),
            self.Rule(
                bool(re.search(r"[a-z]", pwd)),
                "password should have one lowercase letter at least",
                True,
            ),
            self.Rule(
                bool(re.search(r"\d", pwd)), "password should have one number at least"
            ),
        ]

        if not pwd:
            raise Exception("Error: password should not be null")

        _, error = self._has_critical_rule(rules)
        if error:
            raise Exception(error)

        # from https://stackoverflow.com/questions/62840144/if-statement-where-if-3-of-5-conditions-are-true-in-python
        rules_count = sum(rule.value for rule in rules)
        if rules_count >= MIN_RULES_TO_PASS:
            return True

        for rule in rules:
            if not rule.value:
                raise Exception(rule.error_msg)

        return True