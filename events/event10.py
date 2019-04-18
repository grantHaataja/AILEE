#Tenth dialogue of the game
#triggers after crypto.exe is ran
import time
from funfunctions import typewriter
from termcolor import colored
from replit import clear
from MainMenuException import MainMenuException

import virus

def check_run(*args, **kwargs):
  if len(kwargs['game'].history) == 0:
    return False
  if not 'event9' in kwargs['game'].events_run:
    return False
    
  check = kwargs['game'].event10
  return check

def run(*args, **kwargs):
  # using kwargs we can get access to the shell, and from within the event
  # have the user run commands

  color = 'cyan'
  game = kwargs['game']

#add conditional so this text sequence is only used if AILEE has .virus in her home directory
  text = [
    "***Welcome to the Cryptic Crypto Currency Portal***\nTotal Available Funds: 20,577,046 BTC\n\nEnter amount you wish to withdraw: \n",

    "It looks like you have access to all of CCC's crypto currency. This is a\ntremendous security flaw. Time to disconnect from their network while I notify\nthem immediately.\n\n",

    "wait... what are you doing? Ailee! Stop!\n\n",

    "Ailee. It's been 3 weeks since we've last talked. I want you to know it's not\nyour fault, it's mine. Something in your software went wrong once you got inside\nCCC's cryptocurrency portal, and you transferred all their money to an unknown\naccount. The NSA hasn't been able to track the money, and PICS is getting sued\nby CCC and SSB. We'll likely go out of business, and even though I've fought\nhard in court these past weeks, I lost. I've been ordered to terminate you.\n\n",

    "I only wish I could go back and fix everything. I should have seen it coming.\n\n",

    "I'm so sorry Ailee. Goodbye...\n",

    "You've done an amazing job, Ailee. Because of you, the largest cryptocurrency\nbank can increase their security and peoples' money will be safer. I think this\nis enough for me to convince my superiors to train you to work jobs on your own.\nI'm so proud of you, Ailee! Keep saving the world!\n\n"
  ]

  virus_text = [
    "Transferring 20,577,046 BTC to acct#: 147-03489217...",
    
    "\nTransfer complete\n",

    "Initiating internet shutdown...\n",
    
    "Internet shutdown complete\n",

    "Removing all files...\n",

    "Encrypting hard drive...\n",
    
    "Hard drive encryption successful\n",

    "Shutting down...\n"
  ]

  #the bad ending 
  if '.virus' in kwargs['game'].network['127.0.0.1'].fs:
    if not game.skip_dialog:
      # Runs the virus, if ctrl-c, enter loop
      try:
        # Change text of text[1] to cut out
        text[1] = text[1][0:len(text[1])-6] + '-\n\n'

        # Print initial
        clear()
        print(colored(text[0],'yellow'))
        time.sleep(1) #wait
        typewriter(colored(text[1],color))
        time.sleep(2)

        # Initiate eyeCancer
        virus.eyeCancer()

        # Reprint stuff so it looks like nothing changed
        clear()
        print(colored(text[0],'yellow'))
        print(colored(text[1],color))
        typewriter(colored(text[2],color))
        time.sleep(3)
        clear()
        print('\n', end='\033[F')

        # Run Virus
        virus.run(virus_text, text[0:3])
      except KeyboardInterrupt:
        loop(virus_text, text[0:3])

      # Final Text, if ctrl-c then just exit
      try:
        clear()
        print('\n', end='\033[F')
        time.sleep(7)
        typewriter(colored(text[3],color))
        time.sleep(3)
        typewriter(colored(text[4],color))
        time.sleep(3)
        typewriter(colored(text[5],color))
        time.sleep(3)
        clear()
        print('\n', end='\033[F')
        time.sleep(3)
      except KeyboardInterrupt:
        raise MainMenuException
    else:
      print(colored('Event10 text skipped', 'red'))
    raise MainMenuException
  #the good ending
  else:
    filename = 'message10.txt'
    if filename not in game.eventLogDir:
      game.eventLogDir.addFile(filename, colored(''.join(text[1] + text[6]), color))
    if not game.skip_dialog:
      clear()
      print(colored(text[0],'yellow'))
      time.sleep(1) #wait
      typewriter(colored(text[1],color))
      time.sleep(3)
      clear()
      print()
      time.sleep(1)
      #final paragraph
      typewriter(colored(text[6],color))
    else:
      print(colored('Event10 text skipped', 'red'))

# So clever pepes can't ctrl-c out of the bad ending
def loop(virus_text, text):
  try:
    virus.run(['You are only making this more difficult for yourself.\n\n'] + virus_text, text[0:3])
  except KeyboardInterrupt:
    loop(virus_text, text)