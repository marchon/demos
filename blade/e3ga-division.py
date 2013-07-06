from eight import *
from math import random, floor

def showValue(name, m):
    print name + " => " + str(m)
    return m

def ri():
    return floor(100*random())

def cliffordConjugate(A):
    return Euclidean3(A.w, -A.x, -A.y, -A.z, -A.xy, -A.yz, -A.zx, A.xyz)

def gradeInvolution(A):
    return Euclidean3(A.w, -A.x, -A.y, -A.z, A.xy, A.yz, A.zx, -A.xyz)

def inverse(M):
    r = ~M
    m = M * r
    s = r * cliffordConjugate(m)
    k = (M * s).w
    return Euclidean2(s.w/k, s.x/k, s.y/k, s.z/k, s.xy/k, s.yz/k, s.zx/k, s.xyz/k)

A = Euclidean3(ri(),ri(),ri(),ri(),ri(),ri(),ri(),ri())

showValue("A", A)

showValue("inverse(A)", inverse(A))

showValue("A * inverse(A)", A * inverse(A))
