from functools import wraps
from src.utils.update_text_color import update_text_color, EnumColoramaText


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return update_text_color("Please enter expected values (name, phone number).", EnumColoramaText.ERROR)
        except IndexError:
            return update_text_color("Please enter name to check the related phone number.", EnumColoramaText.ERROR)
        except Exception as error:
            return str(update_text_color(error, EnumColoramaText.ERROR))

    return inner