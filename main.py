#! /usr/bin/python

from tkinter import *
from woordTyper import WoordTyper
from optionScreen import OptionScreen
import random

background_color = "#c4dbff"
def myfont(family="Commic Sans MS", size=50, style="bold"):
    return (family, size, style)



def start_game(filename):
    with open(filename) as file:
        words = [line.strip() for line in file]
    if len(words) > 100:
        words = random.sample(words, 100)
    else:
        random.shuffle(words)
    for child in root.winfo_children():
        child.pack_forget()
    app = WoordTyper(words,
                    bg=background_color, font=myfont, master=root)
    app.mainloop()


root = Tk()
root.title("WoordTyper")
root.geometry("600x800")
root.configure(background=background_color)

app = OptionScreen(callback=start_game, font=myfont, master = root)
app.mainloop()

