'''
The first thing we will do is create a linear space, axiom by axiom.
Our space will have two kinds of elements we call vectors and scalars.
With an eye to creating a unified geometric space, the underlying object is a Euclidean.
'''
class Euclidean:
    def __init__(self):
        pass
    
    def __repr__(self):
        return "Euclidean()"

def Vector():
    return Euclidean()

def Scalar():
    return Euclidean()

f = Vector()
g = Vector()
k = Scalar()

# It's not possible to distinguish scalars from vectors yet.
print "f : " + repr(f)
print "g : " + repr(g)
print "k : " + repr(k)
