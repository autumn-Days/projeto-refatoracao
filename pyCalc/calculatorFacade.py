import front.calculatorView as front

class CalculatorController:
    def __init__(self, model):
        self.view = front.CalculatorView(model)
        model.master = self.view

    def config_view(self):
        self.view.set_controller(self)
        self.view.config_window()
        self.view.config_icon()

        self.view.create_buttons()
        
        self.view.display_buttons()
    
    def run_app(self):
        self.config_view()
        self.view.run()
