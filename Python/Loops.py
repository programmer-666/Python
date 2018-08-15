#While
"""İngilizce bir kelime olan while, Türkçede ‘... iken, ... olduğu sürece’ gibi anlamlara gelir.
Python’da while bir döngüdür. Bir önceki bölümde söylediğimiz gibi, döngüler sayesinde
programlarımızın sürekli olarak çalışmasını sağlayabiliriz.
"""
x = 0
while x < 10:
    x+=1
    print(x)
"""ÖRNEK
while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")
    if soru == "q":
         print("çıkılıyor...")
    break #Kaçış komutu
Diğer bir örnek
a = 0
while a < 100:
    a += 1
    if a % 2 == 0:
        print(a)"""
#For
"""Nedir bu for döngüsü denen şey?
for da tıpkı while gibi bir döngüdür. Yani tıpkı while döngüsünde olduğu gibi,
programlarımızın birden fazla sayıda çalışmasını sağlar. Ancak for döngüsü while döngüsüne
göre biraz daha yeteneklidir. while döngüsü ile yapamayacağınız veya yaparken çok
zorlanacağınız şeyleri for döngüsü yardımıyla çok kolay bir şekilde halledebilirsiniz.
Yalnız, söylediğimiz bu cümleden, for döngüsünün while döngüsüne bir alternatif olduğu
sonucunu çıkarmayın. Evet, while ile yapabildiğiniz bir işlemi for ile de yapabilirsiniz çoğu
zaman, ama bu döngülerin, belli vakalar için tek seçenek olduğu durumlar da vardır. Zira bu
iki döngünün çalışma mantığı birbirinden farklıdır.
"""
text = "Test""""
for t in text:
    print(t)
#Direkt sayılar üzerinden döngü kurulamaz
sayılar = "0123456789"
for sayı in sayılar:
    print(int(sayı) * 2)
#Örnek
tr_harfler = "şçöğüİı"
parola = input("Parolanız: ")
for karakter in parola:#passtaki her bir karaktere değer atayıp if ile türkçe olup olmadığını kontrol et
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılamaz")"""
#İlgili araçlar
"""
y = int(input("$:"))
for x in range(0,y,9):
    print(x*x*x*x*x)
#range(ilSayı,SonSayı,AtlamaDegeri)
""""""
for x in range(9,0,-1):
    print(x)
"""
#Pass - Geç
"""
if x == 1:
    print("x = 1")
else:
    pass
    """
#Break - Kır , Parçala , Kaçış
"""
while True:
    parola = input("Lütfen bir parola belirleyiniz:")
    if len(parola) < 5:
        print("Parola 5 karakterden az olmamalı!")
    else:
        print("Parolanız belirlendi!")
        break
"""
#Continue
"""while True:
    s = input("Bir sayı girin: ")
    if s == "iptal":
        break
    if len(s) <= 3:
        continue
    print("En fazla üç haneli bir sayı girebilirsiniz.")
    """