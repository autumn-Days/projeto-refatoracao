from tkinter import *
import math
import os

class calculate():

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("400x450")  # Adjusted height for variable buttons

        self.root.maxsize(400, 450)
        self.root.minsize(400, 450)
        self.root.config(bg="grey")

        self.resultwindow = Entry(self.root, borderwidth=5, relief=SUNKEN)
        self.resultwindow.grid(row=0, column=0, columnspan=6, pady=5)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set()

        # Track if the last button pressed was "="
        self.last_pressed_equal = False

        # Basic calculator buttons
        self.button1 = Button(self.root, text="1", width=3, command=lambda:self.ins('1'), relief=RAISED, bg='light green')
        self.button1.grid(row=1, column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(self.root, text="2", width=3, command=lambda:self.ins('2'), relief=RAISED, bg='light green')
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(self.root, text="3", width=3, command=lambda:self.ins('3'), relief=RAISED, bg='light green')
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(self.root, text="4", width=3, command=lambda:self.ins('4'), relief=RAISED, bg='light green')
        self.button4.grid(row=2, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(self.root, text="5", width=3, command=lambda:self.ins('5'), relief=RAISED, bg='light green')
        self.button5.grid(row=2, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(self.root, text="6", width=3, command=lambda:self.ins('6'), relief=RAISED, bg='light green')
        self.button6.grid(row=2, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(self.root, text="7", width=3, command=lambda:self.ins('7'), relief=RAISED, bg='light green')
        self.button7.grid(row=3, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(self.root, text="8", width=3, command=lambda:self.ins('8'), relief=RAISED, bg='light green')
        self.button8.grid(row=3, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(self.root, text="9", width=3, command=lambda:self.ins('9'), relief=RAISED, bg='light green')
        self.button9.grid(row=3, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="0", width=3, command=lambda:self.ins('0'), relief=RAISED, bg='light green')
        self.button0.grid(row=4, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button_plus = Button(self.root, text="+", width=3, command=lambda:self.ins('+'), relief=RAISED, bg='light grey')
        self.button_plus.grid(row=1, column=3, padx=3, pady=3)
        self.button_plus.config(font=("Arial", 18))

        self.button_minus = Button(self.root, text="-", width=3, command=lambda:self.ins('-'), relief=RAISED, bg='light grey')
        self.button_minus.grid(row=2, column=3, padx=3, pady=3)
        self.button_minus.config(font=("Arial", 18))

        self.button_multiply = Button(self.root, text="*", width=3, command=lambda:self.ins('*'), relief=RAISED, bg='light grey')
        self.button_multiply.grid(row=3, column=3, padx=3, pady=3)
        self.button_multiply.config(font=("Arial", 18))

        self.button_divide = Button(self.root, text="/", width=3, command=lambda:self.ins('/'), relief=RAISED, bg='light grey')
        self.button_divide.grid(row=4, column=3, padx=3, pady=3)
        self.button_divide.config(font=("Arial", 18))

        self.button_equal = Button(self.root, text="=", width=3, command=self.calculate, relief=RAISED, bg='light grey')
        self.button_equal.grid(row=4, column=2, padx=3, pady=3)
        self.button_equal.config(font=("Arial", 18))

        self.button_clear = Button(self.root, text="C", width=3, command=self.clear, relief=RAISED, bg='light grey')
        self.button_clear.grid(row=4, column=0, padx=3, pady=3)
        self.button_clear.config(font=("Arial", 18))

        # Scientific calculator buttons (initially hidden)
        self.button_sin = Button(self.root, text="sin", width=3, command=lambda:self.scientific('sin'), relief=RAISED, bg='light blue')
        self.button_cos = Button(self.root, text="cos", width=3, command=lambda:self.scientific('cos'), relief=RAISED, bg='light blue')
        self.button_tan = Button(self.root, text="tan", width=3, command=lambda:self.scientific('tan'), relief=RAISED, bg='light blue')
        self.button_rad = Button(self.root, text="rad", width=3, command=lambda:self.scientific('rad'), relief=RAISED, bg='light blue')
        self.button_ln = Button(self.root, text="ln", width=3, command=lambda:self.scientific('ln'), relief=RAISED, bg='light blue')
        self.button_log = Button(self.root, text="log", width=3, command=lambda:self.scientific('log'), relief=RAISED, bg='light blue')
        self.button_inv = Button(self.root, text="1/x", width=3, command=lambda:self.scientific('inv'), relief=RAISED, bg='light blue')
        self.button_sqr = Button(self.root, text="x²", width=3, command=lambda:self.scientific('sqr'), relief=RAISED, bg='light blue')
        self.button_pow = Button(self.root, text="x^y", width=3, command=lambda:self.scientific('pow'), relief=RAISED, bg='light blue')
        self.button_mod = Button(self.root, text="mod", width=3, command=lambda:self.scientific('mod'), relief=RAISED, bg='light blue')
        self.button_sqrt = Button(self.root, text="√", width=3, command=lambda:self.scientific('sqrt'), relief=RAISED, bg='light blue')

        # Variable buttons
        self.button_A = Button(self.root, text="A", width=3, command=lambda:self.var('A'), relief=RAISED, bg='light yellow')
        self.button_A.grid(row=5, column=0, padx=3, pady=3)
        self.button_A.config(font=("Arial", 18))

        self.button_B = Button(self.root, text="B", width=3, command=lambda:self.var('B'), relief=RAISED, bg='light yellow')
        self.button_B.grid(row=5, column=1, padx=3, pady=3)
        self.button_B.config(font=("Arial", 18))

        self.button_C = Button(self.root, text="C", width=3, command=lambda:self.var('C'), relief=RAISED, bg='light yellow')
        self.button_C.grid(row=5, column=2, padx=3, pady=3)
        self.button_C.config(font=("Arial", 18))

        # Mode toggle at the bottom
        self.mode = "basic"  # Default mode
        self.mode_button = Button(self.root, text="Switch to Scientific", width=20, command=self.toggle_mode, relief=RAISED, bg='light blue')
        self.mode_button.grid(row=6, column=0, columnspan=6, padx=3, pady=3)

        self.root.mainloop()

    def toggle_mode(self):
        if self.mode == "basic":
            self.mode = "scientific"
            self.mode_button.config(text="Switch to Basic")
            self.show_scientific_buttons()
        else:
            self.mode = "basic"
            self.mode_button.config(text="Switch to Scientific")
            self.hide_scientific_buttons()

    def show_scientific_buttons(self):
        self.button_sin.grid(row=1, column=4, padx=3, pady=3)
        self.button_cos.grid(row=1, column=5, padx=3, pady=3)
        self.button_tan.grid(row=2, column=4, padx=3, pady=3)
        self.button_rad.grid(row=2, column=5, padx=3, pady=3)
        self.button_ln.grid(row=3, column=4, padx=3, pady=3)
        self.button_log.grid(row=3, column=5, padx=3, pady=3)
        self.button_inv.grid(row=4, column=4, padx=3, pady=3)
        self.button_sqr.grid(row=4, column=5, padx=3, pady=3)
        self.button_pow.grid(row=5, column=3, padx=3, pady=3)
        self.button_mod.grid(row=5, column=4, padx=3, pady=3)
        self.button_sqrt.grid(row=5, column=5, padx=3, pady=3)

    def hide_scientific_buttons(self):
        self.button_sin.grid_forget()
        self.button_cos.grid_forget()
        self.button_tan.grid_forget()
        self.button_rad.grid_forget()
        self.button_ln.grid_forget()
        self.button_log.grid_forget()
        self.button_inv.grid_forget()
        self.button_sqr.grid_forget()
        self.button_pow.grid_forget()
        self.button_mod.grid_forget()
        self.button_sqrt.grid_forget()

    def ins(self, value):
        self.last_pressed_equal = False
        self.resultwindow.insert(END, value)

    def clear(self):
        self.last_pressed_equal = False
        self.resultwindow.delete(0, END)

    def calculate(self):
        try:
            result = eval(self.resultwindow.get())
            self.resultwindow.delete(0, END)
            self.resultwindow.insert(0, result)
            self.last_pressed_equal = True
        except:
            self.last_pressed_equal = False
            self.resultwindow.delete(0, END)
            self.resultwindow.insert(0, "Error")

    def scientific(self, operation):
        self.last_pressed_equal = False
        try:
            value = float(self.resultwindow.get())
            if operation == 'sin':
                result = math.sin(value)
            elif operation == 'cos':
                result = math.cos(value)
            elif operation == 'tan':
                result = math.tan(value)
            elif operation == 'rad':
                result = math.radians(value)
            elif operation == 'ln':
                result = math.log(value)
            elif operation == 'log':
                result = math.log10(value)
            elif operation == 'inv':
                result = 1 / value
            elif operation == 'sqr':
                result = value ** 2
            elif operation == 'pow':
                # For x^y, prompt for y
                self.resultwindow.delete(0, END)
                self.resultwindow.insert(0, f"{value}^")
                return
            elif operation == 'mod':
                # For mod, prompt for second value
                self.resultwindow.delete(0, END)
                self.resultwindow.insert(0, f"{value}%")
                return
            elif operation == 'sqrt':
                result = math.sqrt(value)
            self.resultwindow.delete(0, END)
            self.resultwindow.insert(0, result)
        except:
            self.resultwindow.delete(0, END)
            self.resultwindow.insert(0, "Error")

    def var(self, var_name):
        if self.last_pressed_equal:
            try:
                result = float(self.resultwindow.get())
                self.save_var(var_name, result)
            except:
                self.resultwindow.delete(0, END)
                self.resultwindow.insert(0, "Error")
        else:
            # Retrieve the variable value
            value = self.load_var(var_name)
            self.resultwindow.delete(0, END)
            self.resultwindow.insert(0, value)
        self.last_pressed_equal = False

    def save_var(self, var_name, value):
        with open(f"{var_name}.txt", "w") as file:
            file.write(str(value))

    def load_var(self, var_name):
        try:
            with open(f"{var_name}.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return "0"

# Run the calculator
calculate()
