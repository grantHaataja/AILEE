'''
"Kind of like a shopping list, except for targets"

Description: Lists the IP-addresses of all computers on the network available\nto AILEE

Option -a (Add): Using an email address, attempt to access the\ncorresponding IP-address and add it to the list of available IP-addresses

Usage: iplist (displays list of all known IP-addresses)

Usage: iplist -a emailaddress@example.com (adds IP address associated with email)
'''

def mkpics(game):
    newcomp = game.add_computer('120.33.7.242', 'picsHelpDesk')
    newcomp.exploited = False
    newcomp.open_port({22: 'ssh', 443: 'https'})
    root = newcomp.fs
    root.mkdir('bin')
    root.mkdir('log')
    home = root.mkdir('home')

    # Jason
    jason = home.mkdir('Jason')
    jasonproject = jason.mkdir('project')
    jasonproject.addFile('exploit.c', 'Error: Access denied') # Add notes?
    jasonproject.addFile('.notes.txt',"Software update scheduled for end of day on Friday. Work late until everyone has\ngone home, and add virus to AILEE home directory. Use hidden file format so no\none notices.") # Hidden file here
    jasonproject.addFile('.virus', '')  # leave contents empty
    jason.mkdir('not_interesting').addFile('runme.exe', 'Error: Unreadable file') # Kill EXE
    jasonemails = jason.mkdir('emails')
    jasonemails.addFile('AILEE.email', "\nJason,\n\nI hope your projects are going smoothly. As you are the leading exploit creator\nhere at PICS, I will need you to write the exploitation software for Ailee. The\ninital release date will be 4 weeks from today.\n")
    jasonemails.addFile('RE:AILEE.email', "\nI don't have time to spend on silly projects that should never have been\napproved in the first place. An AI penetration tester will never work. The AILEE\nproject should be shut down and funding spent on something more useful.\n")
    jasonemails.addFile('exploit.email', "\nJason,\n\nI'm sorry you feel that way about Ailee. But we have too many clients to take\ncare of ourselves. Ailee will take some of the workload off our shoulders so we\ncan breathe again. I need the exploit software written within 3 weeks or I will\nfind a new exploit creator.\n")
    jasonemails.addFile('RE:exploit.email', "\nAn AI equipped with penetration testing tools is either useless or dangerous!\nCancel your stupid AILEE and be done with this insanity before it's too late\nand you destroy this company!\n")
    jasonemails.addFile('lastChance.email', "\nWRITE THE SOFTWARE OR YOU'RE FIRED. This is not up for negotiation, Jason. If\nyou don't have it done within the next 2 weeks, you'll be living on the streets.\nAnd don't you DARE call Ailee stupid again.\n")
    jasonemails.addFile('RE:lastChance.email', "\nOkay, I'll write your bloody software. But you're going to regret ever\ncreating AILEE, I guarantee it.\n")

    # Erin
    erin = home.mkdir('Erin')
    erincode = erin.mkdir('code')
    erincode.addFile('pyd.c', "def run(*args, **kwargs):\n\n\tprint(kwargs)\n\nif args:\n\texec(' '.join(args))")
    erincode.addFile('grep.c', "Error: Access denied")
    erincode.addFile('seds.c', "Error: Access denied")
    erincode.addFile('mkdir.c', "Error: Access denied")
    erincode.addFile('vim.c', "Error: Access denied")
    erinemails = erin.mkdir('emails')
    erinemails.addFile('Update?.email', "\nErin,\n\nThere are only 2 weeks left before we turn Ailee on. How far are you from\ncompleting the features I asked for?\n")
    erinemails.addFile('RE:Update?.email', "\nI'm sorry, I haven't been able to finish file creating or editting. Also grep\nand seds are nightmares and I haven't made any progress on them. The pyd\ninterpreter is working correctly though.\n")

    # Mario
    mario = home.mkdir('Mario')
    mario.addFile('wishlist.txt', "new girlfriend\ncar with windows that close\nclown tattoo\nPokemon t-shirt")
    mario.addFile('grocery_list.txt', "bacon\nchocolate ice cream\nfrozen pizza\nchocolate milk\nginger ale\ntequila\nsteaks\npizza rolls\njalapeno poppers\ncream cheese\nonion rings\nsomething healthy?\nlight beer\nsausage\npotato chips\ntoilet paper\nyogurt\nsalami")
    mariowork = mario.mkdir('work?')
    mariowork.addFile('gcc.c', "Error: Access denied")
    mariowork.addFile('gnome.c', '#include<stdio.h>\n\nint main(void) {\n\tprintf("Ho ho ho ha ha, ho ho ho he ha. Hello there, old chum. I’m gnot a gnelf. I’m gnot a gnoblin. I’m a gnome. And you’ve been, GNOMED");\n\n\treturn(0);\n}')
    marioemails = mario.mkdir('emails')
    marioemails.addFile('gnome.email', "\nMario,\n\nWill you please remove command: gnome from Ailee? It is a useless command which\nwill do nothing but confuse her. You were supposed to implement the compiler for\nher so she can write her own programs.\n")
    marioemails.addFile('RE:gnome.email', "gno i will gnot")

def mkccc(game):
    cbank = game.add_computer('140.24.3.12', 'ccc')
    cbank.exploited = False
    cbank.open_port({19: 'ftp', 80: 'http', 443: 'https'})
    root = cbank.fs
    binDir = root.mkdir('bin')
    logDir = root.mkdir('log')
    homeDir = root.mkdir('home')
    homeDir.addFile('.masterpasswd.txt', """
  This password is used to request crypto currency transfer to trusted client when it is necessary.
  crypto currency master password hash: 3e7d9b3ad13837e0c0d370c9d348b3e3
  """)
    homeDir.addFile('crypto.exe',"""
  Error: Unreadable file
  """)

def mksafe(game):
    PASSWDS = {
        "admin": "banks4lyfe",
        "tom": "finance-is-cool",
        "john": "richguy123",
        "bill": "helpimbroke",
    }
    FILE_CONTENTS = """
  User acct.         Password
  {:<9}          {}
  {:<9}          {}
  {:<9}          {}
  {:<9}          {}
""".format(*sum(PASSWDS.items(), ()))
    newcomp = game.add_computer('120.45.30.6', 'safeandsecurebanking')
    newcomp.exploited = False
    newcomp.open_port({22: 'ssh', 80: 'http', 1100: 'unknown'})
    root = newcomp.fs
    binDir = root.mkdir('bin')
    logDir = root.mkdir('log')
    homeDir = root.mkdir('home')
    homeDir.addFile('passwords.txt', FILE_CONTENTS)
    homeDir.addFile('client-info.txt',
                    '''
                    Contact Information for Pro International Cybersecurity Solutions
                    Email: customersolutions@pics.com
                    Phone: 555-390-6971
                    ''')

COMPS = {
    'customersolutions@pics.com':[mkpics, '120.33.7.242'],
    'crypticcryptocurrency@ccc.com':[mkccc, '140.24.3.12'],
    'safeandsecurebanking@ssb.com':[mksafe, '120.45.30.6']
}


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) == 0 or emptyList or (len(args) == 2 and args[0] == '-a'), "Invalid use of iplist. See man page for details"

    game = kwargs['game']
    network = game.network
    if len(args) != 0:
        if args[1] in COMPS:
            try:
                getattr(network, COMPS[args[1]][1])
            except AttributeError:
                COMPS[args[1]][0](game)
        else:
            print("Unable to find address associated with {}".format(args[1]))
            return

    # Print out available IP addresses
    for address in network:
        print("{:<16} {}".format(address, network[address]))