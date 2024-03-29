from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
french_word = {}
fr_en_dict = {}

#============= FRENCH-ENGLISH DICTIONARY ==============#

try:
    data = pandas.read_csv("day31\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("day31\\data\\french_words.csv")
    fr_en_dict = data.to_dict(orient="records")
else:
    fr_en_dict = data.to_dict(orient="records")

#============= RANDOM FRENCH WORD ==============#

def new_french_word():
    global french_word
    french_word = random.choice(fr_en_dict)

    #============= RANDOM FRENCH WORD ==============#
    flashcard_fr.itemconfig(fr_bg, image=flashcard_fr_image)
    flashcard_fr.itemconfig(fr_title, text="French", fill="black")
    flashcard_fr.itemconfig(fr_word, text=french_word["French"], fill="black")
    window.after(3000, func=flip_card) # 3 seconds

    return french_word

#============= ENGLISH TRANSLATION ==============#

def flip_card():
    global french_word

    flashcard_fr.itemconfig(fr_bg, image=flashcard_en_image)
    flashcard_fr.itemconfig(fr_title, text="English", fill="white")
    flashcard_fr.itemconfig(fr_word, text=french_word["English"], fill="white")

#============= REMOVING KNOWN WORDS ==============#
def is_known():
    global french_word
    fr_en_dict.remove(french_word)
    words_to_learn = pandas.DataFrame(fr_en_dict)
    words_to_learn.to_csv("day31\\data\\words_to_learn.csv", index=False)
    new_french_word()

#============== UI ==============#
window = Tk()
window.title("PyFlashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card) # 3 seconds


flashcard_fr_image = PhotoImage(file="day31\\images\\card_front.png")
flashcard_en_image = PhotoImage(file="day31\\images\\card_back.png")
flashcard_fr = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
fr_bg = flashcard_fr.create_image(400, 260, image=flashcard_fr_image)
fr_title = flashcard_fr.create_text(400, 150, text="", font=("Arial", 40, "italic"))
fr_word = flashcard_fr.create_text(400, 263, text="", font=("Arial", 60, "bold"))
flashcard_fr.grid(column=1, row=1, columnspan=2)

red_button_image = PhotoImage(file="day31\\images\\wrong.png")
green_button_image = PhotoImage(file="day31\\images\\right.png")


right_answer = Button(image=green_button_image, highlightthickness=0, height=100, width=100, borderwidth=0, command=new_french_word)
right_answer.grid(column=1, row=2)

wrong_answer = Button(image=red_button_image, highlightthickness=0, height=100, width=100, borderwidth=0, command=new_french_word)
wrong_answer.grid(column=2, row=2)


new_french_word()



window.mainloop()
