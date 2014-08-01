from math import *

def T(D, F, R, alpha, N):
    f = F/R
    arg = D * (D - 2* alpha) + f * (f - 2 * N)
    return D - f - sqrt(arg)

D = 8
R = 1700.0
alpha = 2
N = 2

print "Fee versus Time"
for F in range(-1000, 2500, 100):
    print F, T(D, F, R, alpha, N)
