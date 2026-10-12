# Dataset Inspector

A small Python project that inspects a dataset and generates a structured report about its shape, fields, data types, missing values, `None` values, and unique values.

This project was built as a **Learning / Training Project** while studying Python and software engineering fundamentals for AI Engineering.

## Features

* Validate basic dataset structure
* Count records and fields
* Detect fields across all records
* Extract field values
* Detect missing fields
* Detect explicit `None` values
* Detect field data types
* Detect mixed data types
* Count unique non-`None` values
* Generate a structured inspection report
* Display reports through a CLI
* Support `--help` and `--version`
* Automated testing with pytest

## Project Structure

```text
dataset-inspector/
├── src/
│   └── dataset_inspector/
│       ├── __init__.py
│       ├── inspector.py
│       └── main.py
├── tests/
│   ├── test_inspector.py
│   └── test_main.py
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

### Main Components

* `inspector.py` — Contains the dataset validation, inspection, and report generation logic.
* `main.py` — Handles the CLI, report formatting, and program entry point.
* `test_inspector.py` — Contains automated tests for the core inspection logic.
* `test_main.py` — Contains automated tests for the CLI and report formatting.

## Data Flow

```text
Raw Dataset
    ↓
Basic Validation
    ↓
Dataset Inspection
    ├── Shape
    ├── Fields
    └── Field Analysis
          ├── Data Type
          ├── Missing Values
          ├── None Values
          └── Unique Values
    ↓
Structured Report
    ↓
CLI Output
```

## Input

The current version accepts a dataset represented as a Python `list` of `dict` objects.

Example:

```python
dataset = [
    {"name": "Qusay", "age": 25, "country": "Palestine"},
    {"name": "Ahmad", "age": 30, "country": "Jordan"},
    {"name": "Sara", "country": "Palestine"},
    {"name": "Omar", "age": "28", "country": "Egypt"},
]
```

The inspector can identify that:

* `age` has one missing field.
* `age` contains mixed data types (`int` and `str`).
* The dataset contains 4 records and 3 fields.

## Output

The core inspection logic returns a structured Python dictionary.

Example:

```python
{
    "records": 4,
    "fields": 3,
    "field_details": {
        "name": {
            "type": "str",
            "missing": 0,
            "none": 0,
            "unique": 4,
        },
        "age": {
            "type": "mixed",
            "missing": 1,
            "none": 0,
            "unique": 3,
        },
        "country": {
            "type": "str",
            "missing": 0,
            "none": 0,
            "unique": 3,
        },
    },
}
```

The CLI presents the same information in a human-readable format:

```text
Dataset Inspection Report
=========================
Records: 4
Fields: 3

name
  Type: str
  Missing: 0
  None: 0
  Unique: 4

age
  Type: mixed
  Missing: 1
  None: 0
  Unique: 3

country
  Type: str
  Missing: 0
  None: 0
  Unique: 3
```

## Important Scope

This project is an **inspector**, not a data cleaning or validation system.

It observes and reports the current state of the dataset.

It does **not**:

* Clean or modify values
* Convert data types
* Delete records
* Fix missing values
* Determine whether a value is correct according to business rules

For example, the inspector can detect that a field contains both `25` and `"28"` and report it as `mixed`.

Determining whether `"28"` should be converted to `28` requires a separate cleaning or validation step.

## Installation

This project uses [uv](https://docs.astral.sh/uv/) for Python project and dependency management.

Clone the repository and install the project dependencies:

```bash
uv sync
```

## Run

Run the application with:

```bash
uv run dataset-inspector
```

The project currently uses a small built-in dataset to demonstrate the inspection workflow.

### Show Help

```bash
uv run dataset-inspector --help
```

### Show Version

```bash
uv run dataset-inspector --version
```

## Run Tests

The project uses pytest for automated testing.

Run:

```bash
uv run pytest
```

Current test suite:

```text
20 passed
```

## What I Learned

Through this project, I practiced:

* Python lists and dictionaries
* Functions and type hints
* Data validation
* Dataset structure inspection
* Working with missing fields and `None`
* Python type inspection
* Sets and unique values
* `enumerate()`
* Separation of concerns
* Python packages and modules
* CLI development with `argparse`
* Command-line arguments
* `--help` and `--version`
* Automated testing with pytest
* Testing CLI output with `capsys`
* Edge cases and regression testing
* Project structure and dependency management with uv
* Git/GitHub project workflow

## Why This Project Matters for AI Engineering

Data inspection is an important step before data is used in downstream systems.

A simplified workflow can look like:

```text
Raw Data
    ↓
Inspection
    ↓
Validation
    ↓
Cleaning
    ↓
Preprocessing
    ↓
Model / ML Pipeline / LLM Pipeline
```

This project focuses on the **inspection** stage.

The same idea can later appear in larger systems such as data pipelines, machine learning workflows, ETL processes, and LLM/RAG pipelines where understanding the input data before processing it is essential.

## Future Improvements

Possible extensions for future versions include:

* Support for CSV and JSON input
* More detailed data-quality statistics
* Configurable validation rules
* Better handling of complex or unhashable values
* Exporting reports to JSON
* Using the inspector as part of a larger data pipeline

These features are intentionally outside the scope of the current MVP.

## Project Status

Completed ✅

This project is part of my **AI Engineering Learning / Training Projects** and was created to strengthen Python and software engineering fundamentals through practical implementation.
