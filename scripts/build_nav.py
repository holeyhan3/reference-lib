from pathlib import Path
from typing import Any

import yaml

from scripts.utils.discovery import discover_categories
from scripts.utils.paths import DOCS

BASE_CONFIG = Path("mkdocs.base.yml")
MKDOCS = Path("mkdocs.yml")


NavEntry = dict[str, Any]


def build_nav_tree(
    tree: dict[str, Any],
) -> list[NavEntry]:
    """
    Convert discovered category tree into MkDocs nav format.

    Categories with children become sections.
    Their index.md files act as landing pages
    through navigation.indexes.

    Leaf categories become direct pages.
    """

    nav: list[NavEntry] = []

    for name, node in tree.items():

        title = node.get(
            "title",
            name.replace("-", " ").title(),
        )

        path = node.get(
            "path"
        )

        children = node.get(
            "children",
            {},
        )

        # Category with children
        if children:

            nav.append(
                {
                    title: build_nav_tree(children)
                }
            )

        # Leaf category
        elif path:

            nav.append(
                {
                    title: f"{path}/index.md"
                }
            )

    return nav


def update_mkdocs():
    """
    Generate mkdocs.yml from mkdocs.base.yml
    and discovered documentation categories.
    """

    categories = discover_categories(
        DOCS
    )

    with open(
        BASE_CONFIG,
        "r",
        encoding="utf-8",
    ) as f:

        config = yaml.safe_load(f)

    config["nav"] = [
        {
            "Home": "index.md"
        },
        *build_nav_tree(categories),
    ]

    with open(
        MKDOCS,
        "w",
        encoding="utf-8",
    ) as f:

        yaml.dump(
            config,
            f,
            sort_keys=False,
            allow_unicode=True,
        )


def main():
    """
    CLI entry point.
    """

    update_mkdocs()

    print(
        "mkdocs.yml generated."
    )


if __name__ == "__main__":
    main()
