#Kume olusturma
kume = set(["Deneme","1",2,"3"])
print(kume)
#liste,demet,string,sozluk ve char tiplerinden kume olsuturulabilir fakat int lar olusmaz
kume2 = {1,2,3,4,5,6,7,8,9}#diger bir kume atama yolu
print(kume2)
#kumelerde iki ayni veri depolanmaz
k3 = {"1",2,3,"1"}
print(k3)
#Kumelerin uretecleri
import random
liste = [random.randint(0, 10000) for i in range(1000)]
#yüzden_küçük_sayılar = [i for i in liste if i < 100]#ayni iki sayi gelme olsailigi var
yks = {i for i in liste if i < 100}
print(yks)#kume icin de islem yapmak gereklidir
"""Kumelerin Metotlari"""
#clear
km = set("adana")
for i in km:
    print(i)
km.clear()
print(km)
#copy
km = set("kahramanmaras")
yedek = km.copy()
print(yedek)
k4 = set(["elma","armut"])
k4.add("cilek")
print(k4)
"""Kumeler degistirilebilir veri tipleridir.Kumelere eklenebilen veri tipleri degistirilemeyin veri tipleridir"""
#difference - iki kumenin farkini anlamaya yarar "-" kullanilabilir
tk = set([1,2,3,4,5,6,"a"])
tk2 = set({1,3,4,6,3,2,"b"})
print(tk.difference(tk2),tk2.difference(tk))
#difference_update - 2 kume arasindaki eksigi secilen kumeye atar
tt = set([1,2,3])
tt2 = set([1,3,5])
tt.difference_update(tt2)
print(tt)
#discard - oge silme
tt2.discard(3)
print(tt2)
#remove - claer aynisi
tt2.remove(1)
print(tt2)
#intersection - kesisim "&"
xk = set([1,2,3,4,5,6])
yk = set([1,5,2,8,3])
xyk = xk.intersection(yk)
print(xyk)
#intersection_update - x2k ya atama yapar
x2k = set([1,2,3,4,5,6,7,8,9])
y2k = set([1,6,4,7,8,9])
x2k.intersection_update(y2k)
print(x2k)
#isdisjoint - kesisim kumesinin bos olup olmadigini sorgular
print(x2k.isdisjoint(y2k))
s = set([1,2,3])
s2 = set([4,5,6])
print(s.isdisjoint(s2))
#issubset - kumenin baska bir kumenin alt kumesi olup olmaddigini dondurur
b = set([0,1,2,3,4,5,6,7,8,9])
print(s.issubset(b))
#issuperset - b kumesi s kumesini kapsar seklinde bir yorum yapilabilir
print(b.issuperset(s))
#union - iki kumeyi birlestirir
a = set([0,2,78,1,9,3,64375,5342])
print(a.union(b))
#update
asdsa = set(["elma","armut","wtf"])
ynni = [1,22,333]
asdsa.update(ynni)
print(asdsa)
#symmetric_difference - iki kume arasindaki ortak farklari bulur
KihKihKih = set([1,2,5])
MahMahMah = set([1,4,5])
print(KihKihKih.symmetric_difference(MahMahMah))
#symmetric_difference_update - iki kume arasindaki ortak farki belirlenen kumeye atar
a.symmetric_difference_update(b)
print(a)
#pop - kumeden rastgele veri silip ekrana basar
print(a.pop())
"""Dondurulmus Kumeler"""
dKume = frozenset([1,2,3,"Test"])#Uzerin de degisiklik yapilmayan kumeler
