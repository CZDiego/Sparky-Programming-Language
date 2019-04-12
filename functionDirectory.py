# ------------------------------------------------------------
# functionDirectory.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
from varTable import VarTable

class Function:
	def __init__(self, private):
		self.private = private
		self.varTable = VarTable()

class FunctionDirectory:
	def __init__(self):
		self.directory = dict()

	def insert(self, name, function):
		self.directory[name] = function

	def search(self, name):
		if name in self.directory:
			return True
		else:
			return False

	def get(self, name):
		return self.directory[name]