'''
A block slides down an inclined plane that makes a 30 degree angle with the horizontal.
If the coefficient of friction is 0.3, find the acceleration of the block.
'''
from math import *
from e3ga import *
from units import *

# Define standard orthogonal unit vectors and their meanings.
# 
i = VectorE3(1,0,0) # To the right.
j = VectorE3(0,1,0) # Up
k = i.cross(j)      # Must be out of page for a right-handed set.
print "k => %s" % (k)

# The given parameters
theta = (30 / 180) * pi
mu = 0.3

def acceleration(theta, mu):
    m = 23 * kilogram
    W = m * g
    F = W.dot(eDown) * eDown
    
    
print acceleration(theta, mu)
