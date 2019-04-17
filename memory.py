# ------------------------------------------------------------
# memory.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------


class Memory:

    def __init__(self, stage):
        if stage == "program":
            self.INT_LOC = 5000
            self.MAX_INT_LOC = 9999
            self.FLOAT_LOC = 10000
            self.MAX_FLOAT_LOC = 14999
            self.BOOL_LOC = 15000
            self.MAX_BOOL_LOC = 19999
        if stage == "function":
            self.INT_LOC = 20000
            self.MAX_INT_LOC = 24999
            self.FLOAT_LOC = 25000
            self.MAX_FLOAT_LOC = 29999
            self.BOOL_LOC = 30000
            self.MAX_BOOL_LOC = 34999
        if stage == "constant":
            self.INT_LOC = 35000
            self.MAX_INT_LOC = 39000
            self.FLOAT_LOC = 40000
            self.MAX_FLOAT_LOC = 44999
            self.BOOL_LOC = 45000
            self.MAX_BOOL_LOC = 49999
        self.memory = dict()

    def int_check(self):
        return self.INT_LOC <= self.MAX_INT_LOC

    def float_check(self):
        return self.FLOAT_LOC <= self.MAX_FLOAT_LOC

    def bool_check(self):
        return self.BOOL_LOC <= self.MAX_BOOL_LOC

    def get_next_address(self, type):
        if type == "Int":
            self.INT_LOC = self.INT_LOC + 1
            return self.INT_LOC - 1
        elif type == "Float":
            self.FLOAT_LOC = self.FLOAT_LOC + 1
            return self.FLOAT_LOC - 1
        else:
            self.BOOL_LOC = self.BOOL_LOC + 1
            return self.BOOL_LOC - 1

