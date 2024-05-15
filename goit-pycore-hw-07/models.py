
from collections import UserDict
from custom_exceptions import CustomeExceptions

from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not self.__validate(value):
            raise CustomeExceptions.NameError(f"Name '{value}' must be alphabetic")
        super().__init__(value)

    @staticmethod
    def __validate(value: str):
        return value.isalpha()

class Phone(Field):
    def __init__(self, value: str):
        if not self.__validate(value):
            raise CustomeExceptions.PhoneLengthError(f"Phone '{value}' must be 10 digits long")
        super().__init__(value)

    @staticmethod
    def __validate(value: str):
        return len(value) == 10 and value.isdigit()
    
    def __repr__(self):
        return f"Phone(number={self.value}"

class Birthday(Field):
    def __init__(self, value: str):
        if not self.__validate(value):
            raise CustomeExceptions.BirthdayError(f"Birthday '{value}' must be in format 'YYYY-MM-DD'")
        super().__init__(value)

    @staticmethod
    def __validate(value: str):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def add_phone(self, phone: str):
        if self.find_phone(phone):
            raise CustomeExceptions.PhoneAlreadyExists(f"Phone '{phone}' already exists in the record")
        self.phones.append(Phone(phone))
    
    def add_birthday(self, birthday: str):
        if not Birthday.validate(birthday):
            raise CustomeExceptions.BirthdayError(f"Birthday '{birthday}' must be in format 'YYYY-MM-DD'")
        self.birthday = Birthday(birthday)

    def remove_phone(self, phone: str):
        try:
            index = next(i for i, p in enumerate(self.phones) if p.value == phone)
            del self.phones[index]
        except StopIteration:
            raise CustomeExceptions.PhoneNotFound(f"Phone '{phone}' not found while trying to remove it")

    def edit_phone(self, old_phone: str, new_phone: str):
        if not Phone.validate(new_phone):
            raise CustomeExceptions.PhoneLengthError(f"Phone '{new_phone}' must be 10 digits long")
        try:
            phone_to_edit = next(p for p in self.phones if p.value == old_phone)
            phone_to_edit.value = new_phone
        except StopIteration:
            raise CustomeExceptions.PhoneNotFound(f"Phone '{old_phone}' not found while trying to edit it")

    def find_phone(self, phone: str):
        return next((p for p in self.phones if p.value == phone), None)
    
    def to_dict(self):
        result = {
            "phones": [phone.value for phone in self.phones]
        }
        if self.birthday:
            result["birthday"] = self.birthday.value
        return result

    def __str__(self):
            phones = '; '.join(p.value for p in self.phones)
            return f"Contact name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value if self.birthday else 'N/A'}"

    
    @classmethod
    def from_dict(cls, name, data):
        record = cls(name)
        for phone in data.get("phones", []):
            record.add_phone(phone)
        if "birthday" in data:
            record.add_birthday(data["birthday"])
        return record

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
    
    def to_dict(self):
        return {name: record.to_dict() for name, record in self.data.items()}
    
    @classmethod
    def from_dict(cls, data):
        address_book = cls()
        for name, record in data.items():
            address_book.add_record(Record.from_dict(name, record))
        return address_book
    
    
    
    
    
