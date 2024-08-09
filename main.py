# Author: Alvin Dandeebo/

from tkinter import *
import pandas as pd
import random

try:
    open("./data/words_to_learn.csv", 'r')
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
else:
    df = pd.read_csv("data/words_to_learn.csv")
french_words_dict = df.to_dict(orient='records')
dict_value = {}


def know():
    random_dict = random.choice(french_words_dict)
    global dict_value
    dict_value = random_dict
    french_word = random_dict['French']
    canvas.itemconfig(french_text, text=french_word, fill='black')
    window.after(3000, show_back)
    french_words_dict.remove(dict_value)
    df2 = pd.DataFrame.from_records(french_words_dict)
    df2.to_csv("./data/words_to_learn.csv", index=False)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(language_text, text='French', fill='black')


def dont_know():
    random_dict = random.choice(french_words_dict)
    global dict_value
    dict_value = random_dict
    french_word = random_dict['French']
    canvas.itemconfig(french_text, text=french_word, fill='black')
    window.after(3000, show_back)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(language_text, text='French', fill='black')


def show_back():
    global dict_value
    english_word = dict_value['English']
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(french_text, text=english_word, fill='white')
    canvas.itemconfig(language_text, text='English', fill='white')


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashino")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text='French', font=('Ariel', 40, 'italic'), fill='black')
french_text = canvas.create_text(400, 263, text='trouve', font=('Ariel', 40, 'bold'), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=dont_know)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=know)
right_button.grid(row=1, column=1)

window.mainloop()
