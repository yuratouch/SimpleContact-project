from datetime import datetime
from src.handlers.error_handler import input_error
from src.modules.contact import Contact
from src.modules.contact_book import ContactBook
from src.modules.phone import Phone
from src.modules.birthday import Birthday
from src.modules.exceptions import PhoneVerificationError
from src.utils.input_parser import capitalize_name
from src.handlers.file_handler import save_to_file


# TODO: Improvement. Review error decorator for all functions

@capitalize_name
@input_error
def add_contact(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = book.create(name)
        message = "Contact added."

    if phone:
        record.add_phone(phone)

    return message


@capitalize_name
@input_error
def change_contact(args: list, book: ContactBook) -> str:
    name, old, new = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(old, new)

        return f"Number changed successfully."

    return "Contact not found."


@capitalize_name
def show_phone(args: list, book) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        return ", ".join(p.value for p in record.phones)

    return "Contact not found."


def show_all(_: list, book: ContactBook) -> str:
    res = "\n".join(
        f"{record.name.value}{f"({record.birthday.value})" if record.birthday and record.birthday.value else ""}: "
        f"{", ".join(phone.value for phone in record.phones) if record.phones else "The contact has no phone numbers"}"
        for record in book.values()
    )
    return res


@capitalize_name
def add_birthday(args: list, book) -> str:
    name, date = args
    record = book.find(name)

    if record:
        try:
            record.birthday = Birthday(date)
            return f"Birthday added for {name}."
        except ValueError:
            return "Invalid date format. Please enter date in format DD.MM.YYYY"
    else:
        return "Contact not found."


@capitalize_name
def show_birthday(args: list, book) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        try:
            return f"{name}'s birthday is {datetime.strftime(record.birthday.birthday, "%d.%m.%Y")}"
        except AttributeError:
            return f"No record about {name}'s birthday."

    return "Contact not found."


def show_upcoming_birthdays(_: list, book) -> list:
    return book.get_upcoming_birthdays()


def save_book(_: list, book):
    save_to_file(book)
