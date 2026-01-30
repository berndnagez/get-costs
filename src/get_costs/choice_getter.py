#!/usr/bin/env python3

import sys
import getopt


def usage():
    print("usage: main.py [-h] -i -p")
    print("")
    print("options:")
    print("  -h, --help show this help message and exit")
    print("")
    print("positional arguments:")
    print("  -i, --ifile <name of one journal> ")
    print("  -p, --project <project id of one project>")
    print("")
    print("")


def err_mess():
    print("Missing argument. Exit")
    print("")


def get_choice(argv):
    try:
        opts, args = getopt.getopt(
            argv, "hi:p:", ["ifile=", "help", "project="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if opts == []:
        err_mess()
        usage()
        sys.exit()

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            usage()
            sys.exit()

    return opts


def show_debug_infos():
    print(get_choice(sys.argv[1:]))


if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()
