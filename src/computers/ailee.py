# -*- coding: utf-8 -*-

"""
Computer factory for the "base" computer -- the one that AILEE lives on
"""

import computer
import filesystem
from .execfiles import grabfile


def set_fs_owner(fs, name='ailee'):
    for objname in fs.children:
        obj = fs.children[objname]
        obj.owner = name
        if isinstance(obj, filesystem.Directory):
            if not objname in ['.', '..']:
                set_fs_owner(obj, name)


def mkailee(**kwargs):
    comp = computer.Computer('localhost',
                             game=kwargs['game'])
    kwargs['game'].eventLogDir = comp.fs.mkdir('chat_log')
    pDir = comp.fs.mkdir('go_here_first')
    pDir.addFile('readme.txt',
                 'The "run" command runs .exe files\n\nYou can use '
                 'the command "cd .." to move up a directory.')
    pDir.addPrebuiltFile(grabfile.get_exec_file(
        "localhost/go_here_first/executable.exe"
    ))
    pDir.addFile('.hiddenFile.txt',
                 'I am a hidden file.  Good job finding me!')

    prev = comp.fs
    for i in range(1, 11):
        prev = prev.mkdir("folder{}".format(i))
    prev.addFile('file.txt', 'belt')
    prev.addFile('.sign.txt', 'Mario was here')
    comp.add_user('Administrator')
    set_fs_owner(comp.fs)

    return '127.0.0.1', comp
