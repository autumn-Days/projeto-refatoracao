import front.calculatorView as view

class CalculatorState:

    view_class = None

    def __init__(self, controller, model):
        self.controller = controller
        self.model = model

    def switch(self):
        return