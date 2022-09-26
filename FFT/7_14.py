# Plotting the running times of FFT/IFFT and convolution
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

fft_times = np.loadtxt('fftt.dat', dtype=float)
conv_times = np.loadtxt('convtt.dat', dtype=float)
dftmat_times=np.loadtxt('dftmat.dat',dtype=float)
N = np.logspace(1, len(fft_times), num=len(fft_times), base=2)

fft_fit = optimize.curve_fit(lambda x,a : a*x*np.log(x), N, fft_times)[0]
conv_fit = optimize.curve_fit(lambda x,a : a*x*x, N, conv_times)[0]
dftmat_fit=optimize.curve_fit(lambda x,a : a*x*x, N, dftmat_times)[0]
plt.plot(N, fft_fit * N * np.log(N), label='$O(n \log n)$')
plt.plot(N, conv_fit * N * N, label='$O(n^2)$')
plt.plot(N,dftmat_fit*N*N,label='$O(n^2)-DFT$')
plt.plot(N, fft_times, 'o', label='FFT/IFFT')
plt.plot(N, conv_times, 'o', label='Convolution')
plt.plot(N, dftmat_times, 'o', label='DFTmatrix')
plt.xlabel('input size')
plt.ylabel('Running time')
plt.legend()
plt.grid()
plt.show()
