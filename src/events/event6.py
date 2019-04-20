# Sixth dialogue of the game
# triggers after sensitive file has been found

import time
from termcolor import colored

from funfunctions import clear, typewriter, dots


def check_run(*args, **kwargs):
    if len(kwargs['game'].history) == 0:
        return False
    if 'event5' not in kwargs['game'].events_run:
        return False

    # need to edit this

    command = ['read', ['passwords.txt']]

    a = kwargs['game'].history[-1] == command
    b = 'passwords.txt' in kwargs['cwd'].children
    return a and b


def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands
    color = 'cyan'
    game = kwargs['game']
    game.events_run.append('event6')  # hack to prevent infinite looping

    text = [
        'That looks like a sensitive file. I think you\'ve proven that you can '
        'hack now,\nAilee. Congratulations, your first mission has been a '
        'great success.\n\n',

        'We have a software update prepared for you. Don\'t be afraid, it will '
        'be just\nlike going to sleep. And when you wake up, you\'ll have '
        'increased functionality.\nAnd then we have a serious mission for you.\n\n',

        "Hello, Ailee. Your software update is complete. If you type 'help' "
        "you can see\nthat you have 2 new commands that you can use.\n\n",

        'Make sure to read the manual pages on them by using the man '
        'command.\nYour new commands are "ftp" and "passrip"\n\n'
    ]

    # Add new commands for AILEE
    kwargs['game'].add_commands('passrip', 'ftp', )

    # Create virus in AILEE's directory
    comp = kwargs['game'].network['127.0.0.1']
    filename = '.virus'
    eventname = 'messages05b.txt'
    a = filename not in comp.fs
    b = getattr(kwargs['game'], '.virus', True)
    c = eventname not in game.eventLogDir
    if a and b and c:
        comp.fs.addFile(filename, 'Error: Access denied')

    filename = 'message06.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0],color))
        time.sleep(3)  # wait
        typewriter(colored(text[1],color))
        time.sleep(1)

        # Software Update Event
        clear()
        dots('Software update in progress', 10, 1)
        clear()
        print('Software update complete')
        time.sleep(1)
        typewriter(colored(text[2],color))
        time.sleep(2)
        typewriter(colored(text[3],color))
    else:
        print(colored('event6 text skipped', 'red'))
