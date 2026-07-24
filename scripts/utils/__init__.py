"""
Utility functions for reference-lib automation.
"""

from .categories import (
    choose_category,
    resolve_category,
)
from .config import (
    load_config,
)
from .discovery import (
    discover_categories,
    scan_directory,
)
from .files import (
    create_note_file,
    find_similar_notes,
)
from .formatting import (
    create_metadata,
    slugify,
)
from .metadata import (
    load_metadata,
    metadata_to_node,
)
from .paths import (
    CONFIG,
    DOCS,
    MKDOCS,
)
from .types import (
    CategoryNode,
)

__all__ = [
    "CONFIG",
    "DOCS",
    "MKDOCS",
    "CategoryNode",
    "choose_category",
    "create_metadata",
    "create_note_file",
    "discover_categories",
    "find_similar_notes",
    "load_config",
    "load_metadata",
    "metadata_to_node",
    "resolve_category",
    "scan_directory",
    "slugify",
]
