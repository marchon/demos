from three import *
from browser import *

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 2

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

radius = 1
detail = 0 # Must be an integer: 0,1,2,...

octah = OctahedronGeometry(radius, detail)

print repr(octah)
print "radius:         " + str(octah.radius)
print "detail:         " + str(octah.detail)
print octah

mesh = Mesh(octah, MeshNormalMaterial({"wireframe": True, "wireframeLinewidth": 3}))
scene.add(mesh)

movement = Vector3(0.02, 0.02, 0.02)

workbench = Workbench(renderer, camera)

def setUp():
    workbench.setUp()

def tick(elapsed):
    mesh.rotation += movement    
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 6000

def tearDown():
    workbench.tearDown()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
