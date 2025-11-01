#! /usr/bin/env python
import tkinter as tk
from tkinter import ttk
from models.factoryButton import FabricaBotoes

import ast
import base64
from icons import icon_string
from models.button import Botao
#from config.fonts import FONT_LARGE, FONT_MED

class CalculatorView(tk.Tk):

	FONT_LARGE = ("Calibri", 12)  	
	FONT_MED = ("Calibri", 10)
	
	number_btns = [    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
                                ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
                                ('7', 4, 0), ('8', 4, 1), ('9', 4, 2),
                                ('0', 5, 1) ]

	operation_btns = [ ('+', 2, 3), ('-', 3, 3), ('*', 4, 3),
                                ('/', 5, 3), ('pi', 2, 4), ('%', 3, 4),
                                ('(', 4, 4), ('exp', 5, 4), (')', 4, 5),
                                ('POT_2', 5, 5)]

	other_btns = [ ('AC', 5, 0), ("IGUAL", 5, 2), 
                            ("APAG", 2, 5), ("FAT", 3, 5)]

	button_list = {}
	
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

		for (button, y, x) in self.number_btns + self.operation_btns + self.other_btns:
			self.button_list[button] = factory.create(button)
			#self.button_list[button].posicionar((y,x))

	def display_buttons(self):
		for (button, y, x) in self.number_btns + self.operation_btns + self.other_btns:
				self.button_list[button].grid(row=y, column=x)

	def run(self):
		self.mainloop()
