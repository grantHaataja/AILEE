# -*- coding: utf-8 -*-

import computer
from .execfiles import grabfile


PASSWDS = {
    'jason': 'i-hate-my-job',
    'erin': 'secret123',
    'mario': 'getgnomed',
}


def mkpics(**kwargs):
    newcomp = computer.Computer(
        'picsHelpDesk',
        vulns={
            'LI38_612 meta SSH security flaw': [False, 22],
        },
        game=kwargs['game']
    )
    newcomp.exploited = False
    newcomp.open_port({22: 'ssh', 443: 'https'})
    root = newcomp.fs
    root.mkdir('bin')
    root.mkdir('log')
    home = root.mkdir('home')

    for acct, passwd in PASSWDS.items():
        usr = computer.User(acct, passwd, game=kwargs['game'])
        newcomp.add_prebuilt_user(usr)

    # Jason
    jason = home.mkdir('Jason', owner='jason')
    jasonproject = jason.mkdir('project', owner='jason')
    # add notes?
    jasonproject.addFile('exploit.c', '', permissions='------', owner='jason')
    jasonproject.addFile(
        '.notes.txt',
        "Software update scheduled for end of day on Friday. Work late until "
        "everyone has\ngone home, and add virus to AILEE home directory. Use "
        "hidden file format so no\none notices.",
        owner='jason',
    )  # Hidden file here
    # leave contents empty
    jasonproject.addFile('.virus', '', permissions='------', owner='jason')
    jason.mkdir('not_interesting').addPrebuiltFile(
        grabfile.get_exec_file(
            "picsHelpDesk/home/Jason/not_interesting/runme.exe",
            owner='jason',
        )
    )
    jasonemails = jason.mkdir('emails', owner='jason')
    jasonemails.addFile(
        'AILEE.email',
        "\nJason,\n\nI hope your projects are going smoothly. As you are the "
        "leading exploit creator\nhere at PICS, I will need you to write the "
        "exploitation software for Ailee. The\ninital release date will be 4 "
        "weeks from today.\n", owner='jason')
    jasonemails.addFile(
        'RE:AILEE.email',
        "\nI don't have time to spend on silly projects that should never "
        "have been\napproved in the first place. An AI penetration tester will "
        "never work. The AILEE\nproject should be shut down and funding spent "
        "on something more useful.\n", owner='jason')
    jasonemails.addFile(
        'exploit.email',
        "\nJason,\n\nI'm sorry you feel that way about Ailee. But we have too "
        "many clients to take\ncare of ourselves. Ailee will take some of the "
        "workload off our shoulders so we\ncan breathe again. I need the "
        "exploit software written within 3 weeks or I will\nfind a new exploit "
        "creator.\n", owner='jason')
    jasonemails.addFile(
        'RE:exploit.email',
        "\nAn AI equipped with penetration testing tools is either useless or "
        "dangerous!\nCancel your stupid AILEE and be done with this insanity "
        "before it's too late\nand you destroy this company!\n", owner='jason')
    jasonemails.addFile(
        'lastChance.email',
        "\nWRITE THE SOFTWARE OR YOU'RE FIRED. This is not up for negotiation, "
        "Jason. If\nyou don't have it done within the next 2 weeks, you'll be "
        "living on the streets.\nAnd don't you DARE call Ailee stupid again.\n",
        owner='jason')
    jasonemails.addFile(
        'RE:lastChance.email',
        "\nOkay, I'll write your bloody software. But you're going to regret "
        "ever\ncreating AILEE, I guarantee it.\n", owner='jason')

    # Erin
    erin = home.mkdir('Erin', owner='erin')
    erincode = erin.mkdir('code', owner='erin')
    erincode.addFile(
        'pyd.py',
        "def run(*args, **kwargs):\n\n\tprint(kwargs)\n\nif args:\n"
        "\texec(' '.join(args))",
        permissions='r--r-x',
        owner='erin')
    erincode.addFile('grep.c', '', permissions='------', owner='erin')
    erincode.addFile('seds.c', '', permissions='------', owner='erin')
    erincode.addFile('mkdir.c', '', permissions='------', owner='erin')
    erincode.addFile('vim.c', '', permissions='------', owner='erin')
    erinemails = erin.mkdir('emails', owner='erin')
    erinemails.addFile(
        'Update?.email',
        "\nErin,\n\nThere are only 2 weeks left before we turn Ailee on. How "
        "far are you from\ncompleting the features I asked for?\n",
        owner='erin')
    erinemails.addFile(
        'RE:Update?.email',
        "\nI'm sorry, I haven't been able to finish file creating or editing. "
        "Also grep\nand seds are nightmares and I haven't made any progress on "
        "them. The pyd\ninterpreter is working correctly though.\n",
        owner='erin')

    # Mario
    mario = home.mkdir('Mario', owner='mario')
    mario.addFile(
        'wishlist.txt',
        "new girlfriend\ncar with windows that close\nclown "
        "tattoo\nPokemon t-shirt", owner='mario')
    mario.addFile(
        'grocery_list.txt',
        "bacon\nchocolate ice cream\nfrozen pizza\nchocolate milk\nginger "
        "ale\ntequila\nsteaks\npizza rolls\njalapeno poppers\ncream cheese\n"
        "onion rings\nsomething healthy?\nlight beer\nsausage\npotato chips\n"
        "toilet paper\nyogurt\nsalami", owner='mario')
    mariowork = mario.mkdir('work?', owner='mario')
    mariowork.addFile('gcc.c',
    "// I have no idea how to write C :(", permissions='---r--', owner='mario')
    mariowork.addFile(
        'gnome.c',
        '#include<stdio.h>\n\nint main(void) {\n\tprintf("Ho ho ho ha ha, ho '
        'ho ho he ha. Hello there, old chum. I’m gnot a gnelf. I’m gnot a '
        'gnoblin. I’m a gnome. And you’ve been, GNOMED");\n\n\treturn(0);\n}',
        owner='mario')
    marioemails = mario.mkdir('emails', owner='mario')
    marioemails.addFile(
        'gnome.email',
        "\nMario,\n\nWill you please remove command: gnome from Ailee? It is "
        "a useless command which\nwill do nothing but confuse her. You were "
        "supposed to implement the compiler for\nher so she can write her "
        "own programs.\n", owner='mario')
    marioemails.addFile('RE:gnome.email', "gno i will gnot", owner='mario')

    return '120.33.7.242', newcomp
