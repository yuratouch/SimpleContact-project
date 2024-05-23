from collections import UserDict


class Book(UserDict):
    def __init__(self, save_function):
        super().__init__()
        self.save_function = save_function

    def add(self, value):
        pass

    def find(self, value):
        pass

    def delete(self, value):
        pass

    def save(self):
        self.save_function(self)