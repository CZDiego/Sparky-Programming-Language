# ------------------------------------------------------------
# sparky_type.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------


class SparkyType:
    def __init__(self):
        self.spark_type = ""
        self.row = 0
        self.col = 0

    def type_key(self):
        return self.spark_type + "," + str(self.col) + "," + str(self.row)

    def is_object(self):
        return self.spark_type not in ["Int", "Bool", "Float"]

    def is_matrix(self):
        return self.col > 0

    def is_array(self):
        return self.row > 0

    def check_type(self, spark):
        if self.spark_type != spark.spark_type:
            return False
        if self.row != spark.row:
            return False
        if self.col != spark.col:
            return False
        return True

'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
'''
