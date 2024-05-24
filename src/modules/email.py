import re
from src.modules.field import Field
from src.modules.exceptions import EmailVerificationError


# TODO: Improvement. Refactor. Add error handler decorator

class Email(Field):
    def __init__(self, email):
        if self.is_valid(email):
            super().__init__(email)
        else:
            raise EmailVerificationError(f"Invalid email number: {email}")

    @staticmethod
    def is_valid(email: str) -> bool:
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not re.fullmatch(pattern, email):
            raise EmailVerificationError(f"'{email}' is not a email. The email should be"
                                         f" like this 'exemple@ukrposhta.ua'.")

        return True
