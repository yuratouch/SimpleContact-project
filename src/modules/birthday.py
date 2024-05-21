from datetime import datetime
from src.modules.field import Field


# TODO: Improvement. Refactor. Add error handler decorator

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
