# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:44:08 2017

@author: Administrator
"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("copying from %s to %s" % (from_file, to_file))

input = open(from_file)
indata = input.read()

print("the input file is %d bytes long " % len(indata))

print("does the output file exist? %r " % exists(to_file))
print("ready, hit RETURN to continue, CTRL-C to abort")
input()
output = open(to_file, 'w')
output.write(indata)

print("alright, all done")
output.close()
input.close()