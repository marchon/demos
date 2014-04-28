from math import *
from units import *
from cmath import *
'''
Quadrance is a term introduced by NJ Wildberger.
'''

print quadrance(2)
print quadrance(2.0)
try:
    print quadrance("Hello")
except:
    pass

c = complex(1.0,1.0)
print str(c)
print repr(c)
print type(c)
print quadrance(c)
