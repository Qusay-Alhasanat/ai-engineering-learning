from customer_feedback_analyzer.text_cleaner import clean_text


def test_clean_text_converts_text_to_lowercase():
    assert clean_text("GREAT Product") == "great product"


def test_clean_text_removes_punctuation():
    assert clean_text("Great product!!!") == "great product"


def test_clean_text_normalizes_whitespace():
    assert clean_text("  great   product  ") == "great product"


def test_clean_text_combines_all_cleaning_steps():
    assert clean_text("  GREAT   product!!! Really GOOD.  ") == (
        "great product really good"
    )


def test_clean_text_returns_empty_string_for_whitespace_only():
    assert clean_text("   \t\n  ") == ""
