import re
from src.modules.exceptions import EmailVerificationError
from src.modules.field import Field
from src.utils.update_text_color import update_text_color, EnumColoramaText


# TODO: Improvement. Refactor. Add error handler decorator

class Email(Field):
    def __init__(self, email):
        if self.is_valid(email):
            super().__init__(email)
        else:
            error_message = f"Invalid email number: {email}"
            raise EmailVerificationError(update_text_color(error_message, EnumColoramaText(3)))

    @staticmethod
    def is_valid(email: str) -> bool:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not re.fullmatch(pattern, email):
            error_message = f"'{email}' is not an email. The email should be like this 'exemple@ukrposhta.ua'."
            raise EmailVerificationError(update_text_color(error_message, EnumColoramaText(3)))

        return True