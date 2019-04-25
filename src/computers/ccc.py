# -*- coding: utf-8 -*-

import computer
import funfunctions
from .execfiles import grabfile


def mkccc(**kwargs):
    cbank = computer.Computer('ccc',
                              game=kwargs['game'])
    cbank.open_port({19: 'ftp', 80: 'http', 443: 'https'})
    root = cbank.fs
    binDir = root.mkdir('bin')
    logDir = root.mkdir('log')
    homeDir = root.mkdir('home')

    newpwd = funfunctions.passwordRandomizer("$tL8wn@mI0")
    print("About to add {}".format(newpwd))
    kwargs['game'].add_pwd(newpwd)

    for key, val in kwargs['game'].pw_database.items():
        if val[0] == newpwd:
            cbank.crypto_exec_pwd_hash = key
            break

    homeDir.addFile('.masterpasswd.txt', """
  This password is used to request crypto currency transfer to trusted client when it is necessary.
  crypto currency master password hash: {}
  """.format(key))  # key is the hash from the earlier for loop
    homeDir.addPrebuiltFile(grabfile.get_exec_file(
        'ccc/home/crypto.exe'
    ))

    return '140.24.3.12', cbank
