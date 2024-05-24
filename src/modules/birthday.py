import re
from datetime import datetime
from src.modules.field import Field
from src.modules.exceptions import BirthdayVerificationError
from src.utils.update_text_color import update_text_color, EnumColoramaText


# TODO: Improvement. Refactor. Add error handler decorator

class Birthday(Field):
    def __init__(self, value):
        if self.is_valid(value):
            birthday = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(birthday)
            self.birthday = birthday
        else:
            error_text = "Invalid date format. Use DD.MM.YYYY"
            raise BirthdayVerificationError(update_text_color(error_text, EnumColoramaText.ERROR))

    @staticmethod
    def is_valid(value:str):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
       
        if not re.fullmatch(pattern, value):
            error_text = "Invalid date format. Use DD.MM.YYYY"
            raise BirthdayVerificationError(update_text_color(error_text, EnumColoramaText.ERROR))
        
        return True

