import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fftpack import fft

plt.close('all')
# Definição sinais
t = np.linspace(0, 2, num=20000)
sig1 = np.sin(2*np.pi*5*t)+np.sin(2*np.pi*6*t)
plt.figure(0)
plt.plot(t,sig1)
plt.grid()
sig2 = np.sin(2*np.pi*4*t)+np.sin(2*np.pi*7*t)
plt.figure(1)
plt.plot(t,sig2)
plt.grid()
port1 = np.sin(2*np.pi*1000*t)
port2 = np.sin(2*np.pi*3000*t)

#%% Modulação
mu = 0.4
tamV = len(t)
sig1M = np.multiply((np.ones(tamV)+mu*sig1),port1)
plt.figure(2)
plt.plot(t,sig1M)
plt.grid()
sig2M = np.multiply((np.ones(tamV)+mu*sig2),port2)
plt.figure(3)
plt.plot(t,sig2M)
plt.grid()

#%% Sinal a ser transmitido
sigT = sig1M+sig2M
plt.figure(4)
plt.plot(t,sigT)
plt.grid()

#%% Demodulação: Part 1
Nf = 2 #ordem do filtro
Wc = [2*np.pi*800, 2*np.pi*1200]
num, den = signal.butter(Nf, Wc, 'bandpass', analog=True)
Filt1 = signal.TransferFunction(num,den)
w, mag, phase = signal.bode(Filt1)
plt.figure(5)
plt.semilogx(w, mag)
tout, yout, xout = signal.lsim((num, den), U=sigT, T=t)
plt.figure(6)
plt.plot(tout, yout)

#%% Demodulação: Parte 2
for i in range(tamV):
    if (yout[i]>=0):
        yout[i] = yout[i]
    else:
        yout[i] = 0

Nf = 2 #ordem do filtro
Wc = 2*np.pi*10
num, den = signal.butter(Nf, Wc, 'low', analog=True)
tout1, yout1, xout1 = signal.lsim((num, den), U=yout, T=t)
plt.figure(7)
plt.plot(t,yout1)
plt.grid()