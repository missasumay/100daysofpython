from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 20
reps = 0
timer = None
checkmarks = []

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label['text'] = "Timer"
    checkmarks = []

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label['text'] = 'Break'
        countdown(long_sec)
    elif reps % 2 == 0:
        label['text'] = 'Break'
        countdown(short_sec)
    else:
        label['text'] = 'Work'
        countdown(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 == 0:
            checkmark()
            start_timer()
        else:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="python\\100daysofcode\\day28\\tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=1, column=2)

start = Button(text="START", highlightthickness=0, command=start_timer)
start.grid(row=3, column=1, )

reset = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=3)

def checkmark():
    global checkmarks

    checkmark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
    checkmarks.append(checkmark)
    checkmark.grid(row=4, column=2)






window.mainloop()