# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

cars = 100 # number of cars have been assigned here
space_in_a_car = 4.0 # space ina car has been assigned
drivers = 30 # number of drivers available
passengers = 90 # number of passengers 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "available.")
print ("We can transport", carpool_capacity, "people today.")
print ("we have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")


# Here is output as observed from the terminal:
'''
There are 100 cars available.
There are only 30 available.
We can transport 120.0 people today.
we have 90 to carpool today.
We need to put about 3.0 in each car.
'''