from pathlib import Path

import yaml

from scripts.utils.discovery import discover_categories
from scripts.utils.paths import DOCS

BASE_CONFIG = Path("mkdocs.base.yml")
MKDOCS = Path("mkdocs.yml")


def build_nav_tree(tree):

    nav = []

    for name, node in tree.items():

        title = node.get(
            "title",
            name.replace("-", " ").title(),
        )

        section = []

        path = node.get("path")

        children = node.get(
            "children",
            {},
        )

        if path:

            section.append(
                {
                    "Overview": f"{path}/index.md"
                }
            )

        if children:

            section.extend(
                build_nav_tree(children)
            )

        nav.append(
            {
                title: section
            }
        )

    return nav


def update_mkdocs():

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
    update_mkdocs()
    print(
        "mkdocs.yml generated."
    )


if __name__ == "__main__":
    main()
