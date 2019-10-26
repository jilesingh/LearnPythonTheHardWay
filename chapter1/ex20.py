# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

from sys import argv

script, input_file = argv

def print_all(f):
    print (f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


# Here is output as observed from the terminal:
'''
First let's print the whole file:

Weather the file was erased really
This is agin to test your programming skills
Now it will be written agin to the file

Now let's rewind, kind of like a tape.
Let's print three lines:
1 Weather the file was erased really

2 This is agin to test your programming skills

3 Now it will be written agin to the file
'''