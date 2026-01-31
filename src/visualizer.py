import os
import time

from colorama import init, Fore, Style

init(autoreset=True)


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def draw_arr(array, highlight=None):
    highlight = highlight or []
    max_val = max(array) if array else 1

    for i, val in enumerate(array):
        filled = int((val / max_val) * 50)
        bar = "█" * filled

        if i in highlight:
            print(Fore.RED + bar + Style.RESET_ALL)
        else:
            print(bar)


def run(generator, array, delay=0.05):
    for step in generator:
        clear_screen()
        highlight = step.get("comparing", []) + step.get("swaping", [])
        draw_arr(array, highlight)
        time.sleep(delay)
