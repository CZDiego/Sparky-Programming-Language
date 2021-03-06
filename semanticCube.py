# ------------------------------------------------------------
# semanticCube.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------


class SemanticCube:
	def __init__(self):
		self.cube = dict()

		#Int
		self.cube[("&&", "Int", "Int")]     = "Error"
		self.cube[("||", "Int", "Int")]     = "Error"
		self.cube[(">=", "Int", "Int")]     = "Bool"
		self.cube[("<=", "Int", "Int")]     = "Bool"
		self.cube[(">", "Int", "Int")]      = "Bool"
		self.cube[("<", "Int", "Int")]      = "Bool"
		self.cube[("==", "Int", "Int")]     = "Bool"
		self.cube[("!=", "Int", "Int")]     = "Bool"
		self.cube[("+", "Int", "Int")]      = "Int"
		self.cube[("-", "Int", "Int")]      = "Int"
		self.cube[("*", "Int", "Int")]      = "Int"
		self.cube[("/", "Int", "Int")]      = "Int"
		self.cube[("=", "Int", "Int")]      = "Int"

		self.cube[("&&", "Int", "Float")]   = "Error"
		self.cube[("||", "Int", "Float")]   = "Error"
		self.cube[(">=", "Int", "Float")]   = "Bool"
		self.cube[("<=", "Int", "Float")]   = "Bool"
		self.cube[(">", "Int", "Float")]    = "Bool"
		self.cube[("<", "Int", "Float")]    = "Bool"
		self.cube[("==", "Int", "Float")]   = "Bool"
		self.cube[("!=", "Int", "Float")]   = "Bool"
		self.cube[("+", "Int", "Float")]    = "Float"
		self.cube[("-", "Int", "Float")]    = "Float"
		self.cube[("*", "Int", "Float")]    = "Float"
		self.cube[("/", "Int", "Float")]    = "Float"
		self.cube[("=", "Int", "Float")]    = "Int"

		self.cube[("&&", "Int", "Bool")]    = "Error"
		self.cube[("||", "Int", "Bool")]    = "Error"
		self.cube[(">=", "Int", "Bool")]    = "Error"
		self.cube[("<=", "Int", "Bool")]    = "Error"
		self.cube[(">", "Int", "Bool")]     = "Error"
		self.cube[("<", "Int", "Bool")]     = "Error"
		self.cube[("==", "Int", "Bool")]    = "Error"
		self.cube[("!=", "Int", "Bool")]    = "Error"
		self.cube[("+", "Int", "Bool")]     = "Error"
		self.cube[("-", "Int", "Bool")]     = "Error"
		self.cube[("*", "Int", "Bool")]     = "Error"
		self.cube[("/", "Int", "Bool")]     = "Error"
		self.cube[("=", "Int", "Bool")]     = "Error"

		#Float
		self.cube[("&&", "Float", "Int")]   = "Error"
		self.cube[("||", "Float", "Int")]   = "Error"
		self.cube[(">=", "Float", "Int")]   = "Bool"
		self.cube[("<=", "Float", "Int")]   = "Bool"
		self.cube[(">", "Float", "Int")]    = "Bool"
		self.cube[("<", "Float", "Int")]    = "Bool"
		self.cube[("==", "Float", "Int")]   = "Bool"
		self.cube[("!=", "Float", "Int")]   = "Bool"
		self.cube[("+", "Float", "Int")]    = "Float"
		self.cube[("-", "Float", "Int")]    = "Float"
		self.cube[("*", "Float", "Int")]    = "Float"
		self.cube[("/", "Float", "Int")]    = "Float"
		self.cube[("=", "Float", "Int")]    = "Float"

		self.cube[("&&", "Float", "Float")] = "Error"
		self.cube[("||", "Float", "Float")] = "Error"
		self.cube[(">=", "Float", "Float")] = "Bool"
		self.cube[("<=", "Float", "Float")] = "Bool"
		self.cube[(">", "Float", "Float")]  = "Bool"
		self.cube[("<", "Float", "Float")]  = "Bool"
		self.cube[("==", "Float", "Float")] = "Bool"
		self.cube[("!=", "Float", "Float")] = "Bool"
		self.cube[("+", "Float", "Float")]  = "Float"
		self.cube[("-", "Float", "Float")]  = "Float"
		self.cube[("*", "Float", "Float")]  = "Float"
		self.cube[("/", "Float", "Float")]  = "Float"
		self.cube[("=", "Float", "Float")]  = "Float"

		self.cube[("&&", "Float", "Bool")]  = "Error"
		self.cube[("||", "Float", "Bool")]  = "Error"
		self.cube[(">=", "Float", "Bool")]  = "Error"
		self.cube[("<=", "Float", "Bool")]  = "Error"
		self.cube[(">", "Float", "Bool")]   = "Error"
		self.cube[("<", "Float", "Bool")]   = "Error"
		self.cube[("==", "Float", "Bool")]  = "Error"
		self.cube[("!=", "Float", "Bool")]  = "Error"
		self.cube[("+", "Float", "Bool")]   = "Error"
		self.cube[("-", "Float", "Bool")]   = "Error"
		self.cube[("*", "Float", "Bool")]   = "Error"
		self.cube[("/", "Float", "Bool")]   = "Error"
		self.cube[("=", "Float", "Bool")]   = "Error"

		#Bool
		self.cube[("&&", "Bool", "Int")]    = "Error"
		self.cube[("||", "Bool", "Int")]    = "Error"
		self.cube[(">=", "Bool", "Int")]    = "Error"
		self.cube[("<=", "Bool", "Int")]    = "Error"
		self.cube[(">", "Bool", "Int")]     = "Error"
		self.cube[("<", "Bool", "Int")]     = "Error"
		self.cube[("==", "Bool", "Int")]    = "Error"
		self.cube[("!=", "Bool", "Int")]    = "Error"
		self.cube[("+", "Bool", "Int")]     = "Error"
		self.cube[("-", "Bool", "Int")]     = "Error"
		self.cube[("*", "Bool", "Int")]     = "Error"
		self.cube[("/", "Bool", "Int")]     = "Error"
		self.cube[("=", "Bool", "Int")]     = "Error"

		self.cube[("&&", "Bool", "Float")]  = "Error"
		self.cube[("||", "Bool", "Float")]  = "Error"
		self.cube[(">=", "Bool", "Float")]  = "Error"
		self.cube[("<=", "Bool", "Float")]  = "Error"
		self.cube[(">", "Bool", "Float")]   = "Error"
		self.cube[("<", "Bool", "Float")]   = "Error"
		self.cube[("==", "Bool", "Float")]  = "Error"
		self.cube[("!=", "Bool", "Float")]  = "Error"
		self.cube[("+", "Bool", "Float")]   = "Error"
		self.cube[("-", "Bool", "Float")]   = "Error"
		self.cube[("*", "Bool", "Float")]   = "Error"
		self.cube[("/", "Bool", "Float")]   = "Error"
		self.cube[("=", "Bool", "Float")]   = "Error"

		self.cube[("&&", "Bool", "Bool")]   = "Bool"
		self.cube[("||", "Bool", "Bool")]   = "Bool"
		self.cube[(">=", "Bool", "Bool")]   = "Error"
		self.cube[("<=", "Bool", "Bool")]   = "Error"
		self.cube[(">", "Bool", "Bool")]    = "Error"
		self.cube[("<", "Bool", "Bool")]    = "Error"
		self.cube[("==", "Bool", "Bool")]   = "Error"
		self.cube[("!=", "Bool", "Bool")]   = "Error"
		self.cube[("+", "Bool", "Bool")]    = "Error"
		self.cube[("-", "Bool", "Bool")]    = "Error"
		self.cube[("*", "Bool", "Bool")]    = "Error"
		self.cube[("/", "Bool", "Bool")]    = "Error"
		self.cube[("=", "Bool", "Bool")]    = "Bool"

	def checkResult(self, op1, op2, operator):
		key = (op1, op2, operator)
		if key in self.cube:
			return self.cube[key]
		else:
			return "Error"

			