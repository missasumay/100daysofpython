import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[choice])

opponents_choice = random.randint(0, 2)
opponent = options[opponents_choice]

print(f"\nComputer chose:\n{opponent}")

if choice == 0 and opponents_choice == 0:
    print("It's a draw!")
elif choice == 1 and opponents_choice == 1:
    print("It's a draw!")
elif choice == 2 and opponents_choice == 2:
    print("It's a draw!")
elif choice == 0 and opponents_choice == 2:
    print("You win!")
elif choice == 2 and opponents_choice == 1:
    print("You win!")
elif choice == 1 and opponents_choice == 0:
    print("You win!")
elif choice == 1 and opponents_choice == 2:
    print("Computer wins!")
elif choice == 0 and opponents_choice == 1:
    print("Computer wins!")
elif choice == 2 and opponents_choice == 0:
    print("Computer wins!")