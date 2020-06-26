#!/usr/bin/python3

##############
#  @r4v10l1  #
##############

from colorama import Fore, Style, Back
import sys
try:
    from googlesearch import search
except:
    print()
    print("{}{}[!] Google module is not installed {}(pip3 install google){}.{}".format(Style.BRIGHT, Fore.RED, Style.RESET_ALL, Fore.RED, Style.RESET_ALL))
    print()
    exit(1)


arguments = str(len(sys.argv))

if arguments != "2" and arguments != "5":  # Wrong input or no unput
    print()
    print("{}{}[*] Usage:{}          {} <search>".format(Style.BRIGHT, Fore.BLUE, Fore.RESET, sys.argv[0]))
    print("{}[*] Advanced mode:{}  {} <theme> <language> <number of results> <search>".format(Fore.BLUE, Fore.RESET, sys.argv[0]))
    print()
    print("{}[*] Themes:{}         (1) HannahMontanaOS".format(Fore.BLUE, Fore.RESET))  # AKA. Señor Foo's OS
    print("                    (2) Noob theme")
    print()
    print("{}[*] Languages:{}      (es) Spanish".format(Fore.BLUE, Fore.RESET))  # AKA. Señor Foo's OS
    print("                    (en) English{}".format(Style.RESET_ALL))
    print()
    exit(1)


if arguments == "2":  # Simple mode

    ##################### DEFAULT MODE SETTINGS #####################
    THEME = "2"  # Default theme (2 for noob or 1 hm)
    LANG = "es"     # Language, default is spanish (com for english)
    RESULTS = 10  # Number of results
    WAIT = 2.0    # Time between searches
    #################################################################

    SEARCHTERM = str(sys.argv[1])

elif arguments == "5":  # Advanced mode

    THEME = str(sys.argv[1])
    LANG = str(sys.argv[2])
    if LANG == "en":
        LANG = "com"
    RESULTS = int(str(sys.argv[3]))
    SEARCHTERM = str(sys.argv[4])
    WAIT = 2.0    # Time between searches

    # print(SEARCHTERM, THEME, LANG, RESULTS, WAIT)
    # exit(1)

else:
    print()
    print("{}{}[!] Argument error. Run python3 {} to see the options.{}".format(Style.BRIGHT, Fore.RED, sys.argv[0], Style.RESET_ALL))
    print()
    exit(1)


if THEME == "1":
    print(Style.BRIGHT)
    print("{} {}..:: 🌟 Hannah Montana search engine 🌟 ::..{}".format(Back.MAGENTA, Fore.RED, Fore.CYAN))
    print()
    for x in search(SEARCHTERM, tld=LANG, num=RESULTS, stop=RESULTS, pause=WAIT):
        print(x)
    print(Style.RESET_ALL)
elif THEME == "2":
    print(Style.BRIGHT)
    print(" {}..::{} Ravi0li search engine {}::..{}".format(Fore.RED, Fore.WHITE, Fore.RED, Fore.WHITE))
    print()
    for x in search(SEARCHTERM, tld=LANG, num=RESULTS, stop=RESULTS, pause=WAIT):
        print(x)
    print(Style.RESET_ALL)
else:
    print()
    print("{}{}[!] Theme error.{}".format(Style.BRIGHT, Fore.RED, Style.RESET_ALL))
    print()

exit(1)
