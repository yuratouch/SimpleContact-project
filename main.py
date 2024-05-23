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
    "exit": lambda args, book: "exit",
}


def main():
    contact_book = get_contacts()
    note_book = get_notes()

    print("Welcome to the assistant bot!")
    completer = CommandCompleter(comands_dict)

    while True:
        try:
            user_input = prompt("Enter a command: ", completer=completer)
            command, *args = parse_input(user_input)

            if command == "exit":
                save_contacts_book(contact_book)
                save_note_book(note_book)
                print("Good bye!")
                break
            elif command == "help":
                print("Help")
            elif command.startswith("note-"):
                print(comands_dict[command](args, note_book))
            elif command.startswith("contact-"):
                print(comands_dict[command](args, contact_book))
            else:
                print(f"Invalid command {command}.")
        except Exception as e:
            print(f"Invalid command {e}.")


if __name__ == "__main__":
    main()
