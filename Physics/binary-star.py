# binary-star.py
from browser import *
from three import *
from workbench import *
from random import random

scene = Scene()

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

camera = PerspectiveCamera()
camera.position.z = 15

pointLight = PointLight(0xFFFFFF);
pointLight.position = camera.position
scene.add(pointLight)

workbench3D = Workbench(renderer, camera)

i = VectorE3(1, 0, 0)
j = VectorE3(0, 1, 0)
k = VectorE3(0, 0, 1)

giant = SphereBuilder().color("red").radius(0.8).build()
giant.mass     = ScalarE3(1e30)
giant.momentum = VectorE3(0, 0, -1e4) * giant.mass
scene.add(giant)

dt = 0.3

def setUp():
    workbench3D.setUp()

def tick(t):

    renderer.render(scene, camera)

def terminate(t):
    return t > 10

def tearDown():
    workbench3D.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
