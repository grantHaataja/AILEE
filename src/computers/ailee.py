# -*- coding: utf-8 -*-

"""
Computer factory for the "base" computer -- the one that AILEE lives on
"""

import time

import computer
import filesystem
from .execfiles import grabfile


def mkailee(**kwargs):
    comp = computer.Computer('localhost',
                             game=kwargs['game'])
    kwargs['game'].eventLogDir = comp.fs.mkdir('chat_log', owner='ailee')
    pDir = comp.fs.mkdir('go_here_first', owner='ailee')
    pDir.addFile('readme.txt',
                 'The "run" command runs .exe files\n\nYou can use '
                 'the command "cd .." to move up a directory.',
                 owner='ailee')
    pDir.addPrebuiltFile(grabfile.get_exec_file(
        "localhost/go_here_first/executable.exe",
        owner='ailee',
    ))
    pDir.addFile('.hiddenFile.txt',
                 'I am a hidden file.  Good job finding me!',
                 owner='ailee')

    prev = comp.fs
    for i in range(1, 11):
        prev = prev.mkdir("folder{}".format(i), owner='ailee')
    prev.addFile('file.txt', 'belt', owner='ailee')
    prev.addFile('.sign.txt', 'Mario was here', owner='ailee')
    comp.add_user('Administrator')

    pDir.mkdir('test_nested', owner='ailee')

    return '127.0.0.1', comp
