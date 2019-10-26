# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

people = 30
cars = 40
buses = 15

if cars > people:
    print ("We should take cars.")
elif cars < people:
    print ("We should not take cars.")
else:
    print("We can't decide.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("May be we could take the buses.")
else:
    print ("We still can't decide.") 

if people > buses:
    print ("Alright, lets just take the buses.")
else:
    print ("Fine, let's stay home then.")


# Here is output as observed from the terminal:
'''
We should take cars.
May be we could take the buses.
Alright, lets just take the buses.
'''