# ------------------------------------------------------------
# memory.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------


class Memory:

    def __init__(self, stage):
        if stage == "program":
            self.INT_LOC = 5001
            self.MAX_INT_LOC = 10000
            self.FLOAT_LOC = 10001
            self.MAX_FLOAT_LOC = 15000
            self.BOOL_LOC = 15001
            self.MAX_BOOL_LOC = 20000
        if stage == "function":
            self.INT_LOC = 20001
            self.MAX_INT_LOC = 25000
            self.FLOAT_LOC = 25001
            self.MAX_FLOAT_LOC = 30000
            self.BOOL_LOC = 30001
            self.MAX_BOOL_LOC = 35000
        if stage == "constant":
            self.INT_LOC = 35001
            self.MAX_INT_LOC = 40000
            self.FLOAT_LOC = 45001
            self.MAX_FLOAT_LOC = 50000
            self.BOOL_LOC = 50001
            self.MAX_BOOL_LOC = 55000

    def int_check(self):
        return self.INT_LOC <= self.MAX_INT_LOC

    def float_check(self):
        return self.FLOAT_LOC <= self.MAX_FLOAT_LOC

    def bool_check(self):
        return self.BOOL_LOC <= self.MAX_BOOL_LOC

