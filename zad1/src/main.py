#!/usr/bin/env python3
import math

class rootSolver:

    def __init__(self, a: int, b: int, functionNr: int, precision: float):
        assert self.areValidBounds(a, b)

        self.a = a
        self.b = b
        self.functionNr = functionNr
        self.precision = precision

    
    def solve():
        pass

    def bisectionMethod(self):
        
        result = math.inf 
        x = None

        while not -self.precision < result < self.precision:
            if x != None and self.areValidBounds(x, self.b):
                self.a = x
            elif x != None and self.areValidBounds(self.a, x):
                self.b = x
            elif x != None:
                raise ValueError()

            x = (self.a + self.b) / 2
            result = self.f(x)

        return result


    def secantMethod(self):
        pass

    def areValidBounds(self, a, b):
        return self.f(a) * self.f(b)  < 0 

    def f(self, x):
        return x * x * x;

    def print(self):
        print()

def main():
    print("Hello please pick one of the following functions!:")
    print("1) x^3 - 2x^2 + 3x - 1")
    print("2) sin(x) + cos(x)")
    print("3) 2^x - 1/e")
    print("4) e^x * sin(2x) + e^x")
    picked = input()

    solver = rootSolver(-5, 2, 3, 0.5)
    print(solver.bisectionMethod())

main()
