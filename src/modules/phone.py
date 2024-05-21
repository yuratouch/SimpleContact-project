import re
from src.modules.field import Field
from src.modules.exceptions import PhoneVerificationError

class Phone(Field):
    pattern = r'\d{10}$'

    def __init__(self, phone):
        super().__init__(phone)
        if re.match(Phone.pattern, phone):
            self.phone = phone
        else:
             raise PhoneVerificationError(phone)