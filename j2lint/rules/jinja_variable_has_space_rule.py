"""jinja_variable_has_space_rule.py - Rule class to check if jinja variables have
                                  single space between curly brackets and
                                  variable name.
"""
from __future__ import annotations

import re
from typing import Any

from j2lint.linter.error import LinterError
from j2lint.linter.rule import Rule


class JinjaVariableHasSpaceRule(Rule):
    """Rule class to check if jinja variables have single space between curly
    brackets and variable name.
    """

    rule_id = "S1"
    description = (
        "A single space should be added between Jinja2 curly brackets "
        "and a variable name: {{ ethernet_interface }}"
    )

    short_description = "single-space-decorator"
    severity = "LOW"

    regex = re.compile(
        r"{{[^ \-\+\d]|{{[-\+][^ ]|[^ \-\+\d]}}|[^ {][-\+\d]}}|{{ \s+[^ \-\+]|[^ \-\+] \s+}}"
    )

    def __init__(self, ignore: bool = False, warn: list[Any] | None = None) -> None:
        super().__init__()

    def checktext(self, filename: str, text: str) -> list[LinterError]:
        raise NotImplementedError

    def checkline(self, filename: str, line: str, line_no: int) -> list[LinterError]:
        """Checks if the given line matches the error regex

        Args:
            line (string): a single line from the file

        Returns:
            list[LinterError]: the list of LinterError generated by this rule
        """
        matches = self.regex.search(line)
        return [LinterError(line_no, line, filename, self)] if matches else []
