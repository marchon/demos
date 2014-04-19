from numpy import *
from e3ga import *

x = array([1,2,3])
y = array([9,7,5])
print x * y

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)
e3 = VectorE3(0,0,1)

x = array([4*e1,1])
y = array([e2,e3])
print x
print y
print x * y
print y * x
print x * 3
print 3 * x
print x + y

