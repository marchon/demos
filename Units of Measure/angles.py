from units import *
from math import *
from e3ga import *
from e2ga import *

angle1 = pi
angle2 = ScalarE3(pi)
angle3 = ScalarE2(180) * pi / 180

print angle1
print angle2
print angle3
print
print "cos(angle1) %s" % cos(angle1)
print "cos(angle2) %s" % cos(angle2)
print "cos(angle3) %s" % cos(angle3)
print
print "sin(angle1) %s" % sin(angle1)
print "sin(angle2) %s" % sin(angle2)
print "sin(angle3) %s" % sin(angle3)
print
print "tan(angle1) %s" % tan(angle1)
print "tan(angle2) %s" % tan(angle2)
print "tan(angle3) %s" % tan(angle3)
print
print angle1 + angle1
print angle1 + angle2
print angle1 + angle3
print
print cos(sqrt(angle1 * angle1))
print cos(sqrt(angle2 * angle2))
print cos(sqrt(angle3 * angle3))
print
print acos(cos(angle1))
print acos(cos(angle2))
print acos(cos(angle3))
print
print asin(sin(angle1))
print asin(sin(angle2))
print asin(sin(angle3))
print
print atan(tan(angle1))
print atan(tan(angle2))
print atan(tan(angle3))