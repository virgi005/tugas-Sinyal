import numpy as np
import matplotlib.pyplot as plt

print ('Virgiawan Ibrahim')
print ('5009211008')


# Fungsi sinyal kotak 2D
def kotak2D(t1, t2, T):
    return 2 * ((t1 < T / 2) & (t1 > -T / 2) & (t2 < T / 2) & (t2 > -T / 2))

# Fungsi transformasi Fourier 2D
def FFT2D(x):
    return np.fft.fft2(x)

# Inisialisasi
T = 3
t1 = np.linspace(-5, 5, 100)
t2 = np.linspace(-5, 5, 100)
T1, T2 = np.meshgrid(t1, t2)

# Membuat sinyal kotak 2D pertama
x1 = kotak2D(T1, T2, 1)
X1 = FFT2D(x1)

# Membuat sinyal kotak 2D kedua
x2 = kotak2D(T1, T2, 0.5)
X2 = FFT2D(x2)

# Membuat sinyal kotak 2D ketiga
x3 = kotak2D(T1, T2, 3)
X3 = FFT2D(x3)

# Plot sinyal dan hasil transformasi Fourier
plt.figure(figsize=(15, 10))

plt.subplot(3, 2, 1)
plt.imshow(x1, extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Sinyal Kotak 2D - 1')
plt.xlabel('t1')
plt.ylabel('t2')

plt.subplot(3, 2, 2)
plt.imshow(np.abs(X1), extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Hasil Transformasi Fourier 2D - 1')
plt.xlabel('f1')
plt.ylabel('f2')

plt.subplot(3, 2, 3)
plt.imshow(x2, extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Sinyal Kotak 2D - 2')
plt.xlabel('t1')
plt.ylabel('t2')

plt.subplot(3, 2, 4)
plt.imshow(np.abs(X2), extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Hasil Transformasi Fourier 2D - 2')
plt.xlabel('f1')
plt.ylabel('f2')

plt.subplot(3, 2, 5)
plt.imshow(x3, extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Sinyal Kotak 2D - 3')
plt.xlabel('t1')
plt.ylabel('t2')

plt.subplot(3, 2, 6)
plt.imshow(np.abs(X3), extent=[-5, 5, -5, 5], cmap='hot')
plt.colorbar()
plt.title('Hasil Transformasi Fourier 2D - 3')
plt.xlabel('f1')
plt.ylabel('f2')

plt.tight_layout()
plt.show()
