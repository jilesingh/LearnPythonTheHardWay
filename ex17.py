# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" %(from_file, to_file))

# we coild do these two on one line too. How?

in_file = open(from_file)
indata = in_file.read()

print ("The input file is %d bytes long " %len(indata))

print ("Does the output file exists? %r" % exists(to_file))
print ("Ready hit enter to continue, CTRL+C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Alright, all done.")


out_file.close()
in_file.close()

# Output can be seen from the console as:
'''Copying from test.txt to new_file.txt
The input file is 21 bytes long 
Does the output file exists? False
Ready hit enter to continue, CTRL+C to abort.

Alright, all done.
'''