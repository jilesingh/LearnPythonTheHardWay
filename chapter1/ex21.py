# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print ("SUBTRACTING %d, %d", (a, b))
    return a - b

def multiply(a, b):
    print ("MULTIPLYING %d, %d" %(a, b))
    return a * b

def divide(a, b):
    print ("DIVIDING %d. %d" %(a, b))
    return a / b

print ("Let's do math with just functions!")

age = add(30, 5)
height = subtract(78, 2)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for extra credit type it in anyway
print ("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print ("That becomes: ", what, "Can you do it by hand?")

# We get following output in console:
'''
Let's do math with just functions!
ADDING 30 + 5
SUBTRACTING %d, %d (78, 2)
MULTIPLYING 90, 2
DIVIDING 100. 2
Age: 35, Height: 76, Weight: 180, IQ: 50
Here is a puzzle.
DIVIDING 50. 2
MULTIPLYING 180, 25
SUBTRACTING %d, %d (76, 4500.0)
ADDING 35 + -4424
That becomes:  -4389.0 Can you do it by hand?
'''