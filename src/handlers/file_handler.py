import pickle
from src.modules.contact_book import ContactBook


def save_to_file(book: ContactBook, filename="addressbook.pkl") -> None:
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def get_contacts(filename="addressbook.pkl") -> ContactBook:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return ContactBook()
