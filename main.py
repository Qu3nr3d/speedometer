import pandas as pd
from tkinter import *
from PIL import Image


# def convert_img(path, x_size, y_size):
#     img = Image.open(path)
#     resized_img = img.resize((x_size, y_size), Image.Resampling.LANCZOS)
#     resized_img.save(path)
#     img.close()

def enter_pressed(event, word, inputtxt, text_var):
    global words, random_word, used_words, wrong_words_counter, words_counter
    txt = inputtxt.get("1.0", END)
    if txt.strip() != word.strip():
        wrong_words_counter += 1
    words_counter += 1

    words = words[words['WORDS'] != random_word]
    used_words.append(random_word)
    random_word = str(words['WORDS'].sample().iloc[0])
    text_var.set(random_word)

    inputtxt.delete('1.0', END)


def countdown(timer_label, counter, word, inputtxt):
    if counter >= 0:
        timer_label.config(text=f"Time left: {counter} seconds")
        window.after(1000, lambda: countdown(timer_label, counter-1, word, inputtxt))
    else:
        timer_label.config(text="Time's up!")
        results(word, inputtxt, words_counter, wrong_words_counter)


def results(word, inputtxt, wc, wwc):
    word.grid_forget()
    inputtxt.grid_forget()
    result = Label(window, text=f"Words per minute:{wc} with accuracy: {round((wc - wwc)/wc * 100, 2)}%")
    result.grid(column=0, row=2)


def speedometer_start():
    start_button.grid_forget()

    timer_label = Label(window, text="Time left: 60 seconds")
    timer_label.grid(column=0, row=0, pady=10)

    text_var = StringVar()
    text_var.set(random_word)
    word = Label(window, textvariable=text_var, font=('Helvetica', 16))
    word.grid(column=0, row=2)

    inputtxt = Text(window, height=1, width=15, font=("Helvetica", 13))
    inputtxt.grid(column=0, row=3)
    inputtxt.focus_set()

    inputtxt.bind('<space>', lambda event: enter_pressed(event, random_word, inputtxt, text_var))

    countdown(timer_label, 60, word, inputtxt)


BG_COLOR = '#070F2B'
words = pd.read_csv('data/Zeszyt1.csv')
used_words = []
words_counter = 0
wrong_words_counter = 0
random_word = str(str(words['WORDS'].sample().iloc[0]))

window = Tk()
window.title("speedo'meter")
window.config(padx=50, pady=50, background=BG_COLOR)

# convert_img('data/images/speedometer.png', 400, 263)

canvas = Canvas(width=800, height=526)
speedometer = PhotoImage(file='data/images/speedometer.png')
show_img = canvas.create_image(400, 263, image=speedometer)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=1)

start_button = Button(window, text='check your writing speed', command=speedometer_start)
start_button.grid(column=0, row=2)

window.mainloop()
