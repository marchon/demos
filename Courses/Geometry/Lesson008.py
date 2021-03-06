'''
A linear space, V, is a set endowed with a rule for addition.
If f and g are in V, then so is f + g.
There is also a rule for scalar mutiplication.
If f is in V and k is a scalar, then kf is in V.
For al f,g,h in V and c,k scalars, the set also satisfies the following rules:
1. (f + g) + h = f + (g + h)
2. f + g = g + f
3. There exists a neutral element n in V such that f + n = f, for all f in V.
This n is unique and denoted by 0.
4. For each f in V there exists a g in V such that f + g = 0. This g is unique and denoted by (-f).
5. k(f + g) = kf + kg
6 (c + k)f = cf + kf
'''
class Euclidean:
    def __init__(self, w, x, y):
        if isinstance(w, float):
            self.w = w
        else:
            raise AssertionError("w must be a float")
        if isinstance(x, float):
            self.x = x
        else:
            raise AssertionError("x must be a float")
        if isinstance(y, float):
            self.y = y
        else:
            raise AssertionError("y must be a float")
            
    def __add__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Euclidean(self.w + other.w, self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Euclidean(self.w - other.w, self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Euclidean):
            raise AssertionError("other must be a Euclidean")
        return Vector(self.w * other.x, self.w * other.y)

    def __rmul__(self, other):
        if not isinstance(other, float):
            raise AssertionError("other must be a Euclidean or float")
        return Vector(other * self.x, other * self.y)
    
    def __neg__(self):
        # Workaround for a bug requiring a cast to float.
        return Vector(float(-self.x), float(-self.y))

    def __eq__(self, other):
        if not isinstance(other, Euclidean):
            return False
        return self.w == other.w and self.x == other.x and self.y == other.y
    
    def __str__(self):
        parts = []
        if self.w != 0.0:
            parts.append(str(self.w))
        if self.x != 0.0 or self.y != 0.0:
            parts.append(" + ".join([str(self.x)+" * i", str(self.y)+" * j"]))
        if len(parts) > 0:
            return "+".join(parts)
        else:
            return "0"
    
    def __repr__(self):
        parts = []
        if self.w != 0.0:
            parts.append("Scalar(" + str(self.w) + ")")
        if self.x != 0.0 or self.y != 0.0:
            parts.append("Vector(" + ", ".join([str(self.x), str(self.y)]) + ")")
        if len(parts) > 0:
            return "+".join(parts)
        else:
            return "0"

def Vector(x, y):
    return Euclidean(0.0, x, y)

def Scalar(w):
    return Euclidean(w, 0.0, 0.0)

f = Vector(1.0, 2.0)
c = Scalar(5.0)
k = Scalar(4.0)

print "f => " + str(f)
print "c => " + str(c)
print "k => " + str(k)
print ""
print "(c + k) * f   => " + str((c + k) * f)
print "c * f + k * f => " + str(c * f + k * f)
print ""
print "(c - k) * f   => " + str((c - k) * f)
print "c * f - k * f => " + str(c * f - k * f)
