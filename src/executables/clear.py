"""
"Clear your screen you dirty animal"

Description: clears all text from the terminal screen
"""

import argparse

import funfunctions


parser = argparse.ArgumentParser(
    prog='clear',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    funfunctions.clear()
