import numpy as np
import math
import time 
import matplotlib.pyplot as plt
from scipy import optimize
def DFT_matrix(N):
	W=np.ones((N,N),dtype="complex")
	omega = np.exp( - 2 *np.pi * 1J / N )
	for i in range(N):
		for j in range(N):
			W[i][j]=np.exp(-2*np.pi*1J*i*j/N)
	return W
def createx(N):
	return np.random.random((N,1))
with open("dftmat.dat","w") as f1:
	i=2
	while i<10000:
		start=time.time()
		X=np.dot(DFT_matrix(i),createx(i))
		f1.write(f"{time.time()-start}\n")
		i=i*2
	
