#Karakter Dizilerinin Metotlarıni Görmek İçin -dir("")-
"""Replace"""
data = "elliot.py"
text = "python"
text2 = "Deneme112233"
text3 = "Türkiye Büyük Millet Meclisi"
text4 = "TCAnkara , TCİstanbul , TCTekirdağ"
metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""
print(text.replace("p","P"))#karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi)
print(text2.replace("e","",2),text2.replace("1","",1))#Text2 içerisinden 2 adet e harfini siler
"""split, rsplit, splitlines"""
print(text3.split())
for i in text3.split():
    print(i[0],end="")
print(text4.split("TC"))#TC'leri siler
print(text4.split(",",1))#Bölme işlemini dizide 2 kez uygular
print(text3.rsplit(" ",2))#Bölme işlemini sağdan sola doğru yapar
print(metin.splitlines())#Satır satır dilimleme yapar True parametresini verirseniz satır başı karakterlerini de gösterir (\n)
"""lower , upper"""
print(text3.lower() , text3.upper())
"""islower , isupper"""
print(text3.islower() , text3.isupper() , text.islower() , text3.lower().islower())
veri = "Hello World"
böl = veri.split()
for i in böl:
    if i.isupper():
        print("Tamamı büyük harflerden oluşan kelimeler kullanmayın!")
"""endswith"""
print(text.endswith("n"))
print(data.endswith(".py"))
"""startswith"""
print(text.startswith("p"))