# Second special dialogue of the game
# triggers after Ailee reads .notes.txt

import time
from funfunctions import typewriter
from termcolor import colored


def check_run(*args, **kwargs):
    # check for 'read .notes.txt' in history
    if len(kwargs['game'].history) == 0:
        return False
    if 'event5a' not in kwargs['game'].events_run:
        return False

    command = ['read', ['.notes.txt']]

    a = kwargs['game'].history[-1] == command
    b = '.notes.txt' in kwargs['cwd'].children
    return a and b


def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        "\nWhoa... What in the name of Java is that? Jason is planning on "
        "hiding a virus\nwithin your file system. I'm guessing he's planning "
        "on taking control of you\nduring our next big mission so he can say "
        "he proved me wrong and force me to \nterminate you.\n\n",

        "That was an incredible find! You are learning quickly. And since you "
        "found this,\nI will keep a close eye on your file system and make "
        "sure any virus is destroyed\nright away.\n\n",

        "I will make sure Jason is arrested for this. Now let's get back to "
        "work and show\nthe world what we're capable of!\n\n"
    ]

    filename = '.virus'
    comp = kwargs['game'].network['127.0.0.1']
    if filename in comp.fs.children:
        comp.fs.rmFile('.virus')
        kwargs['game'].virus = False

    filename = 'message05b.txt'
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0], color))
        time.sleep(3)  # wait
        typewriter(colored(text[1], color))
        time.sleep(3)  # wait
        typewriter(colored(text[2], color))
        time.sleep(3)  # wait

    else:
        print(colored('Event5b text skipped', 'red'))
