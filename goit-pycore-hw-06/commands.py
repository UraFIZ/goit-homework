from models import AddressBook, Record

def add_record(book: AddressBook, name: str, phone: str):
    record = book.find(name)
    if record:
        record.add_phone(phone)
        print(f"Added phones to existing record: {record}")
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        print(f"Added new record: {record}")

def edit_record(book: AddressBook, name: str, old_phone: str, new_phone: str):
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        print(f"Edited record: {record}")
    else:
        print(f"No record found for name '{name}'")

def delete_record(book: AddressBook, name: str):
    book.delete(name)
    print(f"Deleted record for name '{name}'")

def find_record(book: AddressBook, name: str):
    record = book.find(name)
    if record:
        print(record)
    else:
        print(f"No record found for name '{name}'")

