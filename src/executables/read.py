"""
"Better than looking at cat pics"

Description: Prints contents of a file to the terminal screen

Usage: read file_name.txt
"""

import re

import filesystem

# https://stackoverflow.com/a/373207.  Thanks, @Mark Novakowski!
MD5_REGEX = r"([a-f0-9]{32})"


def deal_with_hashes(content, game):
    """
    Identifies MD5 hashes in the file contents, and deals with it.
    :param content: file data
    :return: nothing
    """

    hashes = re.findall(MD5_REGEX, content)

    for hash in hashes:
        if hash in list(game.pw_database.keys()):
            game.pw_database[hash][2] = True

            # check for the cleartext -- if it's in the file, automatically
            # add it
            cleartext = game.pw_database[hash][0]
            if cleartext in content:
                game.pw_database[hash][1] = True

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
            deal_with_hashes(obj.data, kwargs['game'])
        else:
            print("Unable to read file")
    else:
        print("Not a file")
