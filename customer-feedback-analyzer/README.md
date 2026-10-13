# Customer Feedback Analyzer

A command-line application built with Python to analyze customer feedback stored in CSV files. It classifies comments using a simple rule-based sentiment approach and generates a summary of sentiment distribution and frequently used words.

## Features

- Read customer comments from CSV files.
- Validate the required `comment` column.
- Normalize text by converting it to lowercase, removing English punctuation, and standardizing whitespace.
- Exclude empty comments and comments containing only whitespace.
- Classify comments as `positive`, `negative`, or `neutral` using predefined word lists.
- Calculate sentiment counts and percentages.
- Display the five most frequent words.
- Handle common input errors with clear messages.
- Include automated tests using `pytest`.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/) for dependency and environment management

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd customer-feedback-analyzer
```

Synchronize the project environment and install its dependencies:

```bash
uv sync
```

Replace `<repository-url>` with the URL of your Git repository.

## Input Format

The application expects a CSV file containing a column named `comment`.

Example: `sample_feedback.csv`

```csv
comment
Great product!
The quality is excellent.
Terrible customer service.
The delivery was bad.
Product arrived yesterday.
   
I love this product.
```

Each data row represents one comment. Empty comments and comments containing only whitespace are excluded from analysis.

## Usage

Run the application with the path to your CSV file:

```bash
uv run customer-feedback-analyzer sample_feedback.csv
```

Display the command-line help:

```bash
uv run customer-feedback-analyzer --help
```

## Example Output

```text
Customer Feedback Analysis
==============================

Total rows: 7
Valid comments: 6
Excluded comments: 1

Sentiment Summary
------------------------------
Positive: 3 (50.00%)
Negative: 2 (33.33%)
Neutral: 1 (16.67%)

Top 5 Words
------------------------------
1. product — 3
2. the — 2
3. great — 1
4. quality — 1
5. is — 1
```

The exact output depends on the input data.

## Sentiment Classification

The application uses predefined positive and negative word lists.

- **Positive:** The comment contains recognized positive words but no recognized negative words.
- **Negative:** The comment contains recognized negative words but no recognized positive words.
- **Neutral:** The comment contains both types of words, or neither type.

This is a simple rule-based approach, not a machine learning model. A `neutral` result does not necessarily mean that the comment expresses no sentiment; it may simply contain no recognized sentiment words or contain a mixture of positive and negative indicators.

## Running Tests

Run the automated test suite:

```bash
uv run pytest
```

## Current Limitations

- Designed primarily for English-language feedback.
- Uses predefined word lists rather than machine learning.
- Does not reliably understand negation, sarcasm, context, or complex expressions.
- Removes English ASCII punctuation; it is not a comprehensive multilingual text processor.
- Requires the input CSV to contain a `comment` column.

## Project Structure

```text
customer-feedback-analyzer/
├── src/
│   └── customer_feedback_analyzer/
│       ├── __init__.py
│       ├── main.py
│       ├── csv_reader.py
│       ├── text_cleaner.py
│       ├── classifier.py
│       ├── analyzer.py
│       └── reporter.py
├── tests/
├── pyproject.toml
├── uv.lock
└── README.md
```

## Learning Objectives

This project is part of a practical learning journey toward AI engineering. It focuses on Python fundamentals, modular design, CSV processing, text cleaning, basic data analysis, command-line interfaces, error handling, and automated testing.

The goal is to build a reliable foundation before progressing to machine learning and more advanced AI systems.
