from scipy.integrate import quadrature
import math
import numpy as np

v_t = 54 #m/s
g = 9.8 #m/s^s

def velocity(t, v_t):
    return v_t*((1 - np.exp(-2*g*t/v_t))/(1 + np.exp(-2*g*t/v_t)))

dt = .001
i = 0
x = 4000
t = 0

outFile = open("jumpingOut.txt", "w")

while (x > 0):
    t = i*dt
    i += 1
    dx, err = quadrature(velocity, 0, t, args = v_t, tol=1e-06, rtol=1e-06)
    x = 4000 - dx
    outFile.write(str(t) + " " + str(x) + "\n")
    time = np.array([t])
    pos = np.array([x])
print(t)

outFile.close()
