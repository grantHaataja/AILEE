"""
"Just give up and go home"

Description: Shut the computer down

DISCLAIMER: It is a known issue that if shutdown, AILEE will lose all memory, and\nthe entire training process will have to be redone

Usage: shutdown
"""

from MainMenuException import MainMenuException
from funfunctions import dots


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) in [0, 1] or emptyList, \
        "Invalid use of shutdown.\n\nUsage: shutdown"
    seconds = 5
    if args:
        if args[0] == 'now':
            seconds = 0
        else:
            try:
                seconds = int(args[0])
            except ValueError:
                seconds = 5
    _shutdown(seconds)


def _shutdown(t=5):
    if t != 0:
        dots("Shutting down", t, 1 / t)
    raise MainMenuException
