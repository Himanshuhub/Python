# MathDojo
# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.
#
# Then create a new instance called md. It should be able to do the following task:

MathDojo().add(2).add(2, 5).subtract(3, 2).result
Copy
which should perform 0+2+(2+5)-(3+2) and return 4.

class MathDojo(object):
    def __init__(self, *num):
        self.num = num
        self.total = 0 
    def add(arg):
        pass
