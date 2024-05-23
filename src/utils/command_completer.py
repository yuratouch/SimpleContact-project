import re

from prompt_toolkit.completion import Completer, Completion


class CommandCompleter(Completer):
    def __init__(self, comands_dict):
        self.comands_dict = comands_dict

    def get_completions(self, document, complete_event):
        word_before_cursor = document.text_before_cursor
        match = re.search(r'(\S+)$', word_before_cursor)
        if match:
            word_before_cursor = match.group(1)
            for command in self.comands_dict:
                if command.startswith(word_before_cursor):
                    yield Completion(command, start_position=-len(word_before_cursor))
