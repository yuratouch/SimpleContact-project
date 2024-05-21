from datetime import datetime, timedelta
from src.modules.book import Book
from src.modules.contact import Contact


class ContactBook(Book):
    def add(self, contact):
        self.data[contact.name] = contact

    # TODO: Add edit method for ContactBook / SC-9. Feature-1. Save contacts.
    def edit(self, contact):
        pass

    def find(self, name):
        for contact_name, contact in self.data.items():
            if name == contact_name.name.value:
                return contact

    def delete(self, name):
        for contact_name, _ in self.data.items():
            if name == contact_name.name.value:
                self.data.pop(contact_name)
                break

    # TODO: Add extra parameter days_to for method get_upcoming_birthdays
    # def get_upcoming_birthdays(self, days_to: int = 7):
    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        congratulations = []

        for contact_name, contact in self.data.items():
            try:
                contact_birthday = contact.birthday.birthday.date()
                birthday_this_year = contact_birthday.replace(year=current_date.year)

                if birthday_this_year < current_date:
                    continue

                # TODO: Change static value to days_to parameter
                # if (birthday_this_year - current_date).days > days_to:
                if (birthday_this_year - current_date).days > 7:
                    continue

                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year

                congratulations.append(
                    {"name": contact_name.name.value, "congratulation_date": congratulation_date.strftime("%d.%m.%Y")})
            except AttributeError:
                return "Error"

        if len(congratulations) > 0:
            return congratulations
        else:
            return "No birthdays in upcoming week"

    # TODO: Update __str__ method. show list of contacts + days_to 
    def __str__(self):
        contacts = "List of contacts:"
        for contact_name, contact in self.data.items():
            contact_phones = ','.join(p.value for p in contact.phones)
            try:
                contact_birthday = datetime.strftime(contact.birthday.birthday, "%d.%m.%Y")
            except AttributeError:
                contact_birthday = ""
            contacts = contacts + "\n" + contact_name.name.value + " [" + contact_phones + "]" + " " + contact_birthday
        return contacts
