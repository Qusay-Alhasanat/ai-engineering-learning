from collections import Counter
from dataclasses import dataclass

from customer_feedback_analyzer.classifier import classify_sentiment
from customer_feedback_analyzer.text_cleaner import clean_text


@dataclass
class AnalysisResult:
    total_rows: int
    valid_count: int
    excluded_count: int
    sentiment_counts: dict[str, int]
    sentiment_percentages: dict[str, float]
    top_words: list[tuple[str, int]]


def analyze_comments(comments: list[str]) -> AnalysisResult:
    sentiment_counts = {
        "positive": 0,
        "negative": 0,
        "neutral": 0,
    }
    word_counts = Counter()
    valid_count = 0

    for comment in comments:
        cleaned_comment = clean_text(comment)

        if not cleaned_comment:
            continue

        valid_count += 1

        sentiment = classify_sentiment(cleaned_comment)
        sentiment_counts[sentiment] += 1

        word_counts.update(cleaned_comment.split())

    total_rows = len(comments)
    excluded_count = total_rows - valid_count

    if valid_count:
        sentiment_percentages = {
            sentiment: round(count / valid_count * 100, 2)
            for sentiment, count in sentiment_counts.items()
        }
    else:
        sentiment_percentages = {
            "positive": 0.0,
            "negative": 0.0,
            "neutral": 0.0,
        }

    top_words = word_counts.most_common(5)

    return AnalysisResult(
        total_rows=total_rows,
        valid_count=valid_count,
        excluded_count=excluded_count,
        sentiment_counts=sentiment_counts,
        sentiment_percentages=sentiment_percentages,
        top_words=top_words,
    )
