
class QuadList:
    def __init__(self):
        self.List = []


# Almost like slice deletion
#>>> tup = tup[0:2]
#>>> tup
#('one', 'two')
#>>> tup2 += tup
#>>> tup2
# almost like index assignment
#>>> tup2 = tup2[0:1] + (1,) + tup2[2:]
#>>> tup2
#(0, 1, 'two')