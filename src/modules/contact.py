from src.modules.name import Name
from src.modules.exceptions import (PhoneAlreadyExistsError, PhoneNotFoundError)
from src.modules.phone import Phone
from src.modules.birthday import Birthday
from src.modules.email import Email
from src.modules.address import Address


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.email = None

    def add_phone(self, phone: str):
        existing_phone = self.find_phone(phone)
        if existing_phone is None:
            self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old, new):
        if self.find_phone(old) is None:
            raise PhoneNotFoundError(old)

        if self.find_phone(new):
            raise PhoneAlreadyExistsError(new)

        for index in range(len(self.phones)):
            if self.phones[index].phone == old:
                self.phones[index] = Phone(new)

    def find_phone(self, phone_input):
        for phone in self.phones:
            if phone_input == phone.phone:
                return phone

    def add_birthday(self, birthday):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(e)

    def add_email(self, email):
        try:
            self.email = Email(email)
        except ValueError as e:
            print(e)

    def add_address(self, address):
        try:
            self.address = Address(address)
        except ValueError as e:
            print(e)

    def __str__(self):
        return (f"Contact name: {self.name.value},"
                f" phones: {'; '.join(p.value for p in self.phones)},"
                f" birthday: {self.birthday}"
                f" email: {self.email}"
                f" address: {self.address}")
