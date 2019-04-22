"""
"Better than looking at cat pics"

Description: Prints contents of a file to the terminal screen

Usage: read file_name.txt
"""

import filesystem


def run(*args, **kwargs):
    assert len(args) == 1, "Must specify a file to read.\n\nUsage: read [filename]"

    try:
        obj = kwargs['cwd'].children[args[0]]
    except KeyError:
        print("couldn't file file")
        return

    if isinstance(obj, filesystem.File):
        if 'r' in obj.permissions:
            print(obj.data)
        else:
            print("Unable to read file")
    else:
        print("Not a file")
