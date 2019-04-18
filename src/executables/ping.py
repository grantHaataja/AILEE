# -*- coding: utf-8 -*-
'''
"Determine if another computer wants to play pingpong"

Description: Tells if a computer is connected to the internet

Usage: ping xxx.xxx.xxx.xxx
'''

import random
import time

def run(*args, **kwargs):
    """
    Ping.
    """

    assert len(args) == 1, "Need an address to play pingpong with"
    # Network is a dictionary. ip_address(str):computer(obj)
    # That does make more sense
    comps = kwargs['game'].network
    if args[0] in comps.keys():
        success(args[0])
    else:
        fail(args[0])


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