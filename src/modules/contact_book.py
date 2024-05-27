from datetime import datetime, timedelta
from src.modules.book import Book
from src.modules.name import Name
from src.modules.contact import Contact
from tabulate import tabulate
import textwrap


class ContactBook(Book):
    data: dict[Name, Contact]

    def create(self, name: str) -> Contact:
        contact = Contact(name=name)
        self.add(contact)
        return contact

    def add(self, contact: Contact):
        self.data[contact.name] = contact

    def find(self, name: str) -> Contact:
        for contact_name, contact in self.data.items():
            if name == contact_name.value:
                return contact

    def rename(self, old_name: str, new_name: str):
        old_contact = None
        for contact_name, _ in self.data.items():
            if old_name == contact_name.value:
                old_contact = self.data.pop(contact_name)
                break
        if old_contact:
            old_contact.edit_name(new_name)
            self.add(old_contact)

    def delete(self, name):
        for contact_name, _ in self.data.items():
            if name == contact_name.value:
                self.data.pop(contact_name)
                break

    def get_upcoming_birthdays(self, next_days: int = 7) -> list:
        current_date = datetime.today().date()
        congratulations = []

        for contact_name, contact in self.data.items():
            if contact.birthday:
                contact_birthday = contact.birthday.birthday.date()
                birthday_this_year = contact_birthday.replace(year=current_date.year)

                if birthday_this_year < current_date:
                    continue

                if (birthday_this_year - current_date).days > int(next_days):
                    continue

                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                elif birthday_this_year.weekday() == 6:
                    congratulation_date = birthday_this_year + timedelta(days=1)
                else:
                    congratulation_date = birthday_this_year

                congratulations.append(
                    {"name": contact_name.value, "congratulation_date": congratulation_date.strftime("%d.%m.%Y")})

        return congratulations

    def __str__(self):
        wrapped_table = []
        values = self.data.values()

        if len(values) == 0:
            print("Empty")

        for contact in self.data.values():
            contact_attributes = [
                contact.name.value if contact.name.value else None,
                ", ".join(phone.value for phone in contact.phones) if contact.phones else None,
                contact.email.value if contact.email else None,
                contact.birthday.birthday.strftime("%d.%m.%Y") if contact.birthday else None,
                contact.address.value if contact.address else None
            ]
            wrapped_attributes = []

            for attribute in contact_attributes:
                if attribute:
                    wrapped_attributes.append(textwrap.fill(attribute, width=40))
                else:
                    wrapped_attributes.append(" ")

            wrapped_table.append(wrapped_attributes)
        res = "\n" + tabulate(wrapped_table, headers=["Name", "Phone", "Email", "Date", "Address"], tablefmt="grid")
        return res
    