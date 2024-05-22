import re
from src.modules.field import Field
from src.modules.exceptions import PhoneVerificationError


class Phone(Field):
    
    def __init__(self, phone):
        if self.is_valid(phone):
            super().__init__(phone)
        else:
            raise PhoneVerificationError(f"Invalid phone number: {phone}")

    
    @staticmethod
    def is_valid(phone: str) -> bool:
        # Checking that all symbols are numbers
        if not phone.isdigit():
            raise PhoneVerificationError(f"'{phone}' is not a phone number. The phone number cannot contain letters.")
        
        # Checking that phone has 10 numbers
        if len(phone) != 10:
            raise PhoneVerificationError(f"The phone number must consist of 10 digits. '{phone}' has {len(phone)}")
        
        # Checking that phone starts from one of Ukrainian mobile operators
        ukrainian_prefixes = ["067", "068", "096", "097", "098", "050", "066", "095", "099", "039", "063", "073", "093", "094", "091", "092"]
        if not any(phone.startswith(prefix) for prefix in ukrainian_prefixes):
            raise PhoneVerificationError(f"The phone number does not belong to any of the Ukrainian operators. Here are list of allow operators codes: {", ".join(ukrainian_prefixes)}")

        # If all checks are successed return True
        return True