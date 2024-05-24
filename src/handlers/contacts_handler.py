from datetime import datetime
from src.modules.contact_book import ContactBook
from src.handlers.error_handler import input_error
from src.utils.capitalizer import capitalize_name
from src.utils.update_text_color import update_text_color, EnumColoramaText

CONTACT_NOT_FOUND_MESSAGE = "Contact not found."


@input_error
@capitalize_name
def add_contact(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    contact = book.find(name)
    message = "Contact updated."

    if contact is None:
        contact = book.create(name)
        message = "Contact added."

    if phone:
        result_phone = contact.add_phone(phone)
        if not result_phone:
            message += " Phone didn't"

    book.save()
    return update_text_color(message, EnumColoramaText.SUCCESS)


@input_error
@capitalize_name
def add_phone(args: list, book: ContactBook) -> str:
    name, phone, *_ = args
    contact = book.find(name)
    message = "Contact updated."

    if contact is None:
        return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)

    contact.add_phone(phone)
    book.save()
    return update_text_color(message, EnumColoramaText.SUCCESS)


@input_error
@capitalize_name
def add_email(args: list, book: ContactBook) -> str:
    name, email, *_ = args
    contact = book.find(name)
    message = "Contact updated."

    if contact is None:
        return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)

    contact.add_email(email)
    book.save()
    return update_text_color(message, EnumColoramaText.SUCCESS)


@input_error
@capitalize_name
def add_address(args: list, book: ContactBook) -> str:
    name, *address_list = args
    address = " ".join(address_list)
    contact = book.find(name)
    message = "Contact updated."

    if contact is None:
        return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)

    contact.add_address(address)
    book.save()
    return update_text_color(message, EnumColoramaText.SUCCESS)


@input_error
@capitalize_name
def edit_contact_name(args: list, book: ContactBook) -> str:
    old_name, new_name = args
    contact = book.find(old_name)

    if contact:
        new_name = new_name.lower().capitalize()
        book.rename(old_name, new_name)
        book.save()
        message = "Name changed successfully."
        return update_text_color(message, EnumColoramaText.SUCCESS)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def edit_phone(args: list, book: ContactBook) -> str:
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(old_phone, new_phone)
        book.save()
        message = "Phone changed successfully."
        return update_text_color(message, EnumColoramaText.SUCCESS)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def edit_address(args: list, book: ContactBook) -> str:
    name, new_address = args
    contact = book.find(name)

    if contact:
        contact.edit_address(new_address)
        book.save()
        message = "Name changed successfully."
        return update_text_color(message, EnumColoramaText.SUCCESS)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def contact_delete(args: list, book: ContactBook) -> str:
    name, *_ = args
    contact = book.find(name)

    if contact:
        book.delete(name).save()
        message = "Contact deleted."
        return update_text_color(message, EnumColoramaText.SUCCESS)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def edit_email(args: list, book: ContactBook) -> str:
    name, new_email = args
    contact = book.find(name)

    if contact:
        contact.edit_email(new_email)
        book.save()
        message = "Email changed successfully."
        return update_text_color(message, EnumColoramaText.SUCCESS)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def show_phone(args: list, book) -> str:
    name = args[0]
    contact = book.find(name)

    if contact:
        return ", ".join(p.value for p in contact.phones)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def show_contact(args: list, book):
    name = args[0]
    contact = book.find(name)

    if contact:
        return contact
    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


def show_all(_: list, book: ContactBook) -> ContactBook:
    return book


@input_error
@capitalize_name
def add_birthday(args: list, book: ContactBook) -> str:
    name, date = args
    contact = book.find(name)

    if contact:
        contact.add_birthday(date)
        book.save()
        message = f"Birthday added for {name}."
        return update_text_color(message, EnumColoramaText.SUCCESS)
    else:
        return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@input_error
@capitalize_name
def edit_birthday(args: list, book: ContactBook) -> str:
    if len(args) < 2:
        return "Missing one or more arguments"
    name, date = args
    contact = book.find(name)

    if contact:
        contact.add_birthday(date)
        book.save()
        message = f"Birthday changed to {datetime.strftime(contact.birthday.birthday, "%d.%m.%Y")}"
        return update_text_color(message, EnumColoramaText.SUCCESS)
    else:
        return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


@capitalize_name
def show_birthday(args: list, book: ContactBook) -> str:
    name = args[0]
    contact = book.find(name)

    if contact:
        try:
            message = f"{name}'s birthday is {datetime.strftime(contact.birthday.birthday, "%d.%m.%Y")}"
            return update_text_color(message, EnumColoramaText.SUCCESS)
        except AttributeError:
            message = f"No record about {name}'s birthday."
            return update_text_color(message, EnumColoramaText.WARNING)

    return update_text_color(CONTACT_NOT_FOUND_MESSAGE, EnumColoramaText.WARNING)


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
