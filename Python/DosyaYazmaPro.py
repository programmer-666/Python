import os
os.system("clear")
def DosyaYaz(DosAd,Tur,Icerik,Dosya):
    with open(DosAd+"."+Tur,"w") as Dosya:
        Dosya.write(Icerik)
x = input("Dosya Adi : ")
os.system("clear")
y = input("Dosya Turu : ")
os.system("clear")
z = input("Icerik : ")
os.system("clear")
DosyaYaz(x,y,z,"")