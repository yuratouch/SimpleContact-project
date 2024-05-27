import os
from src.handlers.notes_handler import (note_show_all, note_add, note_change, note_delete,
                                        note_find_by_title, note_find_by_tag)
from src.handlers.contacts_handler import (add_contact, add_phone, show_phone,
                                           show_all, add_birthday, show_birthday,
                                           show_upcoming_birthdays, add_email, add_address,
                                           edit_contact_name, edit_phone, edit_address, edit_email,
                                           edit_birthday, show_contact, contact_delete)

comands_dict = {
    "contact-add": {
        "function": add_contact,
        "description": "Add a new contact with a name and phone number. Syntax: contact-add Name Phone",
    },
    "contact-add-phone": {
        "function": add_phone,
        "description": "Add an additional phone number to an existing contact. Syntax: contact-add-phone Name Phone",
    },
    "contact-add-birthday": {
        "function": add_birthday,
        "description": "Add a birthday to a contact. Syntax: contact-add-birthday Name Birthday",
    },
    "contact-add-email": {
        "function": add_email,
        "description": "Add an email address to a contact. Syntax: contact-add-email Name Email",
    },
    "contact-add-address": {
        "function": add_address,
        "description": "Add an address to a contact. Syntax: contact-add-address Name Address",
    },
    "contact-edit-name": {
        "function": edit_contact_name,
        "description": "Edit the name of a contact. Syntax: contact-edit-name Name new-Name",
    },
    "contact-edit-phone": {
        "function": edit_phone,
        "description": "Edit the phone number of a contact. Syntax: contact-edit-phone Name Phone new_phone",
    },
    "contact-edit-address": {
        "function": edit_address,
        "description": "Edit the address of a contact. Syntax: contact-edit-address Name Address new-Address",
    },
    "contact-edit-email": {
        "function": edit_email,
        "description": "Edit the email address of a contact. Syntax: contact-edit-email Name Email new-Email",
    },
    "contact-edit-birthday": {
        "function": edit_birthday,
        "description": "Edit the birthday of a contact. Syntax: contact-edit-birthday Name Birthday",
    },
    "contact-delete": {
        "function": contact_delete,
        "description": "Delete a contact. Syntax: contact-delete Name",
    },
    "contact-show": {
        "function": show_contact,
        "description": "Display information about a contact by name. Syntax: contact-show Name",
    },
    "contact-show-phone": {
        "function": show_phone,
        "description": "Display the phone number of a contact. Syntax: contact-show-phone Name",
    },
    "contact-show-birthday": {
        "function": show_birthday,
        "description": "Display the birthday of a contact. Syntax: contact-show-birthday Name",
    },
    "contact-birthdays": {
        "function": show_upcoming_birthdays,
        "description": "Show upcoming birthdays within a specified number of days. Syntax: contact-birthdays days_to",
    },
    "contact-show-all": {
        "function": show_all,
        "description": "Display information about all contacts. Syntax: contact-show-all",
    },

    "note-add": {
        "function": note_add,
        "description": "Add a new note with a title and content. Syntax: note-add Title Content",
    },
    "note-change": {
        "function": note_change,
        "description": "Change the content of an existing note. Syntax: note-change Title new_Content",
    },
    "note-find-by-title": {
        "function": note_find_by_title,
        "description": "Find a note by its title. Syntax: note-find-by-title Title",
    },
    "note-find-by-tag": {
        "function": note_find_by_tag,
        "description": "Find notes by a specific tag. Syntax: note-find-by-tag Tag",
    },
    "note-delete": {
        "function": note_delete,
        "description": "Delete a note by its title. Syntax: note-delete Title",
    },
    "note-show-all": {
        "function": note_show_all,
        "description": "Display all notes. Syntax: note-show-all",
    },
    "clear": {
        "function": lambda *_: os.system("clear"),
        "description": "Clear screen. Syntax: clear",
    },
    "help": {
        "function": lambda d: '\n'.join([f"{key:<25} - {value['description']}" for key, value in d.items()]),
        "description": "Show this message",
    },
    "exit": {
        "function": lambda args: "Good bye!",
        "description": "Exit the program",
    }
}
