"""
"Vitality Scanner"

Description: Vulnerability Scan. Use against an IP address to detect system\nvulnerabilities

Usage: vscan xxx.xxx.xxx.xxx
"""

from funfunctions import dots


def run(*args, **kwargs):
    assert len(args) == 1, \
        "You must specify a valid IP address\n\nUsage: vscan [ip_address]"

    if args[0] not in kwargs['game'].network:
        print("Couldn't find computer {}".format(args[0]))
        return

    print('Beginning deep vulnerability scan')
    dots("Scanning", 10, 0.5)

    # need to change this so there are 2-3 possibilities that will execute based on
    # which IP address is entered

    # windoors computer for safeandsecurebanking
    if args[0] == '120.45.30.6':
        print('Vulnerabilities found: WD45_702 Reverse tcp shell')
    # lionux computer for vrypto bank
    elif args[0] == '120.33.7.242':
        print('Vulnerabilities found: LI38_612 meta ssh security flaw')
    else:
        print('No vulnerabilities found')
