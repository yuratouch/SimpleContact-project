from src.handlers.error_handler import input_error
from src.modules.note import Note
from src.modules.note_book import NoteBook


# TODO: Improvement. Review error decorator for all functions

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
def note_find(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note is None:
        return "Note not found."
    return note


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


def note_show_all(_: list, book: NoteBook) -> str:
    return book
