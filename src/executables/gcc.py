"""
 "How do I spell gcc?"

GNU C Compiler.  Used for compiling code.

Compiles a predetermined set of instructions into the executable file "a.exe" and
puts it in the current working directory.

Usage: gcc [filename]
"""

import computers.execfiles.grabfile as grabfile


def run(*args, **kwargs):

    cwd = kwargs['cwd']
    if 'a.exe' not in cwd.children:
        cwd.addPrebuiltFile(
            grabfile.get_exec_file("a.out")
        )
