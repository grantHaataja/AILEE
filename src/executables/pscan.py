"""
"Spell ICUP"

Description: Port Scan. Use against an IP address to detect what ports are open and can be\nconnected to

Usage: pscan xxx.xxx.xxx.xxx
"""


def run(*args, **kwargs):

    assert len(args) == 1, \
        "You must specify a valid IP address.\n\nUsage: pscan [ip_address]"

    print('Scanning {}...'.format(args[0]))

    print('Searching for open ports...')

    try:
        comp = kwargs['game'].network[args[0]]
    except KeyError:
        print("No such computer")
        return

    print('Results:')

    if len(comp.ports) == 0:
        print("Found no open ports on {}.  Check firewall?".format(args[0]))
        return

    print("Port\tStatus\tService")
    print("-----------------------")
    for port, svc in comp.ports.items():
        print("{:5d}\tOpen\t{}".format(port, svc))
