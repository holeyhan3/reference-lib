from scripts.utils.types import CategoryNode


def choose_from_menu(
    options: dict[str, CategoryNode],
    title: str,
) -> str:
    """
    Display menu and return selected key.
    """

    print(f"\n{title}")

    items = list(options.keys())

    for i, item in enumerate(
        items,
        start=1,
    ):
        print(f"{i}. {item}")

    while True:

        choice = input("\nChoice: ")

        try:
            index = int(choice) - 1

            if 0 <= index < len(items):
                return items[index]

        except ValueError:
            pass

        print(
            "Invalid selection. Try again."
        )


def choose_category(
    categories: dict[str, CategoryNode],
) -> str:
    """
    Interactive category selection.
    """

    choice = choose_from_menu(
        categories,
        "Choose category",
    )

    node = categories[choice]

    if "path" in node:
        return node["path"]

    if "children" in node:
        return choose_category(
            node["children"]
        )

    raise ValueError(
        "Invalid category node"
    )


def resolve_category(
    categories: dict[str, CategoryNode],
    inputs: list[str],
) -> str:
    """
    Resolve category path.

    Examples:

        foundations mathematics statistics

    or:

        1 1 2
    """

    if not inputs:
        return choose_category(categories)

    current = categories

    for item in inputs:

        choices = list(current.keys())

        if item.isdigit():

            index = int(item) - 1

            if (
                index < 0
                or index >= len(choices)
            ):
                raise ValueError(
                    f"Invalid selection: {item}"
                )

            item = choices[index]

        if item not in current:
            raise ValueError(
                f"Unknown category: {item}"
            )

        node = current[item]

        if "path" in node:
            return node["path"]

        if "children" in node:
            current = node["children"]
            continue

        raise ValueError(
            "Invalid category node"
        )

    raise ValueError(
        "Category path incomplete"
    )
