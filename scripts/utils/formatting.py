import datetime


def slugify(text):

    return (
        text.lower()
        .replace("-", " ")
        .replace("_", " ")
        .strip()
        .replace(" ", "-")
    )


def create_metadata(title, category):

    today = (
        datetime.datetime.now(
            datetime.UTC
        )
        .date()
    )

    return f"""---
title: {title}
category: {category}
tags:
  -
created: {today}
status: draft
---
"""
