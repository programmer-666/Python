#% İşareti ile Biçimlendirme (Eski Yöntem)
x = int(input("x : "))
print("x = %s"%x)
y = x/2
if x%2==0:
    y = int(y)
    print("%d + %d = x"%(y,y))
elif x%2==1:
    y = float(y)
    print("%s + %s = x"%(y,y))
else:
    pass
for i in range(100):
    pass#İşllem için printi içeri koyarsınız..
print("%%%s"%i)
#for i in dir(str):
#    print("%15s " %i)#Aradaki sayı ne kadar yer kaplayacağını belirler
print("depoda %(miktar)s kilo %(ürün)s kaldı" %{"miktar": 5*5,"ürün": "elma"})
 # "%(değişken_adı)s " % {"değişken_adı": "değişken_değeri"} #
print("İşlemin cevabı %(cevap)s"%{"cevap":x})
# Biçimlendirme Karakterleri #
#d veya i ,Tam Sayılar - s , Stringler - o , Octal(Sekizli) - x , Hexadec - f , Float - c , Char
print("%f"%3.1459)
print("%.3f"%3.1459)
print("%c"%"x")#c ASCII tablosunda sayılara karşılık gelen karakterleri de gösterebilmesidir
#format() Metodu
print("{0} Programlama Dili..".format("Python"))
print("{0} + {0} = {1}".format("2","4"))
print("İşlem Cevabiniz : {cev}".format(cev=x))
#Biçimlendirme Karakterleri
print("{:s}".format("Dizi"))#Bu harf karakter dizilerini temsil eder , sayı girilemez
print("{:c}".format(65))#0 ile 256 arası sayıların ASCII tablosundaki karşılıklarını temsil eder
print("{:d} , {:d}".format(11,2))#Bu harf sayıları temsil eder
print("{:o}".format(55))#onlu düzendeki sayıları sekizli düzendeki karşılıklarına çevirir
print("{:X}".format(65))#onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir
print("{:b}".format(233))#onlu düzendeki sayıları ikili düzendeki karşılıklarına çevirir
print("{:.2f}".format(3.14))#onlu düzendeki sayıları ondalık düzendeki karşılıklarına çevirir
print("{:,}".format(123456789))#sayıları basamaklarına ayırır
#F-String
print(f"fstring")
print(f"Girilen Sayı : {x}")
print(f"2+2={2+2}'tür'")