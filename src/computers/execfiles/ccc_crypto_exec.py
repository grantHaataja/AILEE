import hashlib
import termcolor

pwin = input("master password > ")
game = kwargs['game']
ccc = game.network['140.24.3.12']

inhash = hashlib.md5(pwin.encode('utf-8')).hexdigest()
mphash = ccc.crypto_exec_pwd_hash

if inhash == mphash:
    game.event10 = True
else:
    print(termcolor.colored("Access denied", 'red'))
