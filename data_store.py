"""Persistence helpers for CRUD app.

This module is intentionally focused on file I/O so business logic can stay clean
in a separate module.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_DATA_FILE = Path("data.json")


def ensure_data_file(file_path: Path = DEFAULT_DATA_FILE) -> None:
    """Create the JSON data file if it does not exist."""
    if not file_path.exists():
        file_path.write_text("[]\n", encoding="utf-8")


def load_items(file_path: Path = DEFAULT_DATA_FILE) -> list[dict[str, Any]]:
    """Load all items from JSON storage."""
    ensure_data_file(file_path)
    raw = file_path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    return json.loads(raw)


def save_items(items: list[dict[str, Any]], file_path: Path = DEFAULT_DATA_FILE) -> None:
    """Persist all items to JSON storage."""
    file_path.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
