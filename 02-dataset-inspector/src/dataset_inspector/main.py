import argparse

from dataset_inspector.inspector import inspect_dataset


def format_report(result: dict) -> str:
    if not result["valid"]:
        return f"Error: {result['error']}"

    report = result["report"]

    lines = [
        "Dataset Inspection Report",
        "=========================",
        f"Records: {report['records']}",
        f"Fields: {report['fields']}",
        "",
    ]

    for field, details in report["field_details"].items():
        lines.extend(
            [
                field,
                f"  Type: {details['type']}",
                f"  Missing: {details['missing']}",
                f"  None: {details['none']}",
                f"  Unique: {details['unique']}",
                "",
            ]
        )

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a dataset and generate a data-quality report."
    )

    parser.add_argument(
        "--version",
        action="version",
        version="0.1.0",
    )

    parser.parse_args()

    dataset = [
        {"name": "Qusay", "age": 25, "country": "Palestine"},
        {"name": "Ahmad", "age": 30, "country": "Jordan"},
        {"name": "Sara", "country": "Palestine"},
        {"name": "Omar", "age": "28", "country": "Egypt"},
    ]

    result = inspect_dataset(dataset)

    print(format_report(result))


if __name__ == "__main__":
    main()
