'''
"Clear your screen you dirty animal"

Description: clears all text from the terminal screen

Usage: clear
'''

import funfunctions

def run(*args, **kwargs):
  emptyList = True
  for arg in args:
    if arg:
      emptyList = False
  assert len(args) == 0 or emptyList, "Invalid use of clear.\n\nUsage: clear"
  funfunctions.clear()