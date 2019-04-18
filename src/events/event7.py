# Seventh dialogue of the game
# triggers after man pages on the new commands have been run

import time
from funfunctions import typewriter
from termcolor import colored


def check_run(*args, **kwargs):
    # check for 'man ftp' and 'man passrip' in history
    if len(kwargs['game'].history) == 0:
        return False
    if 'event6' not in kwargs['game'].events_run:
        return False

    # might need to delete this code?
    # need to make it so event triggers after 'man ftp' and 'man passrip' run
    command1 = ['man', ['ftp']]
    command2 = ['man', ['passrip']]

    a = kwargs['game'].history.count(command1) >= 1
    b = kwargs['game'].history.count(command2) >= 1

    c = kwargs['game'].history[-1] in [command1, command2]

    return a and b and c


def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        "Good, now that you've read up on your new commands, let's get to "
        "work.\n\n",
        "Your next target is the largest crypto currency bank in existence "
        "today. The\nonly information we have about them is their name, "
        "Cryptic Crypto Currency and their\nofficial email address, "
        "crypticcryptocurrency@ccc.com.\n\n",
        "There is one other bit of information that could make all the "
        "difference in this\ntest. Safe and Secure Banking is a client of "
        "CCC, they gain most of their cryptocurrency\ncapital from them. "
        "CCC's network will be heavily secured, so you won't be able to run "
        "an\nexploit on them, but there is an ftp file sharing connection "
        "between SSB and CCC.\n\n",
        "With the new functionality we've added, you can use the passwords "
        "you found from\nSafe and Secure Banking to get ftp access into the "
        "file system and see what\ninformation you can find.\n\n"
    ]
    filename = 'message07.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0], color))
        time.sleep(3) # wait
        typewriter(colored(text[1], color))
        typewriter(colored(text[2], color))
        time.sleep(3) # wait
        typewriter(colored(text[3], color))
        time.sleep(3) # wait
    else:
        print(colored('Event7 text skipped', 'red'))

    # Create chat log in AILEE's directory
