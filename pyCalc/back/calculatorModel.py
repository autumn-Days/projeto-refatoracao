import tkinter as tk
from tkinter import ttk
import ast
import math

class CalculatorModel():

    def __init__(self, master = None):
        self.master = master

    def factorial(self, operator):
        number = int(self.master.display.get())
        fact = 1
        try:
            while number > 0:
                fact = fact*number
                number -= 1
            self.clear_all()
            self.master.display.insert(0, fact)
        except Exception:
            self.clear_all()
            self.master.display.insert(0, "Error")

    def clear_all(self, new_operation=True):
        self.master.display.delete(0, tk.END)
        self.master.NEW_OPERATION = new_operation

    def get_variables(self, num):
        if self.master.NEW_OPERATION:
            self.clear_all(new_operation=False)
        self.master.display.insert(self.master.i, num)
        self.master.i += 1

    def get_operation(self, operator):
        #Obtem o operando que o usuario quer aplicar a uma funcao
        length = len(operator)
        self.master.display.insert(self.master.i, operator)
        self.master.i += length

    def undo(self):
        #Remove o ultim operador ou digito inserido
        whole_string = self.master.display.get()
        if len(whole_string):        
            new_string = whole_string[:-1]
            self.clear_all(new_operation=False)
            self.master.display.insert(0, new_string)
        else:
            self.clear_all() 
            self.master.display.insert(0, "Error, press AC")

    def sqrt(self):
        num = int(self.master.display.get())
        num = math.sqrt(num)
        self.master.display.insert(0, num)
    
    def sen(self):
        num = int(self.master.display.get())
        num = math.sin(num)
        self.master.display.insert(0, num)
            
    def cos(self):
        num = int(self.master.display.get())
        num = math.cos(num)
        self.master.display.insert(0, num)

    def tan(self, tan:float):
        num = int(self.master.display.get())
        num = math.tan(num)
        self.master.display.insert(0, num)

    def switch(self):
        return 

    def calculate(self):
        """Evaluates the expression.
        ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
        """
        whole_string = self.master.display.get()
        try:
            result = eval(compile(ast.parse(whole_string, mode="eval"), "<string>", "eval"))
            self.clear_all()
            self.master.display.insert(0, result)
        except Exception:
            self.clear_all()
            self.master.display.insert(0, "Error!")