'''
This example represents efforts to provide convenient abstractions
of the Three.js WebGL Computer Graphics API for use with Physics simulations.
'''
from geometry import *
from e3ga import *
from browser import *
from math import pi

space = CartesianSpace()

space.add(cylinder().translateX(-2.5).translateY(-2.5).rotateX(pi/2))
space.add(cube().translateX(2.5).translateY(2.5))
space.add(sphere().translateX(+2.5).translateY(-2.5))

def onWindowResize(event):
    space.viewSize(window.innerWidth, window.innerHeight)

def tick(elapsed):
    space.render()
    
def terminate(elapsed):
    return elapsed > 15000

def setUp():
    document.removeElementsByTagName("canvas")
    document.body.insertBefore(space.renderer.domElement, document.body.firstChild)
    window.addEventListener("resize", onWindowResize, False)
    onWindowResize(None)

def tearDown():
    window.removeEventListener("resize", onWindowResize, False)
    document.removeElementsByTagName("canvas")

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
