"""
"For The People!"

Description: File Transfer Protocol. Implements a file-sharing network between 2
computers by allowing them to connect to each other. Secured to only allow access
from saved username/password combinations.

"""

import argparse
from termcolor import colored

import funfunctions


parser = argparse.ArgumentParser(
    prog='ftp',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'ipaddr',
    type=str,
    help='IP address of the host'
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    addr = data.ipaddr
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
                ['-n', addr],
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
