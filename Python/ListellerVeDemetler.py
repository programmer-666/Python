#Listelerin ogelerine erismek ile birlikte
l = ["Oge","Oge2"]
print(l[0])
l2 = ["o1","o2",["o11","o12"],"o3"]
print(l2[2][1])
#List()
text = "abcdef"
print(list(text))
#Listelerin ogelerini degistirmek
l[0] = "Oge1"
print(l[0])
#Listeye oge eklemek
l = l + ["Test"]
print(l)
#Listeleri birlestirmek
ll2 = l+l2
print(ll2)
#Listeden Oge Cikarmak
del ll2[0]
print(ll2)
#Listeleri Silmek
#del ll2
print(ll2)#Olmadigindan hata verir...
#Listeleri Kopyalamak
la2 = ll2
print(la2)
#List Comprehensions
liste = [i for i in range(10)]
print(liste)
liste = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]
tumu = [z for i in liste for z in i]
print(tumu)
#Listeler Ozetlendi
#Demetler
d = ("test",1,2,3)
d2 = 1,2,3,4
tuple("123abc")
"""Demet olusturma yollari"""
#Demetlerin OGelerine Erismek
print(d[0])
"""Demetler tanimladiktan sonra degisitirlemez"""
d = d + (4,)
print(d)