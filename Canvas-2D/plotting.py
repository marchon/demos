from browser import *
from workbench import *
from math import *
from units import *
from e3ga import *
from easel import *
from eight import *

glwin = window.open("","","width=800,height=600")
glwin.document.body.style.backgroundColor = "202020"
glwin.document.body.style.overflow = "hidden"
glwin.document.title = "Visualizing Geometric Algebra with WebGL"

canvas2D = glwin.document.createElement("canvas")
canvas2D.style.position = "absolute"
canvas2D.style.top = "0px"
canvas2D.style.left = "0px"
workbench2D = Workbench2D(canvas2D, glwin)
space2D = Stage(canvas2D)
space2D.autoClear = True

font = "20px Helvetica"

output = Text(glwin.document.title + ". Hit Esc key to exit.", font, "white")
output.x = 100
output.y = 60
space2D.addChild(output)

stats = window.Stats()
stats.setMode(0)
stats.domElement.style.position = 'absolute'
stats.domElement.style.left = '0px'
stats.domElement.style.top = '0px'
glwin.document.body.appendChild(stats.domElement)

def setUp():
    workbench2D.setUp()

def tick(t):
    stats.begin()
    space2D.render()
    stats.end()

def terminate(t):
    return False

def tearDown(e):
    glwin.close()
    if e:
        print "Error during animation: %s" % (e)
    else:
        print "Goodbye!"
    workbench2D.tearDown()
    scene.tearDown()

runner = windowAnimationRunner(tick, terminate, setUp, tearDown, glwin)

runner.start()
