from time import sleep
from replit import clear
import curses
import random

def eyeCancer():
  try:
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    colors = {
      0:curses.COLOR_BLACK,
      1:curses.COLOR_BLUE,
      2:curses.COLOR_CYAN,
      3:curses.COLOR_GREEN,
      4:curses.COLOR_MAGENTA,
      5:curses.COLOR_RED,
      6:curses.COLOR_WHITE,
      7:curses.COLOR_YELLOW
    }
    height,width = stdscr.getmaxyx()
    cy, cx = stdscr.getyx()
    i = 1
    while cy < height-1:
      if i > 10:
        i = 1
      else:
        i += random.randint(0, 5)
      curses.init_pair(i, curses.COLOR_WHITE, colors[random.randint(0,7)])
      stdscr.addstr('               ', curses.color_pair(i))
      cy, cx = stdscr.getyx()
    stdscr.refresh()
    sleep(2)
    stdscr.erase()
    curses.endwin()
  except KeyboardInterrupt:
    stdscr.erase()
    curses.endwin()


def run(virus_text, existing_text=[]):
  try:
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.bkgd(' ', curses.color_pair(4))
    if existing_text:
      stdscr.addstr(existing_text[0], curses.color_pair(2))
      i = 1
      while i < len(existing_text):
        stdscr.addstr(existing_text[i], curses.color_pair(1))
        i += 1
    stdscr.refresh()
    sleep(3)
    for text in virus_text:
      stdscr.addstr(text, curses.color_pair(3))
      stdscr.refresh()
      sleep(3)
    stdscr.erase()
    curses.endwin()
  except KeyboardInterrupt:
    stdscr.erase()
    curses.endwin()
    raise KeyboardInterrupt