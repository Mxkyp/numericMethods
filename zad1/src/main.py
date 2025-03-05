#!/usr/bin/env python3


class rootSolver:

    def __init__(self, a, b, functionNr, precision):
        assert self.areValidBounds(a, b)

        self.a = a
        self.b = b
        self.functionNr = functionNr
        self.precision = precision

    def bisectionMethod(self):
        
        result = -1
        x = None

        while not -self.precision < result < self.precision
            """ if(x != None and areValidBounds()) """
            x = self.a + self.b / 2
            result = f(x)


    def secantMethod(self):

    def areValidBounds(self, a, b):
        f(a) * f(b) < 0 

    def f(self, x):
        return x*x;

    def print(self):
        print()

def main():

main()
