# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8
# In this exercise we are going to see lambda, filter and map functions

#num = input(">")
def square(num):
    return (num**2)
my_nums = [1,2,3,4,5,6]
print(list(map(square, my_nums))) # here we do not need to call the function square as square()


# we can also iterate through it

for item in map(square, my_nums):
    print(item)


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "Even"
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print("\nIf length is even its returning Even else first letter.") 
print(list(map(splicer, names)))

def check_even(num):
    return num % 2 == 0

my_num = [1,2,3,4,5,6] # filter function means you need to filter by a function that returns either True or False.

print("\nIn this case filter ius going to return only even number.")
print(list(filter(check_even, my_num)))

# print the reverse of the names
print("\nHere we are going to print the revrse of the names present in the list names:")
print(list(map(lambda x:x[::-1], names)))


# Here is output as observed from the terminal:
'''
[1, 4, 9, 16, 25, 36]
1
4
9
16
25
36

If length is even its returning Even else first letter.
['Even', 'E', 'S']

In this case filter ius going to return only even number.
[2, 4, 6]

Here we are going to print the revrse of the names present in the list names:
['ydnA', 'evE', 'yllaS']
'''
