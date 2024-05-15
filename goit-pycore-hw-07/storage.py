import json
from models import AddressBook

class AddressBookStorage:
    def __init__(self, filename = "address_book.json"):
        self.filename = filename

    def save(self, book: AddressBook):
        with open(self.filename, 'w') as file:
            json.dump(book.to_dict(), file)

    def load(self) -> AddressBook:
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                if not data:
                    return AddressBook()
                return AddressBook.from_dict(data)
        except (FileNotFoundError, json.JSONDecodeError):
            return AddressBook()
