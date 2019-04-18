"""
"Gradually being replaced by iPod"

Description: Change directories (move from current folder to another folder) **see ls**

Usage: cd directory_name

Usage: cd .. (moves back up to the previous directory)
"""


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) != 0 and not emptyList, \
        "No directory specified.\n\nUsage: cd [Directory]"
    assert len(args) == 1, "Invalid use of cd.\n\nUsage: cd [Directory]"

    shell = kwargs['shell']

    assert args[0] == '.' or args[0] == '..' or '.' not in args[0], \
        "Can't change directory into a file"

    try:
        new_cwd = shell.cwd[args[0]]
        shell.cwd = new_cwd
    except AssertionError:
        print("nope, directory doesn't exist")
