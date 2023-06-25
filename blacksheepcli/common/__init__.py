"""
Imports click or rich_click depending on env settings.
Rich click increases import times and it might be desirable to disable it (e.g. when
running automated jobs).
"""
import os

_disable_rich = os.environ.get("NORICH_CLI", "").lower() in {
    "1",
    "true",
} or os.environ.get("POOR_CLI", "").lower() in {"1", "true"}

if _disable_rich:  # pragma: no cover
    import click
else:
    import rich_click as click

__all__ = ["click"]
