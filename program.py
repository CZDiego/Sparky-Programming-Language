from varTable import VarTable
from functionDirectory import FunctionDirectory
from memory import Memory


class Program:
    def __init__(self):
        self.BASE = 0
        self.memory = Memory()
        self.varDir = VarTable()
        self.funDir = FunctionDirectory()
        self.current_class_name = ""
        self.current_var_name = ""
        self.current_function_name = ""
