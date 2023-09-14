# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:24:03 2023

@author: virgi
"""

import numpy as np
import matplotlib.pyplot as plt


print ("Nama : Virgiawan Ibrahim")
print ("NRP  : 5009211008")
# Generate dummy financial data (harga saham)
np.random.seed(0)
stock_price = np.cumsum(np.random.randn(300))  # Data harga saham dummy

# Fungsi untuk menerapkan filter moving average
def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    return np.convolve(data, weights, 'valid')

# Tentukan ukuran jendela (window size) untuk moving average
window_size = 10

# Terapkan filter moving average pada data harga saham
filtered_price = moving_average(stock_price, window_size)

# Plot data asli dan data yang telah difilter
plt.figure(figsize=(12, 6))
plt.plot(stock_price, label='Harga Saham Asli', color='blue', alpha=0.5)
plt.plot(filtered_price, label=f'Moving Average ({window_size}-point)', color='red')
plt.xlabel('Waktu')
plt.ylabel('Harga Saham')
plt.title('Filtering Harga Saham Menggunakan Moving Average')
plt.legend()
plt.grid(True)
plt.show()
