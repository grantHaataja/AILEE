'''
You ran a lot of commands.
'''

def check_run(*args, **kwargs):
  return len(kwargs['game'].history) == 1000000

def run(*args, **kwargs):
  print("You just ran your millionth command. Nerd.")