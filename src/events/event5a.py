#First special dialogue of the game
#triggers after exploit against PICS has been run successfully
import time
from funfunctions import typewriter
from termcolor import colored

def check_run(*args, **kwargs):
    # check for 'vscan' in history
    if len(kwargs['game'].history) == 0:
        return False
    if not 'event5' in kwargs['game'].events_run:
        return False

    cur_shell = kwargs['shell']
    comp = cur_shell.computer
    return ((comp.name == 'picsHelpDesk') and
            (len(cur_shell.history) == 0))

def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        "Hey! This isn't one of your targets, this computer belongs to your developers.\nYou shouldn't be looking in here...\n\n",

        "Okay fine, you're still learning. Feel free to have a look around and read some \nof the code they're working on. Use the shell command to switch back to the\nsafeandsecurebanking computer when you're done so you can continue with the\npenetration test.\n\n"
    ]
    filename = 'message05a.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0], color))
        time.sleep(3)  # wait
        typewriter(colored(text[1], color))
        time.sleep(3)  # wait

    else:
        print(colored('Event5a text skipped', 'red'))

    # Create chat log in AILEE's directory
