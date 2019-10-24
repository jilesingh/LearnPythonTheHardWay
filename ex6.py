# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

x = ("There are %d type of people." % 10) # this is initializing x
binary = 'binary' # definng binary as a string
do_not = "don't" # creating alias for do_not
y = "Those who know %s and those who %s." %(binary, do_not) # here is also a string inside string

print (x) # printing value of x
print (y) # printing value of y
print ("I said: %r." % x) # here is also 1 string inside string
print ("I also said: '%s'." %y) # here is 1 string inside string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This the left side of....."
e = "a string with a right side."

print (w + e)

# Here is output as observed from the terminal:
'''There are 10 type of people.
Those who know binary and those who don't.
I said: 'There are 10 type of people.'.
I also said: 'Those who know binary and those who don't.'.
Isn't that joke so funny?! False
This the left side of.....a string with a right side.
'''
