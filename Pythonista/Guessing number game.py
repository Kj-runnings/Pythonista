# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# Set the initial values

the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop

# Be careful with indentation, especially after them cos it can create infinite loops.

while guess != the_number:
    if guess > the_number:
        print("lower..")
    else:
        print("higher..")
        
    guess = int(input("take a guess: "))
    tries += 1
    
print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")


