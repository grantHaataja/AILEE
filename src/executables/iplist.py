'''
"Kind of like a shopping list, except for targets"

Description: Lists the IP-addresses of all computers on the network available\nto AILEE

Option -a (Add): Using an email address, attempt to access the\ncorresponding IP-address and add it to the list of available IP-addresses

Usage: iplist (displays list of all known IP-addresses)

Usage: iplist -a emailaddress@example.com (adds IP address associated with email)
'''

from computers import factory


COMPS = {
    'customersolutions@pics.com': 'pics',
    'crypticcryptocurrency@ccc.com': 'ccc',
    'safeandsecurebanking@ssb.com': 'ssb',
}


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) == 0 or emptyList or (len(args) == 2 and args[0] == '-a'), \
        "Invalid use of iplist. See man page for details"

    game = kwargs['game']
    network = game.network
    if len(args) != 0:
        if args[1] in COMPS:
            factory.mk_computer(COMPS[args[1]], **kwargs)
        else:
            print("Unable to find address associated with {}".format(args[1]))
            return

    # Print out available IP addresses
    for address in network:
        print("{:<16} {}".format(address, network[address]))
