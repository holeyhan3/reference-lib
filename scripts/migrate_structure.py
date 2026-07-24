import shutil
from pathlib import Path

DOCS = Path("docs")


# Existing folders -> new locations
MOVES = {
    "foundations": "knowledge/foundations",
    "economics": "knowledge/economics",
    "finance": "knowledge/finance",
    "geopolitics": "knowledge/geopolitics",
    "international-relations": "knowledge/international-relations",
    "politics": "knowledge/politics",
    "technology": "knowledge/technology",
}


# New learning structure
LEARNING = [
    "learning",
    "learning/mathematics",
    "learning/programming",
    "learning/statistics",
    "learning/economics",
    "learning/research-methods",
    "learning/writing",
]


def move_directory(
    source: Path,
    destination: Path,
):
    """
    Move directory while preserving contents.
    """

    if not source.exists():
        print(f"SKIP missing: {source}")
        return

    if destination.exists():
        print(
            f"SKIP exists: {destination}"
        )
        return

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.move(
        str(source),
        str(destination),
    )

    print(
        f"MOVED {source} -> {destination}"
    )


def create_learning_structure():
    """
    Create empty learning hierarchy.
    """

    for folder in LEARNING:

        path = DOCS / folder

        if path.exists():
            print(
                f"Exists: {path}"
            )
            continue

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        print(
            f"Created: {path}"
        )


def migrate():

    print(
        "Starting knowledge migration..."
    )

    for old, new in MOVES.items():

        move_directory(
            DOCS / old,
            DOCS / new,
        )

    create_learning_structure()

    print(
        "Migration complete."
    )


if __name__ == "__main__":
    migrate()
