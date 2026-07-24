from pathlib import Path

import yaml

from scripts.utils.paths import DOCS

IGNORE = {
    "assets",
    "templates",
    "site",
    ".git",
    "__pycache__",
}


def format_title(name: str) -> str:
    """
    Convert folder names into display titles.
    """

    return (
        name
        .replace("-", " ")
        .replace("_", " ")
        .title()
    )


def create_category_files(
):
    """
    Create missing index.md and _category.yaml
    files for documentation categories.
    """

    for folder in DOCS.rglob("*"):

        if not folder.is_dir():
            continue

        if folder.name in IGNORE:
            continue

        if folder.name.startswith("."):
            continue

        create_index(folder)
        create_category_yaml(folder)


def create_index(folder: Path):
    """
    Create index.md if missing.
    """

    index = folder / "index.md"

    if index.exists():
        return

    title = format_title(folder.name)

    index.write_text(
        f"# {title}\n\n"
        f"Overview of {title}.\n",
        encoding="utf-8",
    )

    print(f"Created {index}")


def create_category_yaml(folder: Path):
    """
    Create _category.yaml if missing.
    """

    category = folder / "_category.yaml"

    if category.exists():
        return

    title = format_title(folder.name)

    metadata = {
        "title": title,
        "description": (
            f"Documentation about {title}."
        ),
    }

    category.write_text(
        yaml.dump(
            metadata,
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    print(f"Created {category}")


def main():
    create_category_files()

    print("Category files generated.")


if __name__ == "__main__":
    main()
