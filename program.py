from varTable import Var
from varTable import VarTable
from functionDirectory import FunctionDirectory
from functionDirectory import Function
from objects import ClassTable
from objects import Class
from objects import Object
from semanticCube import SemanticCube
from memory import Memory
from copy import deepcopy
from sparky_type import SparkyType

class Program:
    def __init__(self):
        self.BASE                   = 0  # Starting location for Quadruples //list starts with empty so its -1
        self.Quads                  = []
        self.globalMemory           = Memory("program")
        #self.funMemory              = Memory("function")
        self.ConsMemory             = Memory("Constant")
        self.varTable               = VarTable()
        self.funDir                 = FunctionDirectory()
        self.ClassDir               = ClassTable()
        self.semanticCube           = SemanticCube()
        self.pJumps                 = []  #
        self.VP                     = []  # Polish vector
        self.pOper                  = []
        self.pType                  = []
        self.current_quad           = ()
        self.current_class          = Class()
        self.current_object         = Object()
        self.current_var            = Var()
        self.current_function       = Function()
        self.current_params         = VarTable()
        self.current_type           = SparkyType()
        self.current_value          = 0
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

    def add_pJump(self):
        self.pJumps.append(self.BASE)
        self.BASE += 1

    def new_type(self):
        self.current_type = SparkyType()

    def new_object(self):
        self.current_object = Object()

    def new_class(self):
        self.current_class = Class()

    def new_function(self):
        self.current_function = Function()

    def new_params(self):
        self.current_params = VarTable()

    def inherit_class(self, name):
        self.current_class = deepcopy(self.ClassDir[name])

    def print_quads(self):
        for quad in self.Quads:
            print(quad)

    def print_jumps(self):
        for jump in self.pJumps:
            print(jump)

    def get_param_key(self):
        param_key = ""
        for var in self.current_params.directory:
            param_key = param_key + var.s_type.type_key()
        return param_key
