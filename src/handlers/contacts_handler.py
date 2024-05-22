from datetime import datetime
from src.handlers.error_handler import input_error
from src.modules.contact import Contact
from src.modules.contact_book import ContactBook
from src.modules.phone import Phone
from src.modules.birthday import Birthday
from src.modules.exceptions import PhoneVerificationError


# TODO: Improvement. Review error decorator for all functions

@input_error
def add_contact(args: list, book) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Contact(name)
        book.add(record)
        message = "Contact added."

    if phone:
        result_phone = record.add_phone(phone)
        if not result_phone:
            message += " Phone didn't"

    return message


@input_error
def change_contact(args: list, book) -> str:
    name, old, new = args
    record = book.find(name)

    if record:
        for index in range(len(record.phones)):
            if record.phones[index].phone == old:
                try:
                    record.phones[index] = Phone(new)
                    return "Contact updated."
                except PhoneVerificationError as e:
                    return e.message

        return f"Contact {name} does not have entered phone number."

    return "Contact not found."


def show_phone(args: list, book) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        return ", ".join(p.value for p in record.phones)

    return "Contact not found."

@input_error
def show_contact(args: list, book):
    name = args[0]
    contact = book.find(name)
    if contact:
        return contact
    return "Contact not found."

def show_all(_: list, book: ContactBook) -> str:
    res = "\n".join(
        f"{record.name.value}{f"({record.birthday.value})" if record.birthday and record.birthday.value else ""}: "
        f"{", ".join(phone.value for phone in record.phones) if record.phones else "The contact has no phone numbers"}"
        for record in book.values()
    )
    return res


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


def show_birthday(args: list, book) -> str:
    name = args[0]
    record = book.find(name)

    if record:
        try:
            return f"{name}'s birthday is {datetime.strftime(record.birthday.birthday, "%d.%m.%Y")}"
        except AttributeError:
            return f"No record about {name}'s birthday."

    return "Contact not found."


def show_upcoming_birthdays(args:list, contact_book:ContactBook) -> str:
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
        result = f"In the next 7 days, birthdays will have:\n"

        for birthday in upcoming_birthdays:
            result += f"{birthday['name']}, congratulation date - {birthday['congratulation_date']}\n"
        
        return result
