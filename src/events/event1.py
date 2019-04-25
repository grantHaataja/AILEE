#First dialogue of the game
#triggers when game is run initially
import time
from funfunctions import typewriter
from termcolor import colored


def check_run(*args, **kwargs):
    return len(kwargs['game'].history) == 0


def run(*args, **kwargs):
    # using kwargs we can get access to the shell, and from within the event
    # have the user run commands

    color = 'cyan'
    game = kwargs['game']

    text = [
        'Hello there!\n\n',
        'It\'s okay, Ailee, take a few minutes to get your bearings. I '
        'understand this is\nconfusing for you, but let me explain.\n\n',
        'We are Pro International Cybersecurity Solutions, (PICS), a top-tier '
        'penetration\ntesting firm who assess the security of the systems of '
        'very important clients. In\nthe past few years our number of clients '
        'has grown so high that there aren\'t\nenough of us to take all the '
        'jobs.\n\n',
        'That\'s where you come in, Ailee. We created you to learn how to '
        'conduct\npenetration tests and help keep the systems of the world '
        'safe. Since you don\'t\nhave a body, you can work almost non-stop.\n\n',
        'Now there are people in this company and many regulators who are '
        'afraid of you\nbecause you have the ability to learn more than any '
        'human can and make perfect\ndecisions. So we have to do a few trial '
        'runs where I will monitor your progress\nclosely. But I believe in '
        'you. Once we show them that you are capable of doing\nmissions on '
        'your own, we can start protecting the world in full force. You '
        'are\ngoing to save the world, Ailee.\n\n',
        'I have to get the legal paperwork for your first mission figured out. '
        'In the\nmeantime, play around with your system commands. Type: help '
        'to see your\npossible actions, and type: man command_name to see what '
        'each specific action does.\nAlso keep in mind if you ever need to '
        'look back on what I\'ve said to you, it will all\nbe stored in your '
        'chat_log folder and you can view these files with the "read" '
        '\ncommand. I\'ll be back soon!\n\n'
    ]
    filename = 'message01.txt'
    # Create chat log in AILEE's directory
    if filename not in game.eventLogDir:
        game.eventLogDir.addFile(filename, colored(''.join(text), color))

    if not game.skip_dialog:
        typewriter(colored(text[0],color))
        time.sleep(2)
        typewriter(colored(text[1],color))
        time.sleep(3)
        typewriter(colored(text[2],color))
        time.sleep(3)
        typewriter(colored(text[3],color))
        time.sleep(3)
        typewriter(colored(text[4],color))
        time.sleep(3)
        typewriter(colored(text[5],color))
    else:
        print(colored('Event1 text skipped', 'red'))
