'''
This lesson demonstrates animating an object.
The sphere performs cirular motion with radius R and periodic time T.
'''
from browser import WindowAnimationRunner
from geometry import CartesianSpace, SphereBuilder
from math import cos, sin, pi
from workbench import Workbench

x = -5
y = -5
z = 0

moveX = 0
moveY = 0
moveZ = 0

space = CartesianSpace()

sphere = SphereBuilder().radius(0.1).color(0xFFFF00).build()
space.add(sphere)

workbench = Workbench(space.renderer, space.camera)

def tick(t):
    global x, y, z, moveX, moveY, moveZ
    x += moveX
    y += moveY
    z += moveZ
    if x > 3:
        x = 3
    if y > 3:
        y = 3
    if x < -3:
        x = -3
    if y < -3:
        x = 3

    sphere.position.set(x, y, z)
    space.render()

def terminate(t):
    done = t > 10
    return done

def setUp():
    workbench.setUp()

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
