import textwrap
from tabulate import tabulate


class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_note(self, content):
        self.content = content

    def __str__(self):
        wrapped_title = textwrap.fill(self.title, width=40)
        wrapped_content = textwrap.fill(self.content, width=60)
        table = [[wrapped_title, wrapped_content]]
        return tabulate(table, headers=["Titles", "Contents"], tablefmt="grid")
