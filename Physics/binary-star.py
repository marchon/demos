# binary-star.py
from browser import *
from three import *
from workbench import *
from math import pow
from random import random

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera(50,1,0.1,1e20)
camera.position.z = 15

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

giant = SphereBuilder().color("red").radius(0.8).build()
giant.position = VectorE3(-1e11, 0, 0)
giant.mass     = ScalarE3(2e30)
giant.momentum = VectorE3(0, 0, -1e4) * giant.mass
#scene.add(giant)

dwarf = SphereBuilder().color("yellow").radius(0.8).build()
dwarf.position = VectorE3(1.5e11, 0, 0)
dwarf.mass     = ScalarE3(1e30)
dwarf.momentum = -giant.momentum
scene.add(dwarf)

G = 6.7e-11
dt = 0.3

def setUp():
    workbench3D.setUp()

def tick(t):
    r = dwarf.position - giant.position
    F = G * giant.mass * dwarf.mass * r / pow(r % r, 3/2)
    giant.momentum += F * dt
    dwarf.momentum -= F * dt
    
    for star in [giant, dwarf]:
        star.position += (star.momentum / star.mass) * dt
    
    renderer.render(scene, camera)

def terminate(t):
    return t > 1

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
