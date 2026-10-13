import argparse
from pathlib import Path

from customer_feedback_analyzer.analyzer import analyze_comments
from customer_feedback_analyzer.csv_reader import read_comments
from customer_feedback_analyzer.reporter import print_report


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze customer feedback from a CSV file."
    )
    parser.add_argument(
        "file",
        type=Path,
        help="Path to the CSV file containing customer comments.",
    )

    args = parser.parse_args()

    try:
        comments = read_comments(args.file)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    result = analyze_comments(comments)
    print_report(result)
