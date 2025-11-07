from front.state.state_interface import CalculatorState
import front.calculatorView as view

class BasicState(CalculatorState):
    view_class = view.CalculatorBasic

    def switch(self):
        from front.state.advanced_state import AdvancedState  # Isso evita imports circulares
        self.controller.state = AdvancedState(self.controller, self.model)