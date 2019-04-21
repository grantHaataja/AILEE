"""
"Sally sells these by the seashore"

Description: Basically, a shell is the running process behind a terminal window.\nYou are reading this on a shell right now. This command shows what shells are\nopen on which computers and allows the user to switch between them

Usage: shell (shows all open shells and which computer they belong to)

Usage: shell x (switches to shell number x to access the computer shell number x\nis open on)
"""


def run(*args, **kwargs):
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False

    agent = kwargs['agent']
    shells = agent.shells

    if not args or emptyList:
        # list available shells
        print("===== SHELLS =====")
        print("Hello, {}.".format(agent.name))
        print("You are currently in shell #{}".format(shells.index(kwargs['shell'])))

        for i in range(len(shells)):
            print("{}: {}, {}".format(i, shells[i].user.name,
                                      shells[i].computer.name))
        print("==================")

    else:
        if args[0] == "new":
            # making a new shell
            # We either have just
            #   $ shell new
            # or $ shell new {IP address}

            if len(args) == 2:
                try:
                    box = kwargs['game'].network[args[1]]
                except KeyError:
                    print("Couldn't connect to {}.".format(args[1]))
                    return
            elif len(args) == 1:
                box = kwargs['computer']  # this one
            else:
                print("What's going on here? args = {}".format(args))
                return

            if (not any(box.vulns.values())) and (len(box.vulns) != 0):
                print("Couldn't create new shell on that machine")
                return

            new_shell = box.get_shell(kwargs['user'], kwargs['agent'])
            agent.shells.append(new_shell)
            run('-1', **kwargs)  # -1 is last element index in python

        else:
            assert len(args) == 1, "expected only 1 argument"
            try:
                selection = int(args[0])
            except ValueError:
                print("must specify an int")
                return

            try:
                selected_shell = shells[selection]
            except IndexError:
                print("Doesn't exist")
                return
            kwargs['shell'].halt()
            selected_shell.start_shell_loop()
