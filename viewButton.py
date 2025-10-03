from tkinter import *
import math
import os
from typing import *

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

        self.button0 = self.createButton("0", "number", column_ = 0)
        self.button1 = self.createButton("1", "number", 1)
        self.button2 = self.createButton("2", "number", 2)
        self.button3 = self.createButton("3", "number", 3)
        self.button4 = self.createButton("4", "number", 4)
        self.button5 = self.createButton("5", "number", 5)
        self.button6 = self.createButton("6", "number", 6)
        self.button7 = self.createButton("7", "number", 7)
        self.button8 = self.createButton("8", "number", 8)
        self.button9 = self.createButton("9", "number", 9)

    def showButton(self):
        self.button.grid(row=self.row, column=self.col, padx=3, pady=3)
        if self.type == "switch":
            self.mode_button.grid(row=self.row, column=self.col, columnspan=6, padx=3, pady=3)
        if self.type != "sci":
            self.button.config(font=("Arial", 18))
    
    def createButton(self, label:str, typeButton:str, column_:int) -> None:
        text =label
        width_=None
        color=None
        if typeButton == "number":
            width_ = 3
            color = "light green"
        else:
            pass
        
        myButton = Button(self.root, text="1", width=width_, relief=RAISED, bg=color) #command=lambda:self.ins(text): Isso é uma lógica do controller, depois a gente vê como fica
        myButton.config(font=("Arial", 18))
        myButton.grid(row=1, column=column_, padx=3, pady=3)
        return Button