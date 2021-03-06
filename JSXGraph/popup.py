from browser import *
from math import *

graph = window.JXG.JSXGraph

win = window.open("","","width=820,height=820")

link = win.document.createElement("link")
link.rel = "stylesheet"
link.href= "http://fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,400,600"
win.document.head.appendChild(link)

win.document.body.innerHTML = '<div id="box" class="jxgbox"></div>'

div = win.document.getElementById("box")

div.style.width  = "800px"
div.style.height = "800px"
win.document = win.document

board = graph.initBoard("box", {"document":win.document,"axis":True,"grid":True,"showNavigation":False,"showCopyright":False})

A = board.create('point',[1,1],{"name": 'Alice'})
B = board.create('point',[2,2],{"name":'Bob'})

f = board.create('functiongraph',[lambda x,unused: A.X() * sin(x)])

def tick(time):
    angle = time*pi*2/10
    A.moveTo([3 * sin(angle),3 * cos(angle)])

def terminate(time):
    return False

def setUp():
    pass

def tearDown(e):
    win.close()
    if e:
        print e

WindowAnimationRunner(tick, terminate, setUp, tearDown, win).start()
