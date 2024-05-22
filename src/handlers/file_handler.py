import pickle
from src.modules.contact_book import ContactBook
from src.modules.note_book import NoteBook


# Contacts
def save_contacts_book(book: ContactBook, filename="addressbook.pkl") -> None:
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def get_contacts(filename="addressbook.pkl") -> ContactBook:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return ContactBook()


# Notes
def save_note_book(book: NoteBook, filename="notebook.pkl") -> None:
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def get_notes(filename="notebook.pkl") -> NoteBook:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return NoteBook()
