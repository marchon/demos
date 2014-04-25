from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *
from random import random

JXG = window.JXG
JXG.Options.text.useMathJax = True
graph = JXG.JSXGraph

board = graph.initBoard("box", 
                    {"boundingbox": [-100,100,100,-100],
                     "axis":False,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(10,0)
b = VectorE2(0,10)
c = a + b
A = None
B = None
C = None

def toString(mv):
    return "\\[ a_x=%0.3f, a_y=%0.3f \\]" % (mv.x, mv.y)

def Arrow(vector, x, y, color):
    pointDef = {'name':'',
                'size':5,
                'fillOpacity':0.3,
                'strokeOpacity':0.3,
                'strokeColor':'gray',
                'fillColor':'gray',
                'snapToGrid':True}
    tail = board.create('point',[random()*50, random()*50], pointDef)
    head = board.create('point',[tail.X() + vector.x, tail.Y() + vector.y], pointDef)
    txt = board.create('text',[x, y, lambda: toString(vector)], {'fontSize':20, 'strokeColor':color,'fixed':True})
    return board.create('arrow',[tail,head],{'strokeWidth':5, 'strokeOpacity':0.7, 'strokeColor':color});


def tick():
    # Modify the vector to track the User Interface.
    a.x = A.point1.X() - A.point2.X()
    a.y = A.point1.Y() - A.point2.Y()

def terminate():
    pass

def setUp():
    global A
    A = Arrow(a, -100, -50, 'red')
    B = Arrow(b, -100, -60, 'blue')
    C = Arrow(c, -100, -70, 'green')
    print "Press Esc to terminate."

def tearDown():
    print "Goodbye!"
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
