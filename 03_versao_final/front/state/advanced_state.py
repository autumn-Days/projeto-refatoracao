from front.state.state_interface import CalculatorState
import front.calculatorView as view

class AdvancedState(CalculatorState):
    view_class = view.CalculatorAdvanced

    def switch(self):
        from front.state.basic_state import BasicState # tenho que por isso aqui para evitar imports circulares
        self.controller.state = BasicState(self.controller, self.model)