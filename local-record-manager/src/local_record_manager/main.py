from copy import deepcopy
from pathlib import Path

from local_record_manager.records import (
    create_record,
    list_records,
    find_record,
    update_record,
    delete_record,
)
from local_record_manager.storage import load_data, save_data


DATA_FILE = Path("records.json")


def show_menu() -> None:
    print("\n=== Local Record Manager ===")
    print("1. Add record")
    print("2. List records")
    print("3. Find record")
    print("4. Update record")
    print("5. Delete record")
    print("0. Exit")


def show_record(record: dict) -> None:
    print(f"ID: {record['id']}")
    print(f"Title: {record['title']}")
    print(f"Description: {record['description']}")
    print(f"Status: {record['status']}")


def show_all_records(records: list[dict]) -> None:
    if not records:
        print("No records found.")
        return

    for record in records:
        print("-" * 30)
        show_record(record)


def get_record_id() -> int:
    raw_id = input("Enter record ID: ").strip()

    try:
        record_id = int(raw_id)
    except ValueError:
        raise ValueError("ID must be a valid integer.")

    if record_id <= 0:
        raise ValueError("ID must be a positive integer.")

    return record_id


def main() -> None:
    try:
        records, last_id = load_data(DATA_FILE)
    except (OSError, ValueError) as error:
        print(f"Error loading data: {error}")
        return

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Enter title: ")
                description = input("Enter description (optional): ")

                backup_records = deepcopy(records)
                backup_last_id = last_id

                try:
                    record, last_id = create_record(
                        records,
                        last_id,
                        title,
                        description,
                    )

                    save_data(DATA_FILE, records, last_id)

                except (ValueError, OSError):
                    records[:] = backup_records
                    last_id = backup_last_id
                    raise

                print("Record added successfully.")

            elif choice == "2":
                show_all_records(list_records(records))

            elif choice == "3":
                record_id = get_record_id()
                record = find_record(records, record_id)

                if record is None:
                    print("Record not found.")
                else:
                    show_record(record)

            elif choice == "4":
                record_id = get_record_id()
                record = find_record(records, record_id)

                if record is None:
                    print("Record not found.")
                    continue

                print("Leave a field empty to keep its current value.")
                title = input("New title: ")
                description = input("New description: ")
                status = input("New status (pending/in_progress/completed): ")

                backup_records = deepcopy(records)
                backup_last_id = last_id

                try:
                    updated_record = update_record(
                        records,
                        record_id,
                        title=title if title else None,
                        description=description if description else None,
                        status=status if status else None,
                    )

                    save_data(DATA_FILE, records, last_id)

                except (ValueError, OSError):
                    records[:] = backup_records
                    last_id = backup_last_id
                    raise

                print("Record updated successfully.")
                show_record(updated_record)

            elif choice == "5":
                record_id = get_record_id()
                record = find_record(records, record_id)

                if record is None:
                    print("Record not found.")
                    continue

                backup_records = deepcopy(records)
                backup_last_id = last_id

                try:
                    deleted_record = delete_record(records, record_id)
                    save_data(DATA_FILE, records, last_id)

                except (ValueError, OSError):
                    records[:] = backup_records
                    last_id = backup_last_id
                    raise

                print(f"Record {deleted_record['id']} deleted successfully.")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose from the menu.")

        except (ValueError, OSError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
