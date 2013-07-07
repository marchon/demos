# CircleGeometry.py
from eight import *
from browser import *
from math import pi

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera  = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

radius = 50
segments = 32
thetaStart = 0
thetaLength = 2 * pi
circle = CircleGeometry(radius, segments, thetaStart, thetaLength)

mesh = Mesh(circle, MeshNormalMaterial({"wireframe":True, "wireframeLinewidth":3}))
scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
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