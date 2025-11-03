from models.button import Botao
from utils.operations import *
from back.calculatorModel import *

class FabricaBotoes:

    FONT_LARGE = ("Calibri", 12)  	
    FONT_MED = ("Calibri", 10)
      
    def __init__(self, master, model):
        self.token2symboll = {
            "AC": "AC",
            "IGUAL":"=",
            "SOMA":"+",
            "SUB":"-",
            "MULT":"*",
            "DIV":"/",
            "pi":"pi",
            "REST":"%",
            "PAR_ESQ": "(",
            "PAR_DIR":")",
            "EXP":"exp",
            "APAG": "<-",
            "FAT":"x!",
            "POT_2":"^2"
        }
    
        self.master = master
        self.model = model

    def create(self, tipo:str):
        color = "black"
        new_button = None

        if tipo == "AC":
            new_button = Botao(self.token2symboll[tipo], self.FONT_LARGE, self.model.clear_all, "red", master=self.master)
        elif tipo == "IGUAL":
            new_button = Botao(self.token2symboll[tipo], self.FONT_LARGE, self.model.calculate, "red", master=self.master)
        elif tipo == "APAG":
            new_button = Botao(self.token2symboll[tipo], self.FONT_LARGE, self.model.undo, "red", master=self.master)
        elif tipo == "FAT":
            new_button = Botao(self.token2symboll[tipo], self.FONT_LARGE, lambda v="!": self.model.factorial(v), color, master=self.master)
        else :
            if tipo.isdigit():
                new_button = Botao(tipo, self.FONT_LARGE, lambda btn=tipo: self.model.get_variables(int(btn)), color, master=self.master)
            else :
                if tipo == "pi":
                    new_button = Botao(tipo, self.FONT_LARGE, lambda btn=tipo: self.model.get_operation("*3.14"), color, master=self.master)
                elif tipo == "POT_2":
                    new_button = Botao(self.token2symboll[tipo], self.FONT_LARGE, lambda btn=tipo: self.model.get_operation("**2"), color, master=self.master)
                else :
                    new_button = Botao(tipo, self.FONT_LARGE, lambda btn=tipo: self.model.get_operation(btn), color, master=self.master)
        return new_button