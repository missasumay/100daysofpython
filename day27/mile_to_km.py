from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=10, pady=10)



mile = Entry(width=10, justify="center")
mile.insert(END, "0")
mile.grid(column=2, row=1)

miles_txt = Label(text="Miles")

miles_txt.grid(column=3, row=1)

is_equal_to_txt = Label(text="is equal to")

is_equal_to_txt.grid(column=1, row=2)

amount_var = 0
amount_txt = Label(text="0")

amount_txt.grid(column=2, row=2)

km_text = Label(text="Km")

km_text.grid(column=3, row=2)

def calculate():
    to_calc = int(mile.get())
    amount_var = round((to_calc * 1.609), 2)

    amount_txt['text'] = amount_var

calc_button = Button(text="Calculate", command=calculate)

calc_button.grid(column=2, row=3)

window.mainloop()