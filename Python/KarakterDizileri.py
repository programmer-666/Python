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
print(site[:15:-1], site[::2])#İkişer İkişer atlar
print(*reversed(site),sep="")#reversed ile yapılabilir
#for i in reversed("Sana Gül Bahçesi Vadetmedim"): print(i, end="") - Bir çözüm
"""Karakter Dizilerini Alfabe Sırasına Dizmek"""
print(sorted(py))
for h in sorted(py):
    print(h,end="")
#Dikkat! sorted fonksiyonun'da Türkçe karakter sorunu vardır
#Olası çözüm için
import locale 
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") #Windows için 
locale.setlocale(locale.LC_ALL, "tr_TR") #GNU/Linux için 
print(sorted("çiçek", key=locale.strxfrm))
"""KarakterDizileriÜzerindeDeğişiklikYapmak"""
print("P" + py[1:])
py2 = "P" + py[1:]
print(py2,py)
#Örnek program
sesli_harfler = "aeıioöuü" 
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler = "" 
sessizler = ""
kelime = "istanbul"
for i in kelime: 
    if i in sesli_harfler: 
        sesliler += i 
    else: 
        sessizler += i
print("sesli harfler: ", sesliler) 
print("sessiz harfler: ", sessizler)
"""ÜçÖnemliFonksiyon"""
#Dir()
"""İlk olarak dir() adlı özel bir fonksiyondan söz edeceğiz. Bu metot bize Python’daki bir
nesnenin özellikleri hakkında bilgi edinme imkanı verecek. Mesela karakter dizilerinin bize
hangi metotları sunduğunu görmek için bu fonksiyonu kullanabiliriz."""
print(dir(x),"---------------------\n")
print(dir(""))
for j in dir(""):
    if "_" != j[0]:
        print(j)
#enumerate()
"""Eğer yazdığınız bir programda numaralandırmaya ilişkin işlemler yapmanız gerekiyorsa
Python’ın size sunduğu çok özel bir fonksiyondan yararlanabilirsiniz. Bu fonksiyonun adı
enumerate()."""
print(enumerate(py))
print(*enumerate(py))
for sira, metot in enumerate(dir("")):
    print(sira, metot)
#help()
"""Python’la ilgili herhangi bir konuda yardıma ihtiyacınız olduğunda, internetten araştırma
yaparak pek çok ayrıntılı belgeye ulaşabilirsiniz. Ama eğer herhangi bir nesne hakkında
hızlı bir şekilde ve İngilizce olarak yardım almak isterseniz help() adlı özel bir fonksiyondan
yararlanabilirsiniz."""