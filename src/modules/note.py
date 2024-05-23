import re
import textwrap
from tabulate import tabulate


class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def edit_note(self, content):
        self.content = content

    def has_any_tags(self, tags: list[str]) -> bool:
        for tag in tags:
            if re.search(rf'\B{re.escape(tag)}\b', self.content):
                return True
        return False

    def __str__(self):
        wrapped_title = textwrap.fill(self.title, width=40)
        wrapped_content = textwrap.fill(self.content, width=60)
        table = [[wrapped_title, wrapped_content]]
        return tabulate(table, headers=["Title", "Content"], tablefmt="grid")
