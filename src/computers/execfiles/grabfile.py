# -*- coding: utf-8 -*-

"""
Handles manufacture of executable files as used in the filesystem of
"computers".
"""

import filesystem
import os

FILES = {
    "localhost/go_here_first/executable.exe": 'ailee_base_exec.py',
}
RUNTIME_PREFIX = '/computers/execfiles/'


def get_exec_file(path):
    """
    Returns the File object that can be used to represent the executable
    file.
    :param path: The path to the file: {computer_name}/{path}
    :return: filesystem.File object.
    """

    infilename = FILES[path]
    if infilename not in os.listdir(os.getcwd() + RUNTIME_PREFIX):
        print("cwd: {}\n{}".format(os.getcwd(), os.listdir('.')))
        return None

    with open(os.getcwd() + RUNTIME_PREFIX + infilename, 'r') as infile:
        contents = infile.read()

    newfile = filesystem.File(
        path.split('/')[-1],
        contents,
        permissions='--x',
    )

    return newfile
