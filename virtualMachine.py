import sys
import time
from datetime import timedelta

class VirtualMachine:
	def __init__(self):
		self.quads = []
		self.iterators = []
		self.memory = dict()
		self.start_time = 0
		self.end_time = 0
		self.funcs = {
			"+" : self.plus,
			"-" : self.minus,
			"*" : self.multiplication,
			"/" : self.division,
			"=" : self.equals,
			"<" : self.less_than,
			"PRINT" : self.print,
			"INPUT" : self.input,
			"GOTO" : self.goto,
			"GOTOF" : self.gotof,
			"END" : self.end
		}

	def execute(self):
		print("executing...")
		self.start_time = time.monotonic()
		self.iterators.append(0)

		while True:
			clean_quad = self.clean_quad(self.quads[self.iterators[-1]])
			#print(clean_quad)
			self.funcs[clean_quad[0]](clean_quad)
			self.iterators[-1] = self.iterators[-1] + 1

	def clean_quad(self, quad):
		print("cleaning")

		if not quad[1] is None and quad[1].__class__.__name__ in ('tuple'):
			new_quad = quad[:1]+(self.clean_tuple(quad[1],1),)+quad[2:4]
			quad = new_quad

		if not quad[2] is None and quad[2].__class__.__name__ in ('tuple'):
			new_quad = quad[:2]+(self.clean_tuple(quad[2],2),)+quad[3:4]
			quad = new_quad

		if not quad[3] is None and quad[3].__class__.__name__ in ('tuple'):
			new_quad = quad[:3]+(self.clean_tuple(quad[3],3),)
			quad = new_quad

		return quad
		
		#r = result
		#print(r._class.name_ in ('tuple'))

	def clean_tuple(self, tp, n):
		if tp[0] == "cte":
			#asignar a memory
			#memory[50000] = tp[1]
			if n == 1:
				self.memory[50000] = tp[1]
				return 50000
			elif n == 2:
				self.memory[50001] = tp[1]
				return 50001
			else:
				self.memory[50002] = tp[1]
				return 50002
		else:
			#pointer
			return 10 # memory[tp[1]]

	def plus(self, quad):
		print("plus")
		self.memory[quad[3]] = self.memory[quad[1]] + self.memory[quad[2]]

	def minus(self, quad):
		print("minus")
		self.memory[quad[3]] = self.memory[quad[1]] - self.memory[quad[2]]

	def multiplication(self, quad):
		print("multiplication")
		self.memory[quad[3]] = self.memory[quad[1]] * self.memory[quad[2]]

	def division(self, quad):
		print("division")
		self.memory[quad[3]] = self.memory[quad[1]] / self.memory[quad[2]]

	def equals(self, quad):
		print("equals")
		self.memory[quad[3]] = self.memory[quad[1]]

	def less_than(self, quad):
		print("less_than")
		if self.memory[quad[1]] < self.memory[quad[2]]:
			self.memory[quad[3]] = True
		else:
			self.memory[quad[3]] = False

	def goto(self, quad):
		print("goto")
		self.iterators[-1] = quad[3] - 1

	def gotof(self, quad):
		print("gotof")
		if not self.memory[quad[1]]:
			self.iterators[-1] = quad[3] - 1			

	def end(self, quad):
		print("end")
		self.end_time = time.monotonic()
		print("Execution time: " + str((timedelta(seconds=self.end_time - self.start_time))))


		sys.exit(0)

	def print(self, quad):
		print("printing")
		print(self.memory[quad[1]])

	def input(self, quad):
		print("reading")
		#checar el tipo de la entrada
		user_input = input()
		try:
			val = int(user_input)
			self.memory[quad[3]] = val
		except ValueError:
			sys.exit(0)

