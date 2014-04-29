from units import *
from e3ga import *

e1 = VectorE3(1,0,0)
e2 = VectorE3(0,1,0)

print "e1 => %s" % e1
print "e2 => %s" % e2

x = VectorE3(3,4,12) * meter

print "x => %s" % x
print
print e1 * x.quantity
print e1 * x.uom
print e1 * x
print x * meter
print "..."
print e1 % x.quantity
print e2 % x.uom
print e1 % x