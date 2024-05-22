from src.modules.field import Field


# TODO: Improvement. Refactor. Add error handler decorator

class Address(Field):
    def __init__(self, value):
        super().__init__(value)
