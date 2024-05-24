from src.modules.field import Field
from src.modules.exceptions import PhoneVerificationError
from src.utils.update_text_color import update_text_color, EnumColoramaText


class Phone(Field):

    def __init__(self, phone):
        if self.is_valid(phone):
            super().__init__(phone)
        else:
            error_text = f"Invalid phone number: {phone}"
            raise PhoneVerificationError(update_text_color(error_text, EnumColoramaText(3)))

    @staticmethod
    def is_valid(phone: str) -> bool:
        if not phone.isdigit():
            error_text = f"'{phone}' is not a phone number. The phone number cannot contain letters."
            raise PhoneVerificationError(update_text_color(error_text, EnumColoramaText(3)))

        if len(phone) != 10:
            error_text = f"The phone number must consist of 10 digits. '{phone}' has {len(phone)}"
            raise PhoneVerificationError(update_text_color(error_text, EnumColoramaText(3)))
            

        ukrainian_prefixes = ["067", "068", "096", "097", "098", "050", "066", "095", "099", "039", "063", "073", "093",
                              "094", "091", "092"]
        if not any(phone.startswith(prefix) for prefix in ukrainian_prefixes):
            error_text = f'Please enter valid Ukrainian phone number. Run "help" to see allowed numbers.' 
            raise PhoneVerificationError(update_text_color(error_text, EnumColoramaText(3)))

        return True
