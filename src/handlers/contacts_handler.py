from datetime import datetime
from src.modules.contact_book import ContactBook
from src.modules.birthday import Birthday
from src.handlers.error_handler import input_error
from src.utils.capitalizer import capitalize_name


# TODO: Improvement. Review error decorator for all functions

@input_error
@capitalize_name
def add_contact(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = book.create(name)
        message = "Contact added."

    if phone:
        result_phone = record.add_phone(phone)
        if not result_phone:
            message += " Phone didn't"

    book.save()
    return message


@input_error
@capitalize_name
def add_phone(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_phone(phone)
    book.save()
    return "Contact updated."


@input_error
@capitalize_name
def add_email(args: list, book: ContactBook) -> str:
    name, email, *_ = args
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_email(email)
    book.save()
    return "Contact updated."


@input_error
@capitalize_name
def add_address(args: list, book: ContactBook) -> str:
    name, *address_list = args
    address = " ".join(address_list)
    record = book.find(name)

    if record is None:
        return "Contact not found."

    record.add_address(address)
    book.save()
    return "Contact updated."


@input_error
@capitalize_name
def edit_contact_name(args: list, book: ContactBook) -> str:
    old_name, new_name = args
    contact = book.find(old_name)

    if contact:
        new_name = new_name.lower().capitalize()
        book.rename(old_name, new_name)
        book.save()
        return f"Name changed successfully."

    return "Contact not found."


@input_error
@capitalize_name
def edit_phone(args: list, book: ContactBook) -> str:
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(old_phone, new_phone)
        book.save()
        return f"Phone changed successfully."

    return "Contact not found."


@input_error
@capitalize_name
def edit_address(args: list, book: ContactBook) -> str:
    name, new_address = args
    contact = book.find(name)

    if contact:
        contact.edit_address(new_address)
        book.save()
        return f"Name changed successfully."

    return "Contact not found."


@input_error
@capitalize_name
def contact_delete(args: list, book: ContactBook) -> str:
    name, *_ = args
    contact = book.find(name)

    if contact:
        book.delete(name).save()
        return f"Contact delete."

    return "Contact not found."


@input_error
@capitalize_name
def edit_email(args: list, book: ContactBook) -> str:
    name, new_email = args
    contact = book.find(name)

    if contact:
        contact.edit_email(new_email)
        book.save()
        return f"Email changed successfully."

    return "Contact not found."


@input_error
@capitalize_name
def show_phone(args: list, book) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        return ", ".join(p.value for p in record.phones)

    return "Contact not found."


@input_error
@capitalize_name
def show_contact(args: list, book):
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact
    return "Contact not found."


def show_all(_: list, book: ContactBook) -> str:
    return book


@input_error
@capitalize_name
def add_birthday(args: list, book: ContactBook) -> str:
    name, date = args
    record = book.find(name)

    if record:
        record.add_birthday(date)
        book.save()
        return f"Birthday added for {name}."
    else:
        return "Contact not found."


@input_error
@capitalize_name
def edit_birthday(args: list, book: ContactBook) -> str:
    if len(args) < 2:
        return "Missing one or more arguments"
    name, date = args
    record = book.find(name)

    if record:
        record.add_birthday(date)
        book.save()
        return f"Birthday changed to {datetime.strftime(record.birthday.birthday, "%d.%m.%Y")}"
    else:
        return "Contact not found."


@capitalize_name
def show_birthday(args: list, book: ContactBook) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        try:
            return f"{name}'s birthday is {datetime.strftime(record.birthday.birthday, "%d.%m.%Y")}"
        except AttributeError:
            return f"No record about {name}'s birthday."

    return "Contact not found."


def show_upcoming_birthdays(args: list, contact_book: ContactBook) -> str:
    try:
        next_days = args[0]

        if int(next_days) <= 0:
            return "Minimum days range is 1. Please enter valid value."

        upcoming_birthdays = contact_book.get_upcoming_birthdays(next_days)
        result = f"In the next {next_days} days, birthdays will have:\n"
        for birthday in upcoming_birthdays:
            result += f"{birthday['name']}, congratulation date - {birthday['congratulation_date']}\n"

        if len(upcoming_birthdays) > 0:
            return result
        else:
            return f"No upcoming birthdays in the next {next_days} days"

    except IndexError:
        upcoming_birthdays = contact_book.get_upcoming_birthdays()
        result = f"No upcoming birthdays in the next 7 days"

        if len(upcoming_birthdays) > 0:
            result = f"In the next 7 days, birthdays will have:\n"
            for birthday in upcoming_birthdays:
                result += f"{birthday['name']}, congratulation date - {birthday['congratulation_date']}\n"
        else:
            return result
