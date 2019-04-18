# -*- coding: utf-8 -*-
'''
"echo... echo..."

Description: prints input to terminal screen

Usage: echo [text]
'''

def run(*args, **kwargs):
    """
    Return whatever was put in.
    """
    print(' '.join([str(s) for s in args]))