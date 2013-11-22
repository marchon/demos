from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *

e1 = VectorE3(1.0, 0.0, 0.0, False)
e2 = VectorE3(0.0, 1.0, 0.0, False)
e3 = VectorE3(0.0, 0.0, 1.0, False)

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text("Drag to spin the qubit. Hit Esc key to exit.", font, "black")
output.x = 100
output.y = 60
space2D.addChild(output)

txtSpinor = Text("", font, "black")
txtSpinor.x = 100
txtSpinor.y = 120
space2D.addChild(txtSpinor)

timeOut = 6000.0

mouseX = 0
mouseXOnMouseDown = 0
targetRotation = 0
targetRotationOnMouseDown = 0
isShiftDown = False
isCtrlDown = False

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.x = 2
camera.position.y = 0
camera.position.z = 1.5

scene = CartesianSpace().scene

geometry = CubeGeometry(1.0, 1.0, 1.0)
faces = geometry.faces
faces[0].color.setHex(0xFF0000)
faces[1].color.setHex(0xFF0000)
faces[2].color.setHex(0x00FFFF)
faces[3].color.setHex(0x00FFFF)
faces[4].color.setHex(0x00FF00)
faces[5].color.setHex(0x00FF00)
faces[6].color.setHex(0xFF00FF)
faces[7].color.setHex(0xFF00FF)
faces[8].color.setHex(0x0000FF)
faces[9].color.setHex(0x0000FF)
faces[10].color.setHex(0xFFFF00)
faces[11].color.setHex(0xFFFF00)
    
material = MeshBasicMaterial({"vertexColors": FaceColors, "overdraw": 0.5})
cube = Mesh(geometry, material)
scene.add(cube)

camera.up = e3
camera.lookAt(cube.position)

renderer = CanvasRenderer()

workbench = Workbench(renderer, camera)

def shiftKey(event, downFlag):
    global isShiftDown
    isShiftDown = downFlag

def ctrlKey(event, downFlag):
    global isCtrlDown
    isCtrlDown = downFlag
    
def escKey(event, downFlag):
    event.preventDefault()
    global timeOut
    timeOut = 0

keyHandlers = {
 16: shiftKey,
 17: ctrlKey, 
 27: escKey
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except:
        pass

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, False)
    except:
        pass

def onDocumentMouseDown(event):
    global mouseXOnMouseDown, targetRotationOnMouseDown

    event.preventDefault()

    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mouseup", onDocumentMouseUp, False)
    document.addEventListener("mouseout", onDocumentMouseOut, False)

    mouseXOnMouseDown = event.clientX - (float(window.innerWidth) / 2.0)
    targetRotationOnMouseDown = targetRotation
    
def onDocumentMouseMove(event):
    global mouseX, targetRotation

    mouseX = event.clientX - (float(window.innerWidth) / 2.0)
    targetRotation = targetRotationOnMouseDown + (mouseX - mouseXOnMouseDown) * 0.02

def onDocumentMouseUp(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)

def onDocumentMouseOut(event):
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup", onDocumentMouseUp, False)
    document.removeEventListener("mouseout", onDocumentMouseOut, False)

def onDocumentTouchStart(event):
    global mouseXOnMouseDown, targetRotationOnMouseDown

    if len(event.touches) == 1:
        event.preventDefault()

        mouseXOnMouseDown = event.touches[0].pageX - (float(window.innerWidth) / 2.0)
        targetRotationOnMouseDown = targetRotation
        
def onDocumentTouchMove(event):
    global mouseX, targetRotation

    if len(event.touches) == 1:
        event.preventDefault()

        mouseX = event.touches[0].pageX - (float(window.innerWidth) / 2.0)
        targetRotation = targetRotationOnMouseDown + (mouseX - mouseXOnMouseDown) * 0.05

def tick(t):


    cube.rotation.z += (targetRotation - cube.rotation.z) * 0.05
    txtSpinor.text = cube.attitude

    renderer.render(scene, camera)
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown", onDocumentKeyDown, False)
    document.addEventListener("keyup", onDocumentKeyUp, False)
    document.addEventListener("touchstart", onDocumentTouchStart, False)
    document.addEventListener("touchmove", onDocumentTouchMove, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("touchstart", onDocumentTouchStart, False)
    document.removeEventListener("touchmove", onDocumentTouchMove, False)
    document.removeEventListener("keyup", onDocumentKeyUp, False)
    document.removeEventListener("keydown", onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
