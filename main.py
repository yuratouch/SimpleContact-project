import os
from src.comands import comands_dict
from src.utils.command_completer import CommandCompleter
from src.utils.input_parser import parse_input
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from prompt_toolkit import prompt


def main():
    contact_book = get_contacts(save_contacts_book)
    note_book = get_notes(save_note_book)

    os.system("clear")
    print("Welcome to the assistant bot!")
    completer = CommandCompleter(comands_dict)

    while True:
        try:
            user_input = prompt("Enter a command: ", completer=completer)
            command, *args = parse_input(user_input)

            if command == "exit":
                print(comands_dict[command]["function"](args))
                break
            elif command == "help":
                print(comands_dict[command]["function"](comands_dict))
            elif command == "clear":
                comands_dict[command]["function"](comands_dict)
            elif command.startswith("note-"):
                print(comands_dict[command]["function"](args, note_book))
            elif command.startswith("contact-"):
                print(comands_dict[command]["function"](args, contact_book))
            else:
                print(f"Invalid command {command}.")

        except KeyboardInterrupt:
            print(comands_dict['exit']['function'](None))
            break
        except Exception as e:
            print(f"Invalid command {e}.")


if __name__ == "__main__":
    main()
