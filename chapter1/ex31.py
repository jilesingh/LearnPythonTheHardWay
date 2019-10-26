# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

print ("You enter in a dark room with two doors. Do you go through door #1 or door #2")

door = input(">")

if door == "1":
    print ("There is giant bear here eating cheese cake. What do you do?")
    print ("1. take the cake.")
    print ("2. Scream at the bear.")

    bear = input (">")
    
    if bear == "1":
        print ("The bear eats off your face. Good job!")
    elif bear == "2":
        print ("The bear eats your leg off. Good job!")
    else:
        print ("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print ("You stare into the endless abyss at Chutlhu's retina.")
    print ("1. Blueberries.")
    print ("2. Yellow jacket clothspins")
    print ("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print ("Your body survices powered by a mind of jello. Good job!")
    else:
        print ("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print ("You stumble around and fall on a knife and die. Good job!")


#Output is below as observed from the terminal
'''
You enter in a dark room with two doors. Do you go through door #1 or door #2
>1
There is giant bear here eating cheese cake. What do you do?
1. take the cake.
2. Scream at the bear.
>1
The bear eats off your face. Good job!

You enter in a dark room with two doors. Do you go through door #1 or door #2
>2
You stare into the endless abyss at Chutlhu's retina.
1. Blueberries.
2. Yellow jacket clothspins
3. Understanding revolvers yelling melodies.
>2
Your body survices powered by a mind of jello. Good job!

You enter in a dark room with two doors. Do you go through door #1 or door #2
>3
You stumble around and fall on a knife and die. Good job!

You enter in a dark room with two doors. Do you go through door #1 or door #2
>45
You stumble around and fall on a knife and die. Good job!

'''