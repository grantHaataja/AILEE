"""
"Run, run, as fast as you can. You can't catch me, I'm the gingerbread man!"

Description: Runs an executable file

Usage: run file_name.exe
"""

from termcolor import colored


def forkbomb():
    pass


def run(*args, **kwargs):
    assert len(args) == 1, \
        "Must specify an executable to run.\n\nUsage: run [executable]"

    if args[0].split('.')[-1] != 'exe':
        print("Unable to run file, must be .exe")
        return

    if args[0] == 'crypto.exe':
        if ((kwargs['computer'].name == 'ccc') and
                ('crypto.exe' in kwargs['cwd'].children)):

            pwd = input("Enter master password > ")
            if pwd == "%tL8wn@mI0":
                kwargs['game'].event10 = True
            else:
                print(colored("Access denied", "red"))

    if args[0] == 'a.exe':
        if 'a.exe' in kwargs['cwd'].children:
            print("Segmentation fault (core dumped)")

    if args[0] == 'runme.exe':
        if 'runme.exe' in kwargs['cwd'].children:
            if 'event5!' in kwargs['game'].events_run:
                kwargs['game'].events_run.remove('event5!')
            kwargs['game'].forkbomb = True

    if args[0] == 'executable.exe':
        if 'executable.exe' in kwargs['cwd'].children:
            print('I am an executable file! You just ran me.')
