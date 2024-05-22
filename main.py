from src.handlers.notes_handler import note_show_all, note_add, note_change, note_delete, note_find
from src.utils.input_parser import parse_input
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from src.handlers.contacts_handler import (add_contact, change_contact, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address, show_contact, add_phone)

# TODO: add commands: help, 
comands_dict = {
    "contact-add": add_contact,
    "contact-phone": add_phone,
    "contact-phone-change": change_contact, 
    "contact-phone-show": show_phone,
    "contact-email": add_email,
    "contact-address": add_address,
    "contact-birthday": add_birthday,
    "contact-birthday-show": show_birthday,
    "contact-birthdays": show_upcoming_birthdays,
    "contact-show": show_contact,
    "note-add": note_add,
    "note-change": note_change,
    "note-find": note_find,
    "note-delete": note_delete,
    "note-show-all": note_show_all,
    "all": show_all,
}


def main():
    contact_book = get_contacts()
    note_book = get_notes()

    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_contacts_book(contact_book)
                save_note_book(note_book)
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command.startswith("note-"):
                print(comands_dict[command](args, note_book))
            elif command in comands_dict:
                print(comands_dict[command](args, contact_book))
            else:
                print(f"Invalid command {command}.")
        except Exception as e:
            print(f"Invalid command {e}.")


if __name__ == "__main__":
    main()
