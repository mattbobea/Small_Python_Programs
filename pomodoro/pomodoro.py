import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(clock, text="00:00")
    label.config(text="")
    canvas.itemconfig(title, text="Timer", fill=PINK, font=(FONT_NAME, 34))
    label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global mark
    reps += 1
    # work_sec = work
    if reps == 8:
        count_down(LONG_BREAK_MIN*60)
        canvas.itemconfig(title, text="Long Rest", fill="RED")
    # rest time:
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        canvas.itemconfig(title, text="Rest", fill="PINK")
    # work:
    else:
        count_down(WORK_MIN)
        canvas.itemconfig(title, text="Work!", fill="GREEN")



# --------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(clock, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for session in range(work_sessions):
            mark += "✔"
            label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=75, pady=25, bg=YELLOW)

canvas = Canvas(width=250, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 175, image=tomato_img)
clock = canvas.create_text(130, 190, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
title = canvas.create_text(130, 40, text="Timer", fill=PINK, font=(FONT_NAME, 34))
canvas.grid(column=1, row=0)

# Button 1
button = Button(text="Start", command=start_timer)
button.grid(column=0, row=3)


# Button 2
button2 = Button(text="Reset", command=reset_timer)
button2.grid(column=2, row=3)

# check marks
label = Label(fg="green", bg=YELLOW, font=30)
label.grid(column=1, row=2)

window.mainloop()
