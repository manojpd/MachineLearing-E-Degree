# Guessing Game
# import numpy as np

print("How many games you wish to play")
num_of_game = int(input())

from random import *
x = randint(1,25)

# x = 5

print("You need to enter a number between 1 and 25")

i = 1
while i <= num_of_game:
    print("Enter the magic number")
    num_entered = int(input())
#     print (num_entered)
    
    if num_entered == x:
        print("Hurrah!! you predicted the number right in {} chances" .format(i))
        break
    
    elif (num_entered < x) and (i != num_of_game):
        print("Enter a number greater than " ,num_entered)
        
    elif num_entered > x and (i != num_of_game):
        print("Enter a number less than " ,num_entered)
        
    elif (i == num_of_game):
        print("Sorry you lost the game")
        
    i = i+1
