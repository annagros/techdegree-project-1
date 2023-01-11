"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

user_name = input("What´s your name? ")
print("Hey {}! Welcome to the Number Guessing Game! \nGuess a number between 1 and 10 ".format(user_name))

def start_game():
    solution = random.randrange(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("What´s your guess {}? ".format(user_name)))
            attempts += 1
            if guess >=11 or guess <=0:
                raise Exception("Please stay within the range of 1 to 10!")
            elif guess == solution:
                print("Wow, you got it {}! \nNumber of attempts needed: {}\n\nWell played, see you next time!".format(user_name, attempts))
                break
            elif guess > solution:
                print("It´s lower")
            elif guess < solution:
                print("It´s higher")
        except ValueError:
            print("Please enter a valid Number!")
        except Exception as e:
            print(e)
        
start_game()