"""
 "How do I spell gcc?"

GNU C Compiler.  Used for compiling code.

Compiles a predetermined set of instructions into the executable file "a.exe" and
puts it in the current working directory.

Usage: gcc [filename]
"""


def run(*args, **kwargs):

    cwd = kwargs['cwd']
    if 'a.exe' not in cwd.children:
        cwd.addFile('a.exe', "Error: Unreadable file")
