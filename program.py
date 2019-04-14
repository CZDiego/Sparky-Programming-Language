from varTable import VarTable
from functionDirectory import FunctionDirectory
from memory import Memory
from quadruples import QuadList


class Program:
    def __init__(self):
        self.BASE                   = -1  # Starting location for Quadruples //list starts with empty so its -1
        self.Quads                  = []
        self.memory                 = Memory("program")
        self.varDir                 = VarTable()
        self.funDir                 = FunctionDirectory()
        self.current_class_name     = ""
        self.current_var_name       = ""
        self.current_function_name  = ""
        self.current_stage          = True   # Working inside the global program
        self.class_stage            = False  # Working either in a class or a function
        

# IF current_stage == True then Program
# ELSE IF class_stage == True then Class
# ELSE function

# Working with touples (quads)
# Almost like slice deletion
#>>> tup = tup[0:2]
#>>> tup
#('one', 'two')
#>>> tup2 += tup
#>>> tup2
# almost like index assignment
#>>> tup2 = tup2[0:1] + (1,) + tup2[2:]
#>>> tup2
#(0, 1, 'two')
