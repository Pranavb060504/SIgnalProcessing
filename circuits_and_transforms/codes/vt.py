import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
def u(n):
    if n<0:
        return 0.0
    if n>0:
        return 1.0
    if n==0:
        return 0.5
def volta(t):
    return 4/3 *(1-np.exp(-1.5*t*(10**6)))*u(t)
x=np.linspace(-10*10**(-6),10*10**(-6),100)
vec_v=scipy.vectorize(volta)
plt.plot(x,vec_v(x))
plt.xlabel("time")
plt.ylabel("$v_{C_0}(t)$")
plt.grid()
plt.show()
