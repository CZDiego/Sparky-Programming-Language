# ------------------------------------------------------------
# varTable.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------

class Var:
	def __init__(self, type, scope, private, value, address):
	    self.type    = type
	    self.scope   = scope
	    self.private = private
	    self.value   = value
	    self.address = address


class VarTable:
	def __init__(self):
		self.table = dict()

	def insert(self, name, variable):
		self.table[name] = variable

	def search(self, name):
		if name in self.table:
			return True
		else:
			return False

	def get(self, name):
		return self.table[name]