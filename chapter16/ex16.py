# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

from sys import argv
script, filename = argv
print ("We are going to erase %r." % filename)
print ("If you don't want that, hit CTRL+C")
print ("If you do want that, hit Return")

input("?")

print ("Openeing the file.....")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you three lines.")

line1 = input ("line1: ")
line2 = input ("line2: ")
line3 = input ("line3: ")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()

# Here is the output we get from the console
'''We are going to erase 'ex15.txt'.
If you don't want that, hit CTRL+C
If you do want that, hit Return
?
Openeing the file.....
Truncating the file. Goodbye!
Now I'm going to ask you three lines.
line1: Weather the file was erased really
line2: This is agin to test your programming skills
line3: Now it will be written agin to the file
I'm going to write these to the file.
And finally we close it.'''

