# -*- coding: utf-8 -*-
"""
"Lookup the user guide (manual) for a command or cause the computer to mansplain economics"

Description: Shows the manual page for any command to describe its usage

Alternate usage: man (for all you manly men out there)
"""

import argparse

import executables

VITRUVIAN = """
                                   ,...,,.,
                          .«<ⁿ"`                 `'*≈.
                        "                              `ⁿ-.
                  ,⌐                                       `'«
               .^                                              "%
             «`                                                   ⁿ
           φ,.                     . ,,,..  ,...    ... . .......,,,],.,
        ╟¿░╫▓▓å╫╦                  ╦▓Ñ*══]¼V,                   >^ÜM╫░*╠
       ,╬⌐`"╨╣╦ `*««...           ╠▓▓▓φm╗K▓╦Ñ,            w,-ⁿ^,ª═╟╫"  ╚w
      ▄H╠     `"*╦,    "*,        ╫▓▓▌▒▓▒]▓▓╫Ω        ╓ⁿ`  ` ,<^`"     ) \\
     ╣" ╠,         "*«╥,  , `ⁿ«═~≈å╣▓█▀KΦ▓█▓╨,═ⁿⁿ#^`     ,«ª╨          ╚  *
    ╣   ║╫╬╫½ⁿ<wæ,«««.╚w╓╓Ω5Ω╓«%ⁿ^^╚╨╩NÑ╩╧═╝M^^╟^ⁿ╗Ω▄DÜ;;.. -,╓≥w≥^M╠A)í   ]
   ╟┘   ]╙╩▀▀MdM╬,      ░>w . `╠╖   '  `      '╟^`     ╠        ╓▓5║#ΦH]    ½
  j▌    ╚       *^ ``╙┘`    ````╙╫▄    ,╓,   ╬╟╙```` ` ```"`L.         ]     ╕
  ╢░    ]                        "Ö╙^^`` `"``jU                        ]     ╙
  ▌     ]                         ½          ╬                         ]      H
  ▀     j                         'w - .  , ╔░                         ]      Γ
 jΩ     j                        .╔    ╓     ⌐                         ]      ╠
  H ,  `]                        «╫* -      *░..                       ║      ╞
 -M    `j                        "           ╩                         ║      P
  ▌     ]                       ╔╝    ']H╔r "░░ -                      ╟      ⌐
  ║   ' ]                      ╔      ,╩j⌂     ╕                       ║     ]
   ▌    j                     ,H     / ""½   H  U                      ║     `
   ╙   'j                    rΓ   ≈«^  ╔  %     └                      j    A
    ╫   j                  . ╔~ `╓Ω   ,╡   "u   ╙Ñ                     ▐   /
     ╟ç j                  ╔╩r .r`╔  ─╙╣    ╛¥-  └⌂                    j  «
      ╟⌂]                ,A``<≥╨' j∩  ╒╟   ╔ `\`\≈Φ                    j /
       ╙╣             . /`   Ñ.  `]  ,░╟   ]   ¼   *,                  j┘
        j*           `]╬`   Å`    M`*Ñ M``w`   ╚╕    ⌂                æ▐
        ]  \       ., jÑ  ╥"  - .║   ]j   ╙    '"╥    ░             -`
        ╟    ⁿ   . `:╫╟  /`   ..'╜    ▐    `     `]   └,          /`
        j      "«  »╦╠Γ ñ       ⁿ╙N  ╘ ╟«  M       `≈  *       ,^
        j         "╝╬≥,╔         `╚H  ⌐╚^            `U╔╨╙ºÑÅ^
        j            `"╩H        :╙╨H \ ½  ¼          ╘,«*`
        ]                 `. ≈.  ,╔╦M` ½╟-⌐ "ºw╔µ, <^
        "^^^^^^^^^^^^^^^^^^^^^^^ ╙╙▀╨╙╨╙╜*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""


parser = argparse.ArgumentParser(
    prog='man',
    description=__doc__,
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument(
    'command',
    nargs='?',
    default=None,
    help='command to look up'
)


def run(*args, **kwargs):
    """
    Lookup man pages for a command.
    """

    try:
        data = parser.parse_args(args)
    except SystemExit:
        return

    if data.command is None:
        print(VITRUVIAN)
        return

    if (data.command in kwargs['game'].allowed_commands) and \
            (data.command not in executables.BLACKLIST_COMMANDS):
        try:
            getattr(executables, data.command).parser.print_help()
        except AttributeError:
            print("no command {} found".format(data.command))
    else:
        print("command not found")
