# -*- coding: utf-8 -*-

from computers import ailee, ssb, pics, ccc

COMPUTERS = {
    'ailee': ailee.mkailee,
    'pics': pics.mkpics,
    'ssb': ssb.mksafe,
    'ccc': ccc.mkccc,
}


def mk_computer(name, **kwargs):
    """
    Get the computer specified by name, and adds it to the game's
    network.
    :param name:
    :param kwargs:
    :return: computer
    """

    func = COMPUTERS[name]
    addr, comp = func(**kwargs)

    kwargs['game'].add_prebuilt_computer(comp, addr)
    return comp
