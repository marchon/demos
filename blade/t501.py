from e2ga import *

def explain(m):
    print str(m) + " is " + repr(m)
    return m

def showValue(name, m):
    print name + " => " + str(m)
    return m

zero  = Euclidean2(0, 0, 0, 0)
one   = Euclidean2(1, 0, 0, 0)
two   = Euclidean2(2, 0, 0, 0)
three = 3
i     = Euclidean2(0, 1, 0, 0)
j     = Euclidean2(0, 0, 1, 0)
I     = Euclidean2(0, 0, 0, 1)

blades = [zero, one, two, three, i, j, I]

sum = one + i + j + I

print "----------"
print "repr"
print "----------"
print repr(zero)
print repr(one)
print repr(two)
print repr(three)
print repr(i)
print repr(j)
print repr(k)
print repr(ij)
print repr(jk)
print repr(ki)
print repr(I)
print "----------"
print "str"
print "----------"
print str(zero)
print str(one)
print str(two)
print str(three)
print str(i)
print str(j)
print str(k)
print str(ij)
print str(jk)
print str(ki)
print str(I)
print "----------"
print "Addition +"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " + " + str(b), a + b)
    print ""
print "----------"
print "Subtraction -"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " - " + str(b), a - b)
    print ""
print "----------"
print "Multiplication *"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " * " + str(b), a * b)
    print ""
print "----------"
print "Extension ^"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " ^ " + str(b), a ^ b)
    print ""
print "----------"
print "Left Contraction <<"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " << " + str(b), a << b)
    print ""
print "----------"
print "Right Contraction >>"
print "----------"
for a in blades:
    for b in blades:
        showValue(str(a) + " >> " + str(b), a >> b)
    print ""
