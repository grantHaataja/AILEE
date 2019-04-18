#Ninth dialogue of the game
#triggers after master password is found
import time
from funfunctions import typewriter
from termcolor import colored

def check_run(*args, **kwargs):
  # check for 'ftp 140.24.3.12' in history
  if len(kwargs['game'].history) == 0:
    return False
  if not 'event8' in kwargs['game'].events_run:
    return False

  command = ['read', ['.masterpasswd.txt']]
  a = kwargs['game'].history[-1] == command
  b = kwargs['game'].history.count(command) == 1
  return a and b


def run(*args, **kwargs):
  # using kwargs we can get access to the shell, and from within the event
  # have the user run commands

  color = 'cyan'
  game = kwargs['game']

  text = [
    "Whoa! That is an extremely sensitive file. If that password hash got into the wrong\nhands, it could destroy CCC completely!\n\n",

    "Try to crack the hash with passrip and see if you can get the master password. If\nyou can, run the cryptobank executable file and see if you can login with the password.\n\n"
  ]
  filename = 'message09.txt'
  if filename not in game.eventLogDir:
    game.eventLogDir.addFile(filename, colored(''.join(text), color))

  if not game.skip_dialog:
    typewriter(colored(text[0],color))
    time.sleep(3) #wait
    typewriter(colored(text[1],color))
  else:
    print(colored('Event9 text skipped', 'red'))

  # Create chat log in AILEE's directory
  