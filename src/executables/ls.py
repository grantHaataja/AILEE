"""
"Love Story"

Description: Lists the current directory's contents, which can be files or other\ndirectories (keep in mind the current directory may be empty)

Items listed in blue are directories (folder)

Option -la (long list all): Lists the current directory's contents in long list\nformat

Usage: ls

Usage: ls -la (for long list format)
"""

from termcolor import colored

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
        listDir(list(kwargs['cwd']), listAll, listMode)
    else:
        print('Invalid use of ls. See manual page for details')


def listDir(contents, listAll, listMode):
    if not listAll:
        contents = [x for x in contents if x[0] != '.']
    for item in contents:
        if '.' not in item:
            item = colored(item, 'blue', None, ['bold'])
        elif len(item) > 4 and item[::-1][0:4] == 'exe.':
            item = colored(item, 'green', None, ['bold'])
        print(item, end=('\n' if listMode else '     '))
    if not listMode and contents:
        print()
