from src.utils.input_parser import parse_input
from src.handlers.file_handler import save_to_file, get_contacts
from src.handlers.contacts_handler import (add_contact, change_contact, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays)


def main():
    book = get_contacts()
    # TODO: Refactor books initialization. 
    # contact_book = get_contacts()
    # note_book = get_notes()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # TODO: Improvement. Optimize command checker (all commands in one collection(?)).

        if command in ["close", "exit"]:
            save_to_file(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            save_to_file(book)
            print(show_all())

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(show_upcoming_birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
