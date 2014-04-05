from browser import window

BLADE = window.BLADE

third = BLADE.Rational(1,3)
print third

v = BLADE.Euclidean2(1,2,3,4)
w = BLADE.Euclidean2(1,1,1,1)

print v.w, v.x, v.y, v.xy
print str(v)
print repr(v)

z = v.add(w)
print z
print z.grade(1)
# TODO: Possibility of converting arithmetic operators into method calls?
z = v + w
