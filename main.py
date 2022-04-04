from tkinter import *

# This project is based on the Pomodoro technique of time management
# For more info visit https://en.wikipedia.org/wiki/Pomodoro_Technique

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK_GREEN = "#2eb086"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25 * 60
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
slots = 0
checks = ""
timer_window = ""


# ---------------------------- TIMER RESET ------------------------------- #
def resetTime():
    my_button_start.config(state="normal")
    my_button_reset.config(state="disabled")
    my_window.after_cancel(timer_window)  # To stop the timer
    global checks, slots
    slots = 0
    checks = ""
    my_label.config(text="Timer", fg=DARK_GREEN)
    my_checkmark.config(text=checks)
    my_canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    my_button_start.config(state="disabled")
    my_button_reset.config(state="normal")
    global slots
    slots += 1
    if slots % 8 == 0:
        my_label.config(text="Break", fg=RED)
        countDown(LONG_BREAK_SEC)
    elif slots % 2 == 0:
        my_label.config(text="Break", fg=PINK)
        countDown(SHORT_BREAK_SEC)
    else:
        my_label.config(text="Work", fg=GREEN)
        countDown(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    my_canvas.itemconfig(timer_text, text=f"{count//60 :02d}:{count%60 :02d}")
    # 02d ensures single digits are displayed with a leading zero
    if count > 0:
        global timer_window
        timer_window = my_window.after(1000, countDown, count - 1)
    else:
        global checks
        if slots % 8 == 0:
            checks = ""
        elif slots % 2 != 0:
            checks += " ✔ "
        my_checkmark.config(text=checks)
        startTimer()


# ---------------------------- UI SETUP ------------------------------- #
my_window = Tk()
my_window.title("Pomodoro Timer")
my_window.config(padx=50, pady=50, bg=YELLOW)

my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Setting "highlightthickness" to ZERO removes the white/black border between canvas and window
my_photo_img = PhotoImage(file="tomato.png")
my_canvas.create_image(100, 112, image=my_photo_img)
timer_text = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# "state" determines whether the button is clickable or not
my_button_start = Button(text="Start", highlightbackground=YELLOW, fg="black", command=startTimer, state="normal")
my_button_reset = Button(text="Reset", highlightbackground=YELLOW, fg="black", command=resetTime, state="disabled")

my_label = Label(text="Timer", bg=YELLOW, fg=DARK_GREEN, font=(FONT_NAME, 50, "normal"))
my_checkmark = Label(bg=YELLOW, fg=DARK_GREEN)

my_canvas.grid(column=1, row=1)
my_button_start.grid(column=0, row=2)
my_button_reset.grid(column=2, row=2)
my_label.grid(column=1, row=0)
my_checkmark.grid(column=1, row=3)

my_window.mainloop()
