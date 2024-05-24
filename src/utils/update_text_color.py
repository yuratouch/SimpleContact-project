from enum import Enum
from colorama import Fore


class EnumColoramaText(Enum):
    SUCCESS = 1
    WARNING = 2
    ERROR = 3


def update_text_color(text: str, colorama: EnumColoramaText) -> str:
    if colorama == EnumColoramaText.SUCCESS:
        return Fore.GREEN + f" {text}"
    if colorama == EnumColoramaText.WARNING:
        return Fore.YELLOW + f" {text}"
    if colorama == EnumColoramaText.ERROR:
        return Fore.RED + f" {text}"
