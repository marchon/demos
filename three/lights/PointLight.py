# PointLight.py
from three import *

light = PointLight(0xff0000, 1, 100)

print light
print str(light)
print repr(light)
print type(light)
print str(type(light))
print repr(type(light))
print "color:" + str(light.color)
print "intensity:" + str(light.intensity)
print "distance:" + str(light.distance)
print "position:" + str(light.position)
print "rotation:" + str(light.rotation)

light.color = 0x00FF00
light.intensity = 0.5
light.distance = 200

light.position.x = 1
light.position.y = 2
light.position.z = 3

light.rotation.x = 4
light.rotation.y = 5
light.rotation.z = 6
print "color:" + str(light.color)
print "intensity:" + str(light.intensity)
print "distance:" + str(light.distance)
print "position:" + str(light.position)
print "rotation:" + str(light.rotation)

r = Vector3(2,2,2)
print r
print str(r)
print repr(r)
light.position = r
print "position:" + str(light.position)


