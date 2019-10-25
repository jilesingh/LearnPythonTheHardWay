# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

def cheese_and_crackers(cheese_count, boxes_of_crackers): # function is defined
    print ("You have %d cheese" % cheese_count) # printing cheese count
    print ("You have %d boxes of crackers." % boxes_of_crackers) # printing boxes of crackers
    print ("Man that's enough for a party!") # 
    print ("Get a blanket.\n")

print ("We can just give the numbers to function directly:")
cheese_and_crackers(20, 30) # calling function passing two arguments 20 and 30

print ("OR, we can use variables from our script:")
amount_of_cheese = 10  # we are using variables from script
amount_of_crackers = 50  

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # calling function using variables

print ("We can do even math inside too:")

cheese_and_crackers(10 + 20, 5 + 6) # doing math inside function calling

print ("And we can combine the two variables and the math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # inside function combining variables and math


# We get the output from the console as:
'''
We can just give the numbers to function directly:
You have 20 cheese
You have 30 boxes of crackers.
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheese
You have 50 boxes of crackers.
Man that's enough for a party!
Get a blanket.

We can do even math inside too:
You have 30 cheese
You have 11 boxes of crackers.
Man that's enough for a party!
Get a blanket.

And we can combine the two variables and the math
You have 110 cheese
You have 1050 boxes of crackers.
Man that's enough for a party!
Get a blanket.
'''