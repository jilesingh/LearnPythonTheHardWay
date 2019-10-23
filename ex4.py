# -*- coding utf-8 -*-

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