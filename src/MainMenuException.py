'''
Custom Exception to allow the shutdown command to return to the main menu instead of exiting
'''

class MainMenuException(Exception):
    pass