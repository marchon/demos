'''
Experiment with the calculation and visualization of a path integral in the complex plane.

f(z) = 1/(z(z+1)), where the contour is a circle: |z| = R > 1.

We can convert this to polar coordinates and simplify.
We can also chug through the integral using Cartesian coordinates.

'''
from cmath import *
from math import cos, sin

def f(z):
    return one / (z * (z + 1))

def sumOne(R):
    N = 500
    dTheta = tao / N
    sum = 0
    for i in range(1, N + 1):
        theta = i * tao / N 
        c = cos(theta)
        sum += ((R * c + one) / (R * R + 2 * R * c + one))
    return sum * dTheta

for i in range(0,20):
    R = i / 10.0
    print str(R) + " => " + str(sumOne(R))


