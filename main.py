from src.handlers.notes_handler import note_show_all, note_add, note_change, note_delete, note_find
from src.utils.input_parser import parse_input
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from src.handlers.contacts_handler import (add_contact, add_phone, change_contact, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact, edit_phone, edit_address, edit_email,
                                           edit_birthday, show_contact)

# TODO: add commands: help, 
comands_dict = {
    "contact-add": add_contact,
    "contact-add-phone": add_phone,
    "contact-add-birthday": add_birthday,
    "contact-add-email": add_email,
    "contact-add-address": add_address,
    "contact-edit-phone": edit_phone,
    "contact-edit-contact": edit_contact,
    "contact-edit-address": edit_address,
    "contact-edit-email": edit_email,
    "contact-edit-birthday": edit_birthday,
    "contact-show": show_contact,
    "contact-show-phone": show_phone,
    "contact-show-birthday": show_birthday,
    "contact-birthdays": show_upcoming_birthdays,
    "note-add": note_add,
    "note-change": note_change,
    "note-find": note_find,
    "note-delete": note_delete,
    "note-show-all": note_show_all,
    "all": show_all, # TODO: Legacy. Check to change or remove
    "contact-change": change_contact, # TODO: Legacy. Check to change or remove
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
