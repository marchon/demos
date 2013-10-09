from browser import WindowAnimationRunner
from geometry import CartesianSpace, ArrowBuilder
from workbench import Workbench
from e3ga import *
from math import exp, sqrt, pi
'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
For al f,g,h in V and c,k scalars, the set also satisfies the following rules:
1. (f + g) + h = f + (g + h)
2. f + g = g + f
'''
class Euclidean:
    def __init__(self, w, x, y):
        if isinstance(w, float):
            self.w = w
        else:
            raise AssertionError("w must be a float")
        if isinstance(x, float):
            self.x = x
        else:
            raise AssertionError("x must be a float")
        if isinstance(y, float):
            self.y = y
        else:
            raise AssertionError("y must be a float")
            
    def __add__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Vector(self.w * other.x, self.w * other.y)

    def __rmul__(self, other):
        if not isinstance(other, float):
            raise AssertionError("other must be a Euclidean or float")
        return Vector(other * self.x, other * self.y)

    def __eq__(self, other):
        if not isinstance(other, Euclidean):
            return False
        return self.w == other.w and self.x == other.x and self.y == other.y
    
    def __str__(self):
        parts = []
        if self.w != 0.0:
            parts.append(str(self.w))
        if self.x != 0.0 or self.y != 0.0:
            parts.append(" + ".join([str(self.x)+" * i", str(self.y)+" * j"]))
        return "+".join(parts)
    
    def __repr__(self):
        parts = []
        if self.w != 0.0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0.0 or self.y != 0.0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y)]) + ")")
        return "+".join(parts)

def Vector(x, y):
    return Euclidean(0.0, x, y)

def Scalar(w):
    return Euclidean(w, 0.0, 0.0)

f = Vector(3.0, 1.0)
g = Vector(0.0, 2.0)
h = Vector(1.0, 1.0)
u = f + g
v = g + h
i = f + g + h

scene = CartesianSpace()

def magnitude(v):
    return sqrt(v.x * v.x + v.y * v.y)

def attitude(v):
    a = VectorE3(0, 0, 1)
    b = VectorE3(v.x, v.y, 0) / magnitude(v)
    numer = 1 + b * a
    denom = ScalarE3(sqrt(2 + (a % b)))
    R = numer / denom
    return R

arrowF = ArrowBuilder().scale( magnitude(f) ).attitude( attitude(f) ).color("red").build()
scene.add(arrowF)
arrowF.position.set(f.x / 2.0, f.y / 2.0, 0.0)

arrowG = ArrowBuilder().scale( magnitude(g) ).attitude( attitude(g) ).color("green").build()
scene.add(arrowG)
arrowG.position.set(g.x / 2.0, g.y / 2.0, 0.0)

arrowH = ArrowBuilder().scale( magnitude(h) ).attitude( attitude(h) ).color("blue").build()
scene.add(arrowH)
arrowH.position.set(h.x /2.0 , h.y / 2.0, 0.0)

arrowU = ArrowBuilder().scale( magnitude(u) ).attitude( attitude(u) ).color("yellow").build()
scene.add(arrowU)
arrowH.position.set(u.x /2.0 , u.y / 2.0, 0.0)

workbench = Workbench(scene.renderer, scene.camera)

def tick(t):
    scene.render()

def terminate(t):
    done = t > 16
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()

