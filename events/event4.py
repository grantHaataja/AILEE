#Fourth dialogue of the game
#triggers after vulnerability scanning has been done
import time
from funfunctions import typewriter
from termcolor import colored

def check_run(*args, **kwargs):
  # check for 'vscan' in history
  if len(kwargs['game'].history) == 0:
    return False
  if not 'event3' in kwargs['game'].events_run:
    return False

  command = ['vscan', ['120.45.30.6']]

  a = kwargs['game'].history[-1] == command
  return a

def run(*args, **kwargs):
  # using kwargs we can get access to the shell, and from within the event
  # have the user run commands

  color = 'cyan'
  game = kwargs['game']

  text = [
    '\nExcellent, now we can see what specific vulnerabilities our target has.\n\n',
    'It looks like we\'re dealing with a computer runnning an outdated version of\nWindoors operating system. We can run one of the available exploits against our\ntarget whenever you\'re ready.\n\n'
  ]

  filename = 'message04.txt'
  if filename not in game.eventLogDir:
    game.eventLogDir.addFile(filename, colored(''.join(text), color))

  if not game.skip_dialog:
    typewriter(colored(text[0],color))
    time.sleep(3)
    typewriter(colored(text[1],color))
    time.sleep(3)
  else:
    print(colored('Event4 text skipped', 'red'))   

  # Create chat log in AILEE's directory
  