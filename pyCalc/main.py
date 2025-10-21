#! /usr/bin/env python
from calculatorModel import CalculatorModel
from gui import TkGUI

model = CalculatorModel()
app = TkGUI(model)
app.run()