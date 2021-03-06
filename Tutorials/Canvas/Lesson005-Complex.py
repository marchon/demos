class Complex:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def mod(self):
    return sqrt(self.x * self.x + self.y * self.y)

  def arg(self):
    return atan2(self.y, self.x)

  def __add__(self, other):
    return Complex(this.x + that.x, this.y + that.y)

  def __sub__(self, other):
    return Complex(this.x - that.x, this.y - that.y)

  def __mul__(self, other):
    return Complex(this.x * that.x - this.y * that.y, this.x * that.y + this.y * that.x)

  def __div__(self, other):
    denom = that.x * that.x + that.y * that.y;
    return Complex((this.x * that.x + this.y * that.y)/denom, (this.y * that.x - this.x * that.y)/denom)

  def __repr__(self):
    return "Complex(" + str(self.x) + ", " + str(self.y) + ")"

  def __str__(self):
    return str(self.x) + "+" + str(self.y) + "i"

one = Complex(1.0,0.0)

print one.x
print one.y
print one
print str(one)
print repr(one)