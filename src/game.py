"""
The almighty Game class.

Really just here to keep track of events and physical-level abstractions -- things that exist "physically", ie computers and agents.
"""

from computer import Computer, User
import title
from funfunctions import clear
import funfunctions
import executables


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
        self.eventLogDir = None # Set in main.py
        self._variables = {}
        self.event10 = False
        self.forkbomb = False

        self.allowed_commands = [
            'cd', 'clear', 'echo', 'gnome', 'help', 'iplist', 'ls', 'man',
            'ping', 'pscan', 'shell', 'shutdown', 'vscan', 'exploit', 'pyd',
            'read', 'run', 'gcc',
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
        self.network.update({ip_address:newcomp})
        return newcomp


class Agent(object):
    '''
    A (virtual) physical entity in the (virtual) real world
    '''
    def __init__(self, name, game=None):
        self.name = name
        self.user = User(self.name)
        self.computer = None
        self.shells = []
        self.game = game

    def login(self, computer):
        self.computer = computer
        self.shells.append(computer.get_shell(self.user, self))
