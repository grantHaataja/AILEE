# -*- coding: utf-8 -*-
"""
"Determine if another computer wants to play pingpong"

Check if a computer is connected to the internet.
"""

import random
import time
import argparse


parser = argparse.ArgumentParser(
    prog='ping',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'addr',
    type=str,
    help='host to test',
)


def run(*args, **kwargs):
    """
    Ping.
    """

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    # Network is a dictionary. ip_address(str):computer(obj)
    # That does make more sense
    comps = kwargs['game'].network
    if data.addr in comps.keys():
        success(data.addr)
    else:
        fail(data.addr)


def success(addr):
    for i in range(8):
        t = random.random()
        time.sleep(t)
        print("64 bytes from {}: icmp_seq={} ttl=64 time={:1.3f} ms".format(
            addr, i, t
        ))


def fail(addr):
    for i in range(8):
        t = 0.02
        time.sleep(t)
        print("No response from {} time={:1.3f} ms".format(
            addr, t
        ))
