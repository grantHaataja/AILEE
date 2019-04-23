"""
"Love Story"

Description: Lists the current directory's contents, which can be files or other\ndirectories (keep in mind the current directory may be empty)

Items listed in blue are directories (folder)

Option -la (long list all): Lists the current directory's contents in long list\nformat

Usage: ls

Usage: ls -la (for long list format)
"""

from termcolor import colored

import filesystem

# use """list(kwargs['cwd'])""" to get the current working directory's contents


def run(*args, **kwargs):
    listAll = False
    listMode = False
    dirsToSearch = []
    for arg in args:
        if arg[0] == '-':
            if 'a' in arg:
                listAll = True
            if 'l' in arg:
                listMode = True
        elif '.' not in arg:
            dirsToSearch += [arg]
    if len(dirsToSearch) == 0:
        listDir(kwargs['cwd'].children, listAll,     listMode)
    else:
        print('Invalid use of ls. See manual page for details')


def listDir(contents, listAll, listMode):

    if not listAll:
        dolist = [x for x in contents.keys() if x[0] != '.']
    else:
        dolist = contents.keys()

    maxnamelen = max([len(s) for s in dolist]) + 4
    maxsize = max(len(contents[s]) for s in dolist)
    output = ""

    for name in dolist:
        obj = contents[name]
        out = name

        if isinstance(obj, filesystem.Directory):
            out = colored(name, 'blue', None, ['bold'])
        elif 'x' in obj.permissions:
            out = colored(name, 'green', None, ['bold'])

        if listMode:
            out = f"{out:{maxnamelen}} {obj.permissions} {len(obj):>{maxsize}}\n"
        else:
            out = f"{out:{maxnamelen}}"

        output += out
    print("maxnamelen: {}".format(maxnamelen))
    print(output)

    if not listMode and contents:
        print()
