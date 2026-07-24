import argparse
from pathlib import Path

from scripts.utils import (
    DOCS,
    create_metadata,
    discover_categories,
    find_similar_notes,
    load_config,
    resolve_category,
    slugify,
)


def new_note(
    title: str,
    note_type: str,
    category: str,
):

    config = load_config()

    # Validate note type
    if note_type not in config["types"]:
        raise ValueError(
            f"Unknown note type: {note_type}"
        )

    template_path = Path(
        config["types"][note_type]["template"]
    )

    if not template_path.exists():
        raise FileNotFoundError(
            f"Template not found: {template_path}"
        )

    folder = DOCS / category

    filename = slugify(title) + ".md"

    target = folder / filename

    similar = find_similar_notes(
        folder,
        target.stem,
    )

    if similar:

        print("\nPossible existing notes found:")

        for note in similar:
            print(f"- {note}")

        answer = input(
            "\nContinue creating anyway? (y/n): "
        )

        if answer.lower() != "y":
            print("Cancelled.")
            return

    if target.exists():

        print(
            f"Already exists: {target}"
        )
        return

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    template = template_path.read_text(
        encoding="utf-8"
    )

    metadata = create_metadata(
        title,
        category,
    )

    if template.startswith("---"):

        template = template.split(
            "---",
            2
        )[2]

    target.write_text(
        metadata + template.lstrip(),
        encoding="utf-8",
    )

    print(
        f"Created: {target}"
    )


def main():

    parser = argparse.ArgumentParser(
        description="Create a new reference-lib note"
    )

    parser.add_argument(
        "title",
        help="Note title",
    )

    parser.add_argument(
        "category_parts",
        nargs="*",
        help=(
            "Category path or menu selections. "
            "Example: foundations mathematics statistics "
            "or: 1 2 3"
        ),
    )

    parser.add_argument(
        "--type",
        default="concept",
        choices=[
            "concept",
            "book",
            "paper",
            "cheatsheet",
            "project",
        ],
    )

    args = parser.parse_args()

    categories = discover_categories()

    category = resolve_category(
        categories,
        args.category_parts,
    )

    new_note(
        args.title,
        args.type,
        category,
    )


if __name__ == "__main__":
    main()
