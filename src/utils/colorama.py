from enum import Enum
from  colorama import Fore, Back , Style

class EnumColoramaText(Enum):
    SUCCESS = 1
    WARNING = 2
    ERROR = 3


def coloramaText(text: str, colorama: EnumColoramaText) -> str:
    if colorama == EnumColoramaText.SUCCESS:
        return Fore.GREEN + f"🔴 {text}"
    if colorama == EnumColoramaText.WARNING:
        return Fore.YELLOW + f"🟡 {text}"
    if colorama == EnumColoramaText.ERROR:
        return Fore.RED + f"🔴 {text}"