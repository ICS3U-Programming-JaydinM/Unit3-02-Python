#!/usr/bin/env python3
# Made by Jaydin Madore
# Made on 2022-09-27
# get a number and then you have to guess it.

from random import randint

# 2. Print the start screen
print("I'm thinking of a number between 0 and 9.")

# Generate a random number between 0 and 9
answer = randint(0, 9)

# 4.2 Function 2
def guess():

    # Get the guess from the user
    guess = int(float(input("Make a guess: ")))
    # Series of if, elif statements to
    # compare the guess with the answer
    if guess < 0 or guess > 9:
        print(f"Invalid guess!\nIt should be between 0 and 9.")
    elif guess == answer:
        print(f"\nYou got it! The answer was {answer}!\n\n")
    elif guess != answer:
        print(f"\nyou lose.\nThe number was {answer}!\n\n")


# Call the MAIN function
guess()
