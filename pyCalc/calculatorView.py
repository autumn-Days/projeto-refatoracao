#! /usr/bin/env python

try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	# Python 2
	import Tkinter as tk
	import ttk

import ast
import base64
from icons import icon_string

class CalculatorView(tk.Tk):
	FONT_LARGE = ("Calibri", 12)  	
	FONT_MED = ("Calibri", 10)

	
	MAX_ROW = 4 
	MAX_COLUMN = 5
	i = 0
	NEW_OPERATION = False

	def __init__(self, model):
		try:
			super(CalculatorView, self).__init__()
		except TypeError:
			
			tk.Tk.__init__(self)

		self.model = model

	def config_window(self):
		self.title('Calculator')
		self.resizable(width=False, height=False)

		
		style = ttk.Style(self)
		style.theme_use('clam')

	def config_icon(self):
		
		icon_data = base64.b64decode(icon_string)
		self.icon = tk.PhotoImage(data=icon_data)
		self.tk.call('wm', 'iconphoto', self._w, self.icon)

		for row in range(self.MAX_ROW):
			self.columnconfigure(row,pad=3)

		for column in range(self.MAX_COLUMN):
			self.rowconfigure(column,pad=3)

		self.display = tk.Entry(self, font=("Calibri", 13))
		self.display.grid(row=1, columnspan=6, sticky=tk.W + tk.E)

	def _init_ui(self):
		for button, y, x in self.model.number_btns :
			self.model.button_list[button] = tk.Button(self, text=button, command=lambda btn=button: self.get_variables(int(btn)), font=self.FONT_LARGE)
			self.model.button_list[button].grid(row=y, column=x)
        
		for (button, y, x, op) in self.model.operation_btns :
			self.model.button_list[button] = tk.Button(self, text=button, command=lambda v=op : self.get_operation(v), font=self.FONT_LARGE)
			self.model.button_list[button].grid(row=y, column=x)

		for (button, y, x) in self.model.other_btns :
			if button == "AC" :
				self.model.button_list[button] = tk.Button(self, text=button, command=self.clear_all,
					                        font=self.FONT_LARGE, foreground="red")
				self.model.button_list[button].grid(row=y, column=x)
			elif button == "=" :
				self.model.button_list[button] = tk.Button(self, text=button, command=self.calculate,
					                        font=self.FONT_LARGE, foreground="red")
				self.model.button_list[button].grid(row=y, column=x)
			elif button == "x!" :
				self.model.button_list[button] = tk.Button(self, text="x!", command= lambda v="!": self.factorial(v),
					                        font=self.FONT_LARGE)
				self.model.button_list[button].grid(row=y, column=x)
			elif button == "'<-" :
				self.model.button_list[button] = tk.Button(self, text="<-", command= self.undo,
					                        font=self.FONT_LARGE)
				self.model.button_list[button].grid(row=y, column=x)


	def factorial(self, operator):
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
		self.display.delete(0, tk.END)
		self.NEW_OPERATION = new_operation

	def get_variables(self, num):
		if self.NEW_OPERATION:
			self.clear_all(new_operation=False)
		self.display.insert(self.i, num)
		self.i += 1

	def get_operation(self, operator):
		#Obtem o operando que o usuario quer aplicar a uma funcao
		length = len(operator)
		self.display.insert(self.i, operator)
		self.i += length

	def undo(self):
		#Remove o ultim operador ou digito inserido
		whole_string = self.display.get()
		if len(whole_string):        
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
			self.clear_all()
			self.display.insert(0, result)
		except Exception:
			self.clear_all()
			self.display.insert(0, "Error!")

	def run(self):
		self.mainloop()
