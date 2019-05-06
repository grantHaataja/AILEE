"""
"Vitality Scanner"

Description: Vulnerability Scan. Use against an IP address to detect system
vulnerabilities
"""

import argparse

from funfunctions import dots


parser = argparse.ArgumentParser(
    prog='vscan',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'addr',
    type=str,
    help='host to scan for vulnerabilities'
)


def run(*args, **kwargs):
    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    if data.addr not in kwargs['game'].network:
        print("Couldn't find computer {}".format(data.addr))
        return

    print('Beginning deep vulnerability scan')
    dots("Scanning", 10, 0.5)

    # need to change this so there are 2-3 possibilities that will execute based on
    # which IP address is entered

    vulns = kwargs['game'].network[data.addr].vulns
    if len(vulns.keys()) == 0:
        print("No vulnerabilities found")
    else:
        print("{:<40}\tExploited?".format("Vulnerability"))
        print("-" * 40 + "\t----------")
        for vuln in vulns.keys():
            if not vuln.startswith('_'):
                print("{:<40}\t{}".format(
                    vuln, vulns[vuln][0]
                ))
            kwargs['game'].add_vuln(vuln)
