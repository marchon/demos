from three import *
from browser import *

scene = world()

shape = cube()

scene.add(shape)

camera = PerspectiveCamera(45, 1.0, 0.1, 10000)
camera.position.set(8, 8, 8)
camera.lookAt(scene.position)

renderer = None
container = None

movement = Vector3(0.02, 0.02, 0.02)

def discardCanvasElements():
    for element in document.getElementsByTagName("canvas"):
        element.parentNode.removeChild(element)

def tick(elapsed):
    shape.rotation += movement
    renderer.render(scene, camera)
    
def terminate(elapsed):
    return elapsed > 10000

def setUp():
    global renderer

    discardCanvasElements()

    renderer = WebGLRenderer()
    renderer.setClearColor(Color(0x080808), 1.0)

    document.body.insertBefore(renderer.domElement, document.body.firstChild)
#    container = document.getElementById("canvas-container")
#    container.appendChild(renderer.domElement)
    renderer.size = (window.innerWidth, window.innerHeight) 
#   renderer.size = (container.offsetWidth, container.offsetHeight) 
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()


def tearDown():
    discardCanvasElements()

WindowAnimationRunner(window, tick, terminate, setUp, tearDown).start()
