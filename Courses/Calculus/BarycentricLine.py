from e3ga import *

i = VectorE3(1,0,0)
j = VectorE3(0,1,0)
k = VectorE3(0,0,1)

a1 = i + j
a2 = 3 * i + 4 * j

t1 = 0.6
t2 = 0.4

a = t1 * a1 + t2 * a2

print a
