"""
"Better than looking at cat pics"

Description: Prints contents of a file to the terminal screen.  If any MD5
hashes are found, add them to the passrip command and also look for
anything that might be the plaintext of that hash.
"""

import re
import argparse

import filesystem

# https://stackoverflow.com/a/373207.  Thanks, @Mark Novakowski!
MD5_REGEX = r"([a-f0-9]{32})"

parser = argparse.ArgumentParser(
    prog='read',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'filename',
    type=str,
    help='the file to read'
)
parser.add_argument(
    '-n',
    action='store_false',
    dest='doSearchHashes',
    help='disable automatic hash searching'
)


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

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    try:
        obj = kwargs['cwd'].children[data.filename]
    except KeyError:
        print("couldn't file file")
        return

    if isinstance(obj, filesystem.File):
        if kwargs['user'].name == obj.owner:
            allowed = obj.permissions.read_owner
        else:
            allowed = obj.permissions.read_users

        if allowed:
            print(obj.data)
            if data.doSearchHashes:
                deal_with_hashes(obj.data, kwargs['game'])
        else:
            print("Unable to read file")
    else:
        print("Not a file")
