from datetime import datetime, timedelta
from src.modules.book import Book
from src.modules.contact import Contact


class ContactBook(Book):
    def create(self, name: str) -> Contact:
        contact = Contact(name=name)
        self.add(contact)
        return contact

    def show_all(self):
        return self.data.values()

    def add(self, contact: Contact):
        self.data[contact.name] = contact

    def find(self, name: str) -> Contact:
        for contact_name, contact in self.data.items():
            if name == contact_name.value:
                return contact

    def rename(self, old_name: str, new_name: str):
        old_contact = None
        for contact_name, _ in self.data.items():
            if old_name == contact_name.name.value:
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
        res = "\n".join(
            f"{record.name}"
            f"{f'({record.birthday.value})' if record.birthday and record.birthday.value else ''}: "
            f"{', '.join(phone.value for phone in record.phones) if record.phones else 'The contact has no phone'}"
            f"{f' | Email: {record.email.value}' if record.email and record.email.value else ''}"
            f"{f' | Address: {record.address.value}' if record.address and record.address.value else ''}"
            for record in self.data.values()
        )
        return res
