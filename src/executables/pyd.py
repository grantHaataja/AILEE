'''
"Python debugger"

Description: Executes whatever follows as Python code

Usage: Not for civilian use
'''

def run(*args, **kwargs):
    assert kwargs['game'].skip_dialog, 'Dev Access required'
    print(kwargs)
    if args:
        exec(' '.join(args))