from functools import wraps
# TODO: Improvement. Improve error decorator. 

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__)
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please enter expected values (name, phone number)."
        except IndexError:
            return "Please enter name to check the related phone number."
        except Exception as e:
            return str(e)

    return inner