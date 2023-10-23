import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

plt.close('all')
# Estudo auto-correlação de um sinal aleatório qualquer
rng = np.random.default_rng()
t = np.linspace(0,50,100)
sig1 = np.sin(2*np.pi*0.1*t)
sig_noise1 = rng.standard_normal(len(sig1))
sig_noise1  /= np.max(sig_noise1)
sig_noise1 *= 2
sig_noise = sig_noise1+sig1
autcorr = signal.correlate(sig_noise, sig_noise)
autcorr /= np.max(autcorr)
sr = np.std(autcorr)
lags = signal.correlation_lags(sig_noise.size, sig_noise.size, mode="full")
plt.figure(0)
plt.plot(lags,autcorr)
plt.plot(lags,(-1.96*sr)*np.ones(len(lags)),'k--')
plt.plot(lags,(+1.96*sr)*np.ones(len(lags)),'k--')
plt.grid()
plt.figure(1)
plt.plot(t,sig_noise)