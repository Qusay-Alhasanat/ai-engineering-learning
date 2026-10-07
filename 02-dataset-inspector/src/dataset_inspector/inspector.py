def validate_dataset(dataset: list[dict]) -> bool:
    if not isinstance(dataset, list):
        return False

    if not dataset:
        return False

    for record in dataset:
        if not isinstance(record, dict):
            return False

    return True


def get_shape(dataset: list[dict]) -> tuple[int, int]:
    records = len(dataset)

    fields = set()

    for record in dataset:
        fields.update(record.keys())

    return records, len(fields)


def get_fields(dataset: list[dict]) -> list[str]:
    fields = []
    seen = set()

    for record in dataset:
        for field in record:
            if field not in seen:
                seen.add(field)
                fields.append(field)

    return fields


def extract_field(dataset: list[dict], field: str) -> dict:
    values = []
    missing_fields = []
    none_values = []

    for index, record in enumerate(dataset):
        if field not in record:
            missing_fields.append(index)
        else:
            value = record[field]
            values.append(value)

            if value is None:
                none_values.append(index)

    return {
        "values": values,
        "missing_fields": missing_fields,
        "none_values": none_values,
    }


def analyze_field(field_data: dict) -> dict:
    values = field_data["values"]

    types = set()

    for value in values:
        if value is not None:
            types.add(type(value))

    if not types:
        field_type = "no_data"
    elif len(types) == 1:
        field_type = types.pop().__name__
    else:
        field_type = "mixed"

    unique_values = set()

    for value in values:
        if value is not None:
            unique_values.add(value)

    return {
        "type": field_type,
        "missing": len(field_data["missing_fields"]),
        "none": len(field_data["none_values"]),
        "unique": len(unique_values),
    }


def generate_report(dataset: list[dict]) -> dict:
    records, fields_count = get_shape(dataset)
    fields = get_fields(dataset)

    field_details = {}

    for field in fields:
        field_data = extract_field(dataset, field)
        analysis = analyze_field(field_data)
        field_details[field] = analysis

    return {
        "records": records,
        "fields": fields_count,
        "field_details": field_details,
    }


def inspect_dataset(dataset: list[dict]) -> dict:
    if not validate_dataset(dataset):
        return {
            "valid": False,
            "error": "Invalid dataset format",
        }

    report = generate_report(dataset)

    return {
        "valid": True,
        "report": report,
    }
