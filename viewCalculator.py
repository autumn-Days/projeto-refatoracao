from tkinter import *
import math
import os

class viewCalculator():

    def __init__(self):
        self.root = Tk()
        self.resultwindow = Entry(self.root, borderwidth=5, relief=SUNKEN)

        self.rootSetting()
        self.windowSetting()

        # Mode toggle at the bottom
        self.mode = "basic"  # Default mode
        self.mode_button = Button(self.root, text="Switch to Scientific", width=20, command=self.toggle_mode, relief=RAISED, bg='light blue')
        self.mode_button.grid(row=6, column=0, columnspan=6, padx=3, pady=3)

        self.buttons = {}
        self.sci_buttons = {}

    def rootSetting(self):
        self.root.title("Calculator")
        self.root.geometry("400x450")  # Adjusted height for variable buttons

        self.root.maxsize(400, 450)
        self.root.minsize(400, 450)
        self.root.config(bg="grey")

    def windowSetting(self):
        self.resultwindow.grid(row=0, column=0, columnspan=6, pady=5)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()

    def toggle_mode(self):
        if self.mode == "basic":
            self.mode = "scientific"
            self.mode_button.config(text="Switch to Basic")
            self.show_scientific_buttons()
        else:
            self.mode = "basic"
            self.mode_button.config(text="Switch to Scientific")
            self.hide_scientific_buttons()

    def show_buttons(self):
        pass

    def show_scientific_buttons(self):
        pass

    def hide_scientific_buttons(self):
        pass
