from e3ga import *
from units import *
import numpy as np

x = np.linspace(2.0, 3.0, 5, True, False)

print "linspace(2.0, 3.0, 5, True, False)"
print x[0]
print x[1]
print x[2]
print x[3]
print x[4]

x = np.linspace(2.0, 3.0, 5, False, False)

print "linspace(2.0, 3.0, 5, False, False)"
print x[0]
print x[1]
print x[2]
print x[3]
print x[4]

x = np.linspace(2.0, 3.0, 5, True, True)

print "linspace(2.0, 3.0, 5, True, True)"
print x
print x[0]
print x[1]
print x[0][0]
print x[0][1]
print x[0][2]

x = np.linspace(2.0, 3.0, 5, False, True)

print "linspace(2.0, 3.0, 5, False, True)"
print x
print x[0]
print x[1]
print x[0][0]
print x[0][1]
print x[0][2]

x = np.linspace(2.0 * second, 3.0 * second, 5, False, True)
print
print x
print x[0]
print x[1]
print x[0][0]
print x[0][1]
print x[0][2]
print x[0][3]
print x[0][4]

x = np.linspace(VectorE3(1,0,0), VectorE3(0,1,0), 5, False, True)
print
print x
print x[0]
print x[1]
print x[0][0]
print x[0][1]
print x[0][2]
print x[0][3]
print x[0][4]
