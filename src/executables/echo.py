# -*- coding: utf-8 -*-
"""
"echo... echo..."

Description: prints input to terminal screen
"""

import argparse

parser = argparse.ArgumentParser(
    prog='echo',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'content',
    nargs='*',
    help='content to echo',
)

def run(*args, **kwargs):
    """
    Return whatever was put in.
    """
    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    print(' '.join(data.content))
