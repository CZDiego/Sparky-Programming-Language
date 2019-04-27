# ------------------------------------------------------------
# sparky_type.py
#
# Luis Salomon Flores Ugalde | A00817435
# Diego Contreras            | A00817441
# ------------------------------------------------------------


class SparkyType:
    def __init__(self):
        self.spark_type = ""
        self.col = 0
        self.row = 0

    def typeKey(self):
        return self.spark_type+str(self.col)+str(self.row)

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
