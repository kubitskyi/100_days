from tkinter import *
import math

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
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_text.config(text="Timer")
    check_marck_text.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break__sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break__sec)
        title_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        wokr_sessions = math.floor(reps/2)
        for _ in range(wokr_sessions):
            marks += "✓"
        title_text.config(text="Work", fg=GREEN)
        check_marck_text.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image = tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

title_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_text.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0,  bg=YELLOW, command=start_timer)
start_button.grid(column=0 , row=2)

rest_button = Button(text="Rest", highlightthickness=0,  bg=YELLOW, command=reset_time)
rest_button.grid(column=2 , row=2)

check_marck_text = Label(bg=YELLOW, fg=GREEN)
check_marck_text.grid(column=1 , row=3)

window.mainloop()