import numpy as np
import matplotlib.pyplot as plt
import scipy
def h(t):
    return 100*np.sinc(100*t)
def x(t):
    return 12*np.abs(np.sin(2*np.pi*50*t))
def out(x):
    return 5.00
t=100000
vec_h=scipy.vectorize(h)
vec_x=scipy.vectorize(x)
vec_out=scipy.vectorize(out)
z=np.linspace(-1e5,1e5,t)
y=np.convolve(vec_h(z),vec_x(z))
plt.plot((5*np.pi/24)*y*2,label='simulation')
plt.legend()
plt.grid()
plt.show()
