from src.modules.name import Name
from src.modules.exceptions import PhoneVerificationError
from src.modules.phone import Phone
from src.modules.birthday import Birthday


class Contact:
    def __init__(self, name):
        self.name = Name(name)
        self.phones:list[Phone] = []
        self.birthday = None

    # Recursive function to save the phone number.
    # It is called until the number is entered correctly
    def add_phone(self, phone) -> bool:
        try:
            phone_number = Phone(phone)
            self.phones.append(phone_number)
            return True
        except PhoneVerificationError as error_message:
            print(error_message)
            new_phone = input("Type phone one more time or 'exit' to get back: ") # TODO Use colorama here, some yellow color
            
            if new_phone != "exit":
                return self.add_phone(new_phone)
            
            return False

    def remove_phone(self, phone):
        self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old, new):
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

    def __str__(self):
        return (f"Contact name: {self.name.value},"
                f" phones: {'; '.join(p.value for p in self.phones)},"
                f" birthday: {self.birthday}")
