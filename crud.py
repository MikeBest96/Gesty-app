"""CRUD operations for item management."""

from __future__ import annotations

from typing import Any

from data_store import load_items, save_items


def create_item(name: str, description: str) -> dict[str, Any]:
    """Create and store a new item."""
    items = load_items()
    next_id = 1 if not items else max(item["id"] for item in items) + 1
    new_item = {"id": next_id, "name": name, "description": description}
    items.append(new_item)
    save_items(items)
    return new_item


def list_items() -> list[dict[str, Any]]:
    """Return every stored item."""
    return load_items()


def get_item(item_id: int) -> dict[str, Any] | None:
    """Fetch a single item by id."""
    for item in load_items():
        if item["id"] == item_id:
            return item
    return None


def update_item(item_id: int, name: str | None, description: str | None) -> dict[str, Any] | None:
    """Update an existing item and persist changes."""
    items = load_items()
    for item in items:
        if item["id"] == item_id:
            if name is not None:
                item["name"] = name
            if description is not None:
                item["description"] = description
            save_items(items)
            return item
    return None


def delete_item(item_id: int) -> bool:
    """Delete an item by id. Returns True if deleted."""
    items = load_items()
    filtered = [item for item in items if item["id"] != item_id]
    if len(filtered) == len(items):
        return False
    save_items(filtered)
    return True
