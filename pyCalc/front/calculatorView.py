#! /usr/bin/env python
import tkinter as tk
from tkinter import ttk
from models.factoryButton import FabricaBotoes

import ast
import base64
from icons import icon_string
from models.button import Botao

class CalculatorBasic(tk.Tk):
	#as linhas começam do dois
	buttons = [
		["1","2","3","+","pi","APAG"],
		["4","5","6","-","%","FAT"],
		["7","8","9","*","(",")"],
		["AC","0","IGUAL","/","exp","POT_2"],
		["MODE"]
	]

	button_list = {}
	
	MAX_ROW = 4 
	MAX_COLUMN = 5
	i = 0
	NEW_OPERATION = False

	def __init__(self, model):
		try:
			super(CalculatorBasic, self).__init__()
		except TypeError:
			
			tk.Tk.__init__(self)

		self.model = model
		self.controller = None

	def set_controller(self, ctrlr):
		self.controller = ctrlr

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

	def create_buttons(self):
		factory = FabricaBotoes(self, self.model)

		for i in range(len(self.buttons)):
			for j in range(len(self.buttons[i])):
				button = self.buttons[i][j]
				self.button_list[button] = factory.create(button)
				self.button_list[button].grid(row=i+2,column=j)

	def run(self):
		self.mainloop()

class CalculatorAdvanced(CalculatorBasic):
	def __init__(self, model):
		super().__init__(model)
		self.buttons = 	buttons = [
		["1","2","3","+","SQRT","pi","APAG"],
		["4","5","6","-","SEN","%","FAT"],
		["7","8","9","*","COS","(",")"],
		["AC","0","IGUAL","/","TAN","exp","POT_2"],
		["MODE"]
	]
	