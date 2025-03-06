#!/usr/bin/env python3
import math

class rootSolver:

    def __init__(self, functionNr: int, a: int, b: int, 
                 stopTypeNr: int, iterOrPrecision):
        assert self.areValidBounds(a, b)

        self.functionNr = functionNr
        self.a = a
        self.b = b
        self.stopType = stopTypeNr
        if(stopTypeNr == 1):
            self.precision = iterOrPrecision 
        elif(stopTypeNr == 2):
            self.iterCount = iterOrPrecision
    
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
        return self.f(a) * self.f(b) < 0 

    def f(self, x):
        return x * x * x;

    def print(self):
        print()

def main():
    print("Hello please pick one of the following functions!:" + 
        "\n1) x^3 - 2x^2 + 3x - 1" +
        "\n2) sin(x) + cos(x)" +
        "\n3) 2^x - 1/e" +
        "\n4) e^x * sin(2x) + e^x")

    functionNr = int(input())

    print("Input left bound (a)")
    a = int(input())

    print("Input right bound (b)")
    b = int(input())

    print("Choose stop condition: " +
          "\n1) by precision" + 
          "\n2) by iteration")
    stopTypeNr = int(input())

    if stopTypeNr == 1:
        iterOrPrecision = float(input("Input precision"))
    elif stopTypeNr == 2:
        iterOrPrecision = int(input("Input iteration count")) 

    #solver = rootSolver(-5, 2, 3, 0.5)
    solver = rootSolver(functionNr, a, b, stopTypeNr, iterOrPrecision)
    print(solver.bisectionMethod())

main()
