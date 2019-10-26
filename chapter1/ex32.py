# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:  # for loop is iterating through a list
    print ("This is count %d" % number)

for fruit in fruits:
    print ("A fruit of type: %s" % fruit)

for i in change:
    print ("I got %r" % i) # when we don't know the data type we use %r

# here we are going to use empty list and later we extend it

element = []

for i in range(0, 6):
    print ("Adding %d to the list." %i)
    element.append(i)  # append is a function used to append a list.

for i in element:
    print ("Element was: %d" % i)

# Here is the output as observed from the terminal:
'''
This is count 1
This is count 2
This is count 3
This is count 4
This is count 5
A fruit of type: apples
A fruit of type: oranges
A fruit of type: pears
A fruit of type: apricots
I got 1
I got 'pennies'
I got 2
I got 'dimes'
I got 3
I got 'quarters'
Adding 0 to the list.
Adding 1 to the list.
Adding 2 to the list.
Adding 3 to the list.
Adding 4 to the list.
Adding 5 to the list.
Element was: 0
Element was: 1
Element was: 2
Element was: 3
Element was: 4
Element was: 5
'''