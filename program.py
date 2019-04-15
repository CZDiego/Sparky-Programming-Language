from varTable import Var
from varTable import VarTable
from functionDirectory import FunctionDirectory
from objects import ClassTable
from objects import Class
from objects import Object
from memory import Memory
from copy import deepcopy
from sparky_type import SparkyType

class Program:
    def __init__(self):
        self.BASE                   = 0  # Starting location for Quadruples //list starts with empty so its -1
        self.Quads                  = []
        self.globalMemory           = Memory("program")
        self.funMemory              = Memory("function")
        self.ConsMemory             = Memory("Constant")
        self.varDir                 = VarTable()
        self.funDir                 = FunctionDirectory()
        self.ClassDir               = ClassTable()
        self.pOpList                = []  # Operator pending list
        self.Polish                 = []  # Polish vector list
        self.current_quad           = ()
        self.current_class          = Class()
        self.current_object         = Object()
        self.current_var            = Var()
        self.current_type           = SparkyType()
        self.current_class_name     = ""
        self.current_var_name       = ""
        self.current_function_name  = ""
        self.current_stage          = True   # Working inside the global program
        self.class_stage            = False  # Working either in a class or a function

# IF current_stage == True then Program
# ELSE IF class_stage == True then Class
# ELSE function
    def add_quad(self):
        self.Quads.append(deepcopy(self.current_quad))
        self.current_quad = ()

    def add_pop(self):
        self.pOpList.append(self.BASE)
        self.BASE += 1

    def new_type(self):
        self.current_type = SparkyType()

    def new_object(self):
        self.current_object = Object()

    def new_class(self):
        self.current_typ = Object()

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
