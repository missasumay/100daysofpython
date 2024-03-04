import os
import art

list_of_bids = {}
winner = ""
winning_bid = 0

def intro():
    print(art.logo)
    print("Welcome to the secret auction program.")

def add_new_people():
    more_people = True
    
    while more_people == True:
        name = input("What is your name? ")
        bid = int(input("What's your bid? $"))

        list_of_bids[name] = bid

        any_other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

        if any_other_bidders == 'no':
            more_people = False
        elif any_other_bidders == 'yes':
            os.system('cls')

def who_won():
    global winner
    global winning_bid

    for key in list_of_bids:
        value = list_of_bids[key]

        if value > winning_bid:
            winner = key
            winning_bid = list_of_bids[key]
    
    print(f"The winner is {winner} with a bid of ${winning_bid}")

intro()
add_new_people()
who_won()
