import tkinter as tk
from tkinter import ttk
from models.factoryButton import FabricaBotoes
import base64
from icons import icon_string

class CalculatorBasic(tk.Frame):
	#A matriz precisa ficar aqui para que o display do 
	#Modo avançado possa ser trocado.
	buttons = [
		["1","2","3","+","pi","APAG"],
		["4","5","6","-","%","FAT"],
		["7","8","9","*","(",")"],
		["AC","0","IGUAL","/","exp","POT_2"],
		["MODE"]
	]

	def __init__(self, master, model):
		super().__init__(master)
		self.model = model
		self.controller = None
		self.button_list = {}
		self.MAX_ROW = 4
		self.MAX_COLUMN = 5
		self.i = 0
		self.NEW_OPERATION = False
		self.create_widgets()

	def set_controller(self, ctrlr):
		self.controller = ctrlr

	def config_window(self):
		self.master.title('Calculator')
		self.master.resizable(width=False, height=False)
		style = ttk.Style(self.master)
		style.theme_use('clam')

	def config_icon(self):
		icon_data = base64.b64decode(icon_string)
		self.icon = tk.PhotoImage(data=icon_data)
		self.master.tk.call('wm', 'iconphoto', self.master._w, self.icon)

	def create_widgets(self):
		self.display = tk.Entry(self, font=("Calibri", 13))
		self.display.grid(row=1, columnspan=6, sticky=tk.W + tk.E)

		factory = FabricaBotoes(self, self.model)
		for i, row in enumerate(self.buttons):
			for j, button in enumerate(row):
				self.button_list[button] = factory.create(button)
				self.button_list[button].grid(row=i+2, column=j)

class CalculatorAdvanced(CalculatorBasic):
	def __init__(self, master, model):
		self.buttons = [
			["1","2","3","+","SQRT","pi","APAG"],
			["4","5","6","-","SEN","%","FAT"],
			["7","8","9","*","COS","(",")"],
			["AC","0","IGUAL","/","TAN","exp","POT_2"],
			["MODE"]
		]
		super().__init__(master, model)
