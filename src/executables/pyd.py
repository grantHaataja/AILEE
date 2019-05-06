"""
"Python debugger"

Description: Executes whatever follows as Python code

Usage: Not for civilian use
"""

import argparse


parser = argparse.ArgumentParser(
    prog='pyd',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'code',
    nargs='*',
    type=str,
    default=None,
    help='code to run'
)


def run(*args, **kwargs):
    assert kwargs['game'].skip_dialog, 'Dev Access required'

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    print(kwargs)
    if data.code:
        exec(' '.join(data.code))
