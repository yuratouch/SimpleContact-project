from src.handlers.notes_handler import note_show_all, note_add, note_change, note_delete, note_find
from src.utils.input_parser import parse_input
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from src.handlers.contacts_handler import (add_contact, add_phone, change_contact, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact, edit_phone, edit_address, edit_email,
                                           edit_birthday, show_contact)

comands_dict = {
    # "add-contact": add_contact,
    # "add-phone": add_phone,
    # "add-email": add_email,
    # "add-address": add_address,
    # "add-birthday": add_birthday,

    # "edit-contact": edit_contact,
    # "edit-phone": edit_phone,
    # "edit-address": edit_address,
    # "edit-email": edit_email,
    # "edit-birthday": edit_birthday,

    # "change": change_contact,
    # "phone": show_phone,
    # "show-birthday": show_birthday,
    # "birthdays": show_upcoming_birthdays,
    "note-add": note_add,
    "note-change": note_change,
    "note-find": note_find,
    "note-delete": note_delete,
    "note-show-all": note_show_all,
    "all": show_all,
    # "show-contact": show_contact,
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
