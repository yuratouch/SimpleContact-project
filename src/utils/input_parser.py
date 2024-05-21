def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def capitalize_name(func):
    def inner(*args, **kwargs):
        args[0][0] = str(args[0][0]).lower().capitalize()
        return func(*args, **kwargs)
    return inner