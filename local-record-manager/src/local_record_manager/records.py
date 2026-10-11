VALID_STATUSES = {"pending", "in_progress", "completed"}


def create_record(
    records: list[dict],
    last_id: int,
    title: str,
    description: str = "",
) -> tuple[dict, int]:
    """Create a new record and return the record and updated ID."""

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty.")

    if not isinstance(description, str):
        raise ValueError("Description must be a string.")

    new_id = last_id + 1

    record = {
        "id": new_id,
        "title": title.strip(),
        "description": description,
        "status": "pending",
    }

    records.append(record)

    return record, new_id


def list_records(records: list[dict]) -> list[dict]:
    """Return all records."""

    return records.copy()


def find_record(records: list[dict], record_id: int) -> dict | None:
    """Find a record by ID. Return None if it does not exist."""

    for record in records:
        if record["id"] == record_id:
            return record

    return None


def update_record(
    records: list[dict],
    record_id: int,
    title: str | None = None,
    description: str | None = None,
    status: str | None = None,
) -> dict:
    """Update one or more fields and return the updated record."""

    record = find_record(records, record_id)

    if record is None:
        raise ValueError(f"Record with ID {record_id} was not found.")

    if title is not None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title cannot be empty.")

    if description is not None and not isinstance(description, str):
        raise ValueError("Description must be a string.")

    if status is not None and status not in VALID_STATUSES:
        raise ValueError(
            f"Invalid status. Allowed statuses: {', '.join(sorted(VALID_STATUSES))}"
        )

    if title is not None:
        record["title"] = title.strip()

    if description is not None:
        record["description"] = description

    if status is not None:
        record["status"] = status

    return record


def delete_record(records: list[dict], record_id: int) -> dict:
    """Delete a record and return the deleted record."""

    record = find_record(records, record_id)

    if record is None:
        raise ValueError(f"Record with ID {record_id} was not found.")

    records.remove(record)

    return record
