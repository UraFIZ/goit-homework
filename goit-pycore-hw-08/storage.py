from models import AddressBook
import pickle

class AddressBookStorage:
    def __init__(self, filename = "address_book.pkl"):
        self.filename = filename

    def save(self, book: AddressBook):
        if not book:
            return
        with open(self.filename, 'wb') as file:
            pickle.dump(book.to_dict(), file)

    def load(self) -> AddressBook:
        try:
            with open(self.filename, 'rb') as file:
                data = pickle.load(file)
                if not data:
                    return AddressBook()
                return AddressBook.from_dict(data)
        except (FileNotFoundError, pickle.UnpicklingError):
            return AddressBook()

