#! /usr/bin/env python

try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# Python 2
	import Tkinter as tk
	import ttk

#import parser
import ast
import base64
from icons import icon_string
import math


class TkGUI(tk.Tk):
	FONT_LARGE = ("Calibri", 12)  	# selects the font of the text inside buttons
	FONT_MED = ("Calibri", 10)

	# Max rows and columns in the GUI
	MAX_ROW = 4 
	MAX_COLUMN = 5
	i = 0
	NEW_OPERATION = False

	def __init__(self):
		try:
			super(TkGUI, self).__init__()
		except TypeError:
			# Python 2
			tk.Tk.__init__(self)

		self.title('Calculator')
		self.resizable(width=False, height=False)

		# Configure default theme
		style = ttk.Style(self)
		style.theme_use('clam')

		self.show_scientific_buttons = False

		# Configure icon
		icon_data = base64.b64decode(icon_string)
		self.icon = tk.PhotoImage(data=icon_data)
		self.tk.call('wm', 'iconphoto', self._w, self.icon)

		for row in range(self.MAX_ROW):
			self.columnconfigure(row,pad=3)

		for column in range(self.MAX_COLUMN):
			self.rowconfigure(column,pad=3)

		self.display = tk.Entry(self, font=("Calibri", 13))
		self.display.grid(row=1, columnspan=7, sticky=tk.W + tk.E)

		self._init_ui()

	def _init_ui(self):
		self.one = tk.Button(
			self, text="1", command=lambda: self.get_variables(1), font=self.FONT_LARGE)
		self.one.grid(row=2, column=0)
		self.two = tk.Button(
			self, text="2", command=lambda: self.get_variables(2), font=self.FONT_LARGE)
		self.two.grid(row=2, column=1)
		self.three = tk.Button(
			self, text="3", command=lambda: self.get_variables(3), font=self.FONT_LARGE)
		self.three.grid(row=2, column=2)

		self.four = tk.Button(
			self, text="4", command=lambda: self.get_variables(4), font=self.FONT_LARGE)
		self.four.grid(row=3, column=0)
		self.five = tk.Button(
			self, text="5", command=lambda: self.get_variables(5), font=self.FONT_LARGE)
		self.five.grid(row=3, column=1)
		self.six = tk.Button(
			self, text="6", command=lambda: self.get_variables(6), font=self.FONT_LARGE)
		self.six.grid(row=3, column=2)

		self.seven = tk.Button(
			self, text="7", command=lambda: self.get_variables(7), font=self.FONT_LARGE)
		self.seven.grid(row=4, column=0)
		self.eight = tk.Button(
			self, text="8", command=lambda: self.get_variables(8), font=self.FONT_LARGE)
		self.eight.grid(row=4, column=1)
		self.nine = tk.Button(
			self, text="9", command=lambda: self.get_variables(9), font=self.FONT_LARGE)
		self.nine.grid(row=4, column=2)

		self.cls = tk.Button(self, text="AC", command=self.clear_all,
						font=self.FONT_LARGE, foreground="red")
		self.cls.grid(row=5, column=0)
		self.zero = tk.Button(
			self, text="0", command=lambda: self.get_variables(0), font=self.FONT_LARGE)
		self.zero.grid(row=5, column=1)
		self.result = tk.Button(self, text="=", command=self.calculate,
						   font=self.FONT_LARGE, foreground="red")
		self.result.grid(row=5, column=2)

		self.plus = tk.Button(
			self, text="+", command=lambda: self.get_operation("+"), font=self.FONT_LARGE)
		self.plus.grid(row=2, column=3)
		self.minus = tk.Button(
			self, text="-", command=lambda: self.get_operation("-"), font=self.FONT_LARGE)
		self.minus.grid(row=3, column=3)
		self.multiply = tk.Button(
			self, text="*", command=lambda: self.get_operation("*"), font=self.FONT_LARGE)
		self.multiply.grid(row=4, column=3)
		self.divide = tk.Button(
			self, text="/", command=lambda:  self.get_operation("/"), font=self.FONT_LARGE)
		self.divide.grid(row=5, column=3)

		# adding new operations
		self.pi = tk.Button(self, text="pi", command=lambda: self.get_operation(
			"*3.14"), font=self.FONT_LARGE)
		self.pi.grid(row=2, column=5)
		self.modulo = tk.Button(
			self, text="%", command=lambda:  self.get_operation("%"), font=self.FONT_LARGE)
		self.modulo.grid(row=3, column=5)
		self.left_bracket = tk.Button(
			self, text="(", command=lambda: self.get_operation("("), font=self.FONT_LARGE)
		self.left_bracket.grid(row=4, column=5)
		self.exp = tk.Button(self, text="exp",
						command=lambda: self.get_operation("**"), font=self.FONT_LARGE)
		self.exp.grid(row=5, column=5)

		# To be added :
		# sin, cos, log, ln
		self.undo_button = tk.Button(
			self, text="<-", command=self.undo, font=self.FONT_LARGE, foreground="red")
		self.undo_button.grid(row=2, column=6)
		self.fact = tk.Button(
			self, text="x!", command=lambda: self.factorial("!"), font=self.FONT_LARGE)
		self.fact.grid(row=3, column=6)
		self.right_bracket = tk.Button(
			self, text=")", command=lambda: self.get_operation(")"), font=self.FONT_LARGE)
		self.right_bracket.grid(row=4, column=6)
		self.square = tk.Button(
			self, text="^2", command=lambda: self.get_operation("**2"), font=self.FONT_LARGE)
		self.square.grid(row=5, column=6)

		self.root = tk.Button(
			self, text="SQRT", command= self.sqrt, font=self.FONT_LARGE)
		self.root.grid(row=2, column=4)
		self.sine = tk.Button(
			self, text="SIN", command= self.sen, font=self.FONT_LARGE)
		self.sine.grid(row=3, column=4)
		self.cosine = tk.Button(
			self, text="COS", command=self.cos, font=self.FONT_LARGE)
		self.cosine.grid(row=4, column=4)
		self.tangent = tk.Button(
			self, text="TAN", command=self.tan, font=self.FONT_LARGE)
		self.tangent.grid(row=5, column=4)
		
		self.mode = tk.Button(
			self, text="MODE", command=self.switch_mode, font=self.FONT_LARGE,
			foreground="red")
		self.mode.grid(row=6, column=0)

	def switch_mode(self):
		""""Switches the mode of the calculator."""
		if not self.show_scientific_buttons:
			self.root.grid_forget()
			self.sine.grid_forget()
			self.cosine.grid_forget()
			self.tangent.grid_forget()
		else :
			self.root.grid(row=2, column=4)
			self.sine.grid(row=3, column=4)
			self.cosine.grid(row=4, column=4)
			self.tangent.grid(row=5, column=4)


		self.show_scientific_buttons = not self.show_scientific_buttons
		
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

	def clear_all(self, new_operation=True):
		"""clears all the content in the Entry widget."""
		self.display.delete(0, tk.END)
		self.NEW_OPERATION = new_operation

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
		try:
			result = eval(compile(ast.parse(whole_string, mode="eval"), "<string>", "eval"))
			#formulae = ast.parse(whole_string, mode="eval")
			#result = eval(formulae)
			self.clear_all()
			self.display.insert(0, result)
		except Exception:
			self.clear_all()
			self.display.insert(0, "Error!")

	def sqrt(self):
		num = int(self.display.get())
		num = math.sqrt(num)
		self.clear_all()
		self.display.insert(0, num)
    
	def sen(self):
		num = int(self.display.get())
		num = math.sin(num)
		self.clear_all()
		self.display.insert(0, num)
            
	def cos(self):
		num = int(self.display.get())
		num = math.cos(num)
		self.clear_all()
		self.display.insert(0, num)

	def tan(self, tan:float):
		num = int(self.display.get())
		num = math.tan(num)
		self.clear_all()
		self.display.insert(0, num)

	def run(self):
		"""Initiate event loop."""
		self.mainloop()
