# Text Analyzer

A small Python project that analyzes text and extracts basic statistics such as character count, word count, and word frequency.

This project was built as a **Learning / Training Project** while studying Python and software engineering fundamentals for AI Engineering.

## Features

* Validate user input
* Clean and normalize text
* Convert text to lowercase
* Handle punctuation
* Split text into words
* Count characters
* Count words
* Calculate word frequency
* Automated testing with pytest

## Project Structure

```text
text-analyzer/
├── src/
│   └── text_analyzer/
│       ├── __init__.py
│       ├── analyzer.py
│       └── main.py
├── tests/
│   └── test_analyzer.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

### Main Components

* `main.py` — Handles user interaction and controls the program flow.
* `analyzer.py` — Contains the text validation, cleaning, and analysis logic.
* `test_analyzer.py` — Contains automated tests for the analyzer functions.

## Data Flow

```text
Raw Input
    ↓
Validation
    ↓
Cleaning / Normalization
    ↓
Split into Words
    ↓
Analysis
    ├── Character Count
    ├── Word Count
    └── Word Frequency
    ↓
Structured Output
```

## Example

Input:

```text
Hello, hello! WORLD
```

Output:

```text
{
    'character_count': 19,
    'word_count': 3,
    'word_frequency': {
        'hello': 2,
        'world': 1
    }
}
```

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for Python project and dependency management.

Clone the repository and install the project dependencies:

```bash
uv sync
```

## Run

Run the application with:

```bash
uv run text-analyzer
```

Then enter the text you want to analyze.

## Run Tests

The project uses pytest for automated testing.

Run:

```bash
uv run pytest
```

Current test suite:

```text
16 passed
```

## What I Learned

Through this project, I practiced:

* Python strings and string methods
* Lists and dictionaries
* Loops and conditions
* Functions and type hints
* Input validation
* Data cleaning and normalization
* Separation of concerns
* Basic project structure
* Python packages and modules
* Virtual environments and dependency management with uv
* Automated testing with pytest
* Assertions and edge cases
* Debugging and regression testing
* Git/GitHub project workflow

## Project Status

Completed ✅

This project is part of my **AI Engineering Learning / Training Projects** and was created to strengthen Python and software engineering fundamentals through practical implementation.
