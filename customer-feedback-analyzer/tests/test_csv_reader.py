import pytest
from customer_feedback_analyzer.csv_reader import read_comments


def test_read_comments_returns_comments_in_order(tmp_path):
    csv_file = tmp_path / "feedback.csv"
    csv_file.write_text(
        "comment\nGreat product\nDelivery was slow\n",
        encoding="utf-8",
    )

    result = read_comments(csv_file)

    assert result == ["Great product", "Delivery was slow"]


def test_read_comments_raises_error_when_comment_column_is_missing(tmp_path):
    csv_file = tmp_path / "feedback.csv"
    csv_file.write_text(
        "customer_name\nAhmad\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="comment"):
        read_comments(csv_file)


def test_read_comments_returns_empty_list_when_no_data_rows(tmp_path):
    csv_file = tmp_path / "feedback.csv"
    csv_file.write_text("comment\n", encoding="utf-8")

    result = read_comments(csv_file)

    assert result == []


def test_read_comments_raises_error_when_file_does_not_exist(tmp_path):
    csv_file = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="File not found"):
        read_comments(csv_file)


def test_read_comments_raises_error_for_non_csv_file(tmp_path):
    file_path = tmp_path / "feedback.txt"
    file_path.write_text("comment\nGreat product\n", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV file"):
        read_comments(file_path)
