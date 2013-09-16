'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi, exp
from units import *

workbench = Workbench()

space = CartesianSpace()

shape = ConeBuilder().color(0xFFFF00).volume(0.1).build()
space.add(shape)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

# The geometric angular velocity measure (quantity with unit-of-measure).
# The angular velocity describes a motion of one revolution every 12 seconds in the x-y plane, counterclockwise.
omega = 2 * pi * i * j / (12 * second)

timeout = 12 * kilo# * milli * second

def onDocumentKeyDown(event):
    global timeout
    if event.keyCode == 27:
        timeout = 0

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    t = ScalarE3(elapsed) * milli * second
    angle = omega * t / 2
    R = exp(-angle)
    position = (R * (4 * i * meter) * ~R).quantity
    shape.position.set(position.x, position.y, position.z)
    # To convert a Euclidean3 rotor to a Quaternion, use the 'dual' parts with a sign change.
    # The quaternion property of the mesh is what we would call the attitude - a spinor.
    shape.quaternion.set(-R.quantity.yz, -R.quantity.zx, -R.quantity.xy, R.quantity.w)
    space.render()
    
def terminate(elapsed):
    return elapsed > timeout

def setUp():
    workbench.setUp()
    #document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    document.addEventListener("keydown", onDocumentKeyDown, False)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    workbench.tearDown()
    window.removeEventListener("resize", onWindowResize, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    #document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
