import os
os.system("cls")
"""Karakter Dizilerinin Öğelerine Erişmek"""
r = "0123456789"
py = "python"
site = "www.elitbilisim.tech"
for x in py[:]:
    print(x,"\n")
print(py[len(py)-1])
print(py[:])
for ix in range(len(py)):
     print(py[ix])
isim = input("isminiz: ")
for i in range(len(isim)):
    print("isminizin {}. harfi: {}".format(i+1, isim[i]))
"""Karakter Dizilerini Dilimlemek"""
print(site[4:15])
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])
print(py[:4],py[2:])
"""Karakter Dizilerini Ters Çevirmek"""
print(site[::-1])
print(site[:15:-1], site[::2])#İkişe İkişer atlar
print(*reversed(site),sep="")#reversed ile yapılabilir
#Karakter Dizilerini Alfabe Sırasına Dizmek