__all__ = []

import os
files = [f for f in os.listdir('events') if f.endswith('.py')]
__all__ = [f[:-3] for f in files if not f.startswith('__')]
__events__ = [f for f in __all__ if f.startswith('event')]

from events import *