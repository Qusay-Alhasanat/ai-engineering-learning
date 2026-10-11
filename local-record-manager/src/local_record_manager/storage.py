import json
from pathlib import Path

from local_record_manager.records import VALID_STATUSES


def load_data(file_path: Path) -> tuple[list[dict], int]:
    """Load records and last_id from a JSON file."""

    if not file_path.exists():
        return [], 0

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(f"Data file contains invalid JSON: {file_path}") from error

    except OSError as error:
        raise OSError(f"Could not read data file: {file_path}") from error

    if not isinstance(data, dict):
        raise ValueError("Invalid data format: root must be an object.")

    records = data.get("records")
    last_id = data.get("last_id")

    if not isinstance(records, list):
        raise ValueError("Invalid data format: 'records' must be a list.")

    if not isinstance(last_id, int) or isinstance(last_id, bool) or last_id < 0:
        raise ValueError(
            "Invalid data format: 'last_id' must be a non-negative integer."
        )

    seen_ids = set()

    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Invalid record: each record must be an object.")

        record_id = record.get("id")
        title = record.get("title")
        description = record.get("description")
        status = record.get("status")

        if (
            not isinstance(record_id, int)
            or isinstance(record_id, bool)
            or record_id <= 0
        ):
            raise ValueError("Invalid record: 'id' must be a positive integer.")

        if record_id in seen_ids:
            raise ValueError(f"Invalid data: duplicate record ID {record_id}.")

        seen_ids.add(record_id)

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid record: 'title' must be a non-empty string.")

        if not isinstance(description, str):
            raise ValueError("Invalid record: 'description' must be a string.")

        if not isinstance(status, str) or status not in VALID_STATUSES:
            raise ValueError("Invalid record: 'status' is not an allowed status.")

    if seen_ids and max(seen_ids) > last_id:
        raise ValueError("Invalid data: 'last_id' cannot be smaller than a record ID.")

    return records, last_id


def save_data(
    file_path: Path,
    records: list[dict],
    last_id: int,
) -> None:
    """Save records and last_id to a JSON file."""

    data = {
        "last_id": last_id,
        "records": records,
    }

    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except OSError as error:
        raise OSError(f"Could not write data file: {file_path}") from error
