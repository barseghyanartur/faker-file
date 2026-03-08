import re
from typing import Union
from xml.sax.saxutils import escape as xml_escape

from faker import Faker
from faker.generator import Generator
from faker.providers.python import Provider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2025 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "TOKEN_RE",
    "xml_safe_format_func",
)

# Regex that matches faker-file / Faker template tokens: {{word}}
TOKEN_RE = re.compile(r"\{\{(\w+)\}\}")


def xml_safe_format_func(
    generator: Union[Faker, Generator, Provider],
    content: str,
) -> str:
    """
    A drop-in replacement for default format_func (`generator.parse(content)`)
    that XML-escapes every value produced by Faker template directives
    (e.g. `{{country}}`, `{{sentence}}`) before inserting them into the
    template string.

    faker-file's default format_func is essentially:

    which calls Faker's template engine to replace {{directive}} tokens.

    We intercept each substitution and escape the result so that
    values like "Svalbard & Jan Mayen Islands" become
    "Svalbard &amp; Jan Mayen Islands", keeping the XML valid.
    """

    def _replace(match: re.Match) -> str:
        directive = match.group(1)  # e.g. "country"
        value = str(generator.parse(f"{{{{{directive}}}}}"))  # call Faker
        return xml_escape(value)  # escape &, <, >, ", '

    return TOKEN_RE.sub(_replace, content)
