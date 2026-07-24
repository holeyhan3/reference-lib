from pathlib import Path
from typing import Any

import yaml

from scripts.utils.types import CategoryNode


def load_metadata(
    folder: Path,
) -> dict[str, Any]:
    """
    Load _category.yaml metadata.
    """

    file = folder / "_category.yaml"

    if not file.exists():
        return {}

    with file.open(
        "r",
        encoding="utf-8",
    ) as f:
        return yaml.safe_load(f) or {}


def metadata_to_node(
    metadata: dict[str, Any],
) -> CategoryNode:
    """
    Convert YAML metadata into a valid CategoryNode.
    """

    node: CategoryNode = {}

    if "title" in metadata:
        node["title"] = str(
            metadata["title"]
        )

    if "description" in metadata:
        node["description"] = str(
            metadata["description"]
        )

    if "order" in metadata:
        node["order"] = int(
            metadata["order"]
        )

    return node
