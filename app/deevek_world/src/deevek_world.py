
import curses
import time

def hello_boo(text="I Love you Boo, How's my way of saying that, moomsi", delay=0.2):
    stdscr = curses.initscr()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(delay * 1000))
    print("hbsh")

    try:
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(text) // 2
        y = height // 2

        for i in range(len(text)):
            stdscr.clear()
            stdscr.addstr(y, x, text[:i+1])
            stdscr.refresh()
            time.sleep(delay)

    finally:
        curses.endwin()
