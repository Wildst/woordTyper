from tkinter import *

class WoordTyper(Frame):
    def __init__(self, words, bg="white", font=(lambda family="Commic Sans MS", size=50, style="bold": ("Commic Sans MS", 50, "bold")), master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.position = 0
        self.words = words
        self.background_color = bg
        self.font = font
        self.create_widgets()
        self.configure(background=self.background_color)

    def create_widgets(self):
        wrapper = Frame(self)
        wrapper.pack(fill=X, expand=True)
        wrapper.configure(background=self.background_color)
        # Word to type
        self.title = StringVar()
        self.title.set(self.words[self.position])
        Label(wrapper, textvariable=self.title, fg="black", bg=self.background_color, font=self.font()).pack(anchor="w", padx=20, pady=10)

        # Input field
        self.input = Entry(wrapper, font=self.font(), bg=self.background_color, fg="black")
        self.input.pack(fill=X, expand=True, padx=19)
        self.contents = StringVar()
        self.contents.set("")
        self.input["textvariable"] = self.contents
        self.input.bind('<Key-Return>', self.handle_enter_pressed)
        self.input.bind('<KeyRelease>', self.handle_input_changed)

        self.quit = Button(self, text="STOP", bg=self.background_color, relief="groove", fg="red", font=self.font(size=20),
                              command=self.master.destroy)
        self.quit.pack(pady=5)

    def handle_input_changed(self, event):
        if event.keysym != "Return":
            self.input.configure(background=self.background_color)

    def handle_enter_pressed(self, event):
        if self.contents.get().strip().lower() == self.words[self.position].lower():
            self.input.configure(background="green")
            self.next_word()
        else:
            self.input.configure(background="red")

    def next_word(self):
        self.position += 1
        if self.position == len(self.words):
            self.contents.set("")
            self.input.configure(state="disabled")
            self.title.set("Goed gedaan!!")
        else:
            self.contents.set("")
            self.title.set(self.words[self.position])
