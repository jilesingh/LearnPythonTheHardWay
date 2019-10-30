# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8
# In this exercise I am going to create some more functions 

def add_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return(print(f"Sum of {x} and {y} is: {x+y}"))
    
    

def subtract_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return(print(f"Subtraction of {x} minus {y} is {x-y}"))


def multiply_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return(print(f"Multiplication of {x} and {y} is: {x*y}"))


def divide_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return(print(f"Division of {x} divide by {y} is: {x/y}"))


def remainder_of_two_numbers():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return(print(f"Remainder of {x} divide by {y} is: {x%y}"))


def even_numbers(*args):
    x = 1
    y = int(input('Enter the number upto you want to find even numbers: '))
    for item in range (1, y):         
        if item % 2 == 0:
            
            (print(f"Even numbers are: {item}"))
    return (item)       
    

def odd_numbers(*args):
    x = 1
    y = int(input('Enter the number upto you want to find odd numbers: '))
    for item in range (1, y):         
        if item % 2 != 0:
            
            (print(f"Odd numbers are: {item}"))
    return (item)       


def divide_by_three():
    x = 1
    y = int(input('Enter the number upto you want to find divisible by 3: '))
    for item in range (1, y):         
        if item % 3 == 0:
            
            (print(f"Numbers divisible by 3 are: {item}"))
    return (item) 


def divide_by_five():
    x = 1
    y = int(input('Enter the number upto you want to find divisible by 5: '))
    for item in range (1, y):         
        if item % 5 == 0:
            (print(f"Numbers divisible by 5 are: {item}"))
    return (item) 


def start():
    print ('''
        Select numbers according to your choice to perform different mathematical functions:
        addition                                    -->> 1
        subtraction                                 -->> 2
        multiplication                              -->> 3
        division                                    -->> 4
        remainder                                   -->> 5
        even numbers upto a  number of your choice  -->> 6
        odd numbers upto a number of your choice    -->> 7
        divide by 3                                 -->> 8
        dicide by 5                                 -->> 9

        ''')
    choice = input(">")

    if choice == "1":
        add_two_numbers()
        print("\n")
        print("Choose number to continue doing maths or CTRL+C to abort")
        start()
        
        
        
    elif choice == '2':
        subtract_two_numbers()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '3':
        multiply_two_numbers()        
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '4':
        divide_two_numbers()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '5':
        remainder_of_two_numbers()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '6':
        even_numbers()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '7':
        odd_numbers()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '8':
        divide_by_three()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    elif choice == '9':
        divide_by_five()
        print("\n")
        print("Choose number to continue or CTRL+C to abort")
        start()

    else:
        print("Please enter the correct number from given list")
        start()

start()
    
        

