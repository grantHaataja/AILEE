"""
"Open sesame"

Description: Cracks the hash of a password to reveal the original value (hashes\nare secured passwords that look something like this: 286755fad04869ca523320acce0dc6a4)

Usage: passrip 286755fad04869ca523320acce0dc6a4
"""

import random, funfunctions


def run(*args, **kwargs):
    assert len(args) == 1, "Invalid use of passrip.\n\nUsage: passrip [hash]"

    dt = random.random()
    ndots = random.randint(10, 15)
    funfunctions.dots("Cracking", ndots, dt)

    if args[0] == '3e7d9b3ad13837e0c0d370c9d348b3e3':
        print("Password: %tL8wn@mI0")
    elif args[0] == '286755fad04869ca523320acce0dc6a4':
        print("Password: password")
    else:
        print("Unable to determine password.")
