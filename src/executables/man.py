# -*- coding: utf-8 -*-
"""
"Lookup the user guide (manual) for a command or cause the computer to mansplain economics"

Description: Shows the manual page for any command to describe its usage

Usage: man command_name

Usage: man (for all you manly men out there)
"""

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


def run(*args, **kwargs):
    """
    Lookup man pages for a command.
    """
    emptyList = True
    for arg in args:
        if arg:
            emptyList = False
    assert len(args) in [0, 1] or emptyList, \
        "Invalid use of man.\n\nUsage: man [command]"

    if len(args) == 0 or emptyList:
        print(VITRUVIAN)
        return

    if (args[0] in kwargs['game'].allowed_commands) and \
            (args[0] not in executables.BLACKLIST_COMMANDS):
        try:
            print(getattr(executables, args[0]).__doc__)
        except AttributeError:
            print("no command {} found".format(args[0]))
    else:
        print("command not found")
