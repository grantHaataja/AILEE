"""
"SOS"

Description: Lists "all" available commands.
"""

import argparse

from executables import __all__, BLACKLIST_COMMANDS


parser = argparse.ArgumentParser(
    prog='help',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        print("\n\nJust run `help`, dangit.\n\n")

    print('The Artificial Intelligence Lionix Exploit Environment '
          '(A.I.L.E.E.) uses a\nfilestructure called directories, '
          'similar to other operating systems. Each\ndirectory is like a '
          'folder, which can hold other directories or files.\n\nTo display '
          'the contents of a directory, use the "ls" command.\nTo navigate '
          'through directories, use the "cd" command.\nTo display a file\'s '
          'contents, use the "read" command.\n\nHere is a list of all '
          'available commands. For more in-depth help for a specific '
          '\ncommand, type: "man command_name" or "command_name -h".\n')
    temp = list(__all__)
    temp.sort()
    for cmd in temp:
        if (cmd in kwargs['game'].allowed_commands) and \
                (cmd not in BLACKLIST_COMMANDS):
            print(cmd)
    print()
