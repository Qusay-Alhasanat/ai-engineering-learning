from customer_feedback_analyzer.analyzer import analyze_comments


def test_analyze_comments_counts_sentiments():
    result = analyze_comments(
        [
            "Great product!",
            "Terrible service.",
            "Product arrived yesterday",
        ]
    )

    assert result.total_rows == 3
    assert result.valid_count == 3
    assert result.excluded_count == 0
    assert result.sentiment_counts == {
        "positive": 1,
        "negative": 1,
        "neutral": 1,
    }


def test_analyze_comments_calculates_percentages():
    result = analyze_comments(
        ["Great product", "Excellent service", "Terrible product"]
    )

    assert result.sentiment_percentages == {
        "positive": 66.67,
        "negative": 33.33,
        "neutral": 0.0,
    }


def test_analyze_comments_excludes_empty_comments():
    result = analyze_comments(["Great product", "", "   ", "Terrible service"])

    assert result.total_rows == 4
    assert result.valid_count == 2
    assert result.excluded_count == 2


def test_analyze_comments_counts_top_words_after_cleaning():
    result = analyze_comments(["Good product!", "GOOD product.", "Great service"])

    assert result.top_words == [
        ("good", 2),
        ("product", 2),
        ("great", 1),
        ("service", 1),
    ]


def test_analyze_comments_handles_no_valid_comments():
    result = analyze_comments(["", "   ", "\t"])

    assert result.total_rows == 3
    assert result.valid_count == 0
    assert result.excluded_count == 3
    assert result.sentiment_counts == {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
    }
    assert result.sentiment_percentages == {
        "positive": 0.0,
        "negative": 0.0,
        "neutral": 0.0,
    }
    assert result.top_words == []
