#! /usr/bin/env python
import back.calculatorModel as back
from calculatorFacade import CalculatorController

model = back.CalculatorModel()
app = CalculatorController(model)
app.run_app()