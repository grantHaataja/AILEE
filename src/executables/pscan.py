"""
"Potato scanner"

Description: Port Scan. Use against an IP address to detect what ports are open
and can be connected to
"""

import argparse


parser = argparse.ArgumentParser(
    prog='ping',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'addr',
    type=str,
    help='the host to port-scan'
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    print('Scanning {}...'.format(data.addr))

    print('Searching for open ports...')

    try:
        comp = kwargs['game'].network[data.addr]
    except KeyError:
        print("No such computer")
        return

    print('Results:')

    if len(comp.ports) == 0:
        print("Found no open ports on {}.  Check firewall?".format(data.addr))
        return

    print("Port\tStatus\tService")
    print("-----------------------")
    for port, svc in comp.ports.items():
        print("{:5d}\tOpen\t{}".format(port, svc))
