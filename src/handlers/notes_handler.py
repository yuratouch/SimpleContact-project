import re
import textwrap
from tabulate import tabulate

from src.handlers.error_handler import input_error
from src.modules.note import Note
from src.modules.note_book import NoteBook
from src.utils.update_text_color import update_text_color, EnumColoramaText


@input_error
def note_add(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return update_text_color("Title is required.", EnumColoramaText.WARNING)

    note = book.find(title)

    if note:
        return update_text_color(f"Note '{note.title}' already exists.", EnumColoramaText.WARNING)
    
    content = input("Enter a content: ")
    note = Note(title, content)
    book.add(note)
    book.save()
    return update_text_color("Note added.", EnumColoramaText.SUCCESS)


@input_error
def note_find_by_title(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return update_text_color("Title is required.", EnumColoramaText.WARNING)

    note = book.find(title)

    if note is None:
        return update_text_color("Note not found.", EnumColoramaText.WARNING)
    return note


@input_error
def note_find_by_tag(_: list, book: NoteBook) -> str:
    tags = input("Enter tags (separated by spaces or commas): ")

    if not tags:
        return update_text_color("Tags are required.", EnumColoramaText.WARNING)

    tags = [tag if tag.startswith('#') else f'#{tag}' for tag in re.split(r'[\s,]+', tags.strip())]

    found_notes = book.find_by_tag(tags)

    if not found_notes:
        return update_text_color("No notes found.", EnumColoramaText.WARNING)

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
        return update_text_color("Title is required.", EnumColoramaText.WARNING)

    note = book.find(title)

    if note is None:
        return update_text_color("Note not found.", EnumColoramaText.WARNING)

    content = input(f"Edit the note ({note.content}): ")

    if not content:
        content = note.content

    note.content = content
    book.save()
    return update_text_color("Note updated.", EnumColoramaText.SUCCESS)


@input_error
def note_delete(_: list, book: NoteBook) -> str:
    title = input("Enter a title: ")

    if not title:
        return "Title is required."

    note = book.find(title)

    if note is None:
        return "Note not found."
    book.delete(note).save()
    return update_text_color("Note deleted.", EnumColoramaText.SUCCESS)


def note_show_all(_: list, book: NoteBook) -> NoteBook:
    return book
