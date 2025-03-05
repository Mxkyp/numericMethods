#!/usr/bin/env python3


class rootSolver:

    def __init__(self, leftBoundInclusive, rightBoundInclusive, functionNr):
        self.leftBoundInclusive = leftBoundInclusive
        self.rightBoundInclusive = rightBoundInclusive
        self.functionNr = functionNr

    def secantMethod(self):
       self.assertValidBounds()

    def bisectionMethod(self):
       self.assertValidBounds()

    def assertValidBounds(self):
       assert self.leftBoundInclusive * self.rightBoundInclusive < 0 

    def print(self):
        print()

def main():

main()
