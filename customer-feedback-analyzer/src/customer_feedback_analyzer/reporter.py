from customer_feedback_analyzer.analyzer import AnalysisResult


def print_report(result: AnalysisResult) -> None:
    print("\nCustomer Feedback Analysis")
    print("=" * 30)

    print(f"Total rows: {result.total_rows}")
    print(f"Valid comments: {result.valid_count}")
    print(f"Excluded comments: {result.excluded_count}")

    print("\nSentiment Summary")
    print("-" * 30)

    for sentiment, count in result.sentiment_counts.items():
        percentage = result.sentiment_percentages[sentiment]
        print(f"{sentiment.title()}: {count} ({percentage:.2f}%)")

    print("\nTop 5 Words")
    print("-" * 30)

    if not result.top_words:
        print("No words to display.")
    else:
        for index, (word, count) in enumerate(result.top_words, start=1):
            print(f"{index}. {word} — {count}")
