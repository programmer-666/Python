"""Fonksiyon tanimlamak ve cagirmak"""
def kare(a):
    return a*a
print(kare(4))
"""
def fonksiyon_adi(argumanlar):
    kod
fonksiyon_adi(parametreler)
"""
def args(*args):#Demet olarak
    print(args)
args(1,2,3,4,5,6)

def kwarags(**kwarags):#Sozluk olarak
    print(kwarags)
kwarags(x=1)

def topla(a,b):
    return int(a+b)
h = topla(int(input()),int(input()))
print("Sonuc = {}".format(h))