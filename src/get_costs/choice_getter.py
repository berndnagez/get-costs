#!/usr/bin/env python3

import sys, getopt

def usage():
   print("usage: main.py [-h] -i | -a")
   print("")
   print("options:")
   print("  -h, --help show this help message and exit")
   print("")
   print("positional arguments:")
   print("  -i, --ifile <name of one file> ")
   print("  or")
   print("  -a, --all to proceed a files in data-Folder")
   print("")
   print("")
   

def err_mess():
   print ("Missing argument. Exit")
   print("")

def get_file(argv):
   try:
      opts, args = getopt.getopt(argv,"hai:",["ifile=","all","help"])
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
      elif opt in ("-a", "--all"):
         return "all"
      elif opt in ("-i", "--ifile"):
         choice = list()
         choice.append(arg)
         return choice         

def show_debug_infos():
    print(get_file(sys.argv[1:]))

if __name__ == "__main__":
    debug = True
    if (debug):
        show_debug_infos()