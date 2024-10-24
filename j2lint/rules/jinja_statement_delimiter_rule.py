# Copyright (c) 2021-2024 Arista Networks, Inc.
# Use of this source code is governed by the MIT license
# that can be found in the LICENSE file.
"""jinja_statement_delimiter_rule.py - Rule class to check if jinja delimiters
                                    are wrong.
"""

from __future__ import annotations

from typing import Any

from j2lint.linter.error import LinterError
from j2lint.linter.rule import Rule
from j2lint.utils import get_jinja_statements


class JinjaStatementDelimiterRule(Rule):
    """Rule class to check if jinja delimiters are wrong."""

    rule_id = "S6"
    description = "Jinja statements should not have {%- or {%+ or -%} as delimiters"
    short_description = "jinja-statements-delimiter"
    severity = "LOW"

    def __init__(self, ignore: bool = False, warn: list[Any] | None = None) -> None:
        super().__init__()

    def checktext(self, filename: str, text: str) -> list[LinterError]:
        raise NotImplementedError

    def checkline(self, filename: str, line: str, line_no: int) -> list[LinterError]:
        """Checks if the given line matches the wrong delimiters

        Args:
            line (string): a single line from the file

        Returns:
            list[LinterError]: the list of LinterError generated by this rule
        """
        # pylint: disable=fixme
        # TODO think about a better error message that can identify characters
        statements = get_jinja_statements(line)
        return [
            LinterError(line_no, line, filename, self)
            for statement in statements
            if statement[3] in ["{%-", "{%+"] or statement[4] == "-%}"
        ]
