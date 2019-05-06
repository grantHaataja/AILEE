"""
What am I?
"""

import argparse

from termcolor import colored

parser = argparse.ArgumentParser(
    prog='gnome',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)

def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    print(colored('Ho ho ho ha ha, ho ho ho he ha. Hello there, old chum. I’m '
    'gnot a gnelf. I’m gnot a gnoblin. I’m a gnome. And you’ve been, '
    'GNOMED', 'yellow'))
