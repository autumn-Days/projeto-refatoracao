from models.button import Botao
from back.calculatorModel import *
from models.builder import BuilderCalc

class FabricaBotoes:          
    def __init__(self, master, model):
        self.operators:Set[str] = {"+","-","*","/","%","exp", "(", ")"}
        self.angles2methods ={
            "SEN":"sen",
            "COS":"cos",
            "TAN":"tan"
        }
        self.token2parameters = {
            "AC": ("AC","self.model.clear_all","red"),
            "IGUAL":("=","self.model.calculate","red"),
            "APAG":("<-","self.model.undo","red"),
            "FAT":("x!","lambda v='!': self.model.factorial(v)", "black"),
            "pi":("pi","lambda btn='{var_name}': self.model.get_operation('3.14')","black"),
            "POT_2":("^2","lambda btn='{var_name}': self.model.get_operation('**2')","black"),
            "ANG":("{angle}", "self.model.{angle_method}()","black"),
            "MODE":("MODE", "switch","red"),
            "SQRT":("√","sqrt","black"),
        }
        self.master = master
        self.model = model
        self.builder = BuilderCalc(master=self.master, model=self.model)

    def create(self, button:str):
        if button.isdigit():
            return self.builder.buildDigit(button)
        elif button in self.operators:
            return self.builder.buildOperator(button)
        elif button == "MODE" or button == "SQRT":
            label,callback,cor = self.token2parameters[button]
            return self.builder.buildCustom(button, callback, cor)
        else:
            if self.__isAngle(button):
                callbackName = self.angles2methods[button]
                return self.builder.buildAngle(button,callbackName,"black")
            else:
                label,callback,color = self.token2parameters[button]
                return self.builder.buildSpecial(label,callback,color)
    def __isAngle(self,angle):
        return angle in set(["SEN","COS","TAN"])