'''
"For The People!"

Description: File Transfer Protocol. Implements a file-sharing network between 2 computers by\nallowing them to connect to each other. Secured to only allow access from saved\nusername/password combinations.

Usage: ftp xxx.xxx.xxx.xxx

'''

import funfunctions
from termcolor import colored

def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) != 0 and not emptyList, "You must include an IP address to target"
    assert len(args) == 1, "Invalid use of ftp.\n\nUsage: ftp [ip_address]"

    addr = args[0]

    if addr == '140.24.3.12':
        funfunctions.dots("Loading FTP", 5, 0.1)


        creds = (['admin', 'banks4lyfe',])

        print(colored("Username: ", "green") + "admin")
        passwd = input(colored("Password: ", "green"))

        if passwd == creds[1]:
            kwargs['game'].network['140.24.3.12'].exploited = True
        else:
            print("unable to verify password; will try connecting anyways")

        kwargs['shell'].run_command(
            kwargs['shell']._get_command_from_str('shell'),
            ['new', '140.24.3.12']
        )
        if kwargs['game'].network['140.24.3.12'].exploited:
            kwargs['shell'].run_command(
                kwargs['shell']._get_command_from_str('shell'),
                ['-1']
            )
    else:
        print("Unable to establish FTP connection.")