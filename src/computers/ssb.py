# -*- coding: utf-8 -*-

import computer


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


def mksafe(**kwargs):
    newcomp = computer.Computer('safeandsecurebanking', vulns={
        'WD45_702 reverse tcp shell': [False, 1100],
    },
                                game=kwargs['game'])
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
    return '120.45.30.6', newcomp
