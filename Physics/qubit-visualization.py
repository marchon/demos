'''
Under Construction. Nov 22, 2013.
'''
from three import *
from easel import *
from browser import *
from workbench import *
from random import random
from math import *
from geometry import *

class SphericalPolar:
    def __init__(self):
        self.theta = 0.0
        self.phi = 0.0
    def __str__(self):
        return "(" + str(self.theta) + ", " + str(self.phi) + ")"

e1 = VectorE3(1.0, 0.0, 0.0, False)
e2 = VectorE3(0.0, 1.0, 0.0, False)
e3 = VectorE3(0.0, 0.0, 1.0, False)
I = e1 ^ e2 ^ e3

coords = SphericalPolar()

canvas2D = document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"
color = "white"

output = Text("Press arrow keys to rotate the qubit. Hit Esc key to exit.", font, "gray")
output.x = 100
output.y = 60
space2D.addChild(output)

txtCoords = Text("", font, color)
txtCoords.x = 100
txtCoords.y = 100
space2D.addChild(txtCoords)

txtSpinor = Text("", font, color)
txtSpinor.x = 100
txtSpinor.y = 120
space2D.addChild(txtSpinor)

txtRotor = Text("", font, color)
txtRotor.x = 100
txtRotor.y = 140
space2D.addChild(txtRotor)

txtBloch = Text("", font, color)
txtBloch.x = 100
txtBloch.y = 160
space2D.addChild(txtBloch)

txtException = Text("", font, "red")
txtException.x = 100
txtException.y = 200
space2D.addChild(txtException)

txtScratch = Text("", font, color)
txtScratch.x = 100
txtScratch.y = 300
space2D.addChild(txtScratch)

timeOut = 6000.0

isShiftDown = False
isCtrlDown = False

camera = PerspectiveCamera(70, 1, 1, 10000)
camera.position.x = 4
camera.position.y = 0
camera.position.z = 0

space3D = CartesianSpace()

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
space3D.add(cube)
cube.position = 2.0 * e2

probeN = ProbeBuilderE3().color(0xFFFFFF).build()
space3D.add(probeN.grade0)
space3D.add(probeN.grade1)
space3D.add(probeN.grade2)
space3D.add(probeN.grade3)
probeN.position = -2.0 * e2

probeR = ProbeBuilderE3().color(0x0000FF).build()
space3D.add(probeR.grade0)
space3D.add(probeR.grade1)
space3D.add(probeR.grade2)
space3D.add(probeR.grade3)

renderer = CanvasRenderer()
renderer.setClearColor(0x777777, 1.0)

workbench = Workbench(space3D.renderer, space3D.camera)

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

def arrowLeft(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.phi -= 1.0
        coords.phi = max(coords.phi, 0.0)

def arrowRight(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.phi += 1.0
        coords.phi = min(coords.phi, 360.0)

def arrowUp(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.theta -= 1.0
        coords.theta = max(coords.theta, 0.0)

def arrowDown(event, downFlag):
    event.preventDefault()
    if downFlag:
        coords.theta += 1.0
        coords.theta = min(coords.theta, 180.0)

keyHandlers = {
 16: shiftKey,
 17: ctrlKey, 
 27: escKey,
 37: arrowLeft,
 38: arrowUp,
 39: arrowRight,
 40: arrowDown
}
    
def onDocumentKeyDown(event):
    try:
        keyHandlers[event.keyCode](event, True)
    except KeyError as keyError:
        pass
    except Exception as e:
        txtException.text = e

def onDocumentKeyUp(event):
    try:
        keyHandlers[event.keyCode](event, False)
    except KeyError as keyError:
        pass
    except Exception as e:
        txtException.text = e
    
def deviceX(clientX):
    return 2.0 * (float(clientX) / float(window.innerWidth)) - 1.0

def deviceY(clientY):
    return 1.0 - 2.0 * (float(clientY) / float(window.innerHeight))

def onDocumentMouseDown(event):
    event.preventDefault()
    
def onDocumentMouseMove(event):
    mouse.x = deviceX(event.clientX)
    mouse.y = deviceY(event.clientY)

def onDocumentMouseUp(event):
    pass

def onDocumentMouseOut(event):
    pass
        
def render(t):
    txtCoords.text = "Spherical polar coordinates (theta, phi):" + str(coords) + " degrees."
    R = exp(- I * e3 * radians(coords.phi) / 2) * exp(- I * e2 * radians(coords.theta) / 2)
    n = R * e3 * ~R
    
    txtRotor.text = "Rotor: " + str(R)
    txtBloch.text = "Bloch sphere unit vector, n = " + str(n) 
    cube.attitude = R
    
    probeR.quantity = R
    probeN.quantity = n
    
    space3D.render()
    space2D.render()
    
def terminate(t):
    return t > timeOut

def setUp():
    workbench.setUp()
    workbench2D.setUp()
    document.addEventListener("keydown",   onDocumentKeyDown, False)
    document.addEventListener("keyup",     onDocumentKeyUp, False)
    document.addEventListener("mousedown", onDocumentMouseDown, False)
    document.addEventListener("mousemove", onDocumentMouseMove, False)
    document.addEventListener("mouseup",   onDocumentMouseUp, False)
    document.addEventListener("mouseout",  onDocumentMouseOut, False)

def tearDown():
    document.removeEventListener("mousedown", onDocumentMouseDown, False)
    document.removeEventListener("mousemove", onDocumentMouseMove, False)
    document.removeEventListener("mouseup",   onDocumentMouseUp, False)
    document.removeEventListener("mouseout",  onDocumentMouseOut, False)
    document.removeEventListener("keyup",     onDocumentKeyUp, False)
    document.removeEventListener("keydown",   onDocumentKeyDown, False)
    workbench2D.tearDown()
    workbench.tearDown()

WindowAnimationRunner(render, terminate, setUp, tearDown).start()
