# -*- coding utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("type the filename again:")
file_again = open(file_again)

txt_again = open(file_again)

print (txt_again.read())
