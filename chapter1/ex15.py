# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r:" % filename)
print (txt.read())

print ("type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())

# Here is output as observed from the terminal:

'''Here's your file 'ex15.txt':
Hallo Wolrd1
This is the test file to check whether I can write from Terminal or not
Once I learn Coding with Python I will give a big party to Abhimanyu.

type the filename again:
>ex15.txt
Hallo Wolrd1
This is the test file to check whether I can write from Terminal or not
Once I learn Coding with Python I will give a big party to Abhimanyu.
'''