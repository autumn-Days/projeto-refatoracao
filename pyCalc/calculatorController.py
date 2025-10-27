from calculatorView import CalculatorView

class CalculatorController:
    def __init__(self, model):
        self.view = CalculatorView(model)    

    def config_view(self):
        self.view.set_controller(self)
        self.view.config_window()
        self.view.config_icon()

        self.view.create_buttons()
        
        self.view.display_buttons()

    # Essa função serve para verificar se o view consegue acessar o controller
    # Adiante, isso servirá para conectar o calculatorModel (e o arquivo de histórico)
    # ao view. Neste momento, o controller printa um "hello" sempre que o igual é
    # pressionado na interface  
    def func_test(self):
        print("hello")
    
    def run_app(self):
        self.config_view()
        self.view.run()
