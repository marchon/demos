from geometry import *
from three import *
from browser import *
from workbench import *

space = CartesianSpace()

# All arguments are optional and the defaults, in order, are as follows.
radiusCone = 1
radiusShaft = 0.5
length = 4
lengthShaft = 3

a = VectorE3(0, 0, length)
b = VectorE3(radiusCone, 0, lengthShaft)
c = VectorE3(radiusShaft, 0, lengthShaft)
d = VectorE3(radiusShaft, 0, 0)
e = VectorE3(0, 0, 0)
points = [a, b, c, d, e]
# The points are to be rotated in the xy-plane to generate the geometry.
arrow = RevolutionGeometry(points, BivectorE3(1, 0, 0), 12)

material = MeshNormalMaterial({"wireframe":True, "wireframeLinewidth": 1})
mesh = Mesh(arrow, material)
space.add(mesh)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    space.render()
    
def terminate(t):
    return t > 4

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
