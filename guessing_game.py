"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


high_score = []

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """

    print("Welcome to the number guessing game!  Get ready for a thrill!")



def check_number(number_guessed=None):
    number_of_trys = 0
    play = True
    magic_number = random.randint(1,10)
    print("Hey there, sports fan!")

    while play:
        try:
            number_guessed = input("Guess a number between 1 and 10   ")
            number_guessed = int(number_guessed)
            if number_guessed not in range(1, 11):
                raise ValueError
        except ValueError:
            print("{} is not a whole number between 1 and 10, silly".format(number_guessed))
            continue

        if number_guessed > magic_number:
            number_of_trys += 1
            print("Too high, try again!")

        elif number_guessed < magic_number:
            number_of_trys += 1
            print("Too low, try again")

        else:
            number_of_trys += 1
            print("Whoa Nelly! {} is correct")
            print("That took you {} trys.".format(number_of_trys))
            high_score.append(number_of_trys)
            high_score.sort()


            while True:
                again = input("Would you like to play again? [y]es or [n]o?   ")
                if again == ('NO'.lower()) or again == ('N'.lower()):
                #code adapted from stack overflow BjoernD
                    print("Lame, Good Bye")
                    play = False
                    break

                elif again == ('YES'.lower()) or again == ('Y'.lower()):
                #code adapted from stack overflow BjoernD
                    print("I am so glad to hear that")
                    print("Your best score as been {} trys".format(high_score[0]))
                    start_game()
                    check_number()
                    break

                else:
                    print("Please indicate yes or no")














if __name__ == '__main__':
    # Kick off the program by calling the start_game function.

    start_game()
    check_number()

