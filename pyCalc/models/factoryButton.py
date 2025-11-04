from models.button import Botao
from back.calculatorModel import *

class FabricaBotoes:

    FONT_LARGE = ("Calibri", 12)  	
    #FONT_MED = ("Calibri", 10)
      
    def __init__(self, master, model):
        self.operators:Set[str] = {"+","-","*","/","%","√","exp","sen","cos","tan", "(", ")"}
        self.token2parameters = {
            "AC": ("AC","self.model.clear_all","red"),
            "IGUAL":("=","self.model.calculate","red"),
            "APAG":("<-","self.model.undo","red"),
            "FAT":("x!","lambda v='!': self.model.factorial(v)", "black"),
            "pi":("pi","lambda btn='{var_name}': self.model.get_operation('3.14')","black"),
            "POT_2":("^2","lambda btn='{var_name}': self.model.get_operation('**2')","black"),
            "MODE":"MODE"
        }
        self.master = master
        self.model = model

    def create(self, button:str):
        if button == "MODE":
            return tk.Button(self.master, text="Mode")
        if button.isdigit():
            return self.__criarBotaoDigito(button)
        elif button in self.operators:
            return self.__criarBotaoOperador(button)
        else:
            label,callback,color = self.token2parameters[button]
            return self.__criarBotaoEspecial(label,callback,color)

    def __criarBotaoOperador(self, button:str):
        return Botao(button, self.FONT_LARGE, lambda btn=button: self.model.get_operation(btn), "black", master=self.master)

    def __criarBotaoDigito(self, button:str):
        return Botao(button, self.FONT_LARGE, lambda btn=button: self.model.get_variables(int(btn)), "black", master=self.master)
    
    def __criarBotaoEspecial(self, label:str, callback:str, cor:str):
        if '{var_name}' in callback:
            callback = eval(callback.format(var_name=label), {'self':self})#estava usando exec antes, mas ele não retorna nada
        else:
            callback = eval(callback, {'self':self})
        return Botao(label, self.FONT_LARGE, callback,cor, master=self.master)