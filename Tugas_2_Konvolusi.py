# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:17:53 2023

@author: virgi
"""
print ('Virgiawan Ibrahim')
print ('5009211008')
    

import numpy as np

# panjang sinyal dan panjang kernel
def convolv(sinyal, kernel):
    panjang_sinyal = len(sinyal)
    panjang_kernel = len(kernel)

# panjang konvolusi nya
    panjang_hasil = panjang_sinyal + panjang_kernel - 1
    hasil_manual = [0] * panjang_hasil

# fungsi konvolusi nya
    for i in range(panjang_sinyal):
        for j in range(panjang_kernel):
            hasil_manual[i + j] += sinyal[i] * kernel[j]

    return hasil_manual


sinyal = [0, 1, 2, 3, 4, 5, 6]
kernel = [0, 1, 2, 3]

hasil_manual = convolv(sinyal, kernel)
hasil_numpy = np.convolve(sinyal, kernel).tolist()

print("Konvolusi Manual:", hasil_manual)
print("Konvolusi NumPy:", hasil_numpy)


