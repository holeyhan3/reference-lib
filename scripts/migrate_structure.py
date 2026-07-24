from pathlib import Path
import shutil


DOCS = Path("docs")


MOVES = {
    # source : destination

    # Analytical frameworks
    "international-relations/theories/game-theory":
        "analytical-frameworks/game-theory",

    "international-relations/theories/rational-choice-theory":
        "analytical-frameworks/rational-choice-theory",

    "international-relations/theories/decision-theory":
        "analytical-frameworks/decision-theory",

    "international-relations/security-studies/conflict-resolution":
        "analytical-frameworks/conflict-resolution",
}


def move_category(
    source: str,
    destination: str,
):
    """
    Move category folder while preserving contents.
    """

    src = DOCS / source
    dst = DOCS / destination

    if not src.exists():
        print(f"SKIP missing: {src}")
        return

    if dst.exists():
        raise FileExistsError(
            f"Destination already exists: {dst}"
        )

    dst.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    shutil.move(
        str(src),
        str(dst),
    )

    print(
        f"Moved {src} -> {dst}"
    )


def main():

    print(
        "Starting documentation migration..."
    )

    for src, dst in MOVES.items():
        move_category(
            src,
            dst,
        )

    print(
        "Migration complete."
    )


if __name__ == "__main__":
    main()
