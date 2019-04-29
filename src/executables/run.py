"""
"Run, run, as fast as you can. You can't catch me, I'm the gingerbread man!"

Description: Runs an executable file

Usage: run file_name.exe
"""

import filesystem


def run(*args, **kwargs):
    assert len(args) == 1, \
        "Must specify an executable to run.\n\nUsage: run [executable]"

    try:
        obj = kwargs['cwd'].children[args[0]]
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
