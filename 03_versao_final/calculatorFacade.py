import front.calculatorView as front
import back.calculatorModel as calcModel
from front.state import BasicState, AdvancedState
import tkinter as tk

class CalculatorController:
    def __init__(self, model):
        self.model = model
        self.root = tk.Tk()
        self.state = BasicState(self, model)
        self.current_frame = None
        self.model.master = None

    def __destroyWidgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def __buildView(self):
        view_cls = getattr(self.state, "view_class", None)
        if view_cls is None:
            raise RuntimeError("O State não tem nenhum objeto 'view' associado a ele")

        frame = view_cls(self.root, self.model)
        self.model.master = frame
        frame.set_controller(self)
        frame.config_window()
        frame.config_icon()
        frame.pack()
        self.current_frame = frame

    def config_view(self):
        self.__buildView()

    def switchState(self):
        self.__destroyWidgets()
        self.state.switch()
        self.__buildView()

    def run_app(self):
        self.config_view()
        self.root.mainloop()
