from src.utils.input_parser import parse_input
from src.handlers.file_handler import save_to_file, get_contacts
from src.handlers.contacts_handler import (add_contact, add_phone, change_contact, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact, edit_phone, edit_address, edit_email,
                                           edit_birthday)

comands_dict = {
    "add-contact": add_contact,
    "add-phone": add_phone,
    "add-email": add_email,
    "add-address": add_address,
    "add-birthday": add_birthday,

    "edit-contact": edit_contact,
    "edit-phone": edit_phone,
    "edit-address": edit_address,
    "edit-email": edit_email,
    "edit-birthday": edit_birthday,

    "change": change_contact,
    "phone": show_phone,

    "show-birthday": show_birthday,
    "birthdays": show_upcoming_birthdays,
    "all": show_all,
}


def main():
    book = get_contacts()
    # TODO: Refactor books initialization. 
    # contact_book = get_contacts()
    # note_book = get_notes()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_to_file(book)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in comands_dict:
            print(comands_dict[command](args, book))
        else:
            print("Invalid command.")

    # TODO: add protection from ctrl+C. Because we will lost our data if app will close by this way


if __name__ == "__main__":
    main()
