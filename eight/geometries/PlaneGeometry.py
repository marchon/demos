# PlaneGeometry demonstration.
from eight import *
from browser import *
from math import pi

# Discard the old canvas if it exists. 
for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 20

renderer = WebGLRenderer()

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

width = 10
height = 10
widthSegments = 1
heightSegments = 1
plane = PlaneGeometry(width, height, widthSegments, heightSegments)

print repr(plane)
print "width:          " + str(plane.width)
print "height:         " + str(plane.height)
print "widthSegments:  " + str(plane.widthSegments)
print "heightSegments: " + str(plane.heightSegments)
print plane

mesh = Mesh(plane, MeshNormalMaterial({"wireframe":True}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 10000
startTime =  None
movement = Vector3(0.02, 0.02, 0.02)

def render():
    mesh.rotation.add(movement)
        
    renderer.render(scene, camera)

def onWindowResize():
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.size = (window.innerWidth, window.innerHeight)
    
def step(timestamp):
    global requestID, progress, startTime
    if (startTime):
        progress = timestamp - startTime
    else:
        if (timestamp):
            startTime = timestamp
        else:
            progress = 0
        
    if (progress < progressEnd):
        requestID = window.requestAnimationFrame(step)
        render()
    else:
        window.cancelAnimationFrame(requestID)
        # container.removeChild(renderer.domElement)

window.addEventListener("resize", onWindowResize, False)

onWindowResize()

step(None)