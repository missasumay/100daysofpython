import random
import arcanas

card_image = '''\n
                                      .------.
                   .------.           |A .   |
                   |A_  _ |    .------; / \  |
                   |( \/ )|-----. _   |(_,_) |
                   | \  / | /\  |( )  |  I  A|
                   |  \/ A|/  \ |_x_) |------'
                   `-----+'\  / | Y  A|
                         |  \/ A|-----'    
                         `------'
\n
'''
print(card_image)
your_name = input("Welcome to Snake's Card Reading. Please type in your name: ")
age = input("\nPlease provide your age: ")

print(f"Looking for a suitable card for {your_name}, age {age}...")

which_card = random.randint(0, 20)

your_card = arcanas.all[which_card]

print(your_card)