from e3ga import *
from math import *
from random import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

B = e1 ^ e2

print B

x = VectorE3(random(),random(),random())

print x

y = x << B

print y
