import random
import game_data
import art
import os
import sys

current_comparison_a = {}
current_comparison_b = {}
score = 0
correct = True

should_continue = True

def assign():
    global current_comparison_a
    global current_comparison_b

    if len(current_comparison_a) == 0 and len(current_comparison_b) == 0:
        current_comparison_a = random.choice(game_data.data)
        game_data.data.remove(current_comparison_a)
        current_comparison_b = random.choice(game_data.data)

    else:
        game_data.data.append(current_comparison_a)
        current_comparison_a = current_comparison_b
        game_data.data.remove(current_comparison_a)
        current_comparison_b = random.choice(game_data.data)

def comparison():
    global current_comparison_a
    global current_comparison_b
    global should_continue
    global score

    followers_A = current_comparison_a['follower_count']
    followers_B = current_comparison_b['follower_count']

    vote = input("Who has more Instagram followers? Type 'A' or 'B': ").upper()

    if vote != "A" and vote != "B":
        print("Incorrect command. Please use either A or B for your answer.")
        comparison()

    if followers_A > followers_B:
        if vote == "A":
            score += 1
            os.system('cls')
            return
        elif vote == "B":
            should_continue = False
            os.system('cls')
    elif followers_B > followers_A:
        if vote == "B":
            score += 1
            os.system('cls')
            return
        elif vote == "A":
            should_continue = False
            os.system('cls')

def lose():
    global score

    print(art.logo)
    print(f"Sorry, that's an incorrect answer.\nYour final score: {score} point(s).\nThank you for playing!\n")
    input("Press any key to exit.")
    sys.exit()

def gameplay():
    global current_comparison_a
    global current_comparison_b
    global should_continue

    while should_continue:

        assign()

        print(art.logo)
        print(f"Compare A: {current_comparison_a['name']}, a {current_comparison_a['description']}, from {current_comparison_a['country']}.")
        print(art.vs)
        print(f"Against B: {current_comparison_b['name']}, a {current_comparison_b['description']}, from {current_comparison_b['country']}.")

        comparison()

    lose()

gameplay()