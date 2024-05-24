from datetime import datetime
from src.modules.field import Field
from src.utils.update_text_color import update_text_color, EnumColoramaText


# TODO: Improvement. Refactor. Add error handler decorator

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        try:
            self.birthday = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            error_text = "Invalid date format. Use DD.MM.YYYY"
            raise ValueError(update_text_color(error_text, EnumColoramaText(3)))
