# -*- coding utf-8 -*-

from sys import argv

script, user_name = argv # here we are assigning values
prompt = "-->>" # we are taking it as a prompt

print ("Hi %s, I'm %s script." %(user_name, script))
print ("I would like to ask you a few questions.")
print ("Do you like me %s?" %user_name)
likes = input(prompt)

print ("Where do you live %s?" %user_name)
lives = input(prompt)

print ("what kind of computer do you have?")
computer = input(prompt)

print (""" 
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
and You have a %r computer. Nice
""" % (likes, lives, computer))

