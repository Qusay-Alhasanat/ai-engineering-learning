from customer_feedback_analyzer.analyzer import AnalysisResult
from customer_feedback_analyzer.reporter import print_report


def test_print_report_displays_summary(capsys):
    result = AnalysisResult(
        total_rows=3,
        valid_count=2,
        excluded_count=1,
        sentiment_counts={
            "positive": 1,
            "negative": 1,
            "neutral": 0,
        },
        sentiment_percentages={
            "positive": 50.0,
            "negative": 50.0,
            "neutral": 0.0,
        },
        top_words=[("great", 1), ("product", 1)],
    )

    print_report(result)

    output = capsys.readouterr().out

    assert "Customer Feedback Analysis" in output
    assert "Total rows: 3" in output
    assert "Valid comments: 2" in output
    assert "Excluded comments: 1" in output
    assert "Positive: 1 (50.00%)" in output
    assert "Negative: 1 (50.00%)" in output
    assert "1. great — 1" in output


def test_print_report_handles_empty_top_words(capsys):
    result = AnalysisResult(
        total_rows=0,
        valid_count=0,
        excluded_count=0,
        sentiment_counts={
            "positive": 0,
            "negative": 0,
            "neutral": 0,
        },
        sentiment_percentages={
            "positive": 0.0,
            "negative": 0.0,
            "neutral": 0.0,
        },
        top_words=[],
    )

    print_report(result)

    output = capsys.readouterr().out

    assert "No words to display." in output
