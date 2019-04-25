"""
The almighty Game class.

Really just here to keep track of events and physical-level abstractions -- things that exist "physically", ie computers and agents.
"""

import hashlib

from computer import Computer, User
import title


class Game(object):
    """
    Handles Game objects.
    """

    def __init__(self):
        """
        Create a new Game.  No arguments needed, all setup happens here.
        """

        self.agents = []
        self.network = {}
        self.history = []
        self.events_run = []
        self.eventLogDir = None  # Set in main.py
        self._variables = {}
        self.event10 = False
        self.forkbomb = False
        self.vuln_database = []
        self.pw_database = {}

        self.allowed_commands = [
            'cd', 'clear', 'echo', 'gnome', 'help', 'iplist', 'ls', 'man',
            'ping', 'pscan', 'shell', 'shutdown', 'vscan', 'exploit', 'pyd',
            'read', 'run', 'gcc', 'passrip',
        ]

        # Run intro
        try:
            self.skip_dialog = title.run()
            self.leave = self.skip_dialog is None
        except KeyboardInterrupt:
            self.leave = False

    def add_commands(self, *commands):
        """
        Adds commands to the allowed list.
        """
        for command in commands:
            if command in self.allowed_commands:
                continue
            else:
                self.allowed_commands.append(command)
        self.allowed_commands.sort()

    def add_vuln(self, vuln):
        """
        Add a vulnerability to the vuln database if not already present.
        :param vuln: Name of vulnerability to add.
        :return: nothing
        """
        if vuln not in self.vuln_database:
            self.vuln_database.append(vuln)
            self.vuln_database.sort()

    def add_pwd(self, pwd):
        """
        Add a new password to the global database.
        :param newpwd: New password to add
        :return: nothing
        """
        if pwd not in self.pw_database:
            md5 = hashlib.md5()
            md5.update(pwd.encode('utf-8'))
            pwdhash = md5.hexdigest()
            #print("Updating password database with {}: {}".format(pwd, pwdhash))
            # {
            #  [plaintext, is-cracked, is-discovered],
            # }
            newval = [pwd, False, False]
            self.pw_database[pwdhash] = newval

    def spawn_agent(self, agent_name):
        """
        Create an agent.
        """
        newagent = Agent(agent_name, game=self)
        self.agents.append(newagent)
        return newagent

    def add_computer(self, ip_address, computer_name, *args, **kwargs):
        """
        Create a computer and add it to the network.
        Required: computer name and IP address (both str)
        Not required: anything else (but it gets passed to Computer.__init__)
        """
        newcomp = Computer(computer_name, *args, **kwargs, game=self)
        self.network.update({ip_address: newcomp})
        return newcomp

    def add_prebuilt_computer(self, comp, addr):
        """
        Add a computer to the network. Takes one already built computer and
        it's IP address.
        :param comp: computer
        :param addr: ip address
        :return: nothing
        """
        self.network.update({addr: comp})


class Agent(object):
    """
    A (virtual) physical entity in the (virtual) real world
    """
    def __init__(self, name, game=None):
        self.name = name
        self.user = User(self.name, game)
        self.computer = None
        self.shells = []
        self.game = game

    def login(self, computer):
        self.computer = computer
        self.shells.append(computer.get_shell(self.user, self))
