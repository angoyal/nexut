#!/usr/bin/env python


import os
import readline
import sys
from optparse import OptionParser

####################################
# debug fucntions
####################################
def DERR(fmt,*args):
  print fmt % args

def DTRC(fmt,*args):
  if options.verbose >=2:
    print fmt % args

####################################
# command line options
####################################
  
def process_cmd_line(argv):
  myParser = OptionParser()
  global options

  # add options
  # 0:errors, 1:warnings, >=2:all
  myParser.add_option("-v", type=int, action="store", dest="verbose", default=0)

  # parse and switch
  (options, args) = myParser.parse_args(argv)


####################################
# your functions here
####################################

def run_loop():
  prompt ="nexut-> "
  while True:
    try:
      cmd = raw_input(prompt)
    except EOFError:
      print '\n\ngoodbye..\n'
      exit()

    if cmd != '': print cmd
    


####################################
# main 
####################################
if __name__ == '__main__':
  process_cmd_line(sys.argv) 
  run_loop()
  
