def capitalize_name(func):
    def inner(*args, **kwargs):
        args[0][0] = str(args[0][0]).lower().capitalize()
        return func(*args, **kwargs)

    return inner
