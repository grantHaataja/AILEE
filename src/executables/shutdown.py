"""
"Just give up and go home"

Description: Shut the computer down

DISCLAIMER: It is a known issue that if shutdown, AILEE will lose all memory, and
the entire training process will have to be redone.
"""

import argparse

from MainMenuException import MainMenuException
from funfunctions import dots


parser = argparse.ArgumentParser(
    prog='shutdown',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'when',
    type=str,
    default='5',
    nargs='?',
    help='time until shutdown (seconds) or "now"',
)


def run(*args, **kwargs):
    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    try:
        seconds = int(data.when)
    except ValueError as e:
        if data.when == 'now':
            seconds = 0
        else:
            print("Invalid time specification")
            return

    _shutdown(seconds)


def _shutdown(t=5):
    if t != 0:
        dots("Shutting down", t, 1 / t)
    raise MainMenuException
