# ------------------------------------------------------------
# objects.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
from varTable import VarTable
from functionDirectory import FunctionDirectory
from copy import deepcopy


class Object:
    def __init__(self):
        self.private = "Public"
        self.scope   = "Global"
        self.varTable = VarTable()
        self.funDir = FunctionDirectory()

    def deepcopy(self):
        return deepcopy(self)

# program.Objects[Objectkey]
class ObjectTable:
    def __init__(self):
        self.directory = dict()

    # it will be program.varDir.objects[key] = object
    def __set__(self, key, object):
        self.directory[key] = object

    # it will be object = program.Objects[key]
    def __getitem__(self, key):
        return self.directory[key]

    # overload ->  key in program.objects returns true or false if key exists in dir
    def __contains__(self, key):
        return key in self.directory

    def deepcopy(self):
        return deepcopy(self)
