from models.button import Botao
from utils.operations import *

class FabricaBotoes:
    def __init__(self):
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
            "FAT":"!",
            "POT_2":"^2"
        }
    def create(self, tipo:str):
        color = "black"
        if tipo == "NUM":
            
        elif tipo == 
