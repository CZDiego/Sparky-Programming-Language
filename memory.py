class Memory:

    def __init__(self, stage):
        self.INT_SIZE = int.bit_length()
        self.FLOAT_SIZE = float.bit_length()
        self.BOOL_SIZE = bool.bit_length()
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
