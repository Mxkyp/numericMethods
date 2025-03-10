#!/usr/bin/env python3
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import number
from unicodedata import numeric


class rootSolver:

    def __init__(self, functionNr: int, a: float, b: float,
                 stopTypeNr: int, x0: float, x1: float, iterOrPrecision):

        self.functionNr = functionNr
        self.a = a
        self.b = b
        self.stopTypeNr = stopTypeNr
        self.x0 = x0
        self.x1 = x1

        assert self.areValidBounds(a, b)
        if (stopTypeNr == 1):
            self.precision = iterOrPrecision
            self.iterCount = 2000000
        elif (stopTypeNr == 2):
            self.iterCount = int(iterOrPrecision)
            self.precision = 1e-5

    def f(self, x):
        if self.functionNr == 1:
            numbers = [1, -2, 3, -1]
            return self.horner(x, numbers)
        elif self.functionNr == 2:
            return np.sin(x) + np.cos(x)
        elif self.functionNr == 3:
            return 2 ** x - 1 / math.e
        elif self.functionNr == 4:
            return np.exp(x) * np.sin(2 * x) + np.exp(x) - 3
        return None

    def horner(self, x, numbers):
        result = 0
        for num in numbers:
            result = result * x + num
        return result

    def bisectionMethod(self):

        a = self.a
        b = self.b

        x = None
        iterations_ran = 0

        if self.areValidBounds(a, b):
            while iterations_ran < self.iterCount:
                x = (a + b) / 2
                f_x = self.f(x)

                if abs(f_x) < self.precision:
                    return x, iterations_ran, self.f(x)

                if self.f(a) * self.f(x) < 0:
                    b = x
                else:
                    a = x

                iterations_ran += 1

            return x, iterations_ran, self.f(x)
        else:
            return print("function has no zero point")

    def areValidBounds(self, a, b):
        return self.f(a) * self.f(b) < 0

    def check_derivative(self, functionNr, x):
        if(functionNr == 1):
            return 3*x**2 - 4*x + 3
        if(functionNr == 2):
            return math.cos(x) - math.sin(x)
        if(functionNr == 3):
            return math.log(2) * 2**x
        if(functionNr == 4):
            return math.exp(x) * (2 * math.cos(2 * x) + math.sin(2 * x)) + math.exp(x)

    def secantMethod(self):

        x0 = self.x0
        x1 = self.x1

        iterations_ran = 0

        for i in range(int(self.iterCount)):
            f_x0 = self.f(x0)
            f_x1 = self.f(x1)

            f_prime_x0 = self.check_derivative(self.functionNr, x0)
            f_prime_x1 = self.check_derivative(self.functionNr, x1)

            if f_prime_x0 == 0 or f_prime_x1 == 0 :
                return None

            if f_x0-f_x1 == 0:
                return None

            x2 = x1-f_x1*(x1-x0)/(f_x1-f_x0)

            if abs(f_x1) < self.precision and self.a <= x1 <= self.b: 
                return x1, iterations_ran, self.f(x1)

            x0 = x1
            x1 = x2

            iterations_ran += 1

        return x1, iterations_ran, self.f(x1)


    def plotFunction(self):
        x_values = np.linspace(self.a, self.b, 400)

        vectorized_f = np.vectorize(self.f)
        y_values = vectorized_f(x_values)

        resultBisection = self.bisectionMethod()
        resultSecant = self.secantMethod()

        if resultBisection is not None:
            x1, iter_count1, f_x1 = resultBisection
            self.markPoint(x1, f_x1, iter_count1, "red", "B")

        if resultSecant is not None:
            x2, iter_count2, f_x2  = resultSecant
            self.markPoint(x2, f_x2, iter_count2, "green", "S")

        plt.plot(x_values, y_values, label="f(x)")
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.title(f'Plot of the selected function (f{x_values[0]} to f{x_values[-1]})')
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()


    def markPoint(self, x: float, f_x: float, iter_count: int, colorPicked: str, mark: str):
            plt.scatter(x, f_x, color = colorPicked, zorder=5, label=mark + " " + f"{f_x:.4f} at x={x:.4f}, iter = {iter_count}")


def main():
    print("Hello please pick one of the following functions!:")
    print("1) x^3 - 2x^2 + 3x - 1")
    print("2) sin(x) + cos(x)")
    print("3) 2^x - 1/e")
    print("4) e^x * sin(2x) + e^x - 3")

    functionNr = int(input())

    a = float(input("Input left bound (a):\n"))

    b = float(input("Input right bound (b):\n"))

    x0 = float(input("Input first point:\n"))

    x1 = float(input("Input second point:\n"))

    print("Choose stop condition: " +
          "\n1) by precision" +
          "\n2) by iteration")

    stopTypeNr = int(input())

    if stopTypeNr == 1:
        iterOrPrecision = float(input("Input precision:\n"))
    elif stopTypeNr == 2:
        iterOrPrecision = int(input("Input iteration count:\n"))

        # solver = rootSolver(-5, 2, 3, 0.5)
    solver = rootSolver(functionNr, a, b, stopTypeNr, x0, x1, iterOrPrecision)
    solver.plotFunction()

main()
