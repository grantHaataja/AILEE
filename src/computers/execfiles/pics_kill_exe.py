import termcolor
import time
#import os

if 'event5!' in kwargs['game'].events_run:
    kwargs['game'].events_run.remove('event5!')
kwargs['game'].forkbomb = True

print(termcolor.colored(
    "You thought you could hack Jason the unhackable?!  HA!",
    'red'
))

time.sleep(1.5)

print(termcolor.colored(
    "PREPARE TO DIE!!!",
    'red',
    attrs=['bold']
))

# Forkbomb!
# TODO: maybe we shouldn't *actually* forkbomb the player's IRL computer
#       it gets kind of annoying to playtest this part
#while True:
#    os.fork()
