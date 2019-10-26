# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

# We are not going to run anything here. We will just import these functions

def break_words(stuff): # This function will break up words for us
    words = stuff.split(' ')
    return words

def sort_words(words): # This function will sorts the words
    return sorted(words)

def print_first_word(words): # Prints the forst word after popping it up
    word = words.pop(0)
    print (word)

def print_last_word(words): # This function will print the last word after popping it off
    word = words.pop(-1)
    print (word)

def sort_sentence(sentence): # This function will take the full sentence and return the sorted words.
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence): # prints the first and last word of the sentence
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence): # sorts the words and then print first and last one
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Here is output as observed from the terminal:
'''
>>> import ex25
>>> sentence = "All good things happen to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'happen', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25
ex25
>>> sorted_words = ex25
ex25
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'good', 'happen', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'happen', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['good', 'happen', 'things', 'those', 'to', 'wait.']
>>> sorted_words
['good', 'happen', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'good', 'happen', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(setencce)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setencce' is not defined
>>> ex25.print_first_and_last(setence)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'setence' is not defined
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> ex25.print_first_and_last_sorted(sentence)
All
who
>>> 

'''






    