"""
"For The People!"

Description: File Transfer Protocol. Implements a file-sharing network between 2 computers by\nallowing them to connect to each other. Secured to only allow access from saved\nusername/password combinations.

Usage: ftp xxx.xxx.xxx.xxx

"""

import funfunctions
from termcolor import colored


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) != 0 and not emptyList, \
        "You must include an IP address to target"
    assert len(args) == 1, "Invalid use of ftp.\n\nUsage: ftp [ip_address]"

    addr = args[0]
    try:
        comp = kwargs['game'].network[addr]
    except KeyError:
        print("couldn't connect to ftp:{}".format(addr))
        return

    if 'ftp' in comp.ports.values():
        funfunctions.dots("Establishing FTP connection", 5, 0.1)

        acct = input(colored("Username: ", 'green'))
        passwd = input(colored("Password: ", 'green'))

        if acct not in comp.users:
            print("Authentication failed: user account not available")
            return

        user = comp.users[acct]
        if passwd == user.password:
            comp.vulns['_ftp_password_crack'][0] = True
            kwargs['shell'].run_command(
                kwargs['shell']._get_command_from_str('shell'),
                ['new', addr],
                cred_login=True,
            )
            kwargs['shell'].run_command(
                kwargs['shell']._get_command_from_str('shell'),
                ['-1']
            )
        else:
            print("Authentication failed: password incorrect")

    else:
        print("Could not establish FTP connection to {}".format(addr))
        return
