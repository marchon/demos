import numpy as np

x = np.array(['a','b','c'])
print x[0]
print type(x[0])
print x[1]
print type(x[1])
print x[2]
print type(x[2])

x = np.array([0,1,2,3,4,5,6,7,8,9])
z = x[1:7:2]
print z.size
print z.shape
print z[0]
print z[1]
print z[2]

print ""
x = np.array([[1,2],[3,4],[5,6]])
print x.shape
print x.strides
print "y:"
y = x[0]
print y
print y.shape
print y.size
print y.ndim
print y.strides
print y[0]
print y[1]
