import curses
import random
import time

from algorithms import (
    Bubble_Sort,
    Quick_Sort,
    Merge_Sort,
    Heap_Sort,
    Bogo_Sort,
)


ALGORITHMS = [
    ("Bubble Sort", Bubble_Sort),
    ("Quick Sort", Quick_Sort),
    ("Merge Sort", Merge_Sort),
    ("Heap Sort", Heap_Sort),
    ("Bogo Sort (danger 😈)", Bogo_Sort),
]


def draw_bars(stdscr, array, highlight=None):
    highlight = highlight or []
    h, w = stdscr.getmaxyx()

    max_val = max(array)
    usable_height = h - 4

    stdscr.erase()

    bar_width = max(1, w // len(array))

    for i, val in enumerate(array):
        bar_height = int((val / max_val) * usable_height)
        x = i * bar_width

        color = curses.color_pair(2) if i in highlight else curses.color_pair(1)

        for y in range(bar_height):
            stdscr.addstr(h - 2 - y, x, "█" * bar_width, color)

    max_val = max(array)
    usable_height = h - 4

    for y in range(0, h):
        stdscr.move(y, 0)
        stdscr.clrtoeol()

    bar_width = max(1, w // len(array))

    for i, val in enumerate(array):
        bar_height = int((val / max_val) * usable_height)
        x = i * bar_width

        color = curses.color_pair(2) if i in highlight else curses.color_pair(1)

        for y in range(bar_height):
            stdscr.addstr(h - 2 - y, x, "█" * bar_width, color)

    max_val = max(array)
    usable_height = h - 4
    bar_width = max(1, w // len(array))

    for i, val in enumerate(array):
        bar_height = int((val / max_val) * usable_height)
        x = i * bar_width

        color = curses.color_pair(2) if i in highlight else curses.color_pair(1)

        for y in range(bar_height):
            stdscr.addstr(h - 2 - y, x, "█" * bar_width, color)


def run_sort(stdscr, generator, array):
    stdscr.nodelay(True)

    for step in generator:
        key = stdscr.getch()
        if key in (ord("q"), 27):  # q or ESC
            stdscr.nodelay(False)
            stdscr.clear()
            stdscr.refresh()
            return "quit"

        stdscr.erase()
        highlight = step.get("comparing", []) + step.get("swaping", [])
        draw_bars(stdscr, array, highlight)
        stdscr.noutrefresh()
        curses.doupdate()
        time.sleep(0.03)

    stdscr.nodelay(False)
    stdscr.clear()
    stdscr.refresh()
    return "done"


def menu(stdscr, selected):
    h, w = stdscr.getmaxyx()

    title = "Sorting Algorithm Visualizer"
    stdscr.addstr(1, w // 2 - len(title) // 2, title, curses.A_BOLD)

    for i, (name, _) in enumerate(ALGORITHMS):
        y = 3 + i
        if i == selected:
            stdscr.addstr(y, 4, f"> {name}", curses.A_REVERSE)
        else:
            stdscr.addstr(y, 4, f"  {name}")

    stdscr.addstr(h - 2, 4, "↑↓ / j k to move   Enter to run   q to quit")


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    selected = 0
    base_array = list(range(1, 31))

    while True:
        stdscr.clear()
        menu(stdscr, selected)
        stdscr.refresh()

        key = stdscr.getch()

        if key in (curses.KEY_UP, ord("k")):
            selected = (selected - 1) % len(ALGORITHMS)
        elif key in (curses.KEY_DOWN, ord("j")):
            selected = (selected + 1) % len(ALGORITHMS)
        elif key in (ord("q"), 27):
            break
        elif key in (curses.KEY_ENTER, 10, 13):
            name, algo = ALGORITHMS[selected]

            array = base_array.copy()
            random.shuffle(array)

            run_sort(stdscr, algo(array), array)

            stdscr.addstr(2, 4, "Done! Press any key to return to menu")
            stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
