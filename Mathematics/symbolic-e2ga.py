'''
Under Construction. This may not work for you. Oct 29, 2013.
'''
from e2ga import *
from symbolic import *

i = VectorE2(1, 0)
j = VectorE2(0, 1)

w = Variable("w")
x = Variable("x")
y = Variable("y")
s = Variable("s")

p = Euclidean2(1, x, y, s)
print repr(p)
expr = p
env = Environment() + Binding("x", 2) + Binding("y", 3)
print Binding(str(expr), expr.evaluate(env))
