import random
import words
import art

display = []

chosen_word = random.choice(words.word_list)

end_of_game = False

lives = 6

print(art.logo)

for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
            print("This letter has already been guessed. Please enter a different one.")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("This letter is not in the word. You are losing one chance.")
        lives -= 1

        print(art.stages[lives])
        
        if lives == 0:
            end_of_game = True
            print("you failed")

    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("you won")