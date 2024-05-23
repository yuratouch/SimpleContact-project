from src.modules.book import Book
from src.modules.note import Note
from tabulate import tabulate
import textwrap


class NoteBook(Book):
    def add(self, note: Note):
        self.data[note.title] = note

    def find(self, title):
        for _, note in self.data.items():
            if title == note.title:
                return note

    def delete(self, delete_note: Note):
        for _, note in self.data.items():
            print()
            if delete_note.title == note.title:
                self.data.pop(note.title)
                break

    def find_by_tag(self, tags: list[str]) -> list[Note]:
        return [note for note in self.data.values() if note.has_any_tags(tags)]

    def __str__(self):
        wrapped_table = []
        for note in self.data.values():
            wrapped_title = textwrap.fill(note.title, width=40)
            wrapped_content = textwrap.fill(note.content, width=60)
            wrapped_table.append([wrapped_title, wrapped_content])

        res = "\n" + tabulate(wrapped_table, headers=["Titles", "Contents"], tablefmt="grid")
        return res
