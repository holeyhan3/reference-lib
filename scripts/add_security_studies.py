from pathlib import Path


DOCS = Path("docs")


CATEGORIES = [
    "international-relations/security-studies/nuclear-strategy",
    "international-relations/security-studies/deterrence-theory",
    "international-relations/security-studies/arms-control",
    "international-relations/security-studies/proliferation",
    "international-relations/security-studies/escalation-management",
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
