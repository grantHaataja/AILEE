# -*- coding: utf-8 -*-

import filesystem
import shell
import executables
import funfunctions


class Computer(object):
    """
    A glorified rock that does math really, *really* fast.
    """
    def __init__(self, name, *args, **kwargs):
        """
        Put lightning into the math rock.
        """
        self.name = name
        self.fs = filesystem.Directory()
        self.game = kwargs.get('game', None)
        self.ports = kwargs.get('ports', {})
        self.users = kwargs.get('users', {})
        self.vulns = kwargs.get('vulns', {})

    def get_shell(self, user, agent=None):
        """
        Get a shell for a specific agent/user.
        """
        return shell.Shell(self, user, agent=agent, game=self.game)

    def open_port(self, ports):
        for port_no, service in ports.items():
            if port_no in self.ports.keys():
                self.ports[port_no] = service
            else:
                self.ports.update({port_no: service})

    def add_user(self, username):
        self.users.update({username:User(username)})

    def get_user(self, username):
        try:
            return self.users[username]
        except KeyError:
            return None

    def login(self, username, password):
        try:
            if self.users[username].password == password:
                return True
            else:
                return False
        except KeyError:
            return None

    def __repr__(self):
        return self.name
    __str__ = __repr__  # set __str__ as the same method as __repr__


class User:
    '''
    User Account for a computer
    '''
    def __init__(self, name, password=None):
        self.name = name
        self.password = password or funfunctions.passwordRandomizer()

    def changePassword(self, password):
        self.password = password

    def __repr__(self):
        return self.name
    __str__ = __repr__  # set __str__ as the same method as __repr__
