import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, shift_amount):

    global direction
    message = ""

    if direction == "decode":
        shift_amount *= -1

    for char in input_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount

            if new_position >= len(alphabet):
                spare = new_position - len(alphabet)
                new_position = spare
                
            if new_position < 0:
                spare = new_position + len(alphabet)
                new_position = spare

            message += alphabet[new_position]
        
        else:
            message += char



    print(f"The {direction}d message is: {message}")

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(input_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye.")