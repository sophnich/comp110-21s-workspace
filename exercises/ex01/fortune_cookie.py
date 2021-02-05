"""Program that outputs one of at least four random, good fortunes."""

"""__author__ = "730314283" """



# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
# Begin your solution here...



print("Your fourtune cookie says...")
from random import randint
fortune: int = randint(1, 3)
if fortune <= 2: 
    if fortune < 2:
        print("You will lose all your blueberry muffins")
    else: 
        print("You will adopt a rabbit and name it Lil Bunny.")
else: 
    if fortune > 2:
        print ("Your mom will invest all your college fund money in gamestop.")

print("Now, go spread positive vibes!")