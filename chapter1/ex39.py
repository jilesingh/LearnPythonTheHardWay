# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

# Create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print ("-"*40)
print ("NY State has:", cities['NY'])
print ("OR State has:", cities['OR'])

# Print some states
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is:", states['Florida'])

# Do it by using the state then cities dict
print ("-"*40)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# Print every state abbreviation
print ("-"*40)
for state, abbrev in states.items():
    print ("%s is abbreviated as %s" %(state, abbrev))

# Print every city in state
print ("-"*40)
for abbrev, city in cities.items():
    print ("%s has the city %s" %(abbrev, city))

# Now do both at the same time
print ("-"*40)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev]))

# Safely get an abbreviation by state that might not be there
print ("-"*40)
state = states.get('Texas', None)


if not state:
    print ("Sorry, no Texas")

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)


# Here is output as observed from the terminal:
'''
----------------------------------------
NY State has: New York
OR State has: Portland
Michigan's abbreviation is:  MI
Florida's abbreviation is: FL
----------------------------------------
Michigan has: Detroit
Florida has: Jacksonville
----------------------------------------
Oregon is abbreviated as OR
Florida is abbreviated as FL
California is abbreviated as CA
New York is abbreviated as NY
Michigan is abbreviated as MI
----------------------------------------
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
----------------------------------------
Oregon state is abbreviated OR and has city Portland
Florida state is abbreviated FL and has city Jacksonville
California state is abbreviated CA and has city San Francisco
New York state is abbreviated NY and has city New York
Michigan state is abbreviated MI and has city Detroit
----------------------------------------
Sorry, no Texas
The city for the state 'TX' is: Does Not Exist

'''
