# MeshBasicMaterial demonstration.
from three import *
from browser import *
from math import pi

for canvas in document.getElementsByTagName("canvas"):
    canvas.parentNode.removeChild(canvas)

scene = Scene()

camera = PerspectiveCamera(75, 1.0, 0.1, 1000)
camera.position.z = 100

renderer = WebGLRenderer()
renderer.autoClear = True
renderer.gammaInput = True
renderer.gammaOutput = True
renderer.setClearColor(Color(0x080808), 1.0)

container = document.getElementById("canvas-container")
container.appendChild(renderer.domElement)

material = MeshBasicMaterial({"color":0x00FF00, "wireframe":True})
material.wireframeLinewidth = 1
material.name = "greenie"

print "repr(material) => " + repr(material)
print "id: " + str(material.id)
print "uuid: " + material.uuid
print "name: " + material.name
print "color: " + str(material.color)
print "needsUpdate: " + str(material.needsUpdate)
print "opacity: " + str(material.opacity)
print "overdraw: " + str(material.overdraw)
print "transparent: " + str(material.transparent)
print "visible: " + str(material.visible)
print "wireframe: " + str(material.wireframe)
print "wireframeLinewidth: " + str(material.wireframeLinewidth)
print "str(material) => " + str(material)

mesh = Mesh(SphereGeometry(50, 32, 24), material)

scene.add(mesh)

requestID = None
progress = None
progressEnd = 6000
startTime = None

def render():
    mesh.rotation.x = mesh.rotation.x + 0.02
    mesh.rotation.y = mesh.rotation.y + 0.02
    mesh.rotation.z = mesh.rotation.z + 0.02
        
    renderer.render(scene, camera)

def onWindowResize(event):
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

onWindowResize(None)

step(None)