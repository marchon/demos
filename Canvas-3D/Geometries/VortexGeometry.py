'''
Under Construction Sep 25, 2013
'''
from three import *
from browser import *
from workbench import *
from math import pi

space = CartesianSpace()

radius = 2
radiusCone = 0.8
radiusShaft = 0.1
radialSegments = 32
arrowSegments = 24

vortex = VortexGeometry(radius, radiusShaft, radialSegments, arrowSegments)
vortex.name = "Maxwell"

print repr(vortex)
print "id:             " + str(vortex.id)
print "name:           " + str(vortex.name)
print "uuid:           " + str(vortex.uuid)
#print "radius:         " + str(torus.radius)
#print "tube:           " + str(torus.tube)
#print "radialSegments: " + str(torus.radialSegments)
#print "tubularSegments:" + str(torus.tubularSegments)
#print "arc:            " + str(torus.arc)
print vortex

mesh = Mesh(vortex, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 1}))
space.add(mesh)

workbench = Workbench3D(space.renderer.canvas, space.renderer, space.camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 3

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
