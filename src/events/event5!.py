#Third ending dialogue of the game
#triggers after Ailee does run runme.exe
import time
from funfunctions import typewriter
from termcolor import colored
from funfunctions import clear
from MainMenuException import MainMenuException
import virus

def check_run(*args, **kwargs):
    # check for 'read .notes.txt' in history
    if len(kwargs['game'].history) == 0:
        return False
    if not 'event5a' in kwargs['game'].events_run:
        return False
    return kwargs['game'].forkbomb

def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'red'
    game = kwargs['game']

    text = ["Ha! You thought you could hack Jason the Unhackable? Never. Prepare for death...\n\n"]

    virus_text = [
        'Incoming forkbomb',
        '.',
        '.',
        '.\n',
        'System Error. Shutting Down.\n'
    ]

    if not game.skip_dialog:
        try:
            virus.eyeCancer()
            clear()
            typewriter(colored(text[0], color))
            time.sleep(3)  # wait
            clear()
            print('\n', end='\033[F')
            virus.run(virus_text, text)
        except KeyboardInterrupt:
            loop(virus_text, text)

        # Stare at a blank screen for the last seconds. Catch ctrl-c and leave
        try:
            clear()
            print('\n', end='\033[F')
            time.sleep(3)
        except KeyboardInterrupt:
            raise MainMenuException
    else:
        print(colored('Event5! text skipped', 'red'))
    raise MainMenuException

def loop(virus_text, text):
    try:
        virus.run(['You are only making this more difficult for yourself.\n\n'] + virus_text, text[0:3])
    except KeyboardInterrupt:
        loop(virus_text, text)