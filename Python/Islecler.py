"""Aritmetik İşleçler
* Çarpma
/ Bölme
+ Toplama
- Çıkarma
** Kuvvet
% Modülüs 
// Taban bölme
"""
x = 3.123456789
y = 0
z = 12.987
text = "Test"
print(round(x,1))#Sayının yuvarlanmış halini verir round(deger,gösterilecekbasamak)
print(x**x,pow(x,x))#Sayının kuvvetini alır pow(deger,kuvvet,bölecekDeğer)
"""Bool İşleçleri
Nedir bu bool denen şey?
Bilgisayar bilimi iki adet değer üzerine kuruludur: 1 ve 0. Yani sırasıyla True ve False.
Bilgisayar biliminde herhangi bir şeyin değeri ya True, ya da False‘tur. İşte bu True ve False
olarak ifade edilen değerlere bool değerleri adı verilir (George Boole adlı İngiliz matematikçi
ve filozofun adından).
 - İşleçleri - 
 And , Or , Not
"""
print(x==3.123456789,x==pow(x,x))
#Hayati kural : 0 değeri ve boş veri tipleri False‘tur. Bunlar dışında kalan her şey ise True‘dur.

""" Değer Atama İşleçleri 
+= 
-=
/=
*=
%=
**=
//=
"""
z*=x
print(z)
"""Aitlik İşleçleri
Aitlik işleçleri, bir karakter dizisi ya da sayının, herhangi bir veri tipi içinde bulunup
bulunmadığını sorgulamamızı sağlayan işleçlerdir
pi = "3.14"
"1" in pi
>>true
"""
print("e" in text)#Gibi...
"""Kimlik İşleçleri
Python’da her şeyin (ya da başka bir deyişle her nesnenin) bir kimlik numarası (identity)
vardır. Kabaca söylemek gerekirse, bu kimlik numarası denen şey esasında o nesnenin
bellekteki adresini gösterir
id()
Python’da is işlecini kullanarak iki nesne arasında karşılaştırma yapmak güvenli
değildir. Yani is ve == işleçleri birbirleriyle aynı işlevi görmez. Bu iki işleç nesnelerin farklı
yönlerini sorgular: is işleci nesnelerin kimliklerine bakıp o nesnelerin aynı nesneler olup
olmadığını kontrol ederken, == işleci nesnelerin içeriğine bakarak o nesnelerin aynı değere
sahip olup olmadıklarını sorgular. Bu iki tanım arasındaki ince farka dikkat edin.
x is 1000"""
print(id(x))