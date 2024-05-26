from src.handlers.notes_handler import note_show_all, note_add, note_change, note_delete, note_find
from src.handlers.file_handler import get_contacts, get_notes, save_contacts_book, save_note_book
from src.handlers.contacts_handler import (add_contact, add_phone, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact, edit_phone, edit_address, edit_email,
                                           edit_birthday, show_contact)

from InquirerPy import inquirer

comands_dict = {
    "New contact": add_contact,
    "Add Phone": add_phone,
    "Add Birthday": add_birthday,
    "Add Email": add_email,
    "Add Address": add_address,
    "Edit Phone": edit_phone,
    "Edit Contact": edit_contact,
    "Edit Address": edit_address,
    "Edit Email": edit_email,
    "Edit Birthday": edit_birthday,
    "Show Contact": show_contact,
    "Show Phone": show_phone,
    "Show Birthday": show_birthday,
    "Upcoming Birthdays": show_upcoming_birthdays,
    "Show All": show_all,

    "Add Note": note_add,
    "Change Note": note_change,
    "Find Note": note_find,
    "Delete Note": note_delete,
    "Show All Notes": note_show_all,
}

commands_requiring_args = {
    "New contact",
    "Add Phone",
    "Add Birthday",
    "Add Email",
    "Add Address",
    "Edit Phone",
    "Edit Contact",
    "Edit Address",
    "Edit Email",
    "Edit Birthday",
    "Show Contact",
    "Show Phone",
    "Show Birthday",
    "Upcoming Birthdays",
}


def edit_contact_actions(selected_contact, contact_book):
    while True:
        contact_action_edit = inquirer.select(
            message="Select an action for the contact:",
            choices=["<- back", "Change name", "Change phone", "Change birthday", "Change email", "Change address"],
            border=True,
            max_height=300
        ).execute()

        if contact_action_edit == "<- back":
            break

        if contact_action_edit == "Change name":
            print(edit_contact(selected_contact, contact_book))

        if contact_action_edit == "Change phone":
            edit_contact_change_phone_actions(selected_contact, contact_book)


def edit_contact_change_phone_actions(selected_contact, contact_book):
    phones = show_phone(selected_contact, contact_book)
    phones_list = [f"{phone.value}" for phone in phones]

    while True:
        old_phone_select = inquirer.select(
            message="Select a phone number:",
            choices=["<- back"] + phones_list,
            border=True,
            max_height=300
        ).execute()

        if old_phone_select == "<- back":
            break

        print(edit_phone(selected_contact, old_phone_select, contact_book))


def show_all_contacts(contact_book):
    while True:
        contacts = show_all([], contact_book).show_all()
        contact_list = [f"{contact.name}" for contact in contacts]

        selected_contact = inquirer.select(
            message="Select a contact to edit or delete:",
            choices=["<- back"] + contact_list,
            border=True,
            max_height=300
        ).execute()

        if selected_contact == "<- back":
            return

        while True:
            contact_action = inquirer.select(
                message="Select an action for the contact:",
                choices=["<- back", "Edit", "Delete"],
                border=True,
                max_height=300
            ).execute()

            if contact_action == "<- back":
                break

            if contact_action == "Edit":
                edit_contact_actions(selected_contact, contact_book)

            elif contact_action == "Delete":
                print(f"Delete {selected_contact}")


def contacts_menu(contact_book):
    while True:
        contact_action = inquirer.select(
            message="Select an action:",
            choices=["<- back", "Add", "Find", "Show all"],
            border=True,
            show_cursor=False,
            max_height=300
        ).execute()

        if contact_action == "<- back":
            break

        if contact_action == "Add":
            command_choices = ["<- back", "New contact", "Add Phone", "Add Birthday", "Add Email", "Add Address"]
            command = inquirer.select(
                message="Select a command:",
                choices=command_choices,
                border=True,
                max_height=300
            ).execute()

            if command == "<- back":
                continue

            args = []
            if command in commands_requiring_args:
                args_input = input(f"Enter arguments for {command}: ")
                args = args_input.split()

            print(comands_dict[command](args, contact_book))

        elif contact_action == "Find":
            value = show_contact(contact_book)
            print(value)

        elif contact_action == "Show all":
            show_all_contacts(contact_book)


def notes_menu(note_book):
    while True:
        command_choices = ["<- back", "Add Note", "Change Note", "Find Note", "Delete Note", "Show All Notes"]
        command = inquirer.select(
            message=f"Select a command:",
            choices=command_choices,
            border=True,
            max_height=300
        ).execute()

        if command == "<- back":
            break

        args = []

        if command in commands_requiring_args:
            args_input = input(f"Enter arguments for {command}: ")
            args = args_input.split()

        print(comands_dict[command](args, note_book))


def main():
    print("Welcome to the assistant bot!")

    contact_book = get_contacts()
    note_book = get_notes()

    while True:
        main_choice = inquirer.select(
            message="Select a category:",
            choices=["Contacts", "Notes", "Help", "Exit"],
            border=True,
            show_cursor=False,
            max_height=300
        ).execute()

        if main_choice == "Exit":
            save_contacts_book(contact_book)
            save_note_book(note_book)
            print("Good bye!")
            break

        if main_choice == "Help":
            print("Help")
            continue

        if main_choice == "Contacts":
            contacts_menu(contact_book)

        if main_choice == "Notes":
            notes_menu(note_book)


if __name__ == "__main__":
    main()
