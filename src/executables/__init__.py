__all__ = []

import os
files = [f for f in os.listdir('executables') if f.endswith('.py')]
__all__ = [f[:-3] for f in files if not f.startswith('__')]

BLACKLIST_COMMANDS = [
  'pyd'
]

from executables import *