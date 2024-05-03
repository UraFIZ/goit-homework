from colorama import Style # type: ignore

def print_color_text(text: str, color: str, beginning="", end="") -> None:
    print(beginning + color + text + Style.RESET_ALL + end)