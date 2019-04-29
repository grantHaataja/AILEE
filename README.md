# AILEE

This game is a penetration-testing simulator where you play as an Artificial Intelligence named Ailee who is being trained to hack systems and find security flaws.

There is much tension between some of the people involved with the development of this AI. Will the experiment be a success, or cause massive chaos and destruction upon the financial world?

Features a custom built emulator for a Linux-style terminal. Use classic Unix commands, as well as some of our own.

Remember to follow the administrator's instructions, and if you ever get stuck, a log of your conversations will be saved in AILEE's filesystem.


## Quickstart

1. Install Linux
2. Run the following commands in terminal:
```bash
git clone https://github.com/grantHaataja/AILEE.git
cd AILEE/src
python3 main.py
```

Done.

## Requirements

Technically, Linux is not required, but it is better.  The Python package requirements are specified in `requirements.txt` and can be installed in one shot with
```pip install -r requirements.txt```.

* `termcolor` 1.1.0
* `curses`
* Python 3.6 or newer (must support f-strings)
