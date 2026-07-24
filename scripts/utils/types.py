from typing import NotRequired, TypedDict


class CategoryNode(TypedDict):
    """
    Documentation category node.

    A node may contain:
    - metadata from _category.yaml
    - a filesystem path
    - nested categories
    """

    title: NotRequired[str]
    description: NotRequired[str]
    order: NotRequired[int]

    path: NotRequired[str]

    children: NotRequired[
        dict[str, "CategoryNode"]
    ]
