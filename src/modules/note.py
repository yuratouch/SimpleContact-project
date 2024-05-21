from src.modules.name import Name
from src.modules.note_main import Main


# TODO: SC-20. Feature 6. Save Notes
class Note:
    def __init__(self, name, main):
        self.name = Name(name)
        self.main = Main(main)

    # TODO: SC-22. Feature 8.1 Edit Notes functionality
    def edit_note(self, old, new):
        pass

    # TODO: SC-23. Feature 8.2 Delete Notes functionality
    def delete_note(self, note):
        pass

    # TODO: SC-21. Feature 7. Find Notes functionality
    def find_note(self, note_input):
        pass

    # TODO: SC-20. Feature 6. Save Notes
    def __str__(self):
        return f"Title: {self.name.value}\n Note: {self.main.value}"
