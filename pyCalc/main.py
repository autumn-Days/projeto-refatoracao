#! /usr/bin/env python
from calculatorModel import CalculatorModel
from calculatorController import CalculatorController

model = CalculatorModel()
app = CalculatorController(model)
app.run_app()