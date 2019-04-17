# ------------------------------------------------------------
# functionDirectory.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
from varTable import VarTable
from copy import deepcopy


class Function:
	def __init__(self, private):
		self.private = private
		self.varTable = VarTable()

	def __getitem__(self, key):  # it will be program.funDir[funKey][varKey] and not program.funDir.get(key).varTable[key]
		return self.varTable[key]

	def add_params(self,params):
		self.varTable.update(params)

	def deepcopy(self):
		return deepcopy(self)

class FunctionDirectory:
	def __init__(self):
		self.directory = dict()

	# it will be program.funDir[key] = function
	def __set__(self, key, function):
		self.directory[key] = function

	def __getitem__(self, key):  # it will be program.funDir[key] and not program.funDir.get(key)
		return self.directory[key]

	# overload ->  key in program.funDir returns true or false if key exists in dir
	def __contains__(self, key):
		return key in self.directory

	def deepcopy(self):
		return deepcopy(self)
