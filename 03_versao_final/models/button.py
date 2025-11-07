import tkinter as tk
from tkinter import ttk
from typing import Tuple, Callable, Optional

class Botao(tk.Button):
	def __init__(self, simbolo:str, fonte:Tuple[str,int], callback:Callable, cor:str, master:Optional[tk.Widget]=None):
		super().__init__(master, text=simbolo, command=callback, font=fonte, foreground=cor)