from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

FONT_NAME = "Arial"
FONT_SIZE = 10
FONT_WEIGHT = "normal"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    characters = [LETTERS[num] for num in range(nr_letters)]
    symbols = [SYMBOLS[num] for num in range(nr_symbols)]
    numbers = [NUMBERS[num] for num in range(nr_numbers)]

    password_generated = []

    for char in characters:
        password_generated.append(char)

    for sym in symbols:
        password_generated.append(sym)

    for num in numbers:
        password_generated.append(num)

    random.shuffle(password_generated)

    password = ""

    for char in password_generated:
        password += char

    password_input.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    username =  username_input.get()
    password = password_input.get()

    if len(website) == 0:
        messagebox.showerror(title="ERROR", message="Your website name/address is empty, data will not be saved to the file.")
    elif len(username) == 0:
        messagebox.showerror(title="ERROR", message="Your username is empty, data will not be saved to the file.")
    elif len(password) == 0:
        messagebox.showerror(title="ERROR", message="Your pasword is empty, data will not be saved to the file.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}\nPassword: {password}\nIs this ok to save?")

        if is_ok:
            data = open("day29\\password.txt", "a")
            data.write(f"{website} || {username} || {password}\n")
            data.close()

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)
bg_img = PhotoImage(file="day29\\logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=bg_img)

canvas.grid(column=2, row=1)

# Input labels

website_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), highlightthickness=0)
website_label.grid(column=1, row=2)

username_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), highlightthickness=0)
username_label.grid(column=1, row=3)

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, FONT_WEIGHT), highlightthickness=0)
password_label.grid(column=1, row=4)

# Inputs

website_input = Entry(width=35, highlightthickness=0)
website_input.grid(column=2, row=2, columnspan=2, sticky=EW)

username_input = Entry(width=35, highlightthickness=0)
username_input.grid(column=2, row=3, columnspan=2, sticky=EW)

password_input = Entry(width=21, highlightthickness=0)
password_input.grid(column=2, row=4, sticky=EW)


# Buttons

generate_password_button = Button(text="Generate Password", width=15, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=3, row=4, sticky=EW)

add_to_file_button = Button(text="Add", width=36, highlightthickness=0, command=save_password)
add_to_file_button.grid(column=2, row=5, columnspan=2, sticky=EW)








window.mainloop()