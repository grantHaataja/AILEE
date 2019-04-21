"""
Miscellaneous functions for FUN!
"""

from time import sleep
from termcolor import colored
from getpass import getpass
import random
import secrets
import sys
import curses
import os
import platform


class TwoWayDictionary(dict):

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        dict.__setitem__(self, val, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)


def clear():
    if platform.system() == 'Linux':
        cls = lambda: os.system('clear')
    elif platform.system() == 'Windows':
        cls = lambda: os.system('cls')
    cls()


def typewriter(text, speed='FAST'):
    """
      Prints text to the screen as if it was being typed
    """
    if speed == 'NORM':
        speed = 0.1
    elif speed == 'FAST':
        speed = 0.05
    elif speed == 'SLOW':
        speed = 0.2
    else:
        print('DIS BROKE YO, FUN FUNCTION NOT FUN ANYMORE.  PREPARE FOR PUNISHMENT')
        speed = 10
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(speed)


def dots(text, n_dots, delay):
    """
    Running............
    Adds dots with delay.
    """
    for i in range(n_dots):
        print(text + '.'*i, end='\r')
        sleep(delay)
    print(text + '.'*i)


def login(username=None, password=None):
    print(colored('Username: \nPassword: \033[F\033[F', 'green'), end='')
    if username is not None:
        print(colored("Username: ", 'green'), end='')
        sleep(0.5)
        typewriter(username + '\n', 'SLOW')
    else:
        username = input(colored('Username: ', 'green'))

    if password is not None:
        print(colored("Password: ", 'green'), end='')
        sleep(0.5)
        typewriter(('*' * len(password)) + '\n', 'SLOW')
    else:
        password = getpass()

    return username, password


def startAilee():
    print(colored('Administrator: ~/$ \n\033[F', 'green'), end='')
    sleep(2)
    print(colored('Administrator: ~/$ ', 'green'), end='')
    typewriter('AILEE.exe', 'SLOW')
    sleep(0.5)


def passwordRandomizer(password='password', difficulty=0):
    """
      Auto-generates a password and returns it, based on a difficulty provided.

      Default difficulty is 0, and generates a password in the form of "password" but with random letters replaced with symbols and a random number of iterative numbers following. (ex: Pa5sw0rD1234)

      For any other difficulty specified, returns a password of length $difficulty using random tokens from the secrets module.
    """
    if difficulty == 0:
        password = list(password)
        i = 0
        while i < len(password):
            if random.randint(0,3) == 0:
                password[i] = replaceToken(password[i])
            i += 1
        newPassword = ''
        for char in password:
            newPassword += char
        password = newPassword
    else:
        password = secrets.token_urlsafe(difficulty)
    return password


def replaceToken(token):
    """
    This-for-that function to replace letters in a password with harder to crack variants
    """
    mapping = {
        'p': 'P',
        'a': '@',
        's': '5',
        'w': 'W',
        'o': '0',
        'r': 'R',
        'd': 'D',
    }
    return mapping.get(token, token)
