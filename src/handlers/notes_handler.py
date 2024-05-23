import re
import textwrap
from tabulate import tabulate

from src.handlers.error_handler import input_error
from src.modules.note import Note
from src.modules.note_book import NoteBook


@input_error
def note_add(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note:
        return f"Note '{note.title}' already exists."

    content = input("Enter a content: ")
    note = Note(title, content)
    book.add(note)
    return "Note added."


@input_error
def note_find_by_title(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note is None:
        return "Note not found."
    return note


@input_error
def note_find_by_tag(_: list, book: NoteBook) -> str:
    tags = input("Enter tags (separated by spaces or commas): ")

    if not tags:
        return "Tags are required."

    tags = [tag if tag.startswith('#') else f'#{tag}' for tag in re.split(r'[\s,]+', tags.strip())]

    found_notes = book.find_by_tag(tags)

    if not found_notes:
        return "No notes found."

    wrapped_table = []
    for note in found_notes:
        wrapped_title = textwrap.fill(note.title, width=40)
        wrapped_content = textwrap.fill(note.content, width=60)
        wrapped_table.append([wrapped_title, wrapped_content])

    res = "\n" + tabulate(wrapped_table, headers=["Titles", "Contents"], tablefmt="grid")
    return res


@input_error
def note_change(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note is None:
        return "Note not found."

    content = input(f"Edit the note ({note.content}): ")

    if not content:
        content = note.content

    note.content = content
    return "Note updated."


@input_error
def note_delete(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note is None:
        return "Note not found."
    book.delete(note)
    return "Note deleted."


def note_show_all(_: list, book: NoteBook) -> NoteBook:
    return book
