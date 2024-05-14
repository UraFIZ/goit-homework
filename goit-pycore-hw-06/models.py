from collections import UserDict
from phone_exceptions import PhoneExceptions

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise PhoneExceptions.NameError(f"Name '{value}' must be alphabetic")
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        return value.isalpha()

class Phone(Field):
    def __init__(self, value: str):
        if not self.validate(value):
            raise PhoneExceptions.PhoneLengthError(f"Phone '{value}' must be 10 digits long")
        super().__init__(value)

    @staticmethod
    def validate(value: str):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        try:
            index = next(i for i, p in enumerate(self.phones) if p.value == phone)
            del self.phones[index]
        except StopIteration:
            raise PhoneExceptions.PhoneNotFound(f"Phone '{phone}' not found while trying to remove it")

    def edit_phone(self, old_phone: str, new_phone: str):
        try:
            phone_to_edit = next(p for p in self.phones if p.value == old_phone)
            phone_to_edit.value = new_phone
        except StopIteration:
            raise PhoneExceptions.PhoneNotFound(f"Phone '{old_phone}' not found while trying to edit it")

    def find_phone(self, phone: str):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        try:
            del self.data[name]
        except KeyError:
            raise KeyError(f"Record '{name}' not found while trying to delete it")

    def __str__(self):
        return f"Address book: {', '.join(self.data.keys())}"
    
    
    
