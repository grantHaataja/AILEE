"""
"Open sesame"

Description: Cracks the hash of a password to reveal the original value (hashes\nare secured passwords that look something like this: 286755fad04869ca523320acce0dc6a4)

Usage: passrip 286755fad04869ca523320acce0dc6a4
"""

import random

import funfunctions


def run(*args, **kwargs):
    assert len(args) == 1, "Invalid use of passrip.\n\nUsage: passrip [hash]"

    dt = random.random()
    ndots = random.randint(10, 15)
    funfunctions.dots("Cracking", ndots, dt)

    hashes = kwargs['game'].pw_database

    if args[0] in hashes:
        print("Password: {}".format(hashes[args[0]]))
    else:
        print("Unable to determine password.")
