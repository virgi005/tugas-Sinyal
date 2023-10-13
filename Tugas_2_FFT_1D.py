# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 19:27:34 2023

@author: virgi
"""

import numpy as np
import matplotlib.pyplot as plt

print ('Virgiawan Ibrahim')
print ('5009211008')

# Fungsi sinyal kotak
def kotak(t, T):
    return 2 * ((t < T / 2) & (t > -T / 2))

# Fungsi transformasi Fourier
def FFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

# Inisialisasi
T = 3
t = np.linspace(-5, 5, 1000)

# Sinyal kotak pertama
x1 = kotak(t, 1)
X1 = FFT(x1)

# Sinyal kotak kedua
x2 = kotak(t, 0.5)
X2 = FFT(x2)

# Sinyal kotak ketiga
x3 = np.zeros_like(t)
x3[(t < 3) & (t > -3)] = 2
X3 = FFT(x3)

# Plot sinyal
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
plt.plot(t, x1, 'r')
plt.title('Sinyal Kotak 1')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 2)
freq1 = np.fft.fftfreq(len(X1), d=1)
plt.plot(freq1, np.abs(X1), 'r')
plt.title('Transformasi Fourier 1')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 3)
plt.plot(t, x2, 'g')
plt.title('Sinyal Kotak 2')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 4)
freq2 = np.fft.fftfreq(len(X2), d=1)
plt.plot(freq2, np.abs(X2), 'g')
plt.title('Transformasi Fourier 2')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 5)
plt.plot(t, x3, 'b')
plt.title('Sinyal Kotak 3')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(3, 2, 6)
freq3 = np.fft.fftfreq(len(X3), d=1)
plt.plot(freq3, np.abs(X3), 'b')
plt.title('Transformasi Fourier 3')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
