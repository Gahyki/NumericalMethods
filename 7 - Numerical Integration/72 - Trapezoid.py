import numpy as np
upper = 5.8
lower = 1.7
m = 5

def f(x):
    return (np.e**(-1.5*x**2))

def trapezoid():
    return (upper-lower)*(f(upper) + f(lower))/2

print("point: " + '{0:.16f}'.format(trapezoid()))

def comp(x):
    total = 0
    tu = (upper-lower)/x + lower
    tl = lower
    while tu <= upper:
        tr = (tu - tl)*(f(tu) + f(tl))/2
        total += tr
        tu += (upper-lower)/x
        tl += (upper-lower)/x
    return total

print("comp: " + '{0:.16f}'.format(comp(m)))
