"""
"Love Story"

Description: Lists the current directory's contents, which can be files or other
directories (keep in mind the current directory may be empty)

Items listed in blue are directories (folder) and in green are executable
files.
"""

from termcolor import colored
import argparse

import filesystem

# use """list(kwargs['cwd'])""" to get the current working directory's contents

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    '-l',
    action='store_true',
    dest='listMode',
    help='list in long format'
)
parser.add_argument(
    '-a',
    action='store_true',
    dest='listAll',
    help='do not ignore entries starting with .'
)
parser.add_argument(
    'folder',
    nargs='?',
    type=str,
    default='.',
    help='folder to list.  defaults to current working directory'
)


def run(*args, **kwargs):
    try:
        args = parser.parse_args(args)
    except SystemExit as exc:
        return
    listAll = args.listAll
    listMode = args.listMode
    dirsToSearch = []
    if len(dirsToSearch) == 0:
        listDir(kwargs['cwd'].children, listAll, listMode)
    else:
        print('Invalid use of ls. See manual page for details')


def listDir(contents, listAll, listMode):

    if not listAll:
        dolist = [x for x in contents.keys() if x[0] != '.']
    else:
        dolist = list(contents.keys())

    output = []

    for name in dolist:
        obj = contents[name]
        out = name

        if isinstance(obj, filesystem.Directory):
            out = colored(name, 'blue', None, ['bold'])
        elif 'x' in obj.permissions:
            out = colored(name, 'green', None, ['bold'])

        output.append(out)

    maxnamelen = max([len(s) for s in output]) + 4
    maxownerlen = max([len(contents[s].owner) for s in dolist])
    maxsize = max(len(str(len(contents[s]))) for s in dolist)
    final_output = ""

    for i in range(len(output)):
        obj = contents[dolist[i]]
        out = output[i]
        ptype = 'd' if isinstance(obj, filesystem.Directory) else '-'
        if listMode:
            out = f"{ptype}{obj.permissions} {obj.owner:<{maxownerlen}} {len(obj):>{maxsize}} {out}\n"
        else:
            out = f"{out:<{maxnamelen}}"

        final_output += out

    # in listMode, the trailing newline on the end of the format string takes
    # care of the necessary last newline
    if listMode:
        print(final_output, end='')
    else:
        print(final_output)
