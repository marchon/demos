# Import the browser module in order to make the window variable available.
# It's good practice to make imports explicit rather than using wildcards.
from browser import window, WindowAnimationRunner;

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 800
CANVAS_HEIGHT = 800
CANVAS_WIDTH  = 800

popUp = window.open("","","width=%s, height=%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))
context = None

def tick(t):
    context.fillStyle = "#555555"
    context.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)

def terminate(t):
    return False

def setUp():
    # Let the compiler know that context in this scope is a global variable.
    global context
    popDoc = popUp.document
    canvas = popDoc.createElement("canvas")
    
    canvas.setAttribute("id", "graph")
    canvas.setAttribute("width",  str(CANVAS_WIDTH))
    canvas.setAttribute("height", str(CANVAS_HEIGHT))
    
    popDoc.body.appendChild(canvas)
    popDoc.body.style.margin = "0"
    
    context = canvas.getContext("2d")

def tearDown(e):
    popUp.close()
    if e:
        print e

war = WindowAnimationRunner(tick, terminate, setUp, tearDown, popUp)
war.start()