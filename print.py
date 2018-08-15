"""len() - stringteki harfleri sayar
pow() - verilen değerin katlarını döndürür
type() - değiikenin değerini döndürür"""
print("Hello","World",sep="-")#Boşluklara belirtilen değeri yazar
#\n = Alt satır
print("Hello","World",end=".")#Son satıra belirtilen değeri koyar
# - - - FILE - - -
dosya = open("test.txt","w")
print("Hello","World",file=dosya)
#test.txt dosyasının nerede olduğunu öğrenmek için
import os
print("\n",os.getcwd())
#Flush
print("Hello",file=dosya,flush=True)#Değerin tampon'da bekletilmesini sağlar
dosya.close()
import keyword
keyword.kwlist#Hangi kelimeler değişken olarak kullanılmaz
import sys
sys.stdout#kaydedilen dosyaları mevcut dizine aktaran değişken f=poen("test.txt","w") --- sys.stdout = f yaparak yol değiştirilebilir
