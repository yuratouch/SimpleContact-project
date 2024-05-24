import re
from datetime import datetime
from src.modules.field import Field
from src.modules.exceptions import BirthdayVerificationError

# TODO: Improvement. Refactor. Add error handler decorator

class Birthday(Field):
    def __init__(self, value):
        if self.is_valid(value):
            birthday = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(birthday)
            self.birthday = birthday
        else:
            raise BirthdayVerificationError("Invalid date format. Use DD.MM.YYYY")

    @staticmethod
    def is_valid(value:str):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
       
        if not re.fullmatch(pattern, value):
            raise BirthdayVerificationError("Invalid date format. Use DD.MM.YYYY")
        
        return True