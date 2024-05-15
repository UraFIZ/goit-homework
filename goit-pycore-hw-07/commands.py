from models import AddressBook, Record
from utils import format_table
from upcoming_birthday_controller import UpcomingBirthday

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

def list_records(book: AddressBook):
    if not book.data:
        print("Address book is empty.")
        return
    
    headers = ["Name", "Phone Numbers", "Birthday"]
    rows = [[name, ', '.join(phone.value for phone in record.phones), str(record.birthday) ] for name ,record in book.data.items()]
    print(format_table(headers, rows))

def add_birthday(book: AddressBook, name: str, birthday: str):
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        print(f"Added birthday to record: {record}")
    else:
        print(f"No record found for name '{name}'")

def show_birthday(book: AddressBook, name: str):
    record = book.find(name)
    if record:
        if record.birthday:
            print(f"{name} has a birthday in {record.birthday}")
        else:
            print(f"{name} has no birthday date in the address book.")
    else:
        print(f"No birthday date found for name '{name}' in the address book.")

def get_upcoming_birthdays(book: AddressBook):
    birthday_handler = UpcomingBirthday()
    if not book.data:
        print("Address book is empty.")
        return

    birthday_data = [ { "name": name, "birthday": str(record.birthday), "phone": str(record.phones[0]) } for name, record in book.data.items() if record.birthday ]
    if not birthday_data:
        print("No birthdays in the address book.")
        return
    try:
        for item in birthday_handler.get_upcoming_birthdays(birthday_data):
            print(f"Congratulate {item['name']} on {item['congratulation_date']} at phone {item['phone']}")
    except Exception as e:
        print(e)
    



