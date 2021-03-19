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

outFile = open("jumpingOutPara.txt", "w")

while (x > 1200):
    t = i*dt
    i += 1
    dx, err = quadrature(velocity, 0, t, args = v_t, tol=1e-06, rtol=1e-06)
    x = 4000 - dx
    outFile.write(str(t) + " " + str(x) + "\n")
    time = np.array([t])
    pos = np.array([x])

dt = .00000065
i = 0 
t1 = t
print(t1)
a = -15.46

while (v_t > 7.6):
    t = t1 + i*dt # timestep changes 
    t2 = i*dt
    v_t = a*t2 + 54
    i += 1
    dx, err = quadrature(velocity, t, t + dt, args = v_t, tol=1e-06, rtol=1e-06)
    x = x - dx
    outFile.write(str(t) + " " + str(x) + "\n")

print(t1)

dt = .001
i = 0
v_t = 7.6 #m/s
xopen1 = x
t3 = t
while (x > 0):
    t = t3 + i*dt # timestep hasn't been constant the whole code
    i += 1
    dx, err = quadrature(velocity, t3, t, args = v_t, tol=1e-06, rtol=1e-06)
    x = xopen1 - dx
    outFile.write(str(t) + " " + str(x) + "\n")

outFile.close()