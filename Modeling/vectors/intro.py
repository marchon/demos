from e2ga import *
from units import *
import numpy as np
from browser import window
from math import *

JXG = window.JXG
graph = JXG.JSXGraph

b = graph.initBoard("box", 
                    {"boundingbox": [-10,10,10,-10],
                     "axis":True,
                     "showCopyright":False,
                     "showNavigation":False
                     })

e1 = VectorE2(1,0)

print e1
print e1.x
print e1.y
print repr(e1)
print e1.w
print e1.xy

tail = b.create('point',[0,0], {'name':'A'})
head = b.create('point',[lambda: e1.x,lambda: e1.y], {'name':'B'})

line = b.create('line',[tail,head], 
 {'straightFirst':False, 'straightLast':False,'lastArrow':True, 'strokeWidth':2, 'dash':2})
