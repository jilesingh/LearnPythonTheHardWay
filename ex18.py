# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" %(arg1, arg2))

# ok, that *arg is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" %arg1)

# this one takes no arguments
def print_none():
    print("I got nothing.")

print_two("Jile", "Singh")
print_two_again("Jile", "Singh")
print_one("Jile!")
print_none()

# We got the output from the console like this:
'''
arg1: 'Jile', arg2: 'Singh'
arg1: 'Jile', arg2: 'Singh'
arg1: 'Jile!'
I got nothing.
'''