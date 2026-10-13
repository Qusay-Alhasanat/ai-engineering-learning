POSITIVE_WORDS = {
    "amazing",
    "excellent",
    "good",
    "great",
    "happy",
    "love",
    "perfect",
    "wonderful",
}

NEGATIVE_WORDS = {
    "bad",
    "disappointed",
    "hate",
    "poor",
    "terrible",
    "worst",
}


def classify_sentiment(text: str) -> str:
    words = set(text.split())

    has_positive = bool(words & POSITIVE_WORDS)
    has_negative = bool(words & NEGATIVE_WORDS)

    if has_positive and not has_negative:
        return "positive"

    if has_negative and not has_positive:
        return "negative"

    return "neutral"
