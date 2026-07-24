from pathlib import Path

DOCS = Path("docs")


NEW_CATEGORIES = [
    "analytical-frameworks",
    "analytical-frameworks/game-theory",
    "analytical-frameworks/rational-choice-theory",
    "analytical-frameworks/decision-theory",
    "analytical-frameworks/conflict-resolution",
]


def create_categories():

    for category in NEW_CATEGORIES:

        folder = DOCS / category

        if folder.exists():
            print(f"Exists: {folder}")
            continue

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        print(
            f"Created: {folder}"
        )


if __name__ == "__main__":
    create_categories()
