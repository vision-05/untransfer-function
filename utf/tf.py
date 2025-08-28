import re
import sympy
import operator
import functools

s = sympy.Symbol('s')

class tf:
    tf = 0

    def __init__(self, n, d=[]):
        if type(n) == int or type(d) == int:
            raise TypeError
        if n == []:
            self.tf = 0
            return
        numerator = functools.reduce(operator.add, [n[::-1][i]*s**i for i in range(len(n))])
        if d == []:
            self.tf = numerator
        elif len(d) == 1 and d[0] == 0:
            raise ZeroDivisionError
        else:
            denominator = functools.reduce(operator.add, [d[::-1][i]*s**i for i in range(len(d))])
            self.tf = numerator/denominator

    def pprint(self):
        print(f"{self.tf}")

    def get_tf(self):
        print(type(self.tf))
        return self.tf

    
