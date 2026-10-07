from dataset_inspector.inspector import (
    extract_field,
    get_fields,
    get_shape,
    validate_dataset,
    analyze_field,
    generate_report,
    inspect_dataset,
)


def test_valid_dataset():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad", "age": 30},
    ]

    assert validate_dataset(dataset) is True


def test_empty_dataset():
    dataset = []

    assert validate_dataset(dataset) is False


def test_dataset_is_not_list():
    dataset = {"name": "Qusay"}

    assert validate_dataset(dataset) is False


def test_record_is_not_dict():
    dataset = [
        {"name": "Qusay"},
        "Ahmad",
    ]

    assert validate_dataset(dataset) is False


def test_get_shape():
    dataset = [
        {"name": "Qusay", "age": 25, "country": "Palestine"},
        {"name": "Ahmad", "age": 30, "country": "Jordan"},
        {"name": "Sara", "country": "Palestine"},
    ]

    assert get_shape(dataset) == (3, 3)


def test_get_shape_with_different_fields():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad", "country": "Jordan"},
    ]

    assert get_shape(dataset) == (2, 3)


def test_get_fields():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad", "country": "Jordan"},
        {"name": "Sara", "age": 22},
    ]

    assert get_fields(dataset) == ["name", "age", "country"]


def test_extract_field():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad"},
        {"name": "Sara", "age": None},
        {"name": "Omar", "age": "28"},
    ]

    result = extract_field(dataset, "age")

    assert result == {
        "values": [25, None, "28"],
        "missing_fields": [1],
        "none_values": [2],
    }


def test_analyze_field():
    field_data = {
        "values": [25, None, "28", 25],
        "missing_fields": [4],
        "none_values": [1],
    }

    result = analyze_field(field_data)

    assert result == {
        "type": "mixed",
        "missing": 1,
        "none": 1,
        "unique": 2,
    }


def test_analyze_field_single_type():
    field_data = {
        "values": [25, 30, 28],
        "missing_fields": [],
        "none_values": [],
    }

    result = analyze_field(field_data)

    assert result == {
        "type": "int",
        "missing": 0,
        "none": 0,
        "unique": 3,
    }


def test_analyze_field_all_none():
    field_data = {
        "values": [None, None],
        "missing_fields": [],
        "none_values": [0, 1],
    }

    result = analyze_field(field_data)

    assert result == {
        "type": "no_data",
        "missing": 0,
        "none": 2,
        "unique": 0,
    }


def test_generate_report():
    dataset = [
        {"name": "Qusay", "age": 25, "country": "Palestine"},
        {"name": "Ahmad", "age": 30, "country": "Jordan"},
        {"name": "Sara", "country": "Palestine"},
        {"name": "Omar", "age": "28", "country": "Egypt"},
    ]

    result = generate_report(dataset)

    assert result == {
        "records": 4,
        "fields": 3,
        "field_details": {
            "name": {
                "type": "str",
                "missing": 0,
                "none": 0,
                "unique": 4,
            },
            "age": {
                "type": "mixed",
                "missing": 1,
                "none": 0,
                "unique": 3,
            },
            "country": {
                "type": "str",
                "missing": 0,
                "none": 0,
                "unique": 3,
            },
        },
    }


def test_generate_report_with_different_fields():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad", "country": "Jordan"},
        {"name": "Sara", "age": 22, "city": "Gaza"},
    ]

    result = generate_report(dataset)

    assert result == {
        "records": 3,
        "fields": 4,
        "field_details": {
            "name": {
                "type": "str",
                "missing": 0,
                "none": 0,
                "unique": 3,
            },
            "age": {
                "type": "int",
                "missing": 1,
                "none": 0,
                "unique": 2,
            },
            "country": {
                "type": "str",
                "missing": 2,
                "none": 0,
                "unique": 1,
            },
            "city": {
                "type": "str",
                "missing": 2,
                "none": 0,
                "unique": 1,
            },
        },
    }


def test_inspect_dataset_invalid():
    dataset = [
        {"name": "Qusay"},
        "Ahmad",
    ]

    result = inspect_dataset(dataset)

    assert result == {
        "valid": False,
        "error": "Invalid dataset format",
    }


def test_inspect_dataset_valid():
    dataset = [
        {"name": "Qusay", "age": 25},
        {"name": "Ahmad", "age": 30},
    ]

    result = inspect_dataset(dataset)

    assert result == {
        "valid": True,
        "report": {
            "records": 2,
            "fields": 2,
            "field_details": {
                "name": {
                    "type": "str",
                    "missing": 0,
                    "none": 0,
                    "unique": 2,
                },
                "age": {
                    "type": "int",
                    "missing": 0,
                    "none": 0,
                    "unique": 2,
                },
            },
        },
    }


def test_inspect_dataset_with_data_quality_issues():
    dataset = [
        {"name": "Qusay", "age": 25, "country": "Palestine"},
        {"name": "Ahmad", "age": None, "country": "Jordan"},
        {"name": "Sara", "country": "Palestine"},
        {"name": "Omar", "age": "28", "country": "Egypt"},
    ]

    result = inspect_dataset(dataset)

    assert result["valid"] is True
    assert result["report"]["records"] == 4
    assert result["report"]["fields"] == 3

    assert result["report"]["field_details"]["age"] == {
        "type": "mixed",
        "missing": 1,
        "none": 1,
        "unique": 2,
    }
