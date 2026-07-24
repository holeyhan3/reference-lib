from pathlib import Path


def find_similar_notes(folder, filename):

    if not folder.exists():
        return []

    matches = []

    for file in folder.glob("*.md"):

        stem = file.stem

        if filename in stem or stem in filename:
            matches.append(file)

    return matches


def create_note_file(
    folder,
    filename,
    content
):

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    target = folder / filename

    target.write_text(content)

    return target
