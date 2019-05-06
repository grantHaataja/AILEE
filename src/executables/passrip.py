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
import argparse

import funfunctions


parser = argparse.ArgumentParser(
    prog='passrip',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'newhash',
    nargs='?',
    default=None,
    help='new (md5) hash to crack',
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    if data.newhash is None:
        print("                 Already known passwords:           \n")
        print("            Hash (MD5)                 Plaintext    ")
        print("-------------------------------- -------------------")
        for hash, pwd in kwargs['game'].pw_database.items():
            if pwd[2]:
                if pwd[1]:
                    print("{}:{}".format(hash, pwd[0]))
                else:
                    print(hash)

    else:

        dt = random.random()
        ndots = random.randint(10, 15)
        funfunctions.dots("Cracking", ndots, dt)

        hashes = kwargs['game'].pw_database
        for hash, pwd in hashes.items():
            if hash == data.newhash:
                print("Password: {}".format(pwd[0]))
                pwd[1] = True
                return
        print("Unable to determine password")
