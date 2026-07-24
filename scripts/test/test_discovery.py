from pprint import pprint

from scripts.utils.discovery import discover_categories

categories = discover_categories()

pprint(categories)
