import numpy as np
from scipy.fft import fft,ifft
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,2,1])
N=15
xk=[]
for k in range(15):
    c=0
    for i  in range(len(x)):
        c=c+x[i]*np.exp(-1j*2*np.pi*i*k/N)
    xk.append(c)
xk=np.array(xk)
def hn(n):
    if n<0:
        return 0
    if 0<=n<2:
       return (-1/2)**n
    else:
        return (-1/2)**n+(-1/2)**(n-2)
hk=[]
for k in range(15):
    d=0
    for z in range(15):
        d=d+hn(z)*np.exp(-1j*2*np.pi*z*k/N)
    hk.append(d)
hk=np.array(hk)
yk=xk*hk
yn=0
for i in range(len(yk)):
    yn=yn+yk[i]*np.exp(-1j*2*np.pi*i*k/N)
yn=yn/N
#computing the above using fft and ifft
xk1=fft(x)
htemp=np.array([hn(i) for i in range(N)])
hk1=fft(htemp)
c=[]
for q in range(15):
    if q<6:
        c1=xk1[q]*hk1[q]
    else:
        c1=0
    c+=[c1]
yn1=ifft(c)
ntemp=np.array(list(range(N)))
plt.subplot(211)
plt.plot(ntemp,yk,label="DFT")
plt.grid()
plt.legend()
plt.subplot(212)
plt.plot(ntemp,c,label="IFFT")
plt.grid()
plt.legend()
plt.show()
