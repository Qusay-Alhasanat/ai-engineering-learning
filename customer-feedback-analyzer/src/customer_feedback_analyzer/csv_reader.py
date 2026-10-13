import csv
from pathlib import Path


def read_comments(file_path: str | Path) -> list[str]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if "comment" not in (reader.fieldnames or []):
            raise ValueError("CSV file must contain a 'comment' column.")

        comments = [row["comment"] or "" for row in reader]

    return comments
