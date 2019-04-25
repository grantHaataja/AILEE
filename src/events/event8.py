# Eighth dialogue of the game
# triggers after ftp connection has been established

import time
from funfunctions import typewriter
from termcolor import colored


def check_run(*args, **kwargs):
    # check for 'ftp 140.24.3.12' in history
    if len(kwargs['game'].history) == 0:
        return False
    if not 'event7' in kwargs['game'].events_run:
        return False

    cur_shell = kwargs['shell']
    comp = cur_shell.computer
    return ((comp.name == 'ccc') and
            (len(cur_shell.history) == 0))


def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        "Fantastic job, Ailee! You are in the file-sharing system between Safe "
        "and Secure Banking and\nCryptic Crypto Currency.\n\n",

        "Poke around and see what kind of sensitive data you can find.\n\n",

        "By the way, If you haven't been using the '-a' flag with ls, now "
        "would be a\ngood place to start. It allows you to see all files "
        "within the directory,\nincluding hidden files.\n\n"
    ]
    filename = 'message08.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0],color))
        time.sleep(3) #wait
        typewriter(colored(text[1],color))
        time.sleep(3)
        typewriter(colored(text[2],color))
    else:
        print(colored('Event8 text skipped', 'red'))
