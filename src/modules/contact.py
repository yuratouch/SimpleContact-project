from src.modules.exceptions import BirthdayVerificationError, PhoneVerificationError, EmailVerificationError
from src.modules.name import Name
from src.modules.phone import Phone
from src.modules.birthday import Birthday
from src.modules.email import Email
from src.modules.address import Address


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None
        self.address = None
        self.email: Email|None = None

    def add_phone(self, phone) -> bool:
        try:
            phone_number = Phone(phone)
            self.phones.append(phone_number)
            return True
        except PhoneVerificationError as error_message:
            print(error_message)
            new_phone = input(
                "--- Type phone one more time or 'exit' to get back: ")  # TODO Use colorama here, some yellow color

            if new_phone != "exit":
                return self.add_phone(new_phone)

            return False

    def remove_phone(self, phone: str):
        self.phones.remove(self.find_phone(phone))

    def edit_name(self, name: str):
        self.name = Name(name)

    def edit_phone(self, old: str, new: str):
        if self.find_phone(old) is None:
            raise Exception(f"Phone not found: {old}")
        
        if self.find_phone(new):
            raise Exception(f"Phone already exist: {new}")

        try:
            phone_old = Phone(old)
            phone_new = Phone(new)
            for index in range(len(self.phones)):
                if self.phones[index].value == phone_old.value:
                    self.phones[index] = phone_new
        except PhoneVerificationError as error_message:
            print(error_message)
            new_phone = input(
                "--- Type phone one more time or 'exit' to get back: ")  # TODO Use colorama here, some yellow color

            if new_phone != "exit":
                return self.edit_phone(old, new_phone)
            
            return False

    def find_phone(self, phone_input: str):
        for phone in self.phones:
            if phone_input == phone.value:
                return phone

    def add_birthday(self, birthday: str):
        try:
            self.birthday = Birthday(birthday)
            return True
        except BirthdayVerificationError as error_message:
            print(error_message)
            new_birthday = input(
                "--- Type Birthday one more time or 'exit' to get back: ")  # TODO Use colorama here, some yellow color
            
            if new_birthday != "exit":
                return self.add_birthday(new_birthday)
            
            return False

    def add_email(self, email: str):
        try:
            self.email = Email(email)
            return True
        except EmailVerificationError as error_message:
            print(error_message)
            new_email = input(
                "--- Type Email one more time or 'exit' to get back: ")  # TODO Use colorama here, some yellow color

            if new_email != "exit":
                return self.add_email(new_email)

            return False

    def edit_email(self, new_email: str):
        if self.email and new_email == self.email.value:
            # TODO: change exception for this case (This email is already saved to this contact)
            raise Exception("This email is already saved to this contact")
        self.add_email(new_email)

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
