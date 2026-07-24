import yaml
from pathlib import Path

for file in Path("docs").rglob("_category.yaml"):
    data = yaml.safe_load(file.read_text()) or {}

    if data.get("order") is None:
        data.pop("order", None)
        file.write_text(
            yaml.dump(
                data,
                sort_keys=False
            )
        )
        print("Fixed", file)
