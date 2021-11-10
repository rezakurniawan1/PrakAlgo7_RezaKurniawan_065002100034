# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 08:35:13 2021

@author: RezaKurniawan
"""

print('--PROGRAM MENCARI NILAI FAKTORIAL SEBUAH ANGKA--')

def faktorial(n):
	hasil = 1
	for x in range(n, 0, -1):
		hasil = hasil * x
	print(f"Nilai faktorialnya adalah {hasil}")
	
n = int(input('Masukkan nilai n: '))
faktorial(n)