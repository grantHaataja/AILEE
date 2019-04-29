"""
"Vitality Scanner"

Description: Vulnerability Scan. Use against an IP address to detect system
vulnerabilities

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

    vulns = kwargs['game'].network[args[0]].vulns
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
