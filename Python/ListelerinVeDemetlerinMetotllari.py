liste = ["A1","A2","A3",1,2,3,"B1","B2","B3"]
liste2 = [1,2,3,4,5,6,7,8,9,0,666,777,888,999]
y = [10,9,8,7,6,5,4,3,2,1,0]
print("Mevcut Liste {}".format(liste))
#append - Ekleme
liste.append(4)
print(liste)
for i in range(5,7):
    liste.append(i)
print(liste)#Birden fazla ekleme icin (int)
#extend - Genisletme
liste.extend(liste2)
print(liste)
#append'den farkli olarak extend liste2 icindeki verileri liste'ye aktarir append ise liste2 tamamen liste ye ekler
#insert - Yerlestirmek
liste.insert(0,"A0B0")
print(liste)    
#remove - Silme
liste.remove("A0B0")
print(liste)
#reverse - Ters cevirir
liste.reverse()
print(liste)
#pop - Ogeyi silerek ekrana basar
liste.pop(5)
print(liste)
#sort - Alfabetik siraya dizer
liste.sort()#reverse=True ile ters siralama yapilabilir
print(liste)
#index - Liste icindeki verinin numarasini verir
print("- {0} - ".format(liste.index("A1")))
#count - Verinin listede kac kere gecitigini dondurur
print("1 Sayisi Liste'de {0} kere var".format(liste.count(1)))
#copy - Kopyalama
"""yedek = liste.copy()
print(liste) sikintili..."""
#clear - Listenin icerigini siler
#sikintili y.clear()
print(liste)
#Demetler
#index
demet = ("a1","a2","a3",1,2,3,"b1","b2","b3")
print(demet.index("b2"))
#count
print(demet.count("b2"))