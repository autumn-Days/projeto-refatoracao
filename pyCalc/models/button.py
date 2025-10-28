import tkinter as tk
from tkinter import ttk
from typing import Tuple, Callable, Optional

#tk.Button(self, text=button, command=lambda btn=button: self.get_variables(int(btn)), font=self.FONT_LARGE)
#Botao(button,self.FONT_LARGE,callback=lambda btn=button: self.get_variables(int(btn)),"black", master=self)

"""
tk.Button(self, text=button, command=self.clear_all, font=self.FONT_LARGE, foreground="red")

tk.Button(self, text=button, command=self.clear_all, font=self.FONT_LARGE, foreground="red")
Botao(button, self.FONT_LARGE, self.clear_all, "red", master=self)
"""

class Botao(tk.Button):
    def __init__(self, simbolo:str, fonte:Tuple[str,int], callback:Callable, cor:str, master:Optional[tk.Widget]=None):
        super().__init__(master, text=simbolo, command=callback, font=fonte, foreground=cor)

    def posicionar(self,pos:Tuple[int,int]):
        self.place(x=pos[0], y=pos[1])