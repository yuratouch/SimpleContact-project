from datetime import datetime
from src.handlers.error_handler import input_error
from src.modules.contact_book import ContactBook
from src.modules.birthday import Birthday
from src.utils.capitalizer import capitalize_name


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
def add_phone(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_phone(phone)
    return "Contact updated."


@capitalize_name
@input_error
def add_email(args: list, book: ContactBook) -> str:
    name, email, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_email(email)
    return "Contact updated."


@capitalize_name
@input_error
def add_address(args: list, book: ContactBook) -> str:
    name, *address_list = args
    address = " ".join(address_list)
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_address(address)
    return "Contact updated."


@capitalize_name
@input_error
def edit_contact(args: list, book: ContactBook) -> str:
    old_name, new_name = args
    contact = book.find(old_name)

    if contact:
        new_name = new_name.lower().capitalize()
        book.rename(old_name, new_name)

        return f"Name changed successfully."

    return "Contact not found."


@capitalize_name
@input_error
def edit_phone(args: list, book: ContactBook) -> str:
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(old_phone, new_phone)
        return f"Phone changed successfully."
    return "Contact not found."


@capitalize_name
@input_error
def edit_address(args: list, book: ContactBook) -> str:
    name, new_address = args
    contact = book.find(name)

    if contact:
        contact.edit_address(new_address)
        return f"Name changed successfully."
    return "Contact not found."


@capitalize_name
@input_error
def edit_email(args: list, book: ContactBook) -> str:
    name, new_email = args
    contact = book.find(name)

    if contact:
        contact.edit_email(new_email)
        return f"Email changed successfully."
    return "Contact not found."


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
        f"{f" | Email: {record.email.value}" if record.email and record.email.value else ""}"
        f"{f" | Address:  {record.address.value}" if record.address and record.address.value else ""}"
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
def edit_birthday(args: list, book) -> str:
    if len(args) < 2:
        return "Missing one or more arguments"
    name, date = args
    record = book.find(name)

    if record:
        try:
            record.birthday = Birthday(date)
            return f"Birthday changed to {record.birthday}."
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
