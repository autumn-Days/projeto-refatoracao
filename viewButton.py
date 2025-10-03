from tkinter import *
import math
import os

class viewButton:
    def __init__(self, txt, cmd, type, rw, cl):
        self.row = rw
        self.col = cl
        self.type = type
        self.self.last_pressed_equal = False
        if type == "regular" :
            self.button = Button(self.root, text=txt, width=3, command=lambda:self.ins(cmd), relief=RAISED, bg='light green')
        elif type == "equal":
            self.button = Button(self.root, text="=", width=3, command=self.calculate, relief=RAISED, bg='light grey')
        elif type == "clear":
            self.button = Button(self.root, text="C", width=3, command=self.clear, relief=RAISED, bg='light grey')
        elif type == "var":
            self.button = Button(self.root, text=txt, width=3, command=lambda:self.var(cmd), relief=RAISED, bg='light yellow')
        elif type == "switch":
            self.button = Button(self.root, text="Switch to Scientific", width=20, command=self.toggle_mode, relief=RAISED, bg='light blue')
        elif type == "sci":
            self.button = Button(self.root, text=txt, width=3, command=lambda:self.scientific(cmd), relief=RAISED, bg='light blue')
        
    def showButton(self):
        self.button.grid(row=self.row, column=self.col, padx=3, pady=3)
        if self.type == "switch":
            self.mode_button.grid(row=self.row, column=self.col, columnspan=6, padx=3, pady=3)
        if self.type != "sci":
            self.button.config(font=("Arial", 18))