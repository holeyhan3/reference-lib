from pathlib import Path


DOCS = Path("docs")


CATEGORIES = [
    "international-relations/security-studies/military-strategy",
    "international-relations/security-studies/intelligence-studies",
    "international-relations/security-studies/cyber-conflict",
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

        print(
            f"Created: {folder}"
        )


if __name__ == "__main__":
    create_categories()
