# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:46:06 2021

@author: Sukma Julia Nada
"""

print("MENGHITUNG KECEPATAN AKHIR GLBB (diketahui jarak tempuh)")
v0 = int(input("Masukkan v0: "))
a = int(input("Masukkan a: "))
s = int(input("Masukkan s: "))


def vt(kec_awal, percepatan, jarak):
    return (kec_awal ** 2 + (2 * percepatan * jarak)) ** (1 / 2)


vt = vt(v0, a, s)

print("Jarak tempuh jika kecepatan awal:", v0, "percepatan:", a, "dan jarak tempuh:", s, "adalah:", vt)