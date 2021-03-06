# ------------------------------------------------------------
# varTable.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
from copy import deepcopy
from memory import MemoryMap
from sparky_type import SparkyType


class Var:

	def __init__(self):
		self.s_type    = SparkyType()
		self.private   = "public"
		self.address   = 0
		self.constant  = False
		self.is_param  = False

	def deepcopy(self):
		return deepcopy(self)


class VarTable:
	def __init__(self):
		self.directory 	= dict()
		self.objects	= dict()

	# it will be program.Objects[key] = object
	def __set__(self, key, var):
		self.directory[key] = var

	def __getitem__(self, key):  # it will be program.funDir[funKey][varKey] and not program.funDir.get(key).varTable[key]
		return self.directory[key]

	# overload ->  key in program.varTable
	def __contains__(self, key):
		return key in self.directory

	def contains(self, key):
		return key in self.directory

	def update(self, dir):
		self.directory.update(dir)

	def set(self, key, var):
		self.directory[key] = var

	def deepcopy(self):
		return deepcopy(self)
