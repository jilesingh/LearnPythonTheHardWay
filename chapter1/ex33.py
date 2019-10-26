# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

i = 0
numbers = []
loopCount = 6
while i < loopCount:
    print ("At the top i is %d" %i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now:", numbers)
    print ("At the bottom i is %d" %i)

print ("The numbers: ")

for num in numbers:
    print (num)
   

# Here is output as observed from the terminal:
'''
At the top i is 0
Numbers now: [0]
At the bottom i is 1
At the top i is 1
Numbers now: [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now: [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now: [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now: [0, 1, 2, 3, 4]
At the bottom i is 5
At the top i is 5
Numbers now: [0, 1, 2, 3, 4, 5]
At the bottom i is 6
The numbers: 
0
1
2
3
4
5
'''