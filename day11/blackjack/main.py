import random
import art 
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(who):

    if not who:
        who.append(random.choice(CARDS))
        who.append(random.choice(CARDS))
    else:
        who.append(random.choice(CARDS))

    return who


def calculate_score(who):
    score = sum(who)
    return score

def blackjack():

    user = []

    computer = []

    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if want_to_play == "y":
        os.system('cls')

    while want_to_play == "y":
    
        print(art.LOGO)

        should_continue = True

        while should_continue:
            draw_card(user)
            draw_card(computer)

            print(f"Your cards: {user}, current score: {calculate_score(user)}")
            print(f"Computer's first card: {computer[0]}")

            if computer == [11, 10] or computer == [10, 11]:
                print("Computer got Blackjack. You lost!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                computer = []
                user = []
                blackjack()

            elif user == [11, 10] or user == [10, 11]:
                print("You got Blackjack. You win!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                computer = []
                user = []
                blackjack()

            elif calculate_score(user) > 21:
                if user[0] != 11 or user[1] != 11:
                    print("You got over. You lost!")
                    print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                    print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                    should_continue = False
                    want_to_play = "n"
                    computer = []
                    user = []
                    blackjack()

                elif user[0] == 11 or user[1] == 11:
                    if (calculate_score(user) - 10) > 21:
                        print("You got over. You lost!")
                        print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                        print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                        should_continue = False
                        want_to_play = "n"
                        computer = []
                        user = []
                        blackjack()

                    else:
                        user.remove(11)
                        user.append(1)

            elif calculate_score(computer) > 21:
                if computer[0] != 11 or computer[1] != 11:
                    print("Computer got over. You win!")
                    print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                    print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                    should_continue = False
                    want_to_play = "n"
                    computer = []
                    user = []
                    blackjack()

                elif computer[0] == 11 or computer[1] == 11:
                    if (calculate_score(computer) - 10) > 21:
                        print("Computer got over. You win!")
                        print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                        print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                        should_continue = False
                        want_to_play = "n"
                        computer = []
                        user = []
                        blackjack()

                    else:
                        computer.remove(11)
                        computer.append(1)

            decision = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if decision == "y":
                draw_card(user)
                print(f"Your cards: {user}, current score: {calculate_score(user)}")
                print(f"Computer's first card: {computer[0]}")


            if calculate_score(user) > 21:
                print("You got over. You lost!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                blackjack()
            

            if calculate_score(computer) < 17:
                computer_should_continue = True

                while computer_should_continue:
                    draw_card(computer)

                    if calculate_score(computer) >= 17:
                        computer_should_continue = False

            if calculate_score(computer) > 21:
                print("Computer got over. You win!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                computer = []
                user = []
                blackjack()

            if calculate_score(computer) > calculate_score(user):
                print("Computer has a higher score. You lost!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                computer = []
                user = []
                blackjack()

            elif calculate_score(computer) < calculate_score(user):
                print("You have a higher score. You win!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"
                computer = []
                user = []
                blackjack()   

            elif calculate_score(computer) == calculate_score(user):
                print("You both have the same score. It's a draw!")
                print(f"Your final cards: {user}, final score: {calculate_score(user)}")
                print(f"Computer's final cards: {computer}, final score: {calculate_score(computer)}")
                should_continue = False
                want_to_play = "n"   
                computer = []
                user = []
                blackjack()      


blackjack()

