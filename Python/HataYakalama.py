"""Biz bu bölümde hataları üç farklı başlık altında ele alacağız:
1. Programcı Hataları (Error)
2. Program Kusurları (Bug)
3. İstisnalar (Exception)

Python’da hata yakalama işlemleri için try... except... bloklarından yararlanılır. 
try:
hata verebileceğini bildiğimiz kodlar
except HataAdı:
hata durumunda yapılacak işlem

try:
    x = int(input("x = "))
    print(x**x)
except ValueError:
    print("Sayı gir..")""""""
while True:
    ilk_sayı = input("ilk sayı: ")
    ikinci_sayı = input("ikinci sayı: ")
    try:
        sayı1 = int(ilk_sayı)
        sayı2 = int(ikinci_sayı)
        print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    except (ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")"""
"""ValueError = Boş değer , ZeroDivisionError = Sıfır Değeri"""
#Try..Except..As
"""
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")
try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError) as hata:
    print("Bir hata oluştu!")
    print("orijinal hata mesajı: ", hata)"""
#Try..Execpt..Else - Kullanımı nadirdir
"""try:
bölünen = int(input("bölünecek sayı: "))
bölen = int(input("bölen sayı: "))
except ValueError:
print("Lütfen sadece sayı girin!")
else:
try:
print(bölünen/bölen)
except ZeroDivisionError:
print("Bir sayıyı 0'a bölemezsiniz!")"""
#Try..Except..Finally
"""try:
...bir takım işler...
except birHata:
...hata alınınca yapılacak işlemler...
finally:
...hata olsa da olmasa da yapılması gerekenler...
""""""
try:
dosya = open("dosyaadı", "r")
...burada dosyayla bazı işlemler yapıyoruz...
...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()
    #Gibi..."""
#Raise
"""
bölünen = int(input("bölünecek sayı: "))
if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")
bölen = int(input("bölen sayı: "))
print(bölünen/bölen)
"""
"""Burada eğer kullanıcı 23 sayısını girerse, kullanıcıya bir hata mesajı gösterilip programdan
çıkılacaktır. Biz bu kodlarda Exception adlı genel hata mesajını kullandık. Burada Exception
yerine her istediğimizi yazamayız. Yazabileceklerimiz ancak Python’da tanımlı hata mesajları
olabilir. Örneğin NameError, TypeError, ZeroDivisionError, IOError, vb..."""
"""tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")
for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass
print("Parola kabul edildi!")
En kullanışlı yapı
try:
birtakım kodlar
except ValueError:
print("Yanlış değer")
except ZeroDivisionError:
print("Sıfıra bölme hatası")
except:
print("Beklenmeyen bir hata oluştu!")"""
