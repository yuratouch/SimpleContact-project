from src.handlers.notes_handler import note_show_all, note_add, note_change, note_delete, note_find_by_title, note_find_by_tag
from src.utils.command_completer import CommandCompleter
from src.utils.input_parser import parse_input
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from src.handlers.contacts_handler import (add_contact, add_phone, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact_name, edit_phone, edit_address, edit_email,
                                           edit_birthday, show_contact, contact_delete)

from prompt_toolkit import prompt

comands_dict = {
    "contact-add": add_contact,
    "contact-add-phone": add_phone,
    "contact-add-birthday": add_birthday,
    "contact-add-email": add_email,
    "contact-add-address": add_address,
    "contact-edit-name": edit_contact_name,
    "contact-edit-phone": edit_phone,
    "contact-edit-address": edit_address,
    "contact-edit-email": edit_email,
    "contact-edit-birthday": edit_birthday,
    "contact-delete": contact_delete,
    "contact-show": show_contact,
    "contact-show-phone": show_phone,
    "contact-show-birthday": show_birthday,
    "contact-birthdays": show_upcoming_birthdays,
    "contact-show-all": show_all,

    "note-add": note_add,
    "note-change": note_change,
    "note-find-by-title": note_find_by_title,
    "note-find-by-tag": note_find_by_tag,
    "note-delete": note_delete,
    "note-show-all": note_show_all,

    "help": lambda args, book: "help",
    "exit": lambda args: "Good bye!",
}

comands_help_dict = {
    "contact-add": "Add a new contact with a name and phone number. Syntax: contact-add Name Phone",
    "contact-add-phone": "Add an additional phone number to an existing contact. Syntax: contact-add-phone Name Phone",
    "contact-add-birthday": "Add a birthday to a contact. Syntax: contact-add-birthday Name Birthday",
    "contact-add-email": "Add an email address to a contact. Syntax: contact-add-email Name Email",
    "contact-add-address": "Add an address to a contact. Syntax: contact-add-address Name Address",
    "contact-edit-name": "Edit the name of a contact. Syntax: contact-edit-name Name new-Name",
    "contact-edit-phone": "Edit the phone number of a contact. Syntax: contact-edit-phone Name Phone new_phone",
    "contact-edit-address": "Edit the address of a contact. Syntax: contact-edit-address Name Address new-Address",
    "contact-edit-email": "Edit the email address of a contact. Syntax: contact-edit-email Name Email new-Email",
    "contact-edit-birthday": "Edit the birthday of a contact. Syntax: contact-edit-birthday Name Birthday",
    "contact-delete": "Delete a contact. Syntax: contact-delete Name",
    "contact-show": "Display information about a contact by name. Syntax: contact-show Name",
    "contact-show-phone": "Display the phone number of a contact. Syntax: contact-show-phone Name",
    "contact-show-birthday": "Display the birthday of a contact. Syntax: contact-show-birthday Name",
    "contact-birthdays": "Show upcoming birthdays within a specified number of days. Syntax: contact-birthdays days_to",
    "contact-show-all": "Display information about all contacts. Syntax: contact-show-all",

    "note-add": "Add a new note with a title and content. Syntax: note-add Title Content",
    "note-change": "Change the content of an existing note. Syntax: note-change Title new_Content",
    "note-find-by-title": "Find a note by its title. Syntax: note-find-by-title Title",
    "note-find-by-tag": "Find notes by a specific tag. Syntax: note-find-by-tag Tag",
    "note-delete": "Delete a note by its title. Syntax: note-delete Title",
    "note-show-all": "Display all notes. Syntax: note-show-all",

    "help": "Display a list of available commands and their descriptions. Syntax: help",
    "exit": "Terminate the session and exit the application. Syntax: exit",
}


def main():
    contact_book = get_contacts(save_contacts_book)
    note_book = get_notes(save_note_book)

    print("Welcome to the assistant bot!")
    completer = CommandCompleter(comands_dict)

    while True:
        try:
            user_input = prompt("Enter a command: ", completer=completer)
            command, *args = parse_input(user_input)

            if command == "exit":
                print(comands_dict[command](args))
                break
            if command == "help":
                print("Help")
            elif command.startswith("note-"):
                print(comands_dict[command](args, note_book))
            elif command.startswith("contact-"):
                print(comands_dict[command](args, contact_book))
            else:
                print(f"Invalid command {command}.")

        except KeyboardInterrupt:
            print(comands_dict['exit'](None))
            break
        except Exception as e:
            print(f"Invalid command {e}.")


if __name__ == "__main__":
    main()
