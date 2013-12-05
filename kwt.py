#! /usr/bin/env python

import os, sys, itertools, argparse
from termcolor import colored, cprint

def flatten(l):
  if checkbuf(l):
    return sorted(list(set(l)))
  return sorted(list(set(itertools.chain.from_iterable(l))))

def readfile(f):
  try:
    f = open(f, 'r')
    l = [ line.strip().split(',') for line in f if line.strip() is not ""]
    f.close()
    return l
  except IOError:
    return

def printchar(char):
  sys.stdout.write('--')
  sys.stdout.write(char)

def offset(i):
  for i in range((3*i-1)):
    sys.stdout.write(' ')

def display(s,d):
  chars = list(s)
  sys.stdout.write('|')
  if d[s][0] is 1:
    for char in chars:
      printchar(char)
    sys.stdout.write('\n')
  else:
    offset(d[s][1])
    sys.stdout.write('|')
    for char in chars[d[s][1]:]:
      printchar(char)
    sys.stdout.write('\n')

def makedict(l):
  d = dict()
  for i in xrange(0, len(l)-1):
    root = l[i]
    for j in l[i+1:]:
      d[j] = [1,0]
      val = [m==n for m,n in zip(root,j)].index(0)
      if val != '' and val != 0:
        d[j] = [0,val]
  d[l[0]] = [1,0]
  return d

def checkbuf(l):
  if len(l)<2:
    return False
  else:
    return True

def main(l):
  if not checkbuf(l): return
  s = makedict(l)
  sys.stdout.write('*')
  sys.stdout.write('\n')
  for i in l:
    display(i,s)

  done_msg = colored('\nDone! Keyword tree generated.\n', 'green')
  print(done_msg)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='kwt', description='A small nifty program to make a keyword tree based on input from the command line or a file')
  parser.add_argument('-f', '--file', help='takes input from a file. Input should either be a comma separated list of values or values separated on a newline')
  parser.add_argument('-v', '--version', action='version',  version='KWTree Generator 0.1, Licensed under the MIT License', help='print the current version and exit')
  args = parser.parse_args()

  if not args.file:
    buf = []
    print '\nYou could press Ctrl+C to exit'
    input_msg = colored('Please enter input values each on its own line', 'green', attrs=['underline'])
    sys.stdout.write(input_msg)
    sys.stdout.write('\n\n')
    while True:
      try:
        line = raw_input()
        if not line: break
        buf.append(line)
      except KeyboardInterrupt:
        sys.exit(0)
    main(flatten(buf))
    sys.exit(0)
  else:
    if not os.path.exists(args.file):
      fof_msg = colored('\nFile not found ! Please specify a valid file path\n\n', 'red', attrs=['bold'])
      sys.stdout.write(fof_msg)
      parser.print_help()
      sys.exit(0)

  main(flatten(readfile(args.file)))









