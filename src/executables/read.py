'''
"Better than looking at cat pics"

Description: Prints contents of a file to the terminal screen

Usage: read file_name.txt
'''

def run(*args, **kwargs):
  assert len(args) == 1, "Must specify a file to read.\n\nUsage: read [filename]"
  assert '.' in args[0], "target must be a file"

  cdir = kwargs['cwd']
  f = cdir[args[0]]
  data = f.data
  print(data)