import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pathlib import Path
from colorama import Fore, Style # type: ignore
from utils.decorators.log_errors import log_errors
from utils.colors.print_color_text import print_color_text


colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.YELLOW]

@log_errors
def print_directory_structure(directory_path, counter=0):
    directory = Path(directory_path)
    items = sorted(directory.iterdir(), key=lambda item: item.is_file())
    indent = '  ' * counter
    for item in items:
        if item.is_dir():
            print_color_text(item.name, colors[counter % len(colors)] + Style.BRIGHT, indent, '/')
            print_directory_structure(item, counter + 1)
        else:
            print_color_text(item.name, colors[counter % len(colors)] + Style.BRIGHT, indent)



try:
    if len(sys.argv) != 2:
        raise ValueError("Ввідіть наспупний патерн у консоль: python main.py <directory_path>")
    directory_path = sys.argv[1]

    if not Path(directory_path).is_dir():
        raise FileNotFoundError("Помилка: Directory не існує")
    print_directory_structure(directory_path)
except Exception as e:
    print(e)
    sys.exit(1)
        

