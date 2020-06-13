from tkinter import *
from tkinter.filedialog import askopenfilename
import os

class OptionScreen(Frame):
    def __init__(self, callback, bg="white", font=(lambda family="Commic Sans MS", size=50, style="bold": ("Commic Sans MS", 50, "bold")), master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.background_color = bg
        self.font = font
        self.callback = callback
        self.create_widgets()
        self.configure(background=self.background_color)

    def create_widgets(self):

        # File picker
        self.filename = StringVar()
        self.filename.set(os.getcwd() + "/woorden.txt")
        Label(self, textvariable=self.filename, fg="black", bg=self.background_color,
              font=self.font(size=12, style="")).pack(anchor="w", padx=20, pady=10)
        Button(self, text="Kies woorden", bg= self.background_color, relief="groove", fg="black", font=self.font(size=10), command=self.get_filename).pack(anchor="w", pady=20)

        # Select wordcount
        self.linecount = StringVar()
        Label(self, textvariable=self.linecount, fg="black", bg=self.background_color,
              font=self.font(size=12, style="")).pack(anchor="w", padx=20, pady=10)

        # Start main loop
        self.go_button = Button(self, text="Ga verder", bg= self.background_color, relief="groove", fg="black", font=self.font(size=20), command=self.confirm)
        self.go_button.pack(side="bottom")

    def get_filename(self):
        self.filename.set(askopenfilename(title="Selecteer woorden", filetypes=(("tekstbestanden", "*.txt"), ("alle bestanden", "*.*"))))
        if self.filename.get() != "":
            with open(self.filename.get()) as file:
                self.wordcount = len([0 for _ in file]))
                self.linecount.set("the chosen file contains {} words".format(self.wordcount)
            self.go_button.configure(state="active")
        else:
            self.go_button.configure(state="disabled")


    def confirm(self):
        self.callback(self.filename.get())
