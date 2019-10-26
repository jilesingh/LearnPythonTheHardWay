# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

people = 20
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats! The world is doomed1")

if people > cats:
    print ("Not many cats! The world is saved!")

if people < dogs:
    print ("The world is drooled on!")

if people > dogs:
    print ("People are less than or equal to dogs.")

dogs += 5

if people >= dogs:
    print ("People are greater than or equal to dogs.")

if people <=dogs:
    print ("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

# The following output is observed from the terminal:
'''
Too many cats! The world is doomed1
People are less than or equal to dogs.
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
'''