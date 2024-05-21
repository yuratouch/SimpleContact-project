# TODO: Add new class NoteBook(Book)
# Class NoteBook should be duplicated from class AddressBook(UserDict)
# Class NoteBook has 4 methods: add, edit, delete, find
# Class ContactBook has custom __str__ method for the better instance presentation
# Class ContactBook inherited from class Book
# Class ContactBook uses UserDict functionality to store Notes

from src.modules.book import Book

class NoteBookBook(Book):
    # TODO: SC-20. Feature 6. Save Notes
    def add(self, note):
        self.data[note.name] = note

    # TODO: SC-22. Feature 8.1 Edit Notes functionality
    def edit():
        pass

    # TODO: SC-21. Feature 7. Find Notes functionality
    def find():
        pass

    # TODO: SC-23. Feature 8.2 Delete Notes functionality
    def delete():
        pass

    # TODO: SC-20. Feature 6. Save Notes
    def __str__():
        pass
