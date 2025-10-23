try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# Python 2
	import Tkinter as tk
	import ttk


import ast

class CalculatorModel():

    def __init__(self):

        self.FONT_LARGE = ("Calibri", 12)  	# selects the font of the text inside buttons
        self.FONT_MED = ("Calibri", 10)
        self.number_btns = [    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
                                ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
                                ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
                                ('0', 5, 1) ]

        self.operation_btns = [ ('+', 2, 3,'+'), ('-', 3, 3, '-'), ('*', 4, 3, '*'),
                                ('/', 5, 3, '/'), ('pi', 2, 4, "*3.14"), ('%', 3, 4, '%'),
                                ('(', 4, 4, '('), ('exp', 5, 4, "**"), (')', 4, 5, ')'),
                                ('^2', 5, 5, "**2")]

        self.other_btns = [ ('AC', 5, 0), ('=', 5, 2), 
                            ('<-', 2, 5), ('x!', 3, 5)]

        self.button_list = {}
        self.display = None

    def _init_ui(self):
        for button, y, x in self.number_btns :
            parameters = (button)
            self.button_list[button] = self.create_button(parameters, number=True)

        for button, y, x, op in self.operation_btns :
            parameters=(button,op)
            self.button_list[button] = self.create_button(parameters,operation=True)
		
        for button, y, x in self.other_btns :
            if button == "AC" :
                parameters = (button,"red")
                self.button_list[button] = self.create_button(parameters,custom=button)
            elif button == "=" :
                self.button_list[button] = tk.Button(self, text=button, command=self.calculate,
					                        font=self.FONT_LARGE, foreground="red")
            elif button == "x!" :
                self.button_list[button] = tk.Button(self, text="x!", command= lambda v="!": self.factorial(v),
					                        font=self.FONT_LARGE)
            elif button == "<-" :
                self.button_list[button] = tk.Button(self, text="<-", command= self.undo,
					                        font=self.FONT_LARGE)

    def create_button(self,parameters,number=False,operation=False, custom=None):
        if (number):
            button =parameters[0]
            return tk.Button(self, text=button, command=lambda btn=button: self.get_variables(int(btn)), font=self.FONT_LARGE)
        elif (operation):
            button, op = parameters
            return tk.Button(self, text=button, command=lambda v=op : self.get_operation(v), font=self.FONT_LARGE)
        elif (custom):
            if custom == "AC":
               buttom, color = parameters
               return tk.Button(self, text=button, command=self.clear_all,font=self.FONT_LARGE, foreground=color)
            elif custom == "=":
                pass
            elif custom == "x!":
                pass
            elif custom == "<-":
                pass
    def get_variables(self, num):
        """Gets the user input for operands and puts it inside the entry widget.
        If a new operation is being carried out, then the display is cleared.
        """
        if self.NEW_OPERATION:
            self.clear_all(new_operation=False)
        self.display.insert(self.i, num)
        self.i += 1

    def get_operation(self, operator):
        """Gets the operand the user wants to apply on the functions."""
        length = len(operator)
        self.display.insert(self.i, operator)
        self.i += length

    def clear_all(self, new_operation=True):
        """clears all the content in the Entry widget."""
        self.display.delete(0, tk.END)
        self.NEW_OPERATION = new_operation

    def undo(self):
        """removes the last entered operator/variable from entry widget."""
        whole_string = self.display.get()
        if len(whole_string):        ## repeats until
	        ## now just decrement the string by one index
            new_string = whole_string[:-1]
            self.clear_all(new_operation=False)
            self.display.insert(0, new_string)
        else:
            self.clear_all() 
            self.display.insert(0, "Error, press AC")

    def calculate(self):
        """Evaluates the expression.
        ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
        """
        whole_string = self.display.get()
        try :
            formulae = ast.parser.expr(whole_string).compile()
            result = eval(formulae)
            self.clear_all()
            self.display.insert(0, result)
        except Exception:
            self.clear_all()
            self.display.insert(0, "Error!")

    def factorial(self, operator):
        """Calculates the factorial of the number entered."""
        number = int(self.display.get())
        fact = 1
        try:
            while number > 0:
                fact = fact*number
                number -= 1
            self.clear_all()
            self.display.insert(0, fact)
        except Exception:
            self.clear_all()
            self.display.insert(0, "Error")