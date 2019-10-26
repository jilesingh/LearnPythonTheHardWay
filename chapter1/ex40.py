# -*- coding utf-8 -*-
# This code is written and run using Python Version 3.6.8

# Creating first class

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I will stop right there\n"])

bulls_on_parade = Song(["They really around the family",
                        "With pockets full of family\n"])

happy_diwali = Song(["Diwali is the biggest festival of Hindus",
                     "It is celebrated on the ocassaion of ",
                     "Lor rama came back to Ayodhya\n"])

rainy_day = Song(["We used to go out on the rainy day",
                  "We have made paper boats",
                  "Paper boats were very beautiful"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
happy_diwali.sing_me_a_song()
rainy_day.sing_me_a_song()


#Here is output as observed from the terminal:
'''
Happy birthday to you
I don't want to get sued
So I will stop right there

They really around the family
With pockets full of family

Diwali is the biggest festival of Hindus
It is celebrated on the ocassaion of 
Lor rama came back to Ayodhya

We used to go out on the rainy day
We have made paper boats
Paper boats were very beautiful
'''