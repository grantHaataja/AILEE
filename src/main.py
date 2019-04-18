'''
Run the game
'''

"""
Changes made by Misha after you left:
 - Implemented GCC as described (creates a.exe in CWD, `run`ning that segfaults)
 - Increase folder count from 5 to 15 (shits'n'giggles)
 - Removed generic traceback printer -- errors are now handled more politely

Playthrough bugs that should now be fixed:
 - CtrlC'ing during an event no longer prevents message file creation (moved to top)
 - `ls` prints folders in blue
 - Empty commands no longer do anything
 - AILEE@<whatever computer you're on>
 - shell <nonexistent shell number> no longer throws errors
 - vscan doesn't "scan" nonexistant computers
 - exploit doesn't "exploit" nonexistant computers

Things Spencer suggested that aren't implemented (probably don't bother, not worth time):
 - Catching CtrlC before the shell loop enters, i.e. login/title screen
 - Email from address (I think we decided not to do this)
 - `shell` command needs more explanation/better man page
"""


from game import Game
from MainMenuException import MainMenuException
import funfunctions

from funfunctions import clear
import time

while True:
  # Create the game, agent, computer; and get a shell
  game = Game()
  if game.leave:
    break
  ailee = game.spawn_agent("Ailee")
  comp = game.add_computer('127.0.0.1', 'localhost')
  game.eventLogDir = comp.fs.mkdir('chat_log')
  pDir = comp.fs.mkdir('go_here_first')
  pDir.addFile('readme.txt', 'The "run" command runs .exe files.\n\nYou can use the command "cd .." to move up a directory')
  pDir.addFile('executable.exe', """
  Error: Unreadable file
  """)
  pDir.addFile('.hiddenFile.txt', 'I am a hidden file, good job finding me!')
  prev = comp.fs
  for i in range(1, 11):
    prev = prev.mkdir("folder{}".format(i))
  prev.addFile('file.txt', 'belt')
  prev.addFile('.sign.txt', 'Mario was here')
  comp.add_user('Administrator')
  if not game.skip_dialog:
    clear()
    funfunctions.login(comp.get_user('Administrator').name, comp.get_user('Administrator').password)
    clear()
    funfunctions.startAilee()
  ailee.login(comp)
  try:
    ailee.shells[0].start_shell_loop()
    print("Just broke out of main loop")
    time.sleep(10)
  except MainMenuException:
    pass # So the shutdown command returns to the main menu instead of exiting