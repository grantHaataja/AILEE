# -*- coding: utf-8 -*-

"""
Computer factory for the "base" computer -- the one that AILEE lives on
"""

import computer

def mkailee(**kwargs):
    comp = computer.Computer('localhost',
                             game=kwargs['game'])
    kwargs['game'].eventLogDir = comp.fs.mkdir('chat_log')
    pDir = comp.fs.mkdir('go_here_first')
    pDir.addFile('readme.txt',
                 'The "run" command runs .exe files\n\nYou can use '
                 'the command "cd .." to move up a directory.')
    pDir.addFile('executable.exe', 'Error: Unreadable file',
                 permissions='--x')
    pDir.addFile('.hiddenFile.txt',
                 'I am a hidden file.  Good job finding me!')

    prev = comp.fs
    for i in range(1, 11):
        prev = prev.mkdir("folder{}".format(i))
    prev.addFile('file.txt', 'belt')
    prev.addFile('.sign.txt', 'Mario was here')
    comp.add_user('Administrator')

    return '127.0.0.1', comp
