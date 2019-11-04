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


# Here is output as observed from the terminal:
'''
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

        
>1
Enter first number: 2
Enter second number: 3
Sum of 2 and 3 is: 5


Choose number to continue doing maths or CTRL+C to abort

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

        
>7
Enter the number upto you want to find odd numbers: 10
Odd numbers are: 1
Odd numbers are: 3
Odd numbers are: 5
Odd numbers are: 7
Odd numbers are: 9


Choose number to continue or CTRL+C to abort

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

        
>9
Enter the number upto you want to find divisible by 5: 100
Numbers divisible by 5 are: 5
Numbers divisible by 5 are: 10
Numbers divisible by 5 are: 15
Numbers divisible by 5 are: 20
Numbers divisible by 5 are: 25
Numbers divisible by 5 are: 30
Numbers divisible by 5 are: 35
Numbers divisible by 5 are: 40
Numbers divisible by 5 are: 45
Numbers divisible by 5 are: 50
Numbers divisible by 5 are: 55
Numbers divisible by 5 are: 60
Numbers divisible by 5 are: 65
Numbers divisible by 5 are: 70
Numbers divisible by 5 are: 75
Numbers divisible by 5 are: 80
Numbers divisible by 5 are: 85
Numbers divisible by 5 are: 90
Numbers divisible by 5 are: 95


Choose number to continue or CTRL+C to abort

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

>
'''
    
        

