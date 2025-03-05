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

        while not -self.precision < result < self.precision:
            if x != None and self.areValidBounds(x, self.b):
                self.a = x
            elif x != None and self.areValidBounds(self.a, x):
                self.b = x
            elif x != None:
                raise ValueError()

            x = (self.a + self.b) / 2
            result = self.f(x)
            print(x)

        return result


    def secantMethod(self):
        pass

    def areValidBounds(self, a, b):
        return a * b < 0 

    def f(self, x):
        return x*x;

    def print(self):
        print()

def main():
    solver = rootSolver(-5, 2, 3, 0.5)
    print(solver.bisectionMethod())

main()
