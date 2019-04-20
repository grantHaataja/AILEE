# -*- coding: utf-8 -*-

import computer


def mkccc(game):
    cbank = computer.Computer('ccc')
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
    return '140.24.3.12', cbank
