from varTable import Var
from varTable import VarTable
from functionDirectory import FunctionDirectory
from functionDirectory import Function
from objects import ClassTable
from objects import Class
from objects import Object
from semanticCube import SemanticCube
from memory import MemoryMap
from copy import deepcopy
from sparky_type import SparkyType

class Program:
    def __init__(self):
        self.BASE                   = 0  # Starting location for Quadruples //list starts with empty so its -1
        self.Quads                  = []
        self.globalMemory           = MemoryMap("program")
        self.ConsMemory             = MemoryMap("Constant")
        self.varTable               = VarTable()
        self.funDir                 = FunctionDirectory()
        self.ClassDir               = ClassTable()
        self.semanticCube           = SemanticCube()
        self.pJumps                 = []  #
        self.VP                     = []  # Polish vector
        self.pOper                  = []
        self.pType                  = []
        self.pArray                 = []
        self.pIDs                   = []
        self.pEras                  = []
        self.pendingQuads           = []
        self.current_quad           = ()
        self.current_param_num      = 0
        self.current_class          = Class()
        self.current_object         = Object()
        self.current_var            = Var()
        self.current_function       = Function()
        self.current_params         = VarTable()
        self.current_type           = SparkyType()
        self.local_class_func       = FunctionDirectory()
        self.local_func             = Function()
        self.local_class            = Class()
        self.local_type             = SparkyType()
        self.current_value          = 0
        self.current_class_name     = ""
        self.current_var_name       = ""
        self.current_function_name  = ""
        self.called_function        = Function()
        self.current_scope          = ""   # Working inside the global program
        self.class_stage            = False  # Working either in a class or a function
        self.current_id_is_func     = False

# IF current_stage == True then Program
# ELSE IF class_stage == True then Class
# ELSE function
    def add_quad(self):
        self.Quads.append(deepcopy(self.current_quad))
        self.current_quad = ()
        self.BASE += 1

    def add_pJump(self):
        self.pJumps.append(self.BASE)

    def new_type(self):
        self.current_type = SparkyType()

    def new_var(self):
        self.current_var = Var()

    def new_object(self):
        self.current_object = Object()

    def new_class(self):
        self.current_class = Class()

    def new_function(self):
        self.current_function = Function()

    def new_params(self):
        self.current_params = VarTable()

    def new_obj(self):
        self.new_attr()
        self.new_id()
        self.current_id_is_object   = False
        self.id_could_be_function   = False
        self.id_found_in_global     = False
        self.called_function        = Function()
        self.local_class_func       = FunctionDirectory()
        self.local_func             = Function()
        self.local_class            = Class()
        self.local_type             = SparkyType()

    def inherit_class(self, name):
        self.current_class = deepcopy(self.ClassDir[name])

    def print_quads(self):
        for idx, quad in enumerate(self.Quads):
            print(idx, quad)
        #for quad in self.Quads:
            #print(quad)

    def get_param_key(self):
        param_key = ""
        for var in self.current_params.directory:
            param_key = param_key + var.s_type.type_key()
        return param_key

    def fill_quad(self, missing):
        quad_num = self.pJumps.pop()
        quad     = self.Quads[quad_num]
        new_quad = quad[:3]+(missing,)
        self.Quads[quad_num] = new_quad
