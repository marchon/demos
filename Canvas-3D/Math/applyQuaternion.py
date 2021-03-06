# The Quaternion approach to rotation of vectors.
# The Geometric Algebra approach illuminates the fact that Quaternions are isomorphic to 
# the even sub-algebra of Euclidean 3D space.
from three import *

def showValue(name, m):
    print name + " => " + str(m)
    return m

e1 = Vector3(1, 0, 0)
e2 = Vector3(0, 1, 0)
e3 = Vector3(0, 0, 1)

q0 = Quaternion(0, 0, 0, 1).normalize()
q1 = Quaternion(1, 0, 0, 1).normalize()
q2 = Quaternion(0, 1, 0, 1).normalize()
q3 = Quaternion(0, 0, 1, 1).normalize()

print q0
print q1
print q2
print q3
print ""

es = [e1, e2, e3]
qs = [q0, q1, q2, q3]

for e in es:
    for q in qs:
        showValue(str(e) + " applyQuaternion " + str(q), e.clone().applyQuaternion(q))
    print ""
