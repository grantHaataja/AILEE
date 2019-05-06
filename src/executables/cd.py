"""
"Gradually being replaced by iPod"

Description: Change directories (move from current folder to another folder) **see ls**
"""

import argparse

import filesystem

parser = argparse.ArgumentParser(
    prog='cd',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'directory',
    default='.',
    type=str,
    help='target directory to move to',
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    shell = kwargs['shell']

    if data.directory in list(shell.cwd.children.keys()):
        new_cwd = shell.cwd[data.directory]
        if isinstance(new_cwd, filesystem.Directory):
            shell.cwd = new_cwd
        else:
            print("nope, that's a file")
    else:
        print("nope, directory doesn't exist")
