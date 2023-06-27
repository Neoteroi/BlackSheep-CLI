"""
This module provides support for an alternative way to query the user for input, using
questionary (as it gives better control and a better user experience than cookiecutter's
built-in prompt support).
"""
import json
from pathlib import Path


def normalize_questions(extra_context, data):
    for item in data:
        required = item.get("required")

        if required:
            item["validate"] = lambda x: len(x) > 0
            del item["required"]

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
