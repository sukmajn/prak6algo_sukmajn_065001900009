# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:00:47 2021

@author: Sukma Julia Nada
"""

while True:
    print("KALKULATOR LUAS PERMUKAAN BANGUN RUANG")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")
    print("6. Exit")
    menu = input("Pilih menu yang tersedia : ")
    if menu == "1":
        rusuk = int(input("Masukan nilai rusuk : "))
        print("Luas Permukaan Kubus dengan rusuk "+str(rusuk)+" adalah "+str(rusuk*rusuk*6)+"\n")
    elif menu == "2":
        p = int(input("Masukan nilai panjang : "))
        l = int(input("Masukan nilai lebar : "))
        t = int(input("Masukan nilai tinggi : "))
        print("Luas Permukaan Balok dengan panjang "+str(p)+", lebar "+str(l)+", & tinggi "+str(t)+" adalah "+str(2*((p*l)+(p*t)+(l*t)))+"\n")
    elif menu == "3":
        r = int(input("Masukan nilai jari-jari : "))
        t = int(input("Masukan nilai tinggi : "))
        print("Luas Permukaan Tabung dengan jari-jari "+str(r)+" & tinggi "+str(t)+" adalah "+str((2*r*r*22/7)+(2*r*22/7*t))+"\n")
    elif menu == "4":
        r = int(input("Masukan nilai jari-jari : "))
        s = int(input("Masukan nilai garis lukis : "))
        print("Luas Permukaan Kerucut dengan jari-jari "+str(r)+" & garis lukis "+str(s)+" adalah "+str(22/7*r*(r+s))+"\n")
    elif menu == "5":
        r = int(input("Masukan nilai jari-jari : "))
        print("Luas Permukaan Kerucut dengan jari-jari "+str(r)+" adalah "+str(22/7*4*r*r)+"\n")
    elif menu == "6":
        exit("TERIMA KASIH")
    else:
        print("Pilihan salah!")