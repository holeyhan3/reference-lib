import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import feedparser

OUTPUT = Path(
    "docs/dashboard/news.md"
)


DISPLAY_TIMEZONE = ZoneInfo(
    "America/New_York"
)


FEEDS = {
    "Reuters World": {
        "url": "https://feeds.reuters.com/reuters/worldNews",
        "category": "Geopolitics",
    },

    "BBC World": {
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
        "category": "World",
    },

    "Foreign Policy": {
        "url": "https://foreignpolicy.com/feed/",
        "category": "Geopolitics",
    },
}

# 5 means 5 articles per feed, so 15 total articles for 3 feeds


def fetch_news(
    limit: int = 5
) -> list[dict[str, str]]:
    """
    Fetch articles from RSS feeds.

    Args:
        limit:
            Maximum articles per feed.

    Returns:
        List of article dictionaries.
    """

    articles: list[dict[str, str]] = []

    for source, config in FEEDS.items():

        feed = feedparser.parse(
            config["url"]
        )

        for entry in feed.entries[:limit]:

            published = entry.get(
                "published",
                "Unknown",
            )

            articles.append(
                {
                    "source": source,
                    "category": config["category"],
                    "title": entry.get(
                        "title",
                        "Untitled",
                    ),
                    "link": entry.get(
                        "link",
                        "",
                    ),
                    "published": published,
                }
            )

    return articles


def get_timestamp() -> str:
    """
    Return current local timestamp.

    Uses UTC internally.
    """

    utc_now = datetime.datetime.now(
        datetime.UTC
    )

    local_time = utc_now.astimezone(
        DISPLAY_TIMEZONE
    )

    return (
        f"{local_time:%Y-%m-%d %H:%M %Z}"
    )


def build_markdown() -> None:
    """
    Generate dashboard news page.
    """

    articles = fetch_news()

    lines = [
        "# News Dashboard\n",
        "\n",
        "> Automatically generated from RSS feeds.\n",
        "\n",
        f"Updated: {get_timestamp()}\n",
        "\n",
        "---\n",
    ]

    for item in articles:

        lines.append(
            f"""
## {item["title"]}

**Category:** {item["category"]}

**Source:** {item["source"]}

**Published:** {item["published"]}

[Read article]({item["link"]})

---

"""
        )

    OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT.write_text(
        "".join(lines),
        encoding="utf-8",
    )


def main() -> None:
    """
    Script entry point.
    """

    build_markdown()

    print(
        f"Updated {OUTPUT}"
    )


if __name__ == "__main__":
    main()
