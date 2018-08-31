"""capitalize"""
text = "python"
text2 = "python prog lang"
text3 = "MoRuQ NaBErr"
text4 = "İstanbul"
text5 = "kazak"
bl = ["türkiye","büyük","millet","meclisi"]
print(text.capitalize())
"""title"""
print(text2.title())
"""swapcase"""
"""büyük harfleri küçük harfe; küçük harfleri de büyük harfe dönüştürür"""
print(text3.swapcase())
"""casefold"""
print(text4.casefold())
"""strip, lstrip, rstrip"""
#Strip veri içindeki gereksiz kısımları kırpar
"""‘ ‘ boşluk karakteri
\t sekme (TAB) oluşturan kaçış dizisi
\n satır başına geçiren kaçış dizisi
\r imleci aynı satırın başına döndüren kaçış dizisi
\v düşey sekme oluşturan kaçış dizisi
\f yeni bir sayfaya geçiren kaçış dizisi"""
print(text5.strip("k"))
#lstrip soldaki karakteri siler
print(text5.lstrip("k"))
#rstip sağdaki karakteri siler
print(text5.rstrip("k"))
"""join"""
#bölünmüş karakterleri birleştirir
print(" ".join(bl).title())
"""count"""
print(text5.count("a"))#text5'in içinde a dan kaç tane var
print(text5.count("a",2))#ikinci parametre,count() metodunun bir karakteri saymaya başlarken karakter dizisinin kaçıncı sırasından başlayacağını gösteriyor
"""index, rindex"""
"""Karakterlerin, bir karakter dizisi içinde hangi sırada bulunduğunu öğrenmek için index() kullanılır"""
print(text.index("p"))
print(text.index("h",1))#aramaya kaçıncı sıradan itibaren başlıyacağı
print(text5.index("a",1,2))#hangi aralıklarla aramayı yapacağı
print(text.rindex("p"))#aramaya sağdan başlar
"""find, rfind"""
"""index() ve rindex() metotları karakter dizisi içindeki karakteri sorgularken, eğer o karakteri
bulamazsa bir ValueError hatası verir"""
print(text5.find("p"))#find -1 çıktısı verir
"""center"""
print(text.center(10))
print(text.center(10,"_"))
"""rjust, ljust"""
print(text.ljust(9,"."))
print(text.rjust(10,"."))
"""zfill"""
print(text.zfill(7))
"""partition, rpartition"""
print(text.partition("py"))
print(text.rpartition("on"))
print(text.partition("ho"))
"""encode"""
"çilek".encode("cp1254")
"""expandtabs"""
"""karakter dizisi içindeki boşluklar genişletilir"""
print("elma\tbir\tmeyve".expandtabs(10))