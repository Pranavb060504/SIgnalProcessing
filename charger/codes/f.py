import numpy as np
import scipy 
import matplotlib.pyplot as plt
import math
def modsin(x):
    return 12*abs(math.sin(2*math.pi*50*x))
def a(x):
    if x==0:
        return 24/math.pi
    if x%2==0 and x>=1:
        return 48/(math.pi*(1-x**2))
    else:
        return 0.0
def Cn(x):
    if x<0:
        x=x*-1
    if x%2==0:
        return 24/(math.pi*(1-x**2))
    else:
        return 0.0
def fou1(x):
    z=x
    f=50
    y=np.linspace(-1000,1000,2001)
    vec_c=scipy.vectorize(Cn)
    def cex(k):
        return np.exp(1j*2*math.pi*f*k*z)
    vec_exp=scipy.vectorize(cex)
    return np.dot(vec_c(y),cex(y))
def fou(x):
    z=x
    f=50
    y=np.linspace(1,1000,1000)
    vec_a=scipy.vectorize(a)
    def cosi(k):
        if k==0:
            return 0.0
        else:
            return np.cos(2*math.pi*f*k*z)
    vec_cos=scipy.vectorize(cosi)
    return 24/math.pi +np.dot(vec_a(y),vec_cos(y))

x=np.linspace(-4,4,200)
vec_modsin=scipy.vectorize(modsin)
vec_fou=scipy.vectorize(fou)
vec_exc=scipy.vectorize(fou1)
#1.1
plt.plot(x,vec_modsin(x),label='theory')
#2.3
plt.plot(x,vec_exc(x),'.',label='simulation')
#2.6
#plt.plot(x,vec_fou(x),'.',label='simulation')
plt.legend()
plt.grid()
plt.show()

