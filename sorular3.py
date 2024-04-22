# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:16:53 2024

@author: Şenol AKDENİZ
"""

sekil = int(input("""Kare : 1
Dikdortgen : 2
Ucgen : 3 
Daire : 4
                     
Lutfen Cevresini ve Alanini Hesaplamak Istediginiz Sekli Seciniz : """))

def kare(x):
    kareAlan = x**2
    kareCevre = 4*x
    print("Karenin Alani : ", kareAlan, "Karenin Cevresi : ", kareCevre)

def dikdortgen(x,y):
    dikdortgenAlan = x*y
    dikdortgenCevre = (x+y)*2
    print("Dikdortgenin Alani : ", dikdortgenAlan, "Dikdortgenin Cevresi : ",dikdortgenCevre)
    
def ucgen(x,y,z):
    ucgenAlan = (x+y+z)/2
    ucgenCevre = x+y+z
    print("Ucgenin Alani : ", ucgenAlan, "Ucgenin Cevresi : ", ucgenCevre)

def daire(x):
    daireAlan = 3.14*(x**2)
    daireCevre = 2*3.14*x
    print("Dairenin Alani : ", daireAlan, "Dairenin Cevresi : ", daireCevre)
    
    
    
if(sekil==1):
    kareKenar = int(input("Bir kenar uzunluğu giriniz. : "))
    kare(kareKenar)
    
elif(sekil==2):
    dd_kisaKenar = int(input("Bir kenar uzunluğu giriniz. : "))
    dd_uzunKenar = int(input("Bir kenar uzunluğu giriniz. : "))
    dikdortgen(dd_kisaKenar, dd_uzunKenar)
    
elif(sekil==3):
    ucgenKenar1 = int(input("Bir kenar uzunluğu giriniz. : "))
    ucgenKenar2 = int(input("Bir kenar uzunluğu giriniz. : "))
    ucgenKenar3 = int(input("Bir kenar uzunluğu giriniz. : "))
    ucgen(ucgenKenar1, ucgenKenar2, ucgenKenar3)
    
elif(sekil==4):
    yaricap = int(input("Bir yarıcap uzunluğu giriniz. : "))
    daire(yaricap)
else:
    print("Gecersiz Sekil Girdiniz..!")