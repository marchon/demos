from e2ga import *
from units import *
import numpy as np
from browser import *
from math import *

JXG = window.JXG
graph = JXG.JSXGraph

board = graph.initBoard("box", 
                    {"boundingbox": [-2,2,2,-2],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

a = VectorE2(1,1)

tail = board.create('point',[0,0], {'name':'A'})
head = board.create('point',[a.x,a.y], {'name':'B'})

line = board.create('line',[tail,head], 
 {'straightFirst':False, 'straightLast':False,'lastArrow':True})

txt = board.create('text',[-1.5,+1.5, lambda: str(a)], {'fontSize':30})

def moveHandler():
    print "moved"
    
head.on('mousedown', moveHandler)

def tick():
    print head 
    pass

def terminate():
    pass

def setUp():
    print "Press Esc to terminate."
    pass

def tearDown():
    pass

WindowAnimationRunner(tick, terminate, setUp, tearDown).start()
