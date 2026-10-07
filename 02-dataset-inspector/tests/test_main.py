import pytest

from dataset_inspector.main import format_report, main


def test_format_report():
    result = {
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

    output = format_report(result)

    assert "Dataset Inspection Report" in output
    assert "Records: 2" in output
    assert "Fields: 2" in output
    assert "name" in output
    assert "Type: str" in output
    assert "age" in output
    assert "Type: int" in output


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert "Dataset Inspection Report" in captured.out
    assert "Records: 4" in captured.out
    assert "Fields: 3" in captured.out
    assert "name" in captured.out
    assert "age" in captured.out
    assert "country" in captured.out


def test_main_help(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["dataset-inspector", "--help"])

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert "Inspect a dataset and generate a data-quality report." in captured.out
    assert "--version" in captured.out


def test_main_version(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["dataset-inspector", "--version"])

    with pytest.raises(SystemExit):
        main()

    captured = capsys.readouterr()

    assert captured.out.strip() == "0.1.0"
