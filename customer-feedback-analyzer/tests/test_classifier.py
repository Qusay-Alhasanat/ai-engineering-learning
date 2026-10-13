from customer_feedback_analyzer.classifier import classify_sentiment


def test_classifies_positive_comment():
    assert classify_sentiment("great product") == "positive"


def test_classifies_negative_comment():
    assert classify_sentiment("terrible service") == "negative"


def test_classifies_mixed_comment_as_neutral():
    assert classify_sentiment("great product but terrible service") == "neutral"


def test_classifies_unknown_words_as_neutral():
    assert classify_sentiment("product arrived yesterday") == "neutral"


def test_classifies_empty_text_as_neutral():
    assert classify_sentiment("") == "neutral"
