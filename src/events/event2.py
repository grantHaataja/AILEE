#Second dialogue of the game
#triggers after player has run 20? commands
import time
from funfunctions import typewriter, passwordRandomizer
from termcolor import colored

def check_run(*args, **kwargs):
  # number of commands run more than 20
  if not 'event1' in kwargs['game'].events_run:
    return False
  return len(kwargs['game'].history) == 10

def run(*args, **kwargs):
  # using kwargs we can get access to the shell, and from within the event
  # have the user run commands

  color = 'cyan'
  game = kwargs['game']

  text = [
    '\nHello, Ailee!\n\n',
    'I have good news. We\'ve been approved for your first mission. Our client is a\nsmall but quickly-growing banking chain. As they expand their reach, they\nbecome more and more at risk of being attacked and having the accounts of their\ncustomers compromised.\n\n',

    'Your job is to do all the phases of a standard penetration test and see if you\ncan gain access to their systems. I\'ll be guiding you the whole way. But don\'t\nforget that you are not allowed to change anything on the systems. We just want\nto see what information we can access.\n\n',

    'The first thing you have to do is Information Gathering. The email address of\nour target is "safeandsecurebanking@ssb.com". Using their email, you can find\ntheir IP address. I would recommend reading the manual page for the iplist\ncommand in order to do so.\n\n',

    'Once you have added their IP address, do some port scanning. Let\'s see what\nkind of security they have.'
  ]
  filename = 'message02.txt'
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
  else:
    print(colored('Event2 text skipped', 'red'))

  # Create chat log in AILEE's directory
  