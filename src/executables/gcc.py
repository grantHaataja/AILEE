"""
 "How do I spell gcc?"

GNU C Compiler.  Used for compiling code.

Compiles a predetermined set of instructions into the executable file "a.exe" and
puts it in the current working directory.

Usage: gcc [filename]
"""

import argparse

import computers.execfiles.grabfile as grabfile


parser = argparse.ArgumentParser(
    prog='gcc',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'whatever',
    nargs=argparse.REMAINDER,
    help="it doesn't matter what goes here"
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    cwd = kwargs['cwd']
    if 'a.exe' not in cwd.children:
        cwd.addPrebuiltFile(
            grabfile.get_exec_file("a.out")
        )
