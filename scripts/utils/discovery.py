from pathlib import Path

from scripts.utils.metadata import (
    load_metadata,
    metadata_to_node,
)
from scripts.utils.paths import DOCS
from scripts.utils.types import CategoryNode


IGNORE = {
    "assets",
    "templates",
    "site",
    ".git",
    "__pycache__",
}


def should_ignore(
    folder: Path,
) -> bool:
    """
    Determine whether a folder should be excluded
    from category discovery.
    """

    return (
        folder.name in IGNORE
        or folder.name.startswith(".")
    )


def discover_categories(
    root: Path = DOCS,
) -> dict[str, CategoryNode]:
    """
    Build category tree from docs directory.

    Directory structure becomes hierarchy.
    _category.yaml provides metadata.
    """

    return scan_directory(root)


def scan_directory(
    directory: Path,
    relative: Path | None = None,
) -> dict[str, CategoryNode]:

    if relative is None:
        relative = Path()

    tree: dict[str, CategoryNode] = {}

    folders = [
        p
        for p in directory.iterdir()
        if (
            p.is_dir()
            and not should_ignore(p)
        )
    ]

    # Respect _category.yaml order first,
    # alphabetical fallback second
    folders.sort(
        key=lambda folder: (
            load_metadata(folder).get("order") or 999,
            folder.name,
        )
    )

    for folder in folders:

        rel_path = relative / folder.name

        children = scan_directory(
            folder,
            rel_path,
        )

        metadata = load_metadata(folder)

        node = metadata_to_node(
            metadata
        )

        # Folder itself is a documentation page
        if any(folder.glob("*.md")):
            node["path"] = str(rel_path)

        # Folder contains subcategories
        if children:
            node["children"] = children

        # Ignore empty folders
        if not node:
            continue

        tree[folder.name] = node

    return tree
