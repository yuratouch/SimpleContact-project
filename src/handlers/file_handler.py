import pickle
from src.modules.book import AddressBook

def save_to_file(book: AddressBook, filename="addressbook.pkl") -> None:  
    with open(filename, "wb") as file:
        pickle.dump(book, file)

def get_contacts(filename="addressbook.pkl") -> AddressBook:
    book = AddressBook()
    try:
        with open(filename, "rb") as file:
            book = pickle.load(file)
            return book
        
    except FileNotFoundError:
        return book
    