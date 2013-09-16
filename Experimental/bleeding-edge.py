from three import *
from geometry import CartesianSpace, CylinderBuilder
from browser import document, window, Workbench, WindowAnimationRunner

space = CartesianSpace()
timeOut = 6000

workbench = Workbench(space.renderer, space.camera)

def setUp():
    workbench.setUp()

    mesh = ArrowBuilder().build()

    space.add(mesh)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > timeOut

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()