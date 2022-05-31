"""jinja_statement_delimiter_rule.py - Rule class to check if jinja delimeters
                                    are wrong.
"""

from j2lint.linter.rule import Rule
from j2lint.utils import get_jinja_statements
from j2lint.logger import logger


class JinjaStatementDelimiterRule(Rule):
    """Rule class to check if jinja delimeters are wrong.
    """
    id = 'S6'
    short_description = 'jinja-statements-delimeter'
    description = "Jinja statements should not have {%- or {%+ or -%} as delimeters"
    severity = 'LOW'

    @classmethod
    def check(cls, line):
        """Checks if the given line matches the wrong delimeters

        Args:
            line (string): a single line from the file

        Returns:
            Object: Returns True if error is found else False
        """
        statements = get_jinja_statements(line)
        for statement in statements:
            if statement[3] in ["{%-", "{%+"] or statement[4] == "-%}":
                return True

        logger.debug("Check line rule does not exist for %s",
                     __class__.__name__)

        return False
