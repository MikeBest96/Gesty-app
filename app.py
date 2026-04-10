"""CLI entrypoint for CRUD app.

Functions are kept explicit and small so the program is easy to follow.
"""

from __future__ import annotations

import argparse

from crud import create_item, delete_item, get_item, list_items, update_item


def build_parser() -> argparse.ArgumentParser:
    """Build the command parser and subcommands."""
    parser = argparse.ArgumentParser(description="Simple file-based CRUD manager")
    sub = parser.add_subparsers(dest="command", required=True)

    create_cmd = sub.add_parser("create", help="Create a new item")
    create_cmd.add_argument("name", help="Item name")
    create_cmd.add_argument("description", help="Item description")

    sub.add_parser("list", help="List items")

    get_cmd = sub.add_parser("get", help="Get item by id")
    get_cmd.add_argument("id", type=int)

    update_cmd = sub.add_parser("update", help="Update item by id")
    update_cmd.add_argument("id", type=int)
    update_cmd.add_argument("--name")
    update_cmd.add_argument("--description")

    delete_cmd = sub.add_parser("delete", help="Delete item by id")
    delete_cmd.add_argument("id", type=int)

    return parser


def cmd_create(args: argparse.Namespace) -> None:
    item = create_item(args.name, args.description)
    print(f"Created: {item}")


def cmd_list(_: argparse.Namespace) -> None:
    items = list_items()
    if not items:
        print("No items stored.")
        return
    for item in items:
        print(item)


def cmd_get(args: argparse.Namespace) -> None:
    item = get_item(args.id)
    print(item if item else "Item not found")


def cmd_update(args: argparse.Namespace) -> None:
    updated = update_item(args.id, args.name, args.description)
    print(updated if updated else "Item not found")


def cmd_delete(args: argparse.Namespace) -> None:
    deleted = delete_item(args.id)
    print("Deleted" if deleted else "Item not found")


def main() -> None:
    """Main dispatcher for commands."""
    parser = build_parser()
    args = parser.parse_args()

    handlers = {
        "create": cmd_create,
        "list": cmd_list,
        "get": cmd_get,
        "update": cmd_update,
        "delete": cmd_delete,
    }
    handlers[args.command](args)


if __name__ == "__main__":
    main()
