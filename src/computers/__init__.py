# -*- coding: utf-8 -*-

__all__ = []

import os
files = [f for f in os.listdir('computers') if f.endswith('.py')]
__all__ = [f[:-3] for f in files if not f.startswith('__')]


from computers import *
