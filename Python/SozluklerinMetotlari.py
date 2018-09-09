
data = {"a":1,
        "b":2,
        "c":3,
        "d":4}
#Keys - Anahtar
print(data.keys())
DataList = list(data.keys())
print(DataList[0])
#Values - Deger
print(list(data.values()),list(data.keys()))
AllDLS = [list(data.values()),list(data.keys())]
print(AllDLS)
#items - Values ve Keys
print(list(data.items()))
#get - key arama get(key,yoksa_yapilacak)
print(data.get("a","Not found..."))
#clear - sozlugu tamamen bosaltir
#print(data.clear(),"ici bos")#sonraki islemler icin kodu kapatin
#copy - kopyalama (orijinale etki etse de kopyalanan sozluge etki olmaz veya tam tersi iste...)
datacop = data.copy()
data["pi"] = 3.14
print(list(datacop),list(data))#datacop a veri girmedi
#fromkeys - sozluk olusturmak icin kullanilir
citys = "istanbul" , "london" , "semerkand"
From = dict.fromkeys(citys,"world")
print(From)
#pop - belirtilen anahtari siler ve ekrana yazdirir
print(data.pop("a","key not found"))
#popitem - rastgele oge siler
print(data.popitem())
print(list(data))
#setdefault - sozlukte key araması yapar key varsa var olan keyi ekrana yazdirir yoksa yeni keyi olusturur
data.setdefault("a",1)
print(list(data.items()))
#update - veri guncelleme
yenidata = {"a":2,"b":3,"c":4,"d":8}
data.update(yenidata)
print(list(yenidata.items()))