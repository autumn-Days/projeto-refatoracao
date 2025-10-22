from calculatorView import CalculatorView

class CalculatorController:
    def __init__(self, model):
        self.view = CalculatorView(model)    

    def config_view(self):
        self.view.config_window()
        self.view.config_icon()
        self.view._init_ui()
    
    def run_app(self):
        self.config_view()
        self.view.run()
