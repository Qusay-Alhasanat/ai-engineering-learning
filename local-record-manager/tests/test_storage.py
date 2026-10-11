import json

import pytest

from local_record_manager.storage import load_data, save_data


def test_load_data_returns_empty_data_when_file_does_not_exist(tmp_path):
    file_path = tmp_path / "records.json"

    records, last_id = load_data(file_path)

    assert records == []
    assert last_id == 0
    assert not file_path.exists()


def test_save_data_creates_json_file(tmp_path):
    file_path = tmp_path / "records.json"
    records = [
        {
            "id": 1,
            "title": "Learn Python",
            "description": "Practice functions",
            "status": "pending",
        }
    ]

    save_data(file_path, records, 1)

    assert file_path.exists()

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert data["records"] == records
    assert data["last_id"] == 1


def test_load_data_reads_saved_data(tmp_path):
    file_path = tmp_path / "records.json"
    records = [
        {
            "id": 1,
            "title": "تعلم Python",
            "description": "التدرب على الدوال",
            "status": "pending",
        }
    ]

    save_data(file_path, records, 1)

    loaded_records, last_id = load_data(file_path)

    assert loaded_records == records
    assert last_id == 1


def test_save_and_load_empty_records(tmp_path):
    file_path = tmp_path / "records.json"

    save_data(file_path, [], 0)

    records, last_id = load_data(file_path)

    assert records == []
    assert last_id == 0


def test_load_data_raises_value_error_for_invalid_json(tmp_path):
    file_path = tmp_path / "records.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(ValueError, match="invalid JSON"):
        load_data(file_path)


def test_load_data_rejects_records_that_are_not_a_list(tmp_path):
    file_path = tmp_path / "records.json"
    file_path.write_text(
        json.dumps({"records": {}, "last_id": 0}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="'records' must be a list"):
        load_data(file_path)


@pytest.mark.parametrize(
    "last_id",
    [-1, 1.5, "1", None, True],
)
def test_load_data_rejects_invalid_last_id(tmp_path, last_id):
    file_path = tmp_path / "records.json"
    file_path.write_text(
        json.dumps({"records": [], "last_id": last_id}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="last_id"):
        load_data(file_path)


def test_save_data_raises_os_error_when_parent_directory_is_missing(tmp_path):
    file_path = tmp_path / "missing" / "records.json"

    with pytest.raises(OSError, match="Could not write data file"):
        save_data(file_path, [], 0)
