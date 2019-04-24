"""
"Open sesame"

Description: Cracks the hash of a password to reveal the original value (hashes
are secured passwords that look something like this:
286755fad04869ca523320acce0dc6a4)

With no arguments, prints a list of all currently known passwords (already
cracked).

Usage: passrip 286755fad04869ca523320acce0dc6a4
"""

import random

import funfunctions


def run(*args, **kwargs):

    if len(args) == 0:
        print("Known passwords:")
        print("----------------")
        for hash, pwd in kwargs['game'].pw_database.items():
            if pwd[1]:
                print("{}:{}".format(hash, pwd[0]))
            else:
                print(hash)

    if len(args) == 1:

        dt = random.random()
        ndots = random.randint(10, 15)
        funfunctions.dots("Cracking", ndots, dt)

        hashes = kwargs['game'].pw_database
        for hash, pwd in hashes.items():
            if hash == args[0]:
                print("Password: {}".format(pwd[0]))
                pwd[1] = True
                return
        print("Unable to determine password")
