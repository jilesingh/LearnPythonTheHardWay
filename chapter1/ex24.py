# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

print ("Let's practice everything.")
print ("You\'d need to know \'bout escapes with \\ that do \nnew lines and \t tabs. ")
poem = """
\tThe lovely wolrd
with logic so firmly planted
cannot discern \nneed of love
not comprihend passion from intitution
and requires an explanation
\n\twhere there is none.
"""

five = 10 - 2 + 3 - 6
print ("This should be five: %s" %five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" %start_point)
print ("We'd have %d beans, %d jars and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print ("We can also do this way:")
print ("We would have %d beans, %d jars and %d crates." % secret_formula(start_point))

# Here is the output as observed from the terminal:
'''
Let's practice everything.
You'd need to know 'bout escapes with \ that do 
new lines and 	 tabs. 
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 5000 jars and 50 crates.
We can also do this way:
We would have 500000 beans, 500 jars and 5 crates.
'''


    