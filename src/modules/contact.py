from src.modules.name import Name
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

    def remove_phone(self, phone: str):
        self.phones.remove(self.find_phone(phone))

    def edit_name(self, name: str):
        self.name = Name(name)

    def edit_phone(self, old: str, new: str):
        if self.find_phone(old) is None:
            # TODO: change exception for this case (old phone not found)
            raise Exception(f"Phone not found: {old}")

        if self.find_phone(new):
            # TODO: change exception for this case (new phone already exist)
            raise Exception(f"Phone already exist: {new}")

        for index in range(len(self.phones)):
            if self.phones[index].phone == old:
                self.phones[index] = Phone(new)

    def find_phone(self, phone_input: str):
        for phone in self.phones:
            if phone_input == phone.phone:
                return phone

    def add_birthday(self, birthday: str):
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(e)

    def add_email(self, email: str):
        try:
            self.email = Email(email)
        except ValueError as e:
            print(e)

    def edit_email(self, new_email: str):
        if self.email and new_email == self.email.value:
            # TODO: change exception for this case (This email is already saved to this contact)
            raise Exception("This email is already saved to this contact")
        self.email = Email(new_email)

    def add_address(self, address: str):
        self.address = Address(address)

    def edit_address(self, new_address: str):
        if self.address and new_address == self.address.value:
            # TODO: change exception for this case (This address is already saved to this contact)
            raise Exception(new_address)

        self.address = Address(new_address)


    def __str__(self):
        return (f"Contact name: {self.name.value},"
                f" phones: {'; '.join(p.value for p in self.phones)},"
                f" birthday: {self.birthday}"
                f" email: {self.email}"
                f" address: {self.address}")
