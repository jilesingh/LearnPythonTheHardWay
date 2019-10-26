# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
print (stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There's %d items now." % len(stuff))

print ("There we go:", stuff)

print ("Let's do some some things with stuff.")

print (stuff[1])
print (stuff[-1]) # whoa! fancy
print (stuff.pop())
print (' '.join(stuff))
print ('#'.join(stuff[3:5])) # super steller!


# Here is output as observed from the terminal:
'''
Wait there's not 10 things in that list, let's fix that.
['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
Adding:  Boy
There's 7 items now.
Adding:  Girl
There's 8 items now.
Adding:  Banana
There's 9 items now.
Adding:  Corn
There's 10 items now.
There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some some things with stuff.
Oranges
Corn
Corn
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
Telephone#Light
'''
