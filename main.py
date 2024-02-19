import pandas as pd
from tkinter import *
from PIL import Image



def convert_img(path, x_size, y_size):
    img = Image.open(path)
    resized_img = img.resize((x_size, y_size), Image.Resampling.LANCZOS)
    resized_img.save(path)
    img.close()


def enter_pressed(event, word):
    txt = inputtxt.get("1.0", END)
    if txt.strip().lower() == word.strip().lower():
        print('good')
    else:
        print('bad')

BG_COLOR = '#070F2B'
words = pd.read_csv('data/Zeszyt1.csv')
random_word = str(str(words['WORDS'].sample().iloc[0]))
window = Tk()
window.title("speedo'meter")
window.config(padx=50, pady=50, background=BG_COLOR)
convert_img('data/images/speedometer.png', 400, 263)
canvas = Canvas(width=800, height=526)
speedometer = PhotoImage(file='data/images/speedometer.png')
show_img = canvas.create_image(400, 263, image=speedometer)
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)


text_var = StringVar()
text_var.set(random_word)
x = Label(window, textvariable=text_var, font=('Helvet', 16))
x.grid(column=0, row=1)

inputtxt = Text(window, height=1, width=15, font=("Helvetica", 13))
inputtxt.grid(column=0, row=2)

inputtxt.bind('<Return>', lambda event: enter_pressed(event, random_word))

window.mainloop()
