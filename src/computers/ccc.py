# -*- coding: utf-8 -*-

import computer
import funfunctions
import execfiles.grabfile as grabfile

def mkccc(**kwargs):
    cbank = computer.Computer('ccc',
                              game=kwargs['game'])
    cbank.exploited = False
    cbank.open_port({19: 'ftp', 80: 'http', 443: 'https'})
    root = cbank.fs
    binDir = root.mkdir('bin')
    logDir = root.mkdir('log')
    homeDir = root.mkdir('home')

    newpwd = funfunctions.passwordRandomizer("$tL8wn@mI0")
    print("About to add {}".format(newpwd))
    kwargs['game'].add_pwd(newpwd)

    homeDir.addFile('.masterpasswd.txt', """
  This password is used to request crypto currency transfer to trusted client when it is necessary.
  crypto currency master password hash: {}
  """.format(kwargs['game'].pw_database[newpwd]))
    homeDir.addPrebuiltFile(grabfile.get_exec_file(
        'localhost/go_here_first/executable.exe'))

    return '140.24.3.12', cbank
