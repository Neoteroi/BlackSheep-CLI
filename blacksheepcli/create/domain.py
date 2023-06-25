import re
from typing import Optional

value_pattern = re.compile("^[a-zA-Z_]{1}[0-9a-zA-Z_]+$")


def validate_name(value: Optional[str]):
    if not value:
        raise ValueError("Missing value")
    if not value_pattern.match(value):
        raise ValueError("Invalid value")


class ProjectManager:
    def bootstrap(self, source: str, data=None):
        # Lazy import, to not slow down the CLI start-up for every command
        from blacksheepcli.common.cookiemonkey import cookiecutter

        # https://cookiecutter.readthedocs.io/en/stable/advanced/calling_from_python.html

        cookiecutter(source, extra_context=data)
