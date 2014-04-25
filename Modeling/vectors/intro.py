from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *

JXG = window.JXG
JXG.Options.text.useMathJax = True
graph = JXG.JSXGraph

board = graph.initBoard("box", 
                    {"boundingbox": [-2,2,2,-2],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(1,0)
b = VectorE2(0,1)

def toString(mv):
    return "\\[ a_x=%0.3f, a_y=%0.3f \\]" % (mv.x, mv.y)

def Arrow(strokeColor):
    tail = board.create('point',[0,0], {'name':'','size':5,'fillOpacity':0.3,'strokeOpacity':0.3, 'strokeColor':strokeColor, 'fillColor':strokeColor})
    head = board.create('point',[a.x,a.y], {'name':'','size':5,'fillOpacity':0.3,'strokeOpacity':0.3, 'strokeColor':strokeColor})
    return board.create('arrow',[tail,head],{'strokeWidth':5, 'strokeOpacity':0.7, 'strokeColor':strokeColor});

txt = board.create('text',[-1.5,+1.5, lambda: toString(a)], {'fontSize':30, 'strokeColor':'red'})

def tick():
    # Modify the vector to track the User Interface.
    a.x = head.X() - tail.X()
    a.y = head.Y() - tail.Y()

def terminate():
    pass

def setUp():
    A = Arrow('blue')
    print "Press Esc to terminate."

def tearDown():
    print "Goodbye!"
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
