from pathlib import Path


DOCS = Path("docs")


CATEGORIES = [
    "dashboard",

    "journal",
    "journal/daily-notes",
    "journal/weekly-reviews",
    "journal/reading-notes",
    "journal/research-log",

    "intelligence",
    "intelligence/geopolitical",
    "intelligence/economic",
    "intelligence/financial",
    "intelligence/technology",
]


def create_categories():

    for category in CATEGORIES:

        folder = DOCS / category

        if folder.exists():
            print(f"Exists: {folder}")
            continue

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        print(f"Created: {folder}")


if __name__ == "__main__":
    create_categories()
