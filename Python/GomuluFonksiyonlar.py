def p(a):
    return print(a)
x = [1,2,3,4,5,6,7,8,9,"Text","Yazı",3.14]
x_ = [-1,-2,-3,-4,-5,-6,-7,-8,-9,0,-3.14,666]
#abs() - sayinin mutlak degerini dondurur
print(abs(x_[4]),"abs")
#round() - belirli olcutlere gore sayiyi yukari veya asagi yuvarlar
print(round(x[len(x)-1]),"round")
print(round(x[len(x)-1],1),"round")#ikinci parametre ne kadar hassas olacagini belirtir
#all() - list icinde sifir veya bos kardiz varsa false dondurur(degilse true)
print(all(x),all(x_))
#any() - all fonksiyonunun tersidir list icinde bir tane bile true varsa true deger dondurur
print(any(x),any(x_))
#ascii() - nesnenin ekrana basilabilir halini verir (ascii olmayan karakterlerin unicode temsillerini gosterir)
print(ascii(x[len(x)-2]))
#repr() - nesnenin ekrana basılabilir halini verir (ascii fonksiyonunun aksine karakterleri birebir gosterir)
print(repr(x[len(x)-2]))
#bool() - nesnenin bool degerini verir
print(bool(x[5]),bool(x_[len(x_)-2]))
#bin() - sayinin binary karsiligini verir
print(bin(x[4]))
#bytes() - bytes turunden nesneler olusturmak icin kullanilir (degistirilemez)
print(bytes(x[8]))
#bytearray() - bytes ile ayni isi gorur (degistirilebilir)
print(bytearray(x[8]))
#chr() - kendisine parametre olarak verilen tam sayinin karakter karsiligini dondurur
p(chr(65))
#list() - liste olusturur ve farkli verileri listeye cevirir
l = list("list")
p(l)
#set() - farkli veri tiplerini kumeye donusturur
s = set("sozluk")
p(s)
#tuple() - farkli veri tiplerini demete donusturur
p(tuple("a"))
#frozenset() - farkli veri tiplerini donmus kumeye cevirir
s2 = set("textWord")
k = frozenset(s2)
print(k)
#float() - sayiari kayan noktali sayiya cevirir
p(float(2))
#int() - veriyi tam sayiya donusturur (sayilar ve float degerler)
p(int(float(3.14)))
#str() - farkli veri tiplerini stringe cevirir
p(str(int(float(3.1459))))#inanin bana bu bir string...
#dict() - farkli veri tiplerinden sozluk uretmemizi saglar
d = dict(a=1,b=2,c=3)
p(d)
#callable() - nesnenin cagrilabilir olup olmadigini denetler
print(callable(p))#ornek bir fonksiyon
#ord() - karakterin karsilik geldigi ondalik sayiyi verir
print(ord("a"))
#oct() - sayinin sekizli duzendeki karsiligini verir
print(oct(10))
#hex() - sayinin altılı duzendeki karsiligini verir
print(hex(365))
#eval(), exec(), globals(), locals(), compile()
print(eval("55+55"))#eval fonksiyonuna parametre olarak yalnizca ifade verilir
exec("a = 5")#exec fonksiyonuna parametre olarak yalnizca deyim verilir
print(a)
print(globals())#global de hangi anahtar ve degerlerin oldugunu gosterir
print(locals())#fonksiyonlara ve siniflara ait isim alani
#copyright() - python'un telif haklarina iliskin bilgiler
print(copyright())
#dir() - nesnelerin metot ve niteliklerini orenebilirsiniz
p(dir([]))
#divmod() - bolme islemi yapar , sonuc ile kalani dondurur
p(divmod(20,4))
#enumerate() - nesneleri numaralandirir
print(list(enumerate("Hello World")))
#exit() - o anda calisan programdaan cikmamizi saglar
#exit()
#help() - destek
help(dir)
#id() - verinin idsini verir
print(id(x))
#input() - veri almak icin kullanilir
input()
#format() - karakter dizilerini bicimlendirir
print('{:.2f}'.format(12))
#hash() - nesneye karma deger verir
print(hash("123"))
#isinstance() - nesnenin hangi veri tipinde oldugunu ogrenmek icin
print(isinstance(x,list))
#len() - nesne uzunlugunu hesaplar
p(len(x))
#map() - elimizdeki listenin elemanlarini teker teker, bizim belirledigimiz fonksiyona parametre olarak gondermek icin kullanilir
def karesi(n):
    return n ** 2
islenmis = list(map(karesi,x_))
print(islenmis)
#max() - dizi icindeki en buyuk degeri verir min() tam tersini yapar
print(max(x_))
#open() - herhangi bir dosyayi olusturmak veya acmak icin kullanilir
"""open(dosya_adi, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)"""
open("443435.txt")
"""Kipler (mode=?)
‘r’ Okuma kipidir. Öntanımlı değer budur.
‘w’ Yazma kipidir. Eğer belirtilen adda dosya zaten varsa o dosya silinir.
‘x’ Yeni bir dosya oluşturulup yazma kipinde açılır.
‘a’ Dosya ekleme kipinde açılır. Bu kip ile, varolan bir dosyanın sonuna eklemeler yapılabilir.
‘b’ Dosyaları ikili kipte açmak için kullanılır.
‘t’ Dosyaları metin kipinde açmak için kullanılır. Öntanımlı değerdir.
‘+’ Aynı dosya üzerinde hem okuma hem de yazma işlemleri yapılmasını sağlar.
"""
#buffering - verilerin tamponda tutulmasi icin (0 veya 1)
#encoding - dosyanin hangi karakter kodalamasi ile acilacagini belirler
#errors - ignore = hataya sebep olan karakter silinir , replace = '?' veya 'ufffd' karakterleri ile degisicektir , strict = karakter hatalari gorunur
#newline = satir sonu karakteri '\n' olmasi tavsiye
#pow() - girilen sayinin kuvvetini hesaplar
print(pow(2,1024))
#print() - kullaniciya mesaj gonderir
import sys
print("Hello World", sep='_', end='\n', file=sys.stdout, flush=False)
"""sep = bosluklara karakter atar
end = deger sonuna karakter atar
file = ciktilarin hangi dosyaya yazilacagini belirtir
flush = degerlerin tampona alinip alinmadigini belirler"""
#quit() - cikis
#range() - belirli araliktaki sayilari listeler
print(list(range(0,2**3)))
#reversed() - veriyi ters cevirir
print(list(reversed(x)))
#sorted() - dizi icindeki ogeleri belirli bir olcute gore siraya dizer
print(sorted('Hello World!'))
#slice() - dilimleme
dl = ["deneme","bir","iki","uc"]
dd = slice(0,2)
print(dl[dd])
#sum() - dizi icindek, degerler toplamini bulur
print(sum(x_))
#type() - verinin tipini verir
p(type(x))
#zip() - listelerin ogelerini birbirleriyle eslestirir
a = [1,2,3,4,5,6]
b = [6,5,4,3,2,1]
print(list(zip(a,b)))
#vars() = mevcut isim alani icindeki metot fonk ve nitelikleri listeler
print(vars(str),vars(int))
#