from pathlib import Path

import yaml

from scripts.utils.discovery import discover_categories
from scripts.utils.types import CategoryNode

DOCS = Path("docs")
MKDOCS = Path("mkdocs.yml")


def build_nav_tree(
        tree: dict[str, CategoryNode]
):
    """
    Convert discovered category tree
    into MkDocs nav format.
    """

    nav = []

    for name, node in tree.items():

        title = node.get(
            "title",
            name.replace("-", " ").title(),
        )

        path = node.get("path")

        children = node.get(
            "children",
            {}
        )

        section = []

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
        MKDOCS,
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
        "mkdocs.yml navigation updated."
    )


if __name__ == "__main__":
    main()
