# ------------------------------------------------------------
# memory.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------
import sys
error_message = '\033[91m' + "ERROR: " + '\033[0m' 

class MemoryMap:

    def __init__(self, stage):
        if stage == "program":
            self.INT_LOC = 5000
            self.MAX_INT_LOC = 9999
            self.FLOAT_LOC = 10000
            self.MAX_FLOAT_LOC = 14999
            self.BOOL_LOC = 15000
            self.MAX_BOOL_LOC = 19999
            self.OBJ_LOC = 20000
            self.MAX_OBJ_LOC = 24999
        if stage == "function":
            self.INT_LOC = 25000
            self.MAX_INT_LOC = 29999
            self.FLOAT_LOC = 30000
            self.MAX_FLOAT_LOC = 34999
            self.BOOL_LOC = 35000
            self.MAX_BOOL_LOC = 39999
            self.OBJ_LOC = 40000
            self.MAX_OBJ_LOC = 44999
        if stage == "temporal":
            self.INT_LOC = 45000
            self.MAX_INT_LOC = 49999
            self.FLOAT_LOC = 50000
            self.MAX_FLOAT_LOC = 54999
            self.BOOL_LOC = 55000
            self.MAX_BOOL_LOC = 59999
            self.OBJ_LOC = 60000
            self.MAX_OBJ_LOC = 64999
        if stage == "class":
            self.INT_LOC = 65000
            self.MAX_INT_LOC = 69999
            self.FLOAT_LOC = 70000
            self.MAX_FLOAT_LOC = 74999
            self.BOOL_LOC = 75000
            self.MAX_BOOL_LOC = 79999

    def int_check(self):
        return self.INT_LOC <= self.MAX_INT_LOC

    def float_check(self):
        return self.FLOAT_LOC <= self.MAX_FLOAT_LOC

    def bool_check(self):
        return self.BOOL_LOC <= self.MAX_BOOL_LOC

    def get_next_address(self, t):
        total_space = 0
        if t.row == 0 and t.col == 0:
            total_space = 1
        elif t.row >= 0 and t.col == 0:
            total_space = t.row
        else:
            total_space = t.row * t.col

        if t.type == "Int":
            self.INT_LOC = self.INT_LOC + total_space
            if self.INT_LOC > self.MAX_INT_LOC:
                print(error_message + " Too many variables")
                sys.exit(0)
            return self.INT_LOC - total_space
        elif t.type == "Float":
            self.FLOAT_LOC = self.FLOAT_LOC + total_space
            if self.FLOAT_LOC > self.MAX_FLOAT_LOC:
                print(error_message + " Too many variables")
                sys.exit(0)
            return self.FLOAT_LOC - total_space
        elif t.type == "Bool":
            self.BOOL_LOC = self.BOOL_LOC + total_space
            if self.BOOL_LOC > self.MAX_BOOL_LOC:
                print(error_message + " Too many variables")
                sys.exit(0)
            return self.BOOL_LOC - total_space
        elif t.is_object():
            self.OBJ_LOC = self.OBJ_LOC + total_space
            if self.OBJ_LOC > self.MAX_OBJ_LOC:
                print(error_message + " Too many variables")
                sys.exit(0)
            return self.OBJ_LOC - total_space

