import pytest

from local_record_manager.records import (
    create_record,
    list_records,
    find_record,
    update_record,
    delete_record,
)


def test_create_record():
    records = []

    record, last_id = create_record(records, 0, "Learn Python", "Practice functions")

    assert record == {
        "id": 1,
        "title": "Learn Python",
        "description": "Practice functions",
        "status": "pending",
    }
    assert last_id == 1
    assert records == [record]


def test_create_record_strips_title_whitespace():
    records = []

    record, last_id = create_record(records, 0, "  Learn Python  ")

    assert record["title"] == "Learn Python"
    assert last_id == 1


@pytest.mark.parametrize("title", ["", "   ", "\t", "\n", None, 123])
def test_create_record_rejects_invalid_title(title):
    records = []

    with pytest.raises(ValueError):
        create_record(records, 0, title)


def test_create_record_rejects_non_string_description():
    with pytest.raises(ValueError):
        create_record([], 0, "Learn Python", 123)


def test_list_records_returns_all_records():
    records = [
        {"id": 1, "title": "Python"},
        {"id": 2, "title": "Git"},
    ]

    result = list_records(records)

    assert result == records


def test_list_records_returns_a_separate_list():
    records = [{"id": 1, "title": "Python"}]

    result = list_records(records)
    result.append({"id": 2, "title": "Git"})

    assert len(records) == 1
    assert len(result) == 2


def test_find_record_returns_matching_record():
    records = [
        {"id": 1, "title": "Python"},
        {"id": 2, "title": "Git"},
    ]

    result = find_record(records, 2)

    assert result == {"id": 2, "title": "Git"}


def test_find_record_returns_none_when_missing():
    assert find_record([], 99) is None


def test_update_record_changes_title_and_status():
    records = [
        {
            "id": 1,
            "title": "Old title",
            "description": "Practice",
            "status": "pending",
        }
    ]

    result = update_record(
        records,
        1,
        title="New title",
        status="completed",
    )

    assert result["title"] == "New title"
    assert result["status"] == "completed"
    assert result["description"] == "Practice"


def test_update_record_keeps_fields_when_arguments_are_none():
    records = [
        {
            "id": 1,
            "title": "Python",
            "description": "Practice",
            "status": "pending",
        }
    ]

    result = update_record(records, 1)

    assert result == records[0]


def test_update_record_rejects_empty_title():
    records = [{"id": 1, "title": "Python"}]

    with pytest.raises(ValueError):
        update_record(records, 1, title="   ")

    assert records[0]["title"] == "Python"


@pytest.mark.parametrize(
    "status",
    ["invalid", "Completed", "", None],
)
def test_update_record_rejects_invalid_status(status):
    if status is None:
        return

    records = [{"id": 1, "title": "Python", "status": "pending"}]

    with pytest.raises(ValueError):
        update_record(records, 1, status=status)

    assert records[0]["status"] == "pending"


def test_update_record_rejects_missing_id():
    records = [{"id": 1, "title": "Python"}]

    with pytest.raises(ValueError):
        update_record(records, 99, title="New title")

    assert records[0]["title"] == "Python"


def test_delete_record_removes_and_returns_record():
    records = [
        {"id": 1, "title": "Python"},
        {"id": 2, "title": "Git"},
    ]

    deleted = delete_record(records, 1)

    assert deleted == {"id": 1, "title": "Python"}
    assert records == [{"id": 2, "title": "Git"}]


def test_delete_record_rejects_missing_id():
    records = [{"id": 1, "title": "Python"}]

    with pytest.raises(ValueError):
        delete_record(records, 99)

    assert records == [{"id": 1, "title": "Python"}]


from unittest.mock import patch

from local_record_manager import main as main_module


def test_add_record_rolls_back_when_saving_fails(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    def fail_save(*args, **kwargs):
        raise OSError("Simulated save failure")

    monkeypatch.setattr(main_module, "save_data", fail_save)

    inputs = iter(["1", "New record", "Description", "2", "0"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main_module.main()

    assert not (tmp_path / "records.json").exists()
