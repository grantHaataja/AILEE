"""
"Run, run, as fast as you can. You can't catch me, I'm the gingerbread man!"

Description: Runs an executable file
"""

import argparse

import filesystem


parser = argparse.ArgumentParser(
    prog='run',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'filename',
    type=str,
    help='file to run',
)


def run(*args, **kwargs):

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    try:
        obj = kwargs['cwd'].children[data.filename]
    except KeyError:
        print("Couldn't find file")
        return

    if isinstance(obj, filesystem.File):

        if kwargs['user'].name == obj.owner:
            # we're in the owner permissions
            allowed = obj.permissions.exec_owner
        else:
            allowed = obj.permissions.exec_users

        if not allowed:
            print("Permission denied: file is not executable")
            return

        # verify file hash matches original -- don't allow
        # edited executables to be run
        if obj.original_hash != obj.current_hash:
            print("Cannot run modified files.")
            return

        code = obj.data

        # TODO: there has to be a better way than this
        exec(code)
        return
