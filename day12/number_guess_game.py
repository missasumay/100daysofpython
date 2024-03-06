#### define the number (random)
#### choose difficulty - easy has 10 attempts, hard has 5 attempts
#### if not guessed correctly - too low or too high

import random
import sys

LOGO = """
   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
"""

number = 0

def easy():
    global number

    should_continue = True
    lives = 10

    while should_continue:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            should_continue = False
        elif guess > number:
            lives -= 1

            if lives == 0:
                print(f"You did not guess the number correctly! The answer is {number}.")
                should_continue = False
            else:
                print(f"Too high.")
                print("Please, make a guess again.")

        elif guess < number:
           lives -= 1

           if lives == 0:
                print(f"You did not guess the number correctly! The answer is {number}.")
                should_continue = False
           else:
                print(f"Too low.")
                print("Please, make a guess again.")



    input("Thank you for playing! Press any key to exit.")
    sys.exit()

def hard():
    global number

    should_continue = True
    lives = 5

    while should_continue:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}.")
            should_continue = False
        elif guess > number:
            lives -= 1

            if lives == 0:
                print(f"You did not guess the number correctly! The answer is {number}.")
                should_continue = False
            else:
                print(f"Too high.")
                print("Please, make a guess again.")

        elif guess < number:
           lives -= 1

           if lives == 0:
                print(f"You did not guess the number correctly! The answer is {number}.")
                should_continue = False
           else:
                print(f"Too low.")
                print("Please, make a guess again.")



    input("Thank you for playing! Press any key to exit.")
    sys.exit()

def intro():
    print(LOGO)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    global number

    number = random.randrange(0,100)

    difficulty_chosen = False

    while not difficulty_chosen:

        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty != "easy" and difficulty != "hard":
            print("Unknown command. Please follow the instructions.")
        else:
            difficulty_chosen = True
        
    if difficulty == "easy":
        easy()

    elif difficulty == "hard":
        hard()

intro()

