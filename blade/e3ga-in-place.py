# Demonstration of the Geometric Algebra generated by a Euclidean 3D vector space.
from eight import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero  = explain(MultiVector3(0, 0, 0, 0, 0, 0, 0, 0))
one   = explain(Scalar3(1))
two   = explain(Scalar3(2))
three = explain(3)
i     = explain(Vector3(1, 0, 0))
j     = explain(Vector3(0, 1, 0))
k     = explain(Vector3(0, 0, 1))
ij    = explain(Bivector3(1, 0, 0))
jk    = explain(Bivector3(0, 1, 0))
ki    = explain(Bivector3(0, 0, 1))
I     = explain(Pseudoscalar3(1))

x = zero
showValue("x", x)

x += one
showValue("x", x)
x += 1
showValue("x", x)

x -= one
showValue("x", x)
x -= 1
showValue("x", x)

x = one
showValue("x", x)
x *= two
showValue("x", x)
x *= 2
showValue("x", x)

x = j
showValue("x", x)
x ^= j
showValue("x", x)
x ^= 2
showValue("x", x)
