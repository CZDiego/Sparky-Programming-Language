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
        self.varTable = VarTable()

    # it will be program.Objects[key] = object
    def __set__(self, key, var):
        self.varTable[key] = var

    def __getitem__(self, key):  # it will be program.funDir[funKey][varKey] and not program.funDir.get(key).varTable[key]
        return self.varTable[key]

    # overload ->  key in program.varTable
    def __contains__(self, key):
        return key in self.varTable

    def deepcopy(self):
        return deepcopy(self)


class Class:
    def __init__(self):
        self.funDir = FunctionDirectory()
        self.varTable = VarTable()

    def deepcopy(self):
        return deepcopy(self)


class ClassTable:
    def __init__(self):
        self.directory  = dict()

    # it will be program.varTable.objects[key] = object
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