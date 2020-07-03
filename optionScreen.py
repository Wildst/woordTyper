from tkinter import *
from tkinter.filedialog import askopenfilename
import os

MODES = ["Aantal te typen woorden:", "Tijd in minuten:"]

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
        # File picker1
        self.filename = StringVar()
        self.filename.set(os.getcwd() + "/woorden.txt")
        Label(self, textvariable=self.filename, fg="black", bg=self.background_color,
              font=self.font(size=12, style="")).pack(anchor="n", padx=20, pady=10)
        Button(self, text="Kies woorden", bg= self.background_color, relief="groove", fg="black", font=self.font(size=10), command=self.get_filename).pack(anchor="n", pady=20)

        # Select wordcount
        self.linecount = StringVar()
        Label(self, textvariable=self.linecount, fg="black", bg=self.background_color,
              font=self.font(size=12, style="")).pack(anchor="n", padx=20, pady=10)

        # Mode
        self.mode = IntVar()
        self.mode.set(0)
        modeToggle = Frame(self)
        modeToggle.pack()
        modeToggle.configure(bg=self.background_color)
        self.modeLabel = StringVar()
        self.modeLabel.set(MODES[0])
        button = Button(modeToggle, bg=self.background_color, textvariable=self.modeLabel,
        font=self.font(size=10), fg= "black", command=self.toggle_mode)
        button.pack()

        self.amount = StringVar()
        self.amount.set(10)
        entry = Entry(self, font=self.font(size=10, style=""),
              bg=self.background_color, fg="black", textvariable=self.amount)
        entry.pack(pady=10)
        entry.bind('<KeyRelease>', self.handle_input_changed)

        self.validate_label = StringVar()
        Label(self, bg=self.background_color, font=self.font(size=10), textvariable=self.validate_label, fg="black").pack(anchor="n", pady=10)


        # Set settings
        self.go_button = Button(self, text="Ga verder", bg= self.background_color, relief="groove", fg="black", font=self.font(size=20), command=self.confirm)
        self.go_button.pack(side="bottom")

    def handle_input_changed(self, event):
        try:
            int(self.amount.get())
            assert int(self.amount.get()) > 0
            self.validate_label.set("")
            return int(self.amount.get())
        except:
            self.validate_label.set("Ongeldig aantal: \"{}\"".format(self.amount.get()))
            return -1



    def toggle_mode(self):
        self.mode.set((self.mode.get() + 1) % len(MODES))
        self.modeLabel.set(MODES[self.mode.get()])


    def get_filename(self):
        self.filename.set(askopenfilename(title="Selecteer woorden", filetypes=(("tekstbestanden", "*.txt"), ("alle bestanden", "*.*"))))
        if self.filename.get() != "":
            with open(self.filename.get()) as file:
                self.wordcount = len([0 for _ in file])
                self.linecount.set("het gekozen bestand bevat {} woorden".format(self.wordcount))
            self.go_button.configure(state="active")
        else:
            self.go_button.configure(state="disabled")
            self.linecount.set("geen bestand gekozen")


    def confirm(self):
        amount = self.handle_input_changed(None)
        if amount < 0:
            return
        self.callback(self.filename.get(), self.mode.get(), amount)
