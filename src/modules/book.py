# TODO: Refactor book.py.
# Class AddressBook should be renamed to ContactBook(Book) and moved to contact_book.py. 
# In this file class Book shold be created. 
# Class Book has 4 static methods: add, edit, delete, find
# Class Book is a parent for ContactBook and NoteBook
# Class Book inherited from UserDict

import pickle
from collections import UserDict
from datetime import datetime, timedelta


# START Code snippet for the Book class
class Book(UserDict):
    pass

    @staticmethod
    def add():
        pass

    @staticmethod
    def edit():
        pass

    @staticmethod
    def find():
        pass

    @staticmethod
    def delete():
        pass
# END Code snippet for the Book class


class AddressBook(UserDict):
    def add_record(self, contact):
        self.data[contact.name] = contact

    def find(self, name):
        for contact_name, contact in self.data.items():
            if name == contact_name.name.value:
                return contact
            
    def delete(self, name):
        for contact_name, _ in self.data.items():
            if name == contact_name.name.value:
                self.data.pop(contact_name)
                break

    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        congratulations = []

        for contact_name, contact in self.data.items():
            try:
                contact_birthday = contact.birthday.birthday.date()
                birthday_this_year = contact_birthday.replace(year=current_date.year)

                if birthday_this_year < current_date:
                    continue

                if (birthday_this_year - current_date).days > 7:
                    continue

                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year

                congratulations.append({"name": contact_name.name.value, "congratulation_date": congratulation_date.strftime("%d.%m.%Y")})
            except: AttributeError
        
        if len(congratulations) > 0:
            return congratulations
        else: 
            return "No birthdays in upcoming week"
        
    def __str__(self):
        book = "List of contacts:"
        for contact_name, contact in self.data.items():
            contact_phones = ','.join(p.value for p in contact.phones)
            try:
                contact_birthday = datetime.strftime(contact.birthday.birthday, "%d.%m.%Y")
            except AttributeError:
                contact_birthday = ""
            book = book + "\n" + contact_name.name.value + " [" + contact_phones + "]" + " " + contact_birthday
        return book
