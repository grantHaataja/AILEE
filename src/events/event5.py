#Fifth dialogue of the game
#triggers after exploit has been run successfully
import time
from funfunctions import typewriter
from termcolor import colored

def check_run(*args, **kwargs):
    # check for 'vscan' in history
    if len(kwargs['game'].history) == 0:
        return False
    if not 'event4' in kwargs['game'].events_run:
        return False

    #need to edit this to run after exploit has run properly

    cur_shell = kwargs['shell']
    comp = cur_shell.computer
    return ((comp.name == 'safeandsecurebanking') and
            (len(cur_shell.history) == 0))

def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        'Fantastic job, Ailee! You\'ve successfully exploited the system.\n\n',
        'Now that you have access to a machine on the target\'s network, see what kind of\nsensitive information you can find. Just remember not to try to change anything\nyou find.\n\n'
    ]
    filename = 'message05.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0], color))
        time.sleep(3)  # wait
        typewriter(colored(text[1], color))
        time.sleep(3)  # wait

    else:
        print(colored('Event5 text skipped', 'red'))

    # Create chat log in AILEE's directory
