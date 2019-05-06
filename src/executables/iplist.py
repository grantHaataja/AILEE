'''
"Kind of like a shopping list, except for targets"

Description: Lists the IP-addresses of all computers on the network available\nto AILEE

Option -a (Add): Using an email address, attempt to access the
corresponding IP-address and add it to the list of available IP-addresses
'''

import argparse

from computers import factory


COMPS = {
    'customersolutions@pics.com': 'pics',
    'crypticcryptocurrency@ccc.com': 'ccc',
    'safeandsecurebanking@ssb.com': 'ssb',
}


parser = argparse.ArgumentParser(
    prog='iplist',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    '-a',
    nargs='?',
    type=str,
    dest='email',
    default=None,
    help="lookup an email's IP address",
)


def run(*args, **kwargs):
    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    email = data.email
    game = kwargs['game']
    network = game.network
    if email is not None:
        if email in COMPS:
            factory.mk_computer(COMPS[email], **kwargs)
        else:
            print("Unable to find address associated with {}".format(email))
            return

    # Print out available IP addresses
    for address in network:
        print("{:<16} {}".format(address, network[address]))
