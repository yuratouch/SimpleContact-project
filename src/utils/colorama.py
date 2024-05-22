from  colorama import Fore, Back , Style

class EnumColoramaText(Enum):
    SUCCESS = 1
    WARNING = 2
    ERROR = 3


def coloramaText(text: str, colorama: EnumColoramaText) -> str:
    if colorama == EnumColoramaText.SUCCESS:
        return Fore.BLUE + text
    if colorama == EnumColoramaText.WARNING:
        return text
    if colorama == EnumColoramaText.ERROR:
        return Fore.RED + f"ssd {text}"