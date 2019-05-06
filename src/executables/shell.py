"""
"Sally sells these by the seashore"

Description: Basically, a shell is the running process behind a terminal window.
You are reading this on a shell right now. This command shows what shells are
open on which computers and allows the user to switch between them
"""

import argparse

parser = argparse.ArgumentParser(
    prog='shell',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
group = parser.add_mutually_exclusive_group(
    required=False,
)
group.add_argument(
    'switch_to',
    nargs='?',
    type=str,
    default=None,
    help='shell number to switch to',
)
group.add_argument(
    '-n',
    nargs='?',
    type=str,
    dest='mknew',
    const='-1',
    help='create a new shell on this (or other) computer, specified by IP'
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    agent = kwargs['agent']
    shells = agent.shells

    if not (data.switch_to or data.mknew):
        # list available shells
        print("===== SHELLS =====")
        print("Hello, {}.".format(agent.name))
        print("You are currently in shell #{}".format(shells.index(kwargs['shell'])))

        for i in range(len(shells)):
            print("{}: {}, {}".format(i, shells[i].user.name,
                                      shells[i].computer.name))
        print("==================")

    else:
        if data.mknew:
            # making a new shell
            # We either have just
            #   $ shell new
            # or $ shell new {IP address}

            if data.mknew != '-1':
                try:
                    box = kwargs['game'].network[data.mknew]
                except KeyError:
                    print("Couldn't connect to {}.".format(args[1]))
                    return
            elif data.mknew == '-1':
                box = kwargs['computer']  # this one
            else:
                print("What's going on here? args = {}".format(data))
                return

            vulnerable = any(box.vulns.values())
            has_vulns = len(box.vulns) != 0
            have_creds = 'cred_login' in kwargs.keys()

            allowed = (has_vulns and vulnerable) or have_creds

            if allowed:
                new_shell = box.get_shell(kwargs['user'], kwargs['agent'])
                agent.shells.append(new_shell)
                run('-1', **kwargs)  # -1 is last element index in python
            else:
                print("Couldn't create a new shell on that machine.")
        else:
            try:
                selection = int(data.switch_to)
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
