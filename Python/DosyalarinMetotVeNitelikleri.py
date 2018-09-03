f= open("loglar.txt","w")
#Closed Niteligi - dosya kapalimi acik mi
print(f.closed)
#readable - dosya okunabilirmi
print(f.readable())
#writable - yazilabilirmi
print(f.writable())
#truncate - dosyayi istenilen boyuta getirir
print(f.truncate(1))#!Tehlikeli!#
#moode - dosyanin hangi kipye acildigina dair bilgi verir
print(f.mode)
#name - dosyanin adini verir
print(f.name)
#encoding - dosyanin hangi dil kodlamasiyla yazildigini verir
print(f.encoding)
f.close()