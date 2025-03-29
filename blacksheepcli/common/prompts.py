"""
This module provides support for an alternative way to query the user for input, using
questionary (as it gives better control and a better user experience than cookiecutter's
built-in prompt support).
"""

import json
from pathlib import Path


def _is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


_TYPES = {
    "int": {
        "validate": lambda x: x.isdigit(),
    },
    "float": {
        "validate": _is_float,
    },
}


def _normalize_type(item):
    """
    Normalize the type to support more scenarios that are not supported by Python
    questionary.

    https://questionary.readthedocs.io/en/stable/
    """
    type_ = item.get("type")

    if type_ in _TYPES:
        item["type"] = "text"
        item.update(_TYPES[type_])


def _normalize_required(item):
    required = item.get("required")

    if required:
        item["validate"] = lambda x: len(x) > 0
        del item["required"]


def _normalize_when_value(value):
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return value


def _normalize_when(item):
    when = item.get("when")

    if when:
        if "==" in when:
            prop, equals_value = when.split("==")
            item["when"] = lambda x: x[prop.strip()] == _normalize_when_value(
                equals_value.strip(" '\"")
            )
        else:
            raise ValueError(f"Unsupported `when` setting: {when}")
    return item


def normalize_questions(extra_context, data):
    for item in data:
        _normalize_type(item)
        _normalize_required(item)
        _normalize_when(item)

        # if the context already contains the information, skip it
        has_data = item["name"] in extra_context and extra_context[item["name"]]

        if has_data:
            continue

        yield item


def get_questions(context, repo_dir: str):
    questions_file_path = Path(repo_dir) / "questions.json"

    if questions_file_path.exists():
        data = json.loads(questions_file_path.read_text("utf8"))
        return list(normalize_questions(context, data))

    return []
