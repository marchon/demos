from e2ga import *
import math

def isCloseTo(expected, actual, precision):
    return math.fabs(expected - actual) < (math.pow(10, -precision) / 2)

def assertEqual(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

def assertCloseTo(expect, actual, message):
    if expect != actual:
        print {"expect":expect,"actual":actual,"message":message}

# Convenience functions for creating Blades.
def Scalar(w):
    return Euclidean2(w, 0, 0, 0)

def Vector(x, y):
    return Euclidean2(0, x, y, 0)

def Pseudoscalar(s):
    return Euclidean2(0, 0, 0, s)

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, x):
    print name + " => " + str(x)
    return x

z = explain(Euclidean2(0,0,0,0))
u = explain(Scalar(1))
d = explain(Scalar(2))
i   = explain(Vector(1, 0))
j   = explain(Vector(0, 1))
I   = explain(Pseudoscalar(1))

assertEqual(+z, ~z, str(z))
assertEqual(+u, ~u, str(u))
assertEqual(-i, ~i, str(i))
assertEqual(-I, ~I, "0 == 1")
assertEqual(-I, ~I, "0 == 1")

blades = [z, u, d, i, j, I]
for a in blades:
    print ""
    for b in blades:
        showValue(str(a) + " >> " + str(b), repr(a >> b))
